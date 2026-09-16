#!/usr/bin/env python3
"""Run OpenAI-compatible models on EarthVerse tasks.

The runner creates model output folders compatible with scripts/judge.py:
trajectory.json, answer.md, tool_trace.md, and run_notes.md.

It does not read computed_gt.json, solution_en.md, review.json, or
compute_gt.py. It builds a prompt context from each event package and asks the
model to answer the task. Supported context modes range from compact selected
evidence to budgeted all-readable-text package input.
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import statistics
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
TEXT_SUFFIXES = {".json", ".csv", ".md", ".txt", ".html", ".htm", ".shtml", ".xml", ".php", ".aspx"}
SKIP_NAMES = {"computed_gt.json", "solution_en.md", "review.json", "compute_gt.py"}
RETRYABLE_EXCEPTIONS = (
    urllib.error.HTTPError,
    urllib.error.URLError,
    http.client.RemoteDisconnected,
    ConnectionResetError,
    TimeoutError,
    OSError,
)
MODEL_RUN_EXCEPTIONS = RETRYABLE_EXCEPTIONS + (ValueError, json.JSONDecodeError)


def read_text(path: Path, max_chars: int | None = None) -> str:
    data = path.read_text(encoding="utf-8-sig", errors="replace")
    if max_chars is not None and max_chars > 0 and len(data) > max_chars:
        return data[:max_chars] + "\n...[TRUNCATED]..."
    return data


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def compact(text: str, max_chars: int) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 80] + "\n...[TRUNCATED]..."


def load_mode_config(path: Path, mode: str) -> dict[str, Any]:
    data = read_json(path)
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


def rel_to_repo(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def load_task_ids(path: Path | None) -> list[str]:
    if not path:
        return []
    return [line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def iter_task_dirs(task_root: Path, limit: int = 0, task_ids: list[str] | None = None) -> list[Path]:
    wanted = set(task_ids or [])
    dirs = [p for p in sorted(task_root.iterdir()) if p.is_dir() and (p / "question_en.md").exists()]
    if wanted:
        dirs = [p for p in dirs if p.name in wanted]
    if limit > 0:
        dirs = dirs[:limit]
    return dirs


def package_inventory(package_dir: Path, max_chars: int) -> str:
    files_csv = package_dir / "metadata" / "files.csv"
    if files_csv.exists():
        return read_text(files_csv, max_chars)
    rows = []
    for path in sorted(package_dir.rglob("*")):
        if path.is_file():
            rows.append(f"{path.relative_to(package_dir)}\t{path.stat().st_size}")
    return compact("\n".join(rows), max_chars)


def configured_text_suffixes(cfg: dict[str, Any]) -> set[str]:
    raw = cfg.get("text_suffixes")
    if not raw:
        return set(TEXT_SUFFIXES)
    return {str(item).lower() if str(item).startswith(".") else f".{str(item).lower()}" for item in raw}


def priority_package_files(package_dir: Path) -> list[Path]:
    return [
        package_dir / "metadata" / "event.json",
        package_dir / "README.md",
        package_dir / "metadata" / "files.csv",
        package_dir / "metadata" / "sources.csv",
    ]


def selected_context_files(package_dir: Path, max_files: int, context_mode: str = "preferred", text_suffixes: set[str] | None = None) -> list[Path]:
    text_suffixes = text_suffixes or TEXT_SUFFIXES
    if context_mode in {"full_package_text", "all_text_budgeted", "all_package_text"}:
        seen: set[Path] = set()
        out: list[Path] = []
        for path in priority_package_files(package_dir) + sorted(package_dir.rglob("*")):
            if not path.is_file() or path.name in SKIP_NAMES or path in seen:
                continue
            if path.suffix.lower() not in text_suffixes:
                continue
            seen.add(path)
            out.append(path)
            if max_files > 0 and len(out) >= max_files:
                return out
        return out

    preferred_patterns = [
        "metadata/event.json",
        "README.md",
        "data/event_reports/*",
        "data/physical_hazard/*",
        "data/exposure_impact/*",
        "data/remote_sensing/*.json",
        "data/geospatial_context/*.json",
        "data/event_catalogs/*.json",
    ]
    seen: set[Path] = set()
    out: list[Path] = []
    for pattern in preferred_patterns:
        for path in sorted(package_dir.glob(pattern)):
            if not path.is_file() or path.name in SKIP_NAMES or path in seen:
                continue
            if path.suffix.lower() not in text_suffixes:
                continue
            seen.add(path)
            out.append(path)
            if max_files > 0 and len(out) >= max_files:
                return out
    return out


def context_rel(event_id: str, rel: str) -> str:
    return f"event_packages/standard_event_packages/packages/{event_id}/{rel}"


def count_package_files(package_dir: Path, text_suffixes: set[str]) -> dict[str, int]:
    counts = {
        "package_files_total": 0,
        "readable_text_files_total": 0,
        "non_text_files_total": 0,
    }
    if not package_dir.exists():
        return counts
    for path in package_dir.rglob("*"):
        if not path.is_file() or path.name in SKIP_NAMES:
            continue
        counts["package_files_total"] += 1
        if path.suffix.lower() in text_suffixes:
            counts["readable_text_files_total"] += 1
        else:
            counts["non_text_files_total"] += 1
    return counts


def append_file_section(
    sections: list[str],
    path: Path,
    rel: str,
    remaining_chars: int | None,
    max_file_chars: int,
    allow_partial_last_file: bool,
) -> tuple[int | None, dict[str, Any]]:
    raw_text = read_text(path)
    file_chars = len(raw_text)
    file_bytes = path.stat().st_size
    per_file_truncated = max_file_chars > 0 and file_chars > max_file_chars
    text = raw_text[:max_file_chars] + "\n...[TRUNCATED_BY_FILE_LIMIT]..." if per_file_truncated else raw_text
    section_prefix = f"# File: {rel}\n"
    section = section_prefix + text
    entry: dict[str, Any] = {
        "path": rel,
        "bytes": file_bytes,
        "source_chars": file_chars,
        "included_chars": 0,
        "status": "included",
        "truncated_by_file_limit": per_file_truncated,
        "truncated_by_context_budget": False,
    }
    if remaining_chars is not None and len(section) > remaining_chars:
        if not allow_partial_last_file or remaining_chars <= len(section_prefix) + 40:
            entry["status"] = "skipped"
            entry["reason"] = "context_budget_exhausted"
            return remaining_chars, entry
        keep_chars = max(0, remaining_chars - len(section_prefix) - 40)
        text = text[:keep_chars] + "\n...[TRUNCATED_BY_CONTEXT_BUDGET]..."
        section = section_prefix + text
        entry["status"] = "truncated"
        entry["truncated_by_context_budget"] = True
    sections.append(section)
    entry["included_chars"] = len(text)
    if entry["truncated_by_file_limit"] or entry["truncated_by_context_budget"]:
        entry["status"] = "truncated"
    if remaining_chars is None:
        return None, entry
    return max(0, remaining_chars - len(section) - 2), entry


def build_context(task_dir: Path, package_root: Path, cfg: dict[str, Any]) -> tuple[str, list[str], dict[str, Any]]:
    task_id = task_dir.name
    event_id = task_id.split("_")[0]
    package_dir = package_root / event_id
    question = read_text(task_dir / "question_en.md")
    max_context_chars = int(cfg.get("max_context_chars", 36000))
    max_file_chars = int(cfg.get("max_file_chars", 2200))
    max_context_files = int(cfg.get("max_context_files", 18))
    context_mode = str(cfg.get("context_mode") or "preferred")
    text_suffixes = configured_text_suffixes(cfg)
    all_text_mode = context_mode in {"all_text_budgeted", "all_package_text"}
    allow_partial_last_file = bool(cfg.get("allow_partial_last_file", all_text_mode))

    sections = [
        "# Question\n" + question.strip(),
        "# Package inventory\n" + package_inventory(package_dir, 10000),
    ]
    evidence_files: list[str] = []
    selected_files: list[Path] = []
    file_entries: list[dict[str, Any]] = []
    remaining_chars: int | None = None
    if max_context_chars > 0:
        summary_reserve = int(cfg.get("context_summary_reserve_chars", 2500)) if all_text_mode else 0
        fixed_chars = len("\n\n".join(sections)) + 2 + summary_reserve
        remaining_chars = max(0, max_context_chars - fixed_chars)

    if package_dir.exists():
        selected_files = selected_context_files(package_dir, max_context_files, context_mode, text_suffixes)
        for path in selected_files:
            rel = path.relative_to(package_dir).as_posix()
            remaining_chars, entry = append_file_section(
                sections,
                path,
                rel,
                remaining_chars if all_text_mode else None,
                max_file_chars,
                allow_partial_last_file,
            )
            file_entries.append(entry)
            if entry["status"] in {"included", "truncated"}:
                evidence_files.append(context_rel(event_id, rel))
            if all_text_mode and remaining_chars == 0:
                break

    selected_rel = {entry["path"] for entry in file_entries}
    if package_dir.exists() and all_text_mode:
        for path in selected_context_files(package_dir, 0, context_mode, text_suffixes):
            rel = path.relative_to(package_dir).as_posix()
            if rel not in selected_rel:
                file_entries.append({
                    "path": rel,
                    "bytes": path.stat().st_size,
                    "source_chars": None,
                    "included_chars": 0,
                    "status": "skipped",
                    "reason": "context_budget_exhausted",
                })
                selected_rel.add(rel)

    counts = count_package_files(package_dir, text_suffixes)
    included_count = sum(1 for entry in file_entries if entry.get("status") == "included")
    truncated_count = sum(1 for entry in file_entries if entry.get("status") == "truncated")
    skipped_count = sum(1 for entry in file_entries if entry.get("status") == "skipped")
    context_meta = {
        "context_mode": context_mode,
        "package_exists": package_dir.exists(),
        "max_context_chars": max_context_chars,
        "max_file_chars": max_file_chars,
        "max_context_files": max_context_files,
        "text_suffixes": sorted(text_suffixes),
        **counts,
        "candidate_text_files": len(selected_files),
        "embedded_text_files": included_count + truncated_count,
        "included_text_files": included_count,
        "truncated_text_files": truncated_count,
        "skipped_text_files": skipped_count,
        "non_text_files_not_embedded": counts["non_text_files_total"],
        "embedded_file_chars": sum(int(entry.get("included_chars") or 0) for entry in file_entries),
        "files": file_entries,
    }
    if all_text_mode:
        summary_section = "# Context coverage summary\n" + json.dumps({
            key: value
            for key, value in context_meta.items()
            if key != "files"
        }, indent=2, ensure_ascii=False)
        sections.insert(2, summary_section)

    context = "\n\n".join(sections)
    if not all_text_mode and max_context_chars > 0:
        context = compact(context, max_context_chars)
    context_meta["final_context_chars"] = len(context)
    return context, evidence_files, context_meta


def build_messages(task_dir: Path, package_root: Path, cfg: dict[str, Any]) -> tuple[list[dict[str, str]], list[str], int, dict[str, Any]]:
    context, evidence_files, context_meta = build_context(task_dir, package_root, cfg)
    system = (
        "You are solving a local extreme-event benchmark task. Use only the local "
        "package evidence included in the prompt. Do not use outside knowledge as "
        "evidence. Return a JSON object with final_answer, rationale, evidence_files, "
        "and limitations. final_answer must follow the question's requested format."
    )
    user = f"""
