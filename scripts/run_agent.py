#!/usr/bin/env python3
"""Run OpenAI-compatible models as iterative tool agents on benchmark tasks.

This runner differs from run_direct.py:

* The model does not receive a compressed evidence dump.
* The model must choose tools one step at a time.
* Local tools execute against the event package and return observations.
* computed_gt.json, solution_en.md, review.json, and compute_gt.py are forbidden.

The output folder remains compatible with the existing evaluators:
trajectory.json, answer.md, tool_trace.md, run_notes.md, raw_conversation.json.
"""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import http.client
import json
import math
import os
import re
import statistics
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


def find_repo_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (
            (parent / "tasks").exists()
            and (parent / "event_packages" / "standard_event_packages" / "packages").exists()
        ):
            return parent
    return Path.cwd().resolve()


ROOT = find_repo_root(Path(__file__).resolve().parent)
TEXT_SUFFIXES = {".json", ".csv", ".md", ".txt", ".html", ".htm", ".xml", ".geojson", ".yml", ".yaml"}
PUBLIC_TASK_FILES = {"question_en.md"}
FORBIDDEN_NAMES = {"computed_gt.json", "solution_en.md", "review.json", "compute_gt.py"}
FORBIDDEN_CODE_TERMS = [
    "computed_gt",
    "solution_en",
    "review.json",
    "compute_gt",
    "agent_trace_synthesis",
    "minimum_10_runs",
    "outputs",
    "model_result_evaluation",
    "requests",
    "urllib",
    "http.client",
    "socket",
    "subprocess",
    "os.system",
    "os.popen",
    "multiprocessing",
    "ctypes",
    "importlib",
    "shutil",
]
RETRYABLE_EXCEPTIONS = (
    urllib.error.HTTPError,
    urllib.error.URLError,
    http.client.RemoteDisconnected,
    ConnectionResetError,
    TimeoutError,
    OSError,
)
MODEL_RUN_EXCEPTIONS = RETRYABLE_EXCEPTIONS + (ValueError, json.JSONDecodeError, KeyError)


def read_text(path: Path, max_chars: int | None = None) -> str:
    data = path.read_text(encoding="utf-8-sig", errors="replace")
    if max_chars is not None and len(data) > max_chars:
        return data[:max_chars] + "\n...[TRUNCATED]..."
    return data


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(read_text(path))


def load_mode_config(path: Path, mode: str) -> dict[str, Any]:
    data = load_json(path)
    if not isinstance(data, dict):
        raise ValueError(f"configuration root must be an object: {path}")
    mode_config = data.get(mode)
    if not isinstance(mode_config, dict):
        raise ValueError(f"configuration is missing the '{mode}' object: {path}")
    config = {key: value for key, value in data.items() if key not in {"agent", "direct"}}
    config.update(mode_config)
    models = config.get("models")
    if not isinstance(models, list) or not models:
        raise ValueError(f"configuration must define at least one model: {path}")
    return config


def repo_path(path: str | Path) -> Path:
    value = Path(path)
    return value if value.is_absolute() else ROOT / value


def compact_text(text: Any, max_chars: int = 8000) -> str:
    if not isinstance(text, str):
        text = json.dumps(text, ensure_ascii=False, indent=2)
    text = re.sub(r"\n{4,}", "\n\n\n", text.strip())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 80] + "\n...[TRUNCATED]..."


def compact_text_head_tail(text: Any, max_chars: int) -> str:
    """Keep both the start and end of long evidence instead of dropping the tail."""
    if not isinstance(text, str):
        text = json.dumps(text, ensure_ascii=False, separators=(",", ":"))
    text = re.sub(r"\n{4,}", "\n\n\n", text.strip())
    marker = "\n...[MIDDLE TRUNCATED]...\n"
    if len(text) <= max_chars:
        return text
    if max_chars <= len(marker) + 40:
        return compact_text(text, max_chars)
    available = max_chars - len(marker)
    head_chars = max(1, int(available * 0.68))
    tail_chars = max(1, available - head_chars)
    return text[:head_chars] + marker + text[-tail_chars:]


