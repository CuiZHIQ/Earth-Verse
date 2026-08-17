#!/usr/bin/env python3
"""Validate an external EarthVerse submission directory."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_FILES = ["answer.md", "trajectory.json"]
RECOMMENDED_FILES = ["tool_trace.md", "run_notes.md"]


def read_task_ids(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def is_empty_answer(value: Any) -> bool:
    return value in (None, "", [], {})


def validate_task(submission_dir: Path, task_id: str, *, strict: bool) -> dict[str, Any]:
    run_dir = submission_dir / task_id
    errors: list[str] = []
    warnings: list[str] = []
    if not run_dir.is_dir():
        return {
            "task_id": task_id,
            "status": "missing_task_dir",
            "errors": [f"missing task directory: {run_dir}"],
            "warnings": warnings,
        }

    for name in REQUIRED_FILES:
        if not (run_dir / name).is_file():
            errors.append(f"missing required file: {name}")
    for name in RECOMMENDED_FILES:
        if not (run_dir / name).is_file():
            warnings.append(f"missing recommended file: {name}")
            if strict:
                errors.append(f"missing recommended file in strict mode: {name}")

    answer_md = run_dir / "answer.md"
    if answer_md.is_file() and not answer_md.read_text(encoding="utf-8-sig", errors="replace").strip():
        errors.append("answer.md is empty")

    trajectory_path = run_dir / "trajectory.json"
    if trajectory_path.is_file():
        try:
            trajectory = read_json(trajectory_path)
        except json.JSONDecodeError as exc:
            errors.append(f"trajectory.json is invalid JSON: {exc}")
            trajectory = {}
        if isinstance(trajectory, dict):
            if trajectory.get("task_id") not in ("", None, task_id):
                warnings.append(f"trajectory task_id does not match directory: {trajectory.get('task_id')!r}")
            if trajectory.get("run_status", "ok") != "ok":
                warnings.append(f"run_status is not ok: {trajectory.get('run_status')!r}")
            if is_empty_answer(trajectory.get("final_answer")) and answer_md.is_file():
                warnings.append("trajectory final_answer is empty; judge will fall back to answer.md")
            if not isinstance(trajectory.get("tool_calls", []), list):
                warnings.append("trajectory tool_calls is not a list")
            if not isinstance(trajectory.get("raw_usage", []), list):
                warnings.append("trajectory raw_usage is not a list")
        else:
            errors.append("trajectory.json root must be a JSON object")

    return {
        "task_id": task_id,
        "status": "ok" if not errors else "invalid",
        "errors": errors,
        "warnings": warnings,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate an external EarthVerse submission directory.")
    parser.add_argument("--submission-dir", required=True, help="Directory shaped as submissions/<model_name>/")
    parser.add_argument("--task-file", default="task_sets/orig405.txt")
    parser.add_argument("--strict", action="store_true", help="Require the recommended trace and run-note files.")
    parser.add_argument("--out-file", default="", help="Optional JSON validation report path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    submission_dir = Path(args.submission_dir).resolve()
    task_file = Path(args.task_file).resolve()
    task_ids = read_task_ids(task_file)
    rows = [validate_task(submission_dir, task_id, strict=args.strict) for task_id in task_ids]
    summary = {
        "schema_version": "submission_validation_v1",
        "submission_dir": str(submission_dir),
        "task_file": str(task_file),
        "task_count": len(rows),
        "valid_count": sum(1 for row in rows if row["status"] == "ok"),
        "invalid_count": sum(1 for row in rows if row["status"] != "ok"),
        "warning_count": sum(len(row["warnings"]) for row in rows),
        "strict": bool(args.strict),
    }
    report = {"summary": summary, "tasks": rows}
    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.out_file:
        out_file = Path(args.out_file).resolve()
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(text + "\n", encoding="utf-8")
    print(text)
    raise SystemExit(0 if summary["invalid_count"] == 0 else 1)


if __name__ == "__main__":
    main()