Solve the benchmark task below using only the provided local package context.

Return only valid JSON with this schema:
{{
  "final_answer": "object | array | string matching the requested answer format",
  "rationale": "brief evidence-based reasoning",
  "evidence_files": ["relative file paths used"],
  "limitations": ["what the package evidence cannot prove"]
}}

Local context:
```text
{context}
```
    """
    estimated_prompt_tokens = max(1, (len(system) + len(user)) // 4)
    return [{"role": "system", "content": system}, {"role": "user", "content": user}], evidence_files, estimated_prompt_tokens, context_meta


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
        try:
            data, _ = decoder.raw_decode(fenced.group(1).strip())
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            pass
    for match in re.finditer(r"\{", text):
        try:
            data, _ = decoder.raw_decode(text[match.start() :])
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            continue
    raise ValueError("model response did not contain a JSON object")


def call_chat_completion(
    messages: list[dict[str, str]],
    model: str,
    base_url: str,
    api_key: str,
    timeout: int,
    temperature: float | None,
    use_response_format: bool,
    max_tokens: int = 0,
) -> tuple[dict[str, Any], str]:
    payload: dict[str, Any] = {
        "model": model,
        "messages": messages,
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if max_tokens > 0:
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
    content = data["choices"][0]["message"]["content"]
    return data, content


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
    task_id = task_dir.name
    event_id = task_id.split("_")[0]
    safe_model = model.replace("/", "__").replace(":", "_")
    run_dir = out_root / safe_model / task_id
    if not force and (run_dir / "trajectory.json").exists():
        return {"task_id": task_id, "model": model, "status": "skipped", "latency_s": 0.0}

    messages, context_files, prompt_tokens, context_meta = build_messages(task_dir, package_root, cfg)
    timeout = int(cfg.get("timeout_seconds", 180))
    retries = int(cfg.get("retries", 2))
    temperature_raw = cfg.get("temperature", None)
    temperature = None if temperature_raw in (None, "", "default") else float(temperature_raw)
    use_response_format = bool(cfg.get("use_response_format", False))
    max_tokens = int(cfg.get("max_tokens", 0) or cfg.get("max_completion_tokens", 0) or 0)

    started = time.perf_counter()
    last_error = ""
    raw_data: dict[str, Any] | None = None
    content = ""
    parsed: dict[str, Any] = {}
    for attempt in range(retries + 1):
        try:
            raw_data, content = call_chat_completion(
                messages,
                model=model,
                base_url=base_url,
                api_key=api_key,
                timeout=timeout,
                temperature=temperature,
                use_response_format=use_response_format,
                max_tokens=max_tokens,
            )
            parsed = extract_json_object(content)
            break
        except MODEL_RUN_EXCEPTIONS as exc:
            last_error = str(exc)
            if attempt >= retries:
                latency = time.perf_counter() - started
                run_dir.mkdir(parents=True, exist_ok=True)
                write_text(run_dir / "answer.md", f"# {task_id} Answer\n\nERROR: {last_error}\n")
                write_json(run_dir / "trajectory.json", {
                    "task_id": task_id,
                    "event_id": event_id,
                    "question_path": rel_to_repo(task_dir / "question_en.md"),
                    "event_package_path": f"event_packages/standard_event_packages/packages/{event_id}",
                    "tool_profile": str(cfg.get("context_mode", "preferred")),
                    "blind_solve": True,
                    "answer_type": "error",
                    "final_answer": {"error": last_error},
                    "tool_calls": [],
                    "model": model,
                    "api_base_url": base_url,
                    "context_manifest": context_meta,
                    "latency_s": round(latency, 3),
                })
                write_json(run_dir / "context_manifest.json", context_meta)
                write_text(run_dir / "tool_trace.md", f"# {task_id} Tool Trace\n\nAPI error: {last_error}\n")
                write_text(run_dir / "run_notes.md", "No forbidden answer-key or compute files were used. No web evidence was used; only local package evidence was provided to the model prompt.\n")
                return {"task_id": task_id, "model": model, "status": "error", "latency_s": latency, "error": last_error}
            time.sleep(min(20, 2 ** attempt))

    latency = time.perf_counter() - started
    final_answer = parsed.get("final_answer", parsed)
    rationale = parsed.get("rationale", "")
    evidence_files = parsed.get("evidence_files") or context_files[:8]
    limitations = parsed.get("limitations", [])

    trajectory = {
        "task_id": task_id,
        "event_id": event_id,
        "question_path": rel_to_repo(task_dir / "question_en.md"),
        "event_package_path": f"event_packages/standard_event_packages/packages/{event_id}",
        "tool_profile": str(cfg.get("context_mode", "preferred")),
        "blind_solve": True,
        "answer_type": "json",
        "final_answer": final_answer,
        "confidence": None,
        "tool_calls": [
            {
                "step": 1,
                "tool": "read_question",
                "args": {"path": str(task_dir / "question_en.md").replace("\\", "/")},
                "ok": True,
                "output_summary": "Read benchmark question.",
                "warnings": [],
                "evidence_files": [],
            },
            {
                "step": 2,
                "tool": "build_direct_prompt_context",
                "args": {
                    "event_id": event_id,
                    "context_mode": cfg.get("context_mode", "preferred"),
                    "max_context_chars": cfg.get("max_context_chars", 36000),
                    "max_context_files": cfg.get("max_context_files", 18),
                    "max_file_chars": cfg.get("max_file_chars", 2200),
                },
                "ok": True,
                "output_summary": (
                    f"Built {context_meta.get('context_mode')} prompt context from "
                    f"{context_meta.get('included_text_files', len(context_files))} full and "
                    f"{context_meta.get('truncated_text_files', 0)} truncated local package text files; "
                    f"{context_meta.get('skipped_text_files', 0)} readable text files were skipped by budget."
                ),
                "warnings": [],
                "evidence_files": context_files,
            },
            {
                "step": 3,
                "tool": "openai_chat_completion",
                "args": {"model": model},
                "ok": True,
                "output_summary": "Model returned a JSON answer.",
                "warnings": [],
                "evidence_files": evidence_files if isinstance(evidence_files, list) else [],
            },
        ],
        "model": model,
        "api_base_url": base_url,
        "estimated_prompt_tokens": prompt_tokens,
        "context_manifest": context_meta,
        "latency_s": round(latency, 3),
        "raw_usage": (raw_data or {}).get("usage", {}),
    }

    run_dir.mkdir(parents=True, exist_ok=True)
    write_json(run_dir / "trajectory.json", trajectory)
    write_json(run_dir / "context_manifest.json", context_meta)
    write_text(
        run_dir / "answer.md",
        f"# {task_id} Answer\n\n## Final Answer\n\n```json\n{json.dumps(final_answer, indent=2, ensure_ascii=False)}\n```\n\n"
        f"## Rationale\n\n{rationale}\n\n## Evidence Files\n\n"
        + "\n".join(f"- `{x}`" for x in (evidence_files if isinstance(evidence_files, list) else []))
        + "\n\n## Limitations\n\n"
        + "\n".join(f"- {x}" for x in (limitations if isinstance(limitations, list) else [limitations]))
        + "\n",
    )
    write_text(
        run_dir / "tool_trace.md",
        f"# {task_id} Tool Trace\n\n"
        "| Step | Tool | Result |\n| ---: | --- | --- |\n"
        f"| 1 | `read_question` | Read `{task_id}/question_en.md` |\n"
        f"| 2 | `build_direct_prompt_context` | Mode `{context_meta.get('context_mode')}`; embedded {context_meta.get('embedded_text_files', len(context_files))} files ({context_meta.get('included_text_files', 0)} full, {context_meta.get('truncated_text_files', 0)} truncated), skipped {context_meta.get('skipped_text_files', 0)} readable text files |\n"
        f"| 3 | `openai_chat_completion` | `{model}` returned JSON in {latency:.2f}s |\n",
    )
    write_text(
        run_dir / "run_notes.md",
        "No forbidden answer-key or compute files were used. No computed_gt.json, solution_en.md, review.json, or compute_gt.py was used in the model prompt. "
        "No web evidence was used; only local package evidence was provided to the model prompt. "
        "The network call was only the model API invocation.\n",
    )
    write_json(run_dir / "raw_response.json", {"content": content, "usage": (raw_data or {}).get("usage", {})})
    return {
        "task_id": task_id,
        "model": model,
        "status": "ok",
        "latency_s": latency,
        "estimated_prompt_tokens": prompt_tokens,
        "completion_tokens": ((raw_data or {}).get("usage") or {}).get("completion_tokens"),
        "prompt_tokens": ((raw_data or {}).get("usage") or {}).get("prompt_tokens"),
        "context_mode": context_meta.get("context_mode"),
        "embedded_text_files": context_meta.get("embedded_text_files"),
        "included_text_files": context_meta.get("included_text_files"),
        "truncated_text_files": context_meta.get("truncated_text_files"),
        "skipped_text_files": context_meta.get("skipped_text_files"),
    }


def run_model(model: str, task_dirs: list[Path], cfg: dict[str, Any], workers: int, force: bool) -> list[dict[str, Any]]:
    api_key = os.environ.get(cfg.get("api_key_env", "OPENAI_API_KEY"))
    if not api_key:
        raise SystemExit(f"{cfg.get('api_key_env', 'OPENAI_API_KEY')} is not set.")
    base_url = os.environ.get(cfg.get("base_url_env", "OPENAI_BASE_URL"), cfg.get("default_base_url", "https://api.openai.com/v1"))
    package_root = repo_path(cfg.get("package_dir", "event_packages/standard_event_packages/packages"))
    out_root = repo_path(cfg.get("output_root", "outputs/openai_api"))
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
                result = {
                    "task_id": task_dir.name,
                    "model": model,
                    "status": "error",
                    "latency_s": 0.0,
                    "error": f"unhandled worker exception: {type(exc).__name__}: {exc}",
                }
            results.append(result)
            print(json.dumps(result, ensure_ascii=False))
    return sorted(results, key=lambda item: item["task_id"])


def estimate_runtime(results: list[dict[str, Any]], total_tasks: int, workers: int) -> dict[str, Any]:
    ok_latencies = [float(r["latency_s"]) for r in results if r.get("status") == "ok" and float(r.get("latency_s", 0)) > 0]
    if not ok_latencies:
        return {"estimated_seconds": None}
    mean_latency = statistics.fmean(ok_latencies)
    p95_latency = sorted(ok_latencies)[max(0, int(0.95 * (len(ok_latencies) - 1)))]
    return {
        "mean_latency_s": round(mean_latency, 2),
        "p95_latency_s": round(p95_latency, 2),
        "workers": workers,
        "total_tasks": total_tasks,
        "estimated_seconds_mean": round(total_tasks * mean_latency / max(1, workers), 1),
        "estimated_seconds_p95": round(total_tasks * p95_latency / max(1, workers), 1),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run OpenAI-compatible models over benchmark tasks.")
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
    cfg = load_mode_config(repo_path(args.config), "direct")
    task_ids = list(args.task_id) + load_task_ids(repo_path(args.task_file) if args.task_file else None)
    task_dirs = iter_task_dirs(repo_path(cfg.get("task_dir", "tasks")), args.limit, task_ids)
    configured_models = cfg.get("models", [])
    if args.models:
        wanted = {x.strip() for x in args.models.split(",") if x.strip()}
        models = [m for m in configured_models if m["name"] in wanted]
        missing = wanted - {m["name"] for m in models}
        if missing:
            models.extend({"name": name, "workers": args.workers or 8} for name in sorted(missing))
    else:
        models = configured_models
    summary = {
        "task_count": len(task_dirs),
        "models": [],
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    for model_cfg in models:
        model = model_cfg["name"]
        workers = args.workers or int(model_cfg.get("workers", 8))
        started = time.perf_counter()
        results = run_model(model, task_dirs, cfg, workers=workers, force=args.force)
        elapsed = time.perf_counter() - started
        estimate = estimate_runtime(results, len(task_dirs), workers)
        model_summary = {
            "model": model,
            "workers": workers,
            "elapsed_s": round(elapsed, 2),
            "results": {
                "ok": sum(1 for r in results if r.get("status") == "ok"),
                "error": sum(1 for r in results if r.get("status") == "error"),
                "skipped": sum(1 for r in results if r.get("status") == "skipped"),
            },
            "run_estimate": estimate,
        }
        summary["models"].append(model_summary)
        out_root = repo_path(cfg.get("output_root", "outputs/openai_api"))
        safe_model = model.replace("/", "__").replace(":", "_")
        write_json(out_root / safe_model / "run_summary.json", {"model_summary": model_summary, "task_results": results})
    summary["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    out_root = repo_path(cfg.get("output_root", "outputs/openai_api"))
    write_json(out_root / "latest_run_summary.json", summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
