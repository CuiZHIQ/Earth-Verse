#!/usr/bin/env python3
"""Package-scoped EarthVerse tools for MCP-compatible research agents.

The server delegates to the benchmark's audited interactive-tool runtime. The
current task, package, and scratch directories are supplied through environment
variables so one process can never discover a different task's answer files.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
from pathlib import Path
from typing import Any

try:
    from fastmcp import FastMCP
except ImportError:
    from mcp.server.fastmcp import FastMCP


def required_dir(name: str) -> Path:
    raw = os.environ.get(name, "").strip()
    if not raw:
        raise RuntimeError(f"{name} is required")
    path = Path(raw).resolve()
    if not path.is_dir():
        raise RuntimeError(f"{name} is not a directory: {path}")
    return path


BENCHMARK_ROOT = required_dir("EARTHVERSE_ROOT")
TASK_DIR = required_dir("EARTHVERSE_TASK_DIR")
PACKAGE_DIR = required_dir("EARTHVERSE_PACKAGE_DIR")
SCRATCH_DIR = required_dir("EARTHVERSE_SCRATCH_DIR")
CODE_DIR = SCRATCH_DIR / "python_snippets"
CODE_DIR.mkdir(parents=True, exist_ok=True)

task_root = (BENCHMARK_ROOT / "tasks").resolve()
package_root = (
    BENCHMARK_ROOT / "event_packages" / "standard_event_packages" / "packages"
).resolve()
run_root = (BENCHMARK_ROOT / "outputs").resolve()
event_id = TASK_DIR.name.split("_")[0]
if TASK_DIR.parent != task_root:
    raise RuntimeError("EARTHVERSE_TASK_DIR must be a direct child of the EarthVerse tasks directory")
if PACKAGE_DIR != package_root / event_id:
    raise RuntimeError("EARTHVERSE_PACKAGE_DIR does not match the current task event id")
try:
    SCRATCH_DIR.relative_to(run_root)
except ValueError as exc:
    raise RuntimeError("EARTHVERSE_SCRATCH_DIR must be inside the EarthVerse outputs directory") from exc

sys.path.insert(0, str(BENCHMARK_ROOT / "scripts"))
import run_agent as runtime  # noqa: E402


mcp = FastMCP("earthverse-package-tools")
step_counter = itertools.count(1)


def emit(result: dict[str, Any]) -> str:
    return json.dumps(result, ensure_ascii=False, indent=2)


@mcp.tool()
def list_package_files(subdir: str = ".", max_files: int = 120) -> str:
    """List files under the current event package.

    Start here. Paths in the result are package-relative or benchmark-relative.
    Answer-key files and other event packages are outside this tool's boundary.
    """
    return emit(
        runtime.tool_list_package_files(
            {"subdir": subdir, "max_files": max_files},
            PACKAGE_DIR,
            TASK_DIR,
            SCRATCH_DIR,
        )
    )


@mcp.tool()
def search_package_files(query: str, glob: str = "**/*", max_matches: int = 40) -> str:
    """Search readable files in the current event package and return snippets."""
    return emit(
        runtime.tool_search_package_files(
            {"query": query, "glob": glob, "max_matches": max_matches},
            PACKAGE_DIR,
            TASK_DIR,
            SCRATCH_DIR,
        )
    )


@mcp.tool()
def read_text_file(path: str, max_chars: int = 12000) -> str:
    """Read a package text file by a path returned from list or search."""
    return emit(
        runtime.tool_read_text_file(
            {"path": path, "max_chars": max_chars},
            PACKAGE_DIR,
            TASK_DIR,
            SCRATCH_DIR,
        )
    )


@mcp.tool()
def summarize_table_or_json(path: str) -> str:
    """Inspect CSV, JSON, or GeoJSON structure and numeric summaries."""
    return emit(
        runtime.tool_summarize_table_or_json(
            {"path": path},
            PACKAGE_DIR,
            TASK_DIR,
            SCRATCH_DIR,
        )
    )


@mcp.tool()
def inspect_image(path: str) -> str:
    """Return deterministic image dimensions and basic channel statistics."""
    return emit(
        runtime.tool_inspect_image(
            {"path": path},
            PACKAGE_DIR,
            TASK_DIR,
            SCRATCH_DIR,
        )
    )


@mcp.tool()
def python_exec(code: str, timeout_seconds: int = 60) -> str:
    """Run package-scoped Python for calculations.

    Reads are limited to the current package and public question. Writes are
    limited to the task scratch directory. Network and hidden benchmark files
    are blocked by the shared benchmark runtime.
    """
    timeout = max(1, min(int(timeout_seconds), 180))
    return emit(
        runtime.tool_python_exec(
            {"code": code},
            PACKAGE_DIR,
            TASK_DIR,
            SCRATCH_DIR,
            CODE_DIR,
            next(step_counter),
            timeout,
        )
    )


if __name__ == "__main__":
    try:
        mcp.run(transport="stdio", show_banner=False)
    except TypeError:
        mcp.run(transport="stdio")