def rel_to_repo(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def safe_model_name(model: str) -> str:
    return model.replace("/", "__").replace(":", "_")


def iter_task_dirs(task_root: Path, limit: int = 0, task_ids: list[str] | None = None) -> list[Path]:
    available = {
        p.name: p
        for p in sorted(task_root.iterdir())
        if p.is_dir() and (p / "question_en.md").exists()
    }
    if task_ids:
        seen: set[str] = set()
        dirs = []
        for task_id in task_ids:
            if task_id in available and task_id not in seen:
                dirs.append(available[task_id])
                seen.add(task_id)
    else:
        dirs = list(available.values())
    if limit > 0:
        dirs = dirs[:limit]
    return dirs


def load_task_ids(path: Path | None) -> list[str]:
    if not path:
        return []
    return [line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def normalize_local_path(raw_path: str, package_dir: Path, task_dir: Path, scratch_dir: Path) -> Path:
    if not raw_path:
        raise ValueError("path is required")
    raw_path = raw_path.strip().strip("\"'")
    raw_path = raw_path.replace("\\", "/")
    if any(part in raw_path for part in FORBIDDEN_NAMES):
        raise PermissionError(f"forbidden file requested: {raw_path}")

    path = Path(raw_path)
    if path.is_absolute():
        candidate = path
    elif raw_path.startswith("event_packages/") or raw_path.startswith("tasks/"):
        candidate = ROOT / raw_path
    else:
        candidate = package_dir / raw_path

    resolved = candidate.resolve()
    public_task_paths = {(task_dir / name).resolve() for name in PUBLIC_TASK_FILES}
    allowed = (
        any(is_under(resolved, root) for root in [package_dir, scratch_dir])
        or resolved in public_task_paths
    )
    if not allowed:
        raise PermissionError(f"path outside allowed task/package roots: {raw_path}")
    if resolved.name in FORBIDDEN_NAMES:
        raise PermissionError(f"forbidden file requested: {raw_path}")
    return resolved


def observation(ok: bool, output: Any, evidence_files: list[str] | None = None, warnings: list[str] | None = None) -> dict[str, Any]:
    return {
        "ok": bool(ok),
        "output": output,
        "evidence_files": evidence_files or [],
        "warnings": warnings or [],
    }


def tool_list_package_files(args: dict[str, Any], package_dir: Path, task_dir: Path, scratch_dir: Path) -> dict[str, Any]:
    subdir = str(args.get("subdir") or ".")
    max_files = int(args.get("max_files") or 120)
    root = normalize_local_path(subdir, package_dir, task_dir, scratch_dir) if subdir != "." else package_dir
    if not root.exists():
        return observation(False, f"subdir not found: {subdir}", warnings=["missing subdir"])
    if root.is_file():
        files = [root]
    else:
        files = [p for p in sorted(root.rglob("*")) if p.is_file() and p.name not in FORBIDDEN_NAMES]
    rows = []
    for path in files[:max_files]:
        rows.append(
            {
                "path": rel_to_repo(path),
                "package_relative_path": path.relative_to(package_dir).as_posix() if is_under(path, package_dir) else rel_to_repo(path),
                "bytes": path.stat().st_size,
                "suffix": path.suffix.lower(),
            }
        )
    extra = max(0, len(files) - len(rows))
    return observation(
        True,
        {"file_count_returned": len(rows), "file_count_total": len(files), "truncated_extra_files": extra, "files": rows},
        evidence_files=[rel_to_repo(package_dir / "metadata" / "files.csv")] if (package_dir / "metadata" / "files.csv").exists() else [],
    )


def tool_read_text_file(args: dict[str, Any], package_dir: Path, task_dir: Path, scratch_dir: Path) -> dict[str, Any]:
    max_chars = int(args.get("max_chars") or 12000)
    path = normalize_local_path(str(args.get("path") or ""), package_dir, task_dir, scratch_dir)
    if not path.exists() or not path.is_file():
        return observation(False, f"file not found: {args.get('path')}", warnings=["missing file"])
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return observation(False, f"not a text-supported suffix: {path.suffix}", evidence_files=[rel_to_repo(path)], warnings=["binary or image file"])
    return observation(True, {"path": rel_to_repo(path), "text": read_text(path, max_chars)}, evidence_files=[rel_to_repo(path)])


def tool_search_package_files(args: dict[str, Any], package_dir: Path, task_dir: Path, scratch_dir: Path) -> dict[str, Any]:
    query = str(args.get("query") or "").strip()
    if not query:
        return observation(False, "query is required")
    file_glob = str(args.get("glob") or "**/*")
    max_matches = int(args.get("max_matches") or 40)
    terms = [t.lower() for t in re.split(r"\s+", query) if t.strip()]
    matches = []
    for path in sorted(package_dir.glob(file_glob)):
        if not path.is_file() or path.name in FORBIDDEN_NAMES or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = read_text(path, 300000)
        low = text.lower()
        if not all(term in low for term in terms):
            continue
        best_line = ""
        for line in text.splitlines():
            lline = line.lower()
            if any(term in lline for term in terms):
                best_line = line.strip()
                break
        matches.append({"path": rel_to_repo(path), "snippet": compact_text(best_line, 500)})
        if len(matches) >= max_matches:
            break
    evidence = [m["path"] for m in matches[:8]]
    if not evidence and (package_dir / "metadata" / "files.csv").exists():
        evidence = [rel_to_repo(package_dir / "metadata" / "files.csv")]
    return observation(True, {"query": query, "match_count": len(matches), "matches": matches}, evidence_files=evidence)


def numeric_summary(values: list[float]) -> dict[str, Any]:
    clean = [v for v in values if isinstance(v, (int, float)) and math.isfinite(v)]
    if not clean:
        return {}
    return {
        "count": len(clean),
        "min": min(clean),
        "max": max(clean),
        "mean": statistics.fmean(clean),
        "p95": sorted(clean)[max(0, int(0.95 * (len(clean) - 1)))],
    }


def flatten_numeric_lists(obj: Any, prefix: str = "", out: dict[str, list[float]] | None = None) -> dict[str, list[float]]:
    if out is None:
        out = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            next_prefix = f"{prefix}.{key}" if prefix else str(key)
            flatten_numeric_lists(value, next_prefix, out)
    elif isinstance(obj, list):
        if obj and all(isinstance(x, (int, float)) for x in obj):
            out[prefix] = [float(x) for x in obj]
        elif len(obj) <= 5000:
            for idx, value in enumerate(obj[:40]):
                flatten_numeric_lists(value, f"{prefix}[{idx}]", out)
    return out


def json_shape(obj: Any, depth: int = 0) -> Any:
    if depth > 3:
        return type(obj).__name__
    if isinstance(obj, dict):
        return {k: json_shape(v, depth + 1) for k, v in list(obj.items())[:30]}
    if isinstance(obj, list):
        return {"type": "list", "length": len(obj), "sample": json_shape(obj[0], depth + 1) if obj else None}
    return type(obj).__name__


def tool_summarize_table_or_json(args: dict[str, Any], package_dir: Path, task_dir: Path, scratch_dir: Path) -> dict[str, Any]:
    path = normalize_local_path(str(args.get("path") or ""), package_dir, task_dir, scratch_dir)
    if not path.exists() or not path.is_file():
        return observation(False, f"file not found: {args.get('path')}", warnings=["missing file"])
    suffix = path.suffix.lower()
    try:
        if suffix == ".csv":
            with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as fh:
                reader = csv.DictReader(fh)
                rows = list(reader)
            columns = reader.fieldnames or []
            summaries: dict[str, Any] = {}
            for col in columns:
                vals = []
                for row in rows:
                    try:
                        vals.append(float(str(row.get(col, "")).replace(",", "")))
                    except ValueError:
                        pass
                if vals:
                    summaries[col] = numeric_summary(vals)
            output = {
                "path": rel_to_repo(path),
                "type": "csv",
                "rows": len(rows),
                "columns": columns,
                "sample_rows": rows[:5],
                "numeric_summaries": summaries,
            }
        elif suffix in {".json", ".geojson"}:
            data = load_json(path)
            numeric = {
                key: numeric_summary(vals)
                for key, vals in flatten_numeric_lists(data).items()
                if len(vals) >= 1
            }
            output = {
                "path": rel_to_repo(path),
                "type": suffix.lstrip("."),
                "shape": json_shape(data),
                "numeric_list_summaries": dict(list(numeric.items())[:60]),
                "text_preview": compact_text(data, 3000),
            }
        else:
            return observation(False, f"unsupported table/json suffix: {suffix}", evidence_files=[rel_to_repo(path)])
    except Exception as exc:
        return observation(False, f"failed to summarize {rel_to_repo(path)}: {type(exc).__name__}: {exc}", evidence_files=[rel_to_repo(path)])
    return observation(True, output, evidence_files=[rel_to_repo(path)])


def tool_inspect_image(args: dict[str, Any], package_dir: Path, task_dir: Path, scratch_dir: Path) -> dict[str, Any]:
    path = normalize_local_path(str(args.get("path") or ""), package_dir, task_dir, scratch_dir)
    if not path.exists() or not path.is_file():
        return observation(False, f"file not found: {args.get('path')}", warnings=["missing file"])
    try:
        from PIL import Image, ImageStat

        with Image.open(path) as img:
            stat = ImageStat.Stat(img.convert("RGB"))
            output = {
                "path": rel_to_repo(path),
                "format": img.format,
                "mode": img.mode,
                "width": img.width,
                "height": img.height,
                "rgb_mean": [round(x, 2) for x in stat.mean],
                "rgb_stddev": [round(x, 2) for x in stat.stddev],
            }
        return observation(True, output, evidence_files=[rel_to_repo(path)])
    except Exception as exc:
        return observation(False, f"image inspection failed: {type(exc).__name__}: {exc}", evidence_files=[rel_to_repo(path)])


def make_python_wrapper(
    user_code: str,
    package_dir: Path,
    task_dir: Path,
    scratch_dir: Path,
) -> str:
    encoded = base64.b64encode(user_code.encode("utf-8")).decode("ascii")
    allowed_roots = [str(package_dir.resolve()), str(scratch_dir.resolve())]
    allowed_files = [str((task_dir / "question_en.md").resolve())]
    forbidden = sorted(FORBIDDEN_NAMES)
    return f"""
import base64, builtins, csv, glob, io, json, math, os, pathlib, re, statistics, sys
try:
    import numpy as np
except Exception:
    np = None
try:
    import pandas as pd
except Exception:
    pd = None
try:
    from PIL import Image
except Exception:
    Image = None

ALLOWED_ROOTS = [pathlib.Path(x).resolve() for x in {allowed_roots!r}]
ALLOWED_READ_FILES = set(pathlib.Path(x).resolve() for x in {allowed_files!r})
FORBIDDEN_NAMES = set({forbidden!r})
SCRATCH_DIR = pathlib.Path({str(scratch_dir.resolve())!r}).resolve()
EVENT_PACKAGE_DIR = pathlib.Path({str(package_dir.resolve())!r}).resolve()
TASK_DIR = pathlib.Path({str(task_dir.resolve())!r}).resolve()
REPO_ROOT = pathlib.Path({str(ROOT.resolve())!r}).resolve()
os.environ['EVENT_PACKAGE_DIR'] = str(EVENT_PACKAGE_DIR)
os.environ['TASK_DIR'] = str(TASK_DIR)
os.environ['SCRATCH_DIR'] = str(SCRATCH_DIR)
os.environ['PUBLIC_TASK_FILES'] = json.dumps([str(x) for x in ALLOWED_READ_FILES])

_orig_open = builtins.open
_orig_io_open = io.open
_orig_path_open = pathlib.Path.open
_orig_read_text = pathlib.Path.read_text
_orig_read_bytes = pathlib.Path.read_bytes
_orig_os_open = os.open
_orig_import = builtins.__import__

def _resolve_checked(file, mode='r'):
    if not isinstance(file, (str, bytes, os.PathLike)):
        return file
    raw = os.fspath(file).replace('\\\\', '/')
    p = pathlib.Path(file)
    if not p.is_absolute():
        if raw.startswith('event_packages/') or raw.startswith('tasks/'):
            p = REPO_ROOT / raw
        else:
            p = (pathlib.Path.cwd() / p)
    rp = p.resolve()
    if rp.name in FORBIDDEN_NAMES:
        raise PermissionError(f'Forbidden benchmark file: {{rp}}')
    write_mode = any(x in str(mode) for x in ['w', 'a', '+', 'x'])
    if write_mode:
        try:
            rp.relative_to(SCRATCH_DIR)
        except ValueError:
            raise PermissionError(f'Writes are allowed only inside SCRATCH_DIR: {{rp}}')
        return rp
    if rp in ALLOWED_READ_FILES:
        return rp
    for root in ALLOWED_ROOTS:
        try:
            rp.relative_to(root)
            return rp
        except ValueError:
            pass
    raise PermissionError(f'Reads are restricted to the event package, current public question, and scratch dir: {{rp}}')

def guarded_open(file, mode='r', *args, **kwargs):
    return _orig_open(_resolve_checked(file, mode), mode, *args, **kwargs)

def guarded_io_open(file, mode='r', *args, **kwargs):
    return _orig_io_open(_resolve_checked(file, mode), mode, *args, **kwargs)

def guarded_path_open(self, mode='r', *args, **kwargs):
    return _orig_path_open(_resolve_checked(self, mode), mode, *args, **kwargs)

def guarded_read_text(self, *args, **kwargs):
    _resolve_checked(self, 'r')
    return _orig_read_text(self, *args, **kwargs)

def guarded_read_bytes(self, *args, **kwargs):
    _resolve_checked(self, 'rb')
    return _orig_read_bytes(self, *args, **kwargs)

def guarded_os_open(file, flags, mode=0o777, *, dir_fd=None):
    write_flags = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
    checked = _resolve_checked(file, 'w' if flags & write_flags else 'r')
    return _orig_os_open(checked, flags, mode, dir_fd=dir_fd)

BLOCKED_IMPORT_ROOTS = {{
    'ctypes', 'ftplib', 'http', 'importlib', 'multiprocessing', 'paramiko',
    'requests', 'shutil', 'socket', 'ssl', 'subprocess', 'telnetlib', 'urllib',
}}

def guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
    root = str(name).split('.', 1)[0]
    if root in BLOCKED_IMPORT_ROOTS:
        raise PermissionError(f'Import blocked in benchmark Python: {{name}}')
    return _orig_import(name, globals, locals, fromlist, level)

def blocked_process_call(*args, **kwargs):
    raise PermissionError('Process creation is blocked in benchmark Python')

builtins.open = guarded_open
io.open = guarded_io_open
pathlib.Path.open = guarded_path_open
pathlib.Path.read_text = guarded_read_text
pathlib.Path.read_bytes = guarded_read_bytes
os.open = guarded_os_open
builtins.__import__ = guarded_import
for _name in (
    'system', 'popen', 'startfile', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe',
    'spawnv', 'spawnve', 'spawnvp', 'spawnvpe',
):
    if hasattr(os, _name):
        setattr(os, _name, blocked_process_call)
os.chdir(EVENT_PACKAGE_DIR)

code = base64.b64decode({encoded!r}).decode('utf-8')
globals_dict = {{
    '__name__': '__main__',
    'json': json,
    'csv': csv,
    'glob': glob,
    'math': math,
    'os': os,
    'pathlib': pathlib,
    're': re,
    'statistics': statistics,
    'np': np,
    'pd': pd,
    'Image': Image,
    'EVENT_PACKAGE_DIR': EVENT_PACKAGE_DIR,
    'TASK_DIR': TASK_DIR,
    'SCRATCH_DIR': SCRATCH_DIR,
}}
exec(compile(code, '<agent_python_exec>', 'exec'), globals_dict, globals_dict)
"""


def tool_python_exec(
    args: dict[str, Any],
    package_dir: Path,
    task_dir: Path,
    scratch_dir: Path,
    code_dir: Path,
    step: int,
    timeout_s: int,
) -> dict[str, Any]:
    code = str(args.get("code") or "")
    if not code.strip():
        return observation(False, "code is required")
    low = code.lower().replace("\\", "/")
    forbidden_hits = [term for term in FORBIDDEN_CODE_TERMS if term in low]
    if forbidden_hits:
        return observation(False, {"error": "forbidden code terms", "terms": forbidden_hits}, warnings=["forbidden code term"])
    code_hash = hashlib.sha1(code.encode("utf-8")).hexdigest()[:12]
    code_path = code_dir / f"step_{step:02d}_{code_hash}.py"
    write_text(code_path, code)
    wrapper_path = code_dir / f"step_{step:02d}_{code_hash}_wrapper.py"
    write_text(wrapper_path, make_python_wrapper(code, package_dir, task_dir, scratch_dir))
    child_env = {
        key: value
        for key in (
            "PATH",
            "SYSTEMROOT",
            "WINDIR",
            "HOME",
            "USERPROFILE",
            "TMP",
            "TEMP",
            "LANG",
            "LC_ALL",
        )
        if (value := os.environ.get(key))
    }
    child_env.update({"PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"})
    started = time.perf_counter()
    proc = subprocess.run(
        [sys.executable, str(wrapper_path)],
        cwd=str(package_dir),
        env=child_env,
        capture_output=True,
        text=True,
        timeout=timeout_s,
        encoding="utf-8",
        errors="replace",
    )
    latency = time.perf_counter() - started
    stdout = compact_text(proc.stdout, 12000)
    stderr = compact_text(proc.stderr, 4000)
    ok = proc.returncode == 0
    output = {
        "code_path": rel_to_repo(code_path),
        "returncode": proc.returncode,
        "latency_s": round(latency, 3),
        "stdout": stdout,
        "stderr": stderr,
    }
    warnings = [] if ok else ["python execution returned non-zero exit status"]
    return observation(ok, output, evidence_files=[rel_to_repo(code_path)], warnings=warnings)


TOOL_DESCRIPTIONS = """
Available tools. Call exactly one tool per turn until ready to answer.

1. list_package_files(args)
   args: {"subdir": ".", "max_files": 120}
   Use first to discover local evidence files. subdir may be a package-relative directory.

2. read_text_file(args)
   args: {"path": "package-relative-or-repo-relative path", "max_chars": 12000}
   Reads md/txt/html/json/csv/xml/geojson text from the event package, current public question, or scratch dir.
   Forbidden: computed_gt.json, solution_en.md, review.json, compute_gt.py.

3. search_package_files(args)
   args: {"query": "keywords", "glob": "**/*", "max_matches": 40}
   Searches text files inside the event package and returns snippets.

4. summarize_table_or_json(args)
   args: {"path": "package-relative-or-repo-relative path"}
   Inspects CSV/JSON/GeoJSON schema, samples, and numeric summaries.

5. inspect_image(args)
   args: {"path": "package-relative-or-repo-relative image path"}
   Returns image size, mode, and basic RGB statistics. It does not infer hidden damage.

6. python_exec(args)
   args: {"code": "Python code"}
   Runs controlled Python. Reads are restricted to the event package, current public question, and scratch dir.
   Writes are restricted to scratch dir. Network, computed_gt, solution_en, review, compute_gt, previous runs, and evaluation reports are forbidden.
   Useful for time-series statistics, rolling windows, thresholds, vector-like GeoJSON summaries, image stats, and JSON calculations.
"""


def build_initial_messages(task_dir: Path, package_dir: Path, cfg: dict[str, Any]) -> list[dict[str, str]]:
    task_id = task_dir.name
    event_id = task_id.split("_")[0]
    question = read_text(task_dir / "question_en.md", int(cfg.get("max_question_chars", 12000)))
    evidence_boundary_note = "Strict package-only mode: only the current question and event package evidence are visible."
    if bool(cfg.get("minimal_protocol", False)):
        system = (
            "Return only valid compact JSON. Use local tools to solve the benchmark task. "
            "No prose outside JSON. Do not read computed_gt.json, solution_en.md, review.json, or compute_gt.py. "
            "Use python_exec for calculations when needed."
        )
        user = f"""
Task: {task_id}
Package: {rel_to_repo(package_dir)}
Question:
{question}

Evidence boundary:
{evidence_boundary_note}

Tools:
- list_package_files {{"subdir":".","max_files":80}}
- read_text_file {{"path":"...","max_chars":6000}}
- search_package_files {{"query":"...","glob":"**/*","max_matches":20}}
- summarize_table_or_json {{"path":"..."}}
- inspect_image {{"path":"..."}}
- python_exec {{"code":"..."}}

Reply with one compact JSON object only.
Tool call schema:
{{"action":"tool_call","tool":"list_package_files","args":{{"subdir":".","max_files":80}},"reason":"..."}}
Final schema:
{{"action":"final_answer","final_answer":"...","confidence":0.0,"evidence":[],"reasoning_summary":[],"unsupported_or_unresolved":[]}}

First call list_package_files.
"""
        return [{"role": "system", "content": system}, {"role": "user", "content": user}]
    system = (
        "You are an autonomous extreme-event benchmark solver. You must solve the task by planning, "
        "selecting local files, executing tools, reading observations, and then producing a final JSON answer. "
        "Use only local event-package evidence returned by tools. Do not use web knowledge. "
        "Never read computed_gt.json, solution_en.md, review.json, or compute_gt.py. Prefer deterministic Python calculations when the task asks for metrics. "
        "You must make real tool calls before finalizing. Return only valid JSON in every assistant message."
    )
    user = f"""
Task id: {task_id}
Event id: {event_id}
Question path: {rel_to_repo(task_dir / "question_en.md")}
Event package path: {rel_to_repo(package_dir)}

Question:
```markdown
{question}
```

Evidence boundary:
{evidence_boundary_note}

{TOOL_DESCRIPTIONS}

Output protocol:

For a tool call, return exactly:
{{
  "action": "tool_call",
  "tool": "<tool_name>",
  "args": {{...}},
  "reason": "<why this tool is needed>"
}}

When finished, return exactly:
{{
  "action": "final_answer",
  "final_answer": <answer in the exact format requested by the question>,
  "confidence": 0.0,
  "evidence": [
    {{"claim": "...", "source_file": "event_packages/...", "support_type": "direct_metric|report_claim|metadata|image_context|table_metric|derived_metric|unsupported_boundary"}}
  ],
  "reasoning_summary": ["brief multi-step reasoning"],
  "unsupported_or_unresolved": ["important limits"]
}}

Start by inspecting the package inventory, then choose only the files needed for this event-specific disaster analysis.
"""
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def extract_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    text = text.lstrip("\ufeff")
    decoder = json.JSONDecoder()
    try:
        data, _ = decoder.raw_decode(text)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        data, _ = decoder.raw_decode(fenced.group(1).strip())
        if isinstance(data, dict):
            return data
    for match in re.finditer(r"\{", text):
        try:
            data, _ = decoder.raw_decode(text[match.start() :])
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            continue
    raise ValueError("model response did not contain a JSON object")


def compact_raw_model_text(text: str, limit: int = 4000) -> str:
    text = text or ""
    if len(text) <= limit:
        return text
    return text[:limit] + "\n...[truncated]..."


def summarize_old_observation(content: str, max_chars: int) -> str:
    """Turn one old tool observation into a compact, evidence-first memory entry."""
    step_match = re.search(r"Observation for step\s+(\d+)", content, flags=re.IGNORECASE)
    step = step_match.group(1) if step_match else "?"
    fenced = re.search(r"```(?:json)?\s*(.*?)\s*```", content, flags=re.DOTALL | re.IGNORECASE)
    raw_body = fenced.group(1).strip() if fenced else content.strip()
    parsed: dict[str, Any] | None = None
    try:
        candidate = json.loads(raw_body)
        if isinstance(candidate, dict):
            parsed = candidate
    except json.JSONDecodeError:
        pass

    if parsed is not None:
        tool = str(parsed.get("tool") or "unknown")
        ok = parsed.get("ok")
        evidence = [str(path) for path in (parsed.get("evidence_files") or []) if path]
        warnings = [str(item) for item in (parsed.get("warnings") or []) if item]
        output = parsed.get("output")
    else:
        tool_match = re.search(r'"tool"\s*:\s*"([^"]+)"', raw_body)
        ok_match = re.search(r'"ok"\s*:\s*(true|false)', raw_body, flags=re.IGNORECASE)
        tool = tool_match.group(1) if tool_match else "unknown"
        ok = ok_match.group(1).lower() == "true" if ok_match else "unknown"
        evidence = []
        seen_paths: set[str] = set()
        for path in re.findall(
            r'"((?:event_packages/|tasks/|data/|metadata/|scratch/)[^"]+)"',
            raw_body,
        ):
            if path not in seen_paths:
                seen_paths.add(path)
                evidence.append(path)
        warnings = []
        output = raw_body

    path_text = json.dumps(evidence[:4], ensure_ascii=False, separators=(",", ":"))
    header = f"OBS step={step} tool={tool} ok={str(ok).lower()} evidence={path_text}"
    if warnings:
        header += " warnings=" + compact_text_head_tail(warnings, 180)
    remaining = max(80, max_chars - len(header) - len("\noutput="))
    output_text = output if isinstance(output, str) else json.dumps(
        output,
        ensure_ascii=False,
        separators=(",", ":"),
    )
    entry = header + "\noutput=" + compact_text_head_tail(output_text, remaining)
    return compact_text_head_tail(entry, max_chars)


def build_old_history_summary(messages: list[dict[str, str]], max_chars: int) -> str:
    """Preserve every old observation under a shared budget and omit tool-call boilerplate."""
    observations = [
        str(message.get("content") or "")
        for message in messages
        if message.get("role") == "user"
        and "Observation for step" in str(message.get("content") or "")
    ]
    header = (
        "Earlier tool history was compacted into evidence-first memory. "
        "Assistant tool-call JSON was omitted; each OBS entry retains step, tool status, "
        "evidence paths, and a head/tail view of the result. Re-read a file only when a "
        "required value is absent."
    )
    if not observations:
        fallback = [
            str(message.get("content") or "")
            for message in messages
            if message.get("role") == "user" and str(message.get("content") or "").strip()
        ]
        if not fallback:
            return header
        observations = fallback

    separators = 2 * max(0, len(observations) - 1)
    available = max(80, max_chars - len(header) - separators - 2)
    per_observation = max(80, min(1400, available // max(1, len(observations))))
    entries = [summarize_old_observation(content, per_observation) for content in observations]
    summary = header + "\n\n" + "\n\n".join(entries)
    return compact_text_head_tail(summary, max_chars)


def compact_messages_for_model(
    messages: list[dict[str, str]],
    cfg: dict[str, Any],
) -> list[dict[str, str]]:
    """Bound request context while retaining question, evidence memory, and recent turns."""
    recent_count = max(2, int(cfg.get("context_recent_messages", 16)))
    if recent_count % 2:
        recent_count += 1
    if len(messages) <= 2 + recent_count:
        return messages
    summary_chars = max(1000, int(cfg.get("context_summary_chars", 24000)))
    recent_start = max(2, len(messages) - recent_count)
    summary = build_old_history_summary(messages[2:recent_start], summary_chars)
    request_messages = [dict(messages[0]), dict(messages[1])]
    request_messages.append({"role": "system", "content": summary})
    for message in messages[recent_start:]:
        copied = dict(message)
        limit = 8000 if copied.get("role") == "assistant" else 12000
        copied["content"] = compact_text(copied.get("content", ""), limit)
        request_messages.append(copied)
    return request_messages


def normalize_agent_payload(parsed: dict[str, Any], has_tool_calls: bool) -> dict[str, Any]:
    """Accept common OpenAI-compatible JSON variants without weakening tool access."""
    action = str(parsed.get("action") or parsed.get("type") or "").strip()
    tool = parsed.get("tool") or parsed.get("tool_name")
    args = parsed.get("args") if isinstance(parsed.get("args"), dict) else parsed.get("arguments")
    if isinstance(args, str):
        try:
            args = json.loads(args)
        except json.JSONDecodeError:
            args = {}
    if isinstance(tool, str) and (action in {"", "tool", "tool_call"}):
        return {
            "action": "tool_call",
            "tool": tool,
            "args": args if isinstance(args, dict) else {},
            "reason": parsed.get("reason", parsed.get("rationale", "")),
        }
    if action in {"final", "answer", "final_answer"}:
        return {
            "action": "final_answer",
            "final_answer": parsed.get("final_answer", parsed.get("answer", parsed)),
            "confidence": parsed.get("confidence", 0.0),
            "evidence": parsed.get("evidence", []),
            "reasoning_summary": parsed.get("reasoning_summary", parsed.get("reasoning", [])),
            "unsupported_or_unresolved": parsed.get("unsupported_or_unresolved", []),
        }
    if "final_answer" in parsed and "tool" not in parsed:
        parsed["action"] = "final_answer"
        return parsed
    if has_tool_calls and "tool" not in parsed and "args" not in parsed and "arguments" not in parsed:
        return {
            "action": "final_answer",
            "final_answer": parsed,
            "confidence": parsed.get("confidence", 0.0),
            "evidence": parsed.get("evidence", []),
            "reasoning_summary": parsed.get("reasoning_summary", []),
            "unsupported_or_unresolved": parsed.get("unsupported_or_unresolved", []),
        }
    return parsed


def validate_required_tool_policy(tool_calls: list[dict[str, Any]], cfg: dict[str, Any]) -> dict[str, Any]:
    """Check an optional policy for required, distinct external-tool operations."""
    policy = cfg.get("required_tool_policy")
    if not isinstance(policy, dict) or not policy.get("tool_names"):
        return {
            "enabled": False,
            "compliant": True,
            "tool_names": [],
            "minimum_successful_distinct_calls": 0,
            "target_successful_calls": 0,
            "maximum_counted_calls": 0,
            "successful_calls": 0,
            "distinct_successful_calls": 0,
            "duplicate_successful_calls": 0,
            "corrective_prompt": "",
        }

    tool_names = {str(name) for name in policy.get("tool_names", []) if str(name)}
    excluded_operations = {
        str(name) for name in policy.get("excluded_operations", ["probe"]) if str(name)
    }
    minimum = max(1, int(policy.get("minimum_successful_distinct_calls", 1)))
    target = max(minimum, int(policy.get("target_successful_calls", minimum)))
    maximum = max(target, int(policy.get("maximum_counted_calls", target)))
    successful = [
        call
        for call in tool_calls
        if call.get("ok")
        and str(call.get("tool")) in tool_names
        and str((call.get("args") or {}).get("operation", "")) not in excluded_operations
    ]
    signatures = {
        json.dumps(
            {
                "tool": call.get("tool"),
                "args": call.get("args") if isinstance(call.get("args"), dict) else {},
            },
            sort_keys=True,
            ensure_ascii=False,
            default=str,
        )
        for call in successful
    }
    distinct = min(len(signatures), maximum)
    compliant = distinct >= minimum
    corrective_prompt = ""
    if not compliant:
        allowed = ", ".join(sorted(tool_names))
        corrective_prompt = (
            f"This run requires at least {minimum} successful, distinct operations using {allowed}. "
            f"You currently have {distinct}. Continue with a relevant operation that provides a different "
            "diagnostic or an independent check. Failed, unavailable, not-applicable, probe, and exact "
            "duplicate calls do not count."
        )
    return {
        "enabled": True,
        "compliant": compliant,
        "tool_names": sorted(tool_names),
        "excluded_operations": sorted(excluded_operations),
        "minimum_successful_distinct_calls": minimum,
        "target_successful_calls": target,
        "maximum_counted_calls": maximum,
        "successful_calls": len(successful),
        "distinct_successful_calls": distinct,
        "duplicate_successful_calls": max(0, len(successful) - len(signatures)),
        "corrective_prompt": corrective_prompt,
    }


def call_chat_completion(
    messages: list[dict[str, str]],
    model: str,
    base_url: str,
    api_key: str,
    timeout: int,
    temperature: float | None,
    max_tokens: int | None,
    use_response_format: bool,
) -> tuple[dict[str, Any], str]:
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if max_tokens is not None and max_tokens > 0:
        payload["max_tokens"] = max_tokens
    if use_response_format:
        payload["response_format"] = {"type": "json_object"}
    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8")
    data = json.loads(raw)
    content = data["choices"][0]["message"].get("content")
    if content is None:
        raise ValueError("model returned null assistant content")
    if not isinstance(content, str):
        content = json.dumps(content, ensure_ascii=False)
    return data, content


def call_model_with_retries(
    messages: list[dict[str, str]],
    model: str,
    base_url: str,
    api_key: str,
    cfg: dict[str, Any],
    *,
    deadline: float | None = None,
    retries_override: int | None = None,
) -> tuple[dict[str, Any], str]:
    timeout = int(cfg.get("timeout_seconds", 180))
    retries = int(cfg.get("retries", 2)) if retries_override is None else retries_override
    temperature_raw = cfg.get("temperature", None)
    temperature = None if temperature_raw in (None, "", "default") else float(temperature_raw)
    max_tokens_raw = cfg.get("max_tokens", None)
    max_tokens = None if max_tokens_raw in (None, "", 0, "0", "default") else int(max_tokens_raw)
    use_response_format = bool(cfg.get("use_response_format", False))
    request_messages = compact_messages_for_model(messages, cfg)
    last_exc: BaseException | None = None
    for attempt in range(retries + 1):
        request_timeout = timeout
        if deadline is not None:
            remaining = deadline - time.perf_counter()
            if remaining <= 0:
                raise TimeoutError("model-call deadline exhausted")
            request_timeout = max(1, min(timeout, math.ceil(remaining)))
        try:
            return call_chat_completion(
                request_messages,
                model,
                base_url,
                api_key,
                request_timeout,
                temperature,
                max_tokens,
                use_response_format,
            )
        except MODEL_RUN_EXCEPTIONS as exc:
            last_exc = exc
            if attempt < retries:
                max_retry_delay = max(1.0, float(cfg.get("max_retry_delay_seconds", 60) or 60))
                retry_delay = min(max_retry_delay, 2 ** attempt)
                if isinstance(exc, urllib.error.HTTPError) and exc.code in (429, 503):
                    retry_after = exc.headers.get("Retry-After") if exc.headers else None
                    if retry_after:
                        try:
                            retry_delay = max(retry_delay, min(max_retry_delay, float(retry_after)))
                        except ValueError:
                            pass
                if deadline is not None:
                    remaining = deadline - time.perf_counter()
                    if remaining <= 0:
                        raise TimeoutError("model-call deadline exhausted") from exc
                    retry_delay = min(retry_delay, remaining)
                time.sleep(max(0, retry_delay))
                continue
    raise last_exc or RuntimeError("unknown model call failure")


def resolve_research_budgets(cfg: dict[str, Any]) -> tuple[float, float, float]:
    """Return research, total, and reserved-finalization budgets in seconds."""
    total = max(0.0, float(cfg.get("max_task_wall_seconds", 0) or 0))
    reserve = max(0.0, float(cfg.get("finalization_reserve_seconds", 120) or 0))
    research_raw = cfg.get("max_research_seconds", None)
    if research_raw in (None, "", "default"):
        research = max(0.0, total - reserve) if total > 0 else 0.0
    else:
        research = max(0.0, float(research_raw or 0))
    if total > 0 and research > 0:
        research = min(research, max(0.0, total - reserve))
    return research, total, reserve


def budget_fallback_payload(reason: str, raw_candidate: str = "") -> dict[str, Any]:
    """Keep a run scorable even when the final model call misses its deadline."""
    candidate = raw_candidate.strip()
    final_answer: Any = candidate or {
        "answer": None,
        "status": "budget_exhausted",
        "reason": reason,
    }
    return {
        "action": "final_answer",
        "final_answer": final_answer,
        "confidence": 0.0,
        "evidence": [],
        "reasoning_summary": [
            "The research budget ended before a normal final response was completed."
        ],
        "unsupported_or_unresolved": [reason],
    }


def compact_args_for_trace(tool: str, args: dict[str, Any], code_path: str | None = None) -> dict[str, Any]:
    if tool == "python_exec":
        code = str(args.get("code") or "")
        out = {
            "code_chars": len(code),
            "code_sha1": hashlib.sha1(code.encode("utf-8")).hexdigest()[:12],
            "code_preview": compact_text(code, 600),
        }
        if code_path:
            out["code_path"] = code_path
        return out
    return args


def run_tool(
    tool: str,
    args: dict[str, Any],
    package_dir: Path,
    task_dir: Path,
    scratch_dir: Path,
    code_dir: Path,
    step: int,
    cfg: dict[str, Any],
) -> dict[str, Any]:
    try:
        if tool == "list_package_files":
            return tool_list_package_files(args, package_dir, task_dir, scratch_dir)
        if tool == "read_text_file":
            return tool_read_text_file(args, package_dir, task_dir, scratch_dir)
        if tool == "search_package_files":
            return tool_search_package_files(args, package_dir, task_dir, scratch_dir)
        if tool == "summarize_table_or_json":
            return tool_summarize_table_or_json(args, package_dir, task_dir, scratch_dir)
        if tool == "inspect_image":
            return tool_inspect_image(args, package_dir, task_dir, scratch_dir)
        if tool == "python_exec":
            return tool_python_exec(
                args,
                package_dir,
                task_dir,
                scratch_dir,
                code_dir,
                step,
                int(cfg.get("python_timeout_seconds", 60)),
            )
        return observation(False, f"unknown tool: {tool}", warnings=["unknown tool"])
    except Exception as exc:
        return observation(
            False,
            {
                "tool": tool,
                "error_type": type(exc).__name__,
                "error": str(exc),
            },
            warnings=["tool exception"],
        )


def infer_answer_type(final_answer: Any) -> str:
    if isinstance(final_answer, dict):
        return "json"
    if isinstance(final_answer, list):
        return "ranking"
    text = str(final_answer).strip()
    if re.fullmatch(r"[A-E](?:\s*,\s*[A-E])*", text):
        return "multiple_choice"
    if len(text) > 500:
        return "briefing"
    return "short_text"


def error_result(
    task_dir: Path,
    model: str,
    package_dir: Path,
    out_root: Path,
    base_url: str,
    error: str,
    cfg: dict[str, Any] | None = None,
) -> dict[str, Any]:
    task_id = task_dir.name
    event_id = task_id.split("_")[0]
    cfg = cfg or {}
    run_dir = out_root / safe_model_name(model) / task_id
    run_dir.mkdir(parents=True, exist_ok=True)
    trajectory = {
        "task_id": task_id,
        "event_id": event_id,
        "question_path": rel_to_repo(task_dir / "question_en.md"),
        "event_package_path": rel_to_repo(package_dir),
        "tool_profile": "minimum_10",
        "run_status": "error",
        "blind_solve": True,
        "forbidden_files_checked": True,
        "evidence_boundary": "current_question_and_event_package_only",
        "answer_type": "unknown",
        "final_answer": {"error": error},
        "confidence": 0.0,
        "tool_calls": [],
        "evidence": [],
        "reasoning_summary": [],
        "unsupported_or_unresolved": [error],
        "model": model,
        "api_base_url": base_url,
    }
    write_json(run_dir / "trajectory.json", trajectory)
    write_text(run_dir / "answer.md", f"# {task_id} Tool-Agent Answer\n\nERROR: {error}\n")
    write_text(run_dir / "tool_trace.md", f"# {task_id} Tool Trace\n\nNo successful tool-agent trajectory. Error: {error}\n")
    write_text(
        run_dir / "run_notes.md",
        "Tool-agent run failed before completion. Forbidden files were not intentionally used. "
        "Network access was not available to local tools; only model API calls were made.\n",
    )
    return {"task_id": task_id, "model": model, "status": "error", "latency_s": 0.0, "error": error}


def _solve_one_unlocked(
    task_dir: Path,
    model: str,
    package_root: Path,
    out_root: Path,
    cfg: dict[str, Any],
    api_key: str,
    base_url: str,
    force: bool,
) -> dict[str, Any]:
    task_id = task_dir.name
    event_id = task_id.split("_")[0]
    package_dir = package_root / event_id
    run_dir = out_root / safe_model_name(model) / task_id
    trajectory_path = run_dir / "trajectory.json"
    if not force and trajectory_path.exists():
        try:
            existing = load_json(trajectory_path)
        except (OSError, ValueError, json.JSONDecodeError):
            existing = {}
        if existing.get("run_status") == "ok":
            return {"task_id": task_id, "model": model, "status": "skipped", "latency_s": 0.0}
    if not package_dir.exists():
        return error_result(task_dir, model, package_dir, out_root, base_url, f"missing package: {package_dir}", cfg)

    scratch_dir = run_dir / "scratch"
    code_dir = run_dir / "python_snippets"
    scratch_dir.mkdir(parents=True, exist_ok=True)
    code_dir.mkdir(parents=True, exist_ok=True)

    messages = build_initial_messages(task_dir, package_dir, cfg)
    transcript: list[dict[str, Any]] = []
    tool_calls: list[dict[str, Any]] = []
    raw_usage: list[dict[str, Any]] = []
    max_turns_raw = cfg.get("max_agent_turns", 12)
    unlimited_turns = max_turns_raw in (None, "", 0, "0", "none", "None", "null", "Null", "unlimited", "Unlimited")
    max_turns = None if unlimited_turns else int(max_turns_raw)
    observation_max_chars = int(cfg.get("observation_max_chars", 12000))
    started = time.perf_counter()
    max_research_seconds, max_task_wall_seconds, finalization_reserve_seconds = (
        resolve_research_budgets(cfg)
    )
    research_deadline = started + max_research_seconds if max_research_seconds > 0 else None
    total_deadline = started + max_task_wall_seconds if max_task_wall_seconds > 0 else None

    final_payload: dict[str, Any] | None = None
    step = 1
    parse_error_count = 0
    max_parse_repairs = int(cfg.get("max_parse_repairs", 2))
    termination_reason = "round_limit"
    forced_finalization = False
    required_tool_policy_rejections = 0
    while unlimited_turns or (max_turns is not None and step <= max_turns):
        if research_deadline is not None and time.perf_counter() >= research_deadline:
            termination_reason = "research_time_limit"
            break
        try:
            raw_data, content = call_model_with_retries(
                messages,
                model,
                base_url,
                api_key,
                cfg,
                deadline=research_deadline,
            )
        except TimeoutError:
            if research_deadline is not None and time.perf_counter() >= research_deadline:
                termination_reason = "research_time_limit"
                break
            raise
        raw_usage.append((raw_data or {}).get("usage", {}))
        try:
            parsed = normalize_agent_payload(extract_json_object(content), bool(tool_calls))
        except ValueError as exc:
            parse_error_count += 1
            transcript.append({
                "step": step,
                "assistant_parse_error": str(exc),
                "raw_content": compact_raw_model_text(content),
            })
            if parse_error_count > max_parse_repairs:
                raise ValueError(f"model response did not follow the EarthVerse agent JSON protocol after {max_parse_repairs} repair prompts")
            messages.append({"role": "assistant", "content": compact_raw_model_text(content)})
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "Your previous message was not valid JSON for this benchmark runner. "
                        "Return one JSON object only, with action='tool_call' or action='final_answer'. "
                        "If you already have the answer, wrap it inside {'action':'final_answer','final_answer':...}. "
                        "Do not include Markdown fences or prose."
                    ),
                }
            )
            step += 1
            continue
        transcript.append({"step": step, "assistant": parsed, "raw_content": content})
        action = str(parsed.get("action") or "").strip()
        if action == "final_answer" or "final_answer" in parsed and "tool" not in parsed:
            required_status = validate_required_tool_policy(tool_calls, cfg)
            if not required_status["compliant"]:
                required_tool_policy_rejections += 1
                transcript[-1]["required_tool_policy_rejected"] = True
                transcript[-1]["required_tool_policy_status"] = required_status
                messages.append({"role": "assistant", "content": content})
                messages.append({"role": "user", "content": required_status["corrective_prompt"]})
                step += 1
                continue
            final_payload = parsed
            termination_reason = "model_final"
            break
        if action != "tool_call":
            messages.append({"role": "assistant", "content": content})
            messages.append(
                {
                    "role": "user",
                    "content": "Invalid protocol. Return a JSON object with action='tool_call' or action='final_answer'.",
                }
            )
            step += 1
            continue

        tool = str(parsed.get("tool") or "")
        args = parsed.get("args") if isinstance(parsed.get("args"), dict) else {}
        result = run_tool(tool, args, package_dir, task_dir, scratch_dir, code_dir, step, cfg)
        code_path = None
        if tool == "python_exec" and isinstance(result.get("output"), dict):
            code_path = result["output"].get("code_path")
        call_record = {
            "step": len(tool_calls) + 1,
            "tool": tool,
            "args": compact_args_for_trace(tool, args, code_path),
            "ok": bool(result.get("ok")),
            "output_summary": compact_text(result.get("output"), int(cfg.get("tool_summary_chars", 1800))),
            "warnings": result.get("warnings") or [],
            "evidence_files": result.get("evidence_files") or [],
            "reason": parsed.get("reason", ""),
        }
        tool_calls.append(call_record)
        obs_text = compact_text(
            {
                "tool": tool,
                "ok": result.get("ok"),
                "output": result.get("output"),
                "evidence_files": result.get("evidence_files"),
                "warnings": result.get("warnings"),
            },
            observation_max_chars,
        )
        messages.append({"role": "assistant", "content": content})
        messages.append({"role": "user", "content": f"Observation for step {step}:\n```json\n{obs_text}\n```"})
        step += 1

    if final_payload is None:
        forced_finalization = True
        messages.append(
            {
                "role": "user",
                "content": (
                    f"Research must stop because {termination_reason} was reached. Do not call another tool. "
                    "Return the best final_answer JSON now, using only observations already collected. "
                    "Preserve the exact answer schema requested by the question and explicitly mark unresolved fields."
                ),
            }
        )
        finalization_timeout = max(
            1.0,
            float(cfg.get("finalization_timeout_seconds", finalization_reserve_seconds or 120) or 120),
        )
        finalization_deadline = time.perf_counter() + finalization_timeout
        if total_deadline is not None:
            finalization_deadline = min(finalization_deadline, total_deadline)
        content = ""
        try:
            raw_data, content = call_model_with_retries(
                messages,
                model,
                base_url,
                api_key,
                cfg,
                deadline=finalization_deadline,
                retries_override=0,
            )
            raw_usage.append((raw_data or {}).get("usage", {}))
            parsed = normalize_agent_payload(extract_json_object(content), bool(tool_calls))
            final_payload = parsed if "final_answer" in parsed else {"final_answer": parsed}
        except MODEL_RUN_EXCEPTIONS:
            final_payload = budget_fallback_payload(termination_reason, content)
            termination_reason += "_fallback"
        transcript.append(
            {
                "step": step,
                "assistant": final_payload,
                "raw_content": content,
                "forced_finalization": True,
                "termination_reason": termination_reason,
            }
        )

    latency = time.perf_counter() - started
    final_answer = final_payload.get("final_answer", final_payload)
    confidence = final_payload.get("confidence", None)
    try:
        confidence = float(confidence)
    except (TypeError, ValueError):
        confidence = None
    if confidence is not None:
        confidence = min(1.0, max(0.0, confidence))

    trajectory = {
        "task_id": task_id,
        "event_id": event_id,
        "question_path": rel_to_repo(task_dir / "question_en.md"),
        "event_package_path": rel_to_repo(package_dir),
        "tool_profile": "minimum_10",
        "max_agent_turns": max_turns,
        "unlimited_agent_turns": unlimited_turns,
        "max_research_seconds": max_research_seconds,
        "max_task_wall_seconds": max_task_wall_seconds,
        "finalization_reserve_seconds": finalization_reserve_seconds,
        "forced_finalization": forced_finalization,
        "termination_reason": termination_reason,
        "run_status": "ok",
        "blind_solve": True,
        "forbidden_files_checked": True,
        "evidence_boundary": "current_question_and_event_package_only",
        "answer_type": infer_answer_type(final_answer),
        "final_answer": final_answer,
        "confidence": confidence,
        "tool_calls": tool_calls,
        "required_tool_policy": validate_required_tool_policy(tool_calls, cfg),
        "required_tool_policy_rejections": required_tool_policy_rejections,
        "evidence": final_payload.get("evidence") if isinstance(final_payload.get("evidence"), list) else [],
        "reasoning_summary": final_payload.get("reasoning_summary") if isinstance(final_payload.get("reasoning_summary"), list) else [],
        "unsupported_or_unresolved": final_payload.get("unsupported_or_unresolved") if isinstance(final_payload.get("unsupported_or_unresolved"), list) else [],
        "model": model,
        "api_base_url": base_url,
        "latency_s": round(latency, 3),
        "raw_usage": raw_usage,
        "agent_runner": "crossscale_react_v2",
    }

    write_json(run_dir / "trajectory.json", trajectory)
    write_text(
        run_dir / "answer.md",
        f"# {task_id} Tool-Agent Answer\n\n## Final Answer\n\n```json\n{json.dumps(final_answer, indent=2, ensure_ascii=False)}\n```\n\n"
        f"## Reasoning Summary\n\n"
        + "\n".join(f"- {x}" for x in trajectory["reasoning_summary"])
        + "\n\n## Evidence\n\n"
        + "\n".join(
            f"- `{item.get('source_file', '')}`: {item.get('claim', '')}"
            for item in trajectory["evidence"]
            if isinstance(item, dict)
        )
        + "\n",
    )
    write_text(
        run_dir / "tool_trace.md",
        "# Tool-Agent Trace\n\n"
        "| Step | Tool | OK | Evidence | Summary |\n| ---: | --- | --- | --- | --- |\n"
        + "\n".join(
            "| {step} | `{tool}` | {ok} | {evidence_count} files | {summary} |".format(
                step=call["step"],
                tool=call["tool"],
                ok=call["ok"],
                evidence_count=len(call.get("evidence_files") or []),
                summary=str(call.get("output_summary", "")).replace("\n", " ")[:500],
            )
            for call in tool_calls
        )
        + "\n",
    )
    write_text(
        run_dir / "run_notes.md",
        "This is an iterative tool-agent run. The model did not receive computed_gt.json, solution_en.md, review.json, or compute_gt.py. "
        "Forbidden files were checked at the tool layer and in Python execution. "
        "Evidence was limited to the current public question and the local event package. "
        "Local tools had no web/network access; only the model API call used the network. "
        "Python writes were restricted to the task scratch directory.\n",
    )
    write_json(run_dir / "raw_conversation.json", {"messages": messages, "transcript": transcript, "usage": raw_usage})

    return {
        "task_id": task_id,
        "model": model,
        "status": "ok",
        "latency_s": round(latency, 3),
        "tool_calls": len(tool_calls),
        "ok_tool_calls": sum(1 for call in tool_calls if call.get("ok")),
        "answer_type": trajectory["answer_type"],
    }


def solve_one(
    task_dir: Path,
    model: str,
    package_root: Path,
    out_root: Path,
    cfg: dict[str, Any],
    api_key: str,
    base_url: str,
    force: bool,
) -> dict[str, Any]:
    """Run one task while preventing duplicate work across runner processes."""
    task_id = task_dir.name
    model_root = out_root / safe_model_name(model)
    lock_dir = model_root / ".locks"
    lock_dir.mkdir(parents=True, exist_ok=True)
    lock_path = lock_dir / f"{task_id}.lock"
    lock_handle = lock_path.open("a+b")
    try:
        lock_handle.seek(0, os.SEEK_END)
        if lock_handle.tell() == 0:
            lock_handle.write(b"\0")
            lock_handle.flush()
        lock_handle.seek(0)
        if os.name == "nt":
            import msvcrt

            msvcrt.locking(lock_handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except (BlockingIOError, OSError):
        lock_handle.close()
        return {"task_id": task_id, "model": model, "status": "skipped", "latency_s": 0.0}
    try:
        lock_handle.seek(0)
        lock_handle.truncate()
        lock_handle.write(f"pid={os.getpid()}\nstarted={time.time()}\n".encode("ascii"))
        lock_handle.flush()
        return _solve_one_unlocked(task_dir, model, package_root, out_root, cfg, api_key, base_url, force)
    finally:
        try:
            lock_handle.seek(0)
            if os.name == "nt":
                msvcrt.locking(lock_handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)
        finally:
            lock_handle.close()


def run_model(model: str, task_dirs: list[Path], cfg: dict[str, Any], workers: int, force: bool) -> list[dict[str, Any]]:
    api_key = os.environ.get(cfg.get("api_key_env", "OPENAI_API_KEY"))
    if not api_key:
        raise SystemExit(f"{cfg.get('api_key_env', 'OPENAI_API_KEY')} is not set.")
    base_url = os.environ.get(cfg.get("base_url_env", "OPENAI_BASE_URL"), cfg.get("default_base_url", "https://api.openai.com/v1"))
    package_root = repo_path(cfg.get("package_dir", "event_packages/standard_event_packages/packages"))
    out_root = repo_path(cfg.get("output_root", "outputs/openai_tool_agent"))
    results: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
        future_map = {
            executor.submit(solve_one, task_dir, model, package_root, out_root, cfg, api_key, base_url, force): task_dir
            for task_dir in task_dirs
        }
        for future in as_completed(future_map):
            task_dir = future_map[future]
            try:
                result = future.result()
            except Exception as exc:
                package_dir = package_root / task_dir.name.split("_")[0]
                result = error_result(task_dir, model, package_dir, out_root, base_url, f"{type(exc).__name__}: {exc}", cfg)
            results.append(result)
            print(json.dumps(result, ensure_ascii=False))
    return sorted(results, key=lambda item: item["task_id"])


def estimate_runtime(results: list[dict[str, Any]], total_tasks: int, workers: int) -> dict[str, Any]:
    ok_latencies = [float(r["latency_s"]) for r in results if r.get("status") == "ok" and float(r.get("latency_s", 0)) > 0]
    if not ok_latencies:
        return {"estimated_seconds": None}
    mean_latency = statistics.fmean(ok_latencies)
    p95_latency = sorted(ok_latencies)[max(0, int(0.95 * (len(ok_latencies) - 1)))]
    mean_tool_calls = statistics.fmean(float(r.get("tool_calls", 0)) for r in results if r.get("status") == "ok")
    return {
        "mean_latency_s": round(mean_latency, 2),
        "p95_latency_s": round(p95_latency, 2),
        "mean_tool_calls": round(mean_tool_calls, 2),
        "workers": workers,
        "total_tasks": total_tasks,
        "estimated_seconds_mean": round(total_tasks * mean_latency / max(1, workers), 1),
        "estimated_seconds_p95": round(total_tasks * p95_latency / max(1, workers), 1),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run OpenAI-compatible models as iterative local-tool agents.")
    parser.add_argument("--config", default="configs/evaluation.json")
    parser.add_argument("--models", default="", help="Comma-separated model names. Default: all config models.")
    parser.add_argument("--workers", type=int, default=0, help="Override workers for every model.")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--task-id", action="append", default=[])
    parser.add_argument("--task-file", default="", help="Newline-separated task ids to run.")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = load_mode_config(repo_path(args.config), "agent")
    task_ids = list(args.task_id) + load_task_ids(repo_path(args.task_file) if args.task_file else None)
    task_dirs = iter_task_dirs(repo_path(cfg.get("task_dir", "tasks")), args.limit, task_ids)
    configured_models = cfg.get("models", [])
    if args.models:
        wanted = {x.strip() for x in args.models.split(",") if x.strip()}
        models = [m for m in configured_models if m["name"] in wanted]
        missing = wanted - {m["name"] for m in models}
        if missing:
            models.extend({"name": name, "workers": args.workers or 4} for name in sorted(missing))
    else:
        models = configured_models
    summary = {"task_count": len(task_dirs), "models": [], "started_at": time.strftime("%Y-%m-%dT%H:%M:%S")}
    out_root = repo_path(cfg.get("output_root", "outputs/openai_tool_agent"))
    for model_cfg in models:
        model = model_cfg["name"]
        workers = args.workers or int(model_cfg.get("workers", 4))
        started = time.perf_counter()
        results = run_model(model, task_dirs, cfg, workers=workers, force=args.force)
        elapsed = time.perf_counter() - started
        model_summary = {
            "model": model,
            "workers": workers,
            "elapsed_s": round(elapsed, 2),
            "results": {
                "ok": sum(1 for r in results if r.get("status") == "ok"),
                "error": sum(1 for r in results if r.get("status") == "error"),
                "skipped": sum(1 for r in results if r.get("status") == "skipped"),
            },
            "run_estimate": estimate_runtime(results, len(task_dirs), workers),
        }
        summary["models"].append(model_summary)
        write_json(out_root / safe_model_name(model) / "run_summary.json", {"model_summary": model_summary, "task_results": results})
    summary["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    write_json(out_root / "latest_run_summary.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
