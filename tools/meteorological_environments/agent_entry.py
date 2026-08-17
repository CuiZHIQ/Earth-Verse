from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scripts import run_agent as base

from .catalog import get_environment
from .runtime import execute_environment_tool, probe_environment


_BASE_BUILD_INITIAL_MESSAGES = base.build_initial_messages
_BASE_RUN_TOOL = base.run_tool
_BASE_SOLVE_ONE = base.solve_one
_INSTALLED = False


def _tool_instructions(condition_id: str) -> str:
    spec = get_environment(condition_id)
    operations = ", ".join(spec.operations)
    return f"""
Meteorological research environment:

- {spec.tool_name}(args)
  Environment: {spec.display_name}
  Use: {spec.purpose}
  Allowed operations: {operations}
  args: {{"operation":"<allowed operation>","source_files":["package/relative.ext"],"values":[...],"unit":"...", ...}}

Use source_files to preserve package-relative provenance. Inspect the package before constructing physical arrays or variable mappings. This environment requires at least {spec.min_calls} successful, distinct scientific operations and targets {spec.target_calls}. A version probe, failed call, not-applicable call, or exact duplicate does not count. Use different operations for the main diagnostic and its independent check. Do not call unrelated environments.
""".strip()


def build_initial_messages(task_dir: Path, package_dir: Path, cfg: dict[str, Any]) -> list[dict[str, str]]:
    messages = _BASE_BUILD_INITIAL_MESSAGES(task_dir, package_dir, cfg)
    condition_id = str(cfg.get("environment_id") or "")
    if not condition_id:
        return messages
    spec = get_environment(condition_id)
    cfg.setdefault(
        "required_tool_policy",
        {
            "tool_names": [spec.tool_name],
            "excluded_operations": ["probe"],
            "minimum_successful_distinct_calls": spec.min_calls,
            "target_successful_calls": spec.target_calls,
            "maximum_counted_calls": spec.max_calls,
        },
    )
    user = messages[-1]["content"] + "\n\n" + _tool_instructions(condition_id)
    messages[-1] = {**messages[-1], "content": user}
    return messages


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
    condition_id = str(cfg.get("environment_id") or "")
    if condition_id:
        spec = get_environment(condition_id)
        if tool == spec.tool_name:
            return execute_environment_tool(condition_id, args, package_dir, scratch_dir)
    return _BASE_RUN_TOOL(tool, args, package_dir, task_dir, scratch_dir, code_dir, step, cfg)


def _annotate(path: Path, cfg: dict[str, Any]) -> None:
    if not path.is_file():
        return
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    condition_id = str(cfg.get("environment_id") or "")
    spec = get_environment(condition_id)
    environment_calls = [
        call for call in payload.get("tool_calls", []) if isinstance(call, dict) and call.get("tool") == spec.tool_name
    ]
    payload.update(
        {
            "meteorological_environment": {
                "condition_id": condition_id,
                "tier": spec.tier,
                "category": spec.category,
                "display_name": spec.display_name,
                "runtime": spec.runtime,
                "probe": probe_environment(condition_id),
                "call_count": len(environment_calls),
                "successful_call_count": sum(1 for call in environment_calls if call.get("ok")),
            },
        }
    )
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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
    result = _BASE_SOLVE_ONE(task_dir, model, package_root, out_root, cfg, api_key, base_url, force)
    path = out_root / base.safe_model_name(model) / task_dir.name / "trajectory.json"
    if cfg.get("environment_id"):
        _annotate(path, cfg)
    return result


def install() -> None:
    global _INSTALLED
    if _INSTALLED:
        return
    base.build_initial_messages = build_initial_messages
    base.run_tool = run_tool
    base.solve_one = solve_one
    _INSTALLED = True


def main() -> None:
    install()
    base.main()


if __name__ == "__main__":
    main()
