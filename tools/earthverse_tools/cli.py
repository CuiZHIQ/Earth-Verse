from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from .core import ToolRegistry
from .profiles import ToolProfileManager
from .workflows import ExtremeEventWorkflowEngine


def parse_scalar(value: str):
    value = value.strip().strip("\"'")
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered == "null":
        return None
    try:
        numeric = float(value)
    except ValueError:
        return value
    return int(numeric) if numeric.is_integer() else numeric


def parse_tool_args(raw: str, args_file: str = "") -> dict:
    if args_file:
        return json.loads(Path(args_file).read_text(encoding="utf-8-sig"))
    try:
        parsed = json.loads(raw)
        if not isinstance(parsed, dict):
            raise ValueError("--args must decode to a JSON object")
        return parsed
    except json.JSONDecodeError:
        pass

    # PowerShell or nested launchers sometimes strip JSON double quotes from
    # simple command-line examples. Accept a small key:value object fallback for
    # smoke tests; complex arguments should use --args-file.
    text = raw.strip()
    if text.startswith("{") and text.endswith("}"):
        text = text[1:-1]
    out = {}
    if text:
        for part in text.split(","):
            if ":" not in part:
                raise ValueError(f"Could not parse argument fragment: {part!r}")
            key, value = part.split(":", 1)
            out[key.strip().strip("\"'")] = parse_scalar(value)
    return out


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="EarthVerse event-evidence tool runner")
    parser.add_argument("tool", nargs="?", help="Tool name to call. Omit with --list to list tools.")
    parser.add_argument("--list", action="store_true", help="List registered tools.")
    parser.add_argument("--profiles", action="store_true", help="List layered tool profiles.")
    parser.add_argument("--kit", help="Filter tools by kit.")
    parser.add_argument("--profile", help="Filter tools by profile or run a profile-scoped call.")
    parser.add_argument("--plan", action="store_true", help="Create a workflow plan instead of calling a tool.")
    parser.add_argument("--question", default="", help="Question text used by workflow routing.")
    parser.add_argument("--event-id", help="Event package id used by workflow planning.")
    parser.add_argument("--args", default="{}", help="JSON object passed as tool arguments.")
    parser.add_argument("--args-file", default="", help="Path to a JSON object file passed as tool arguments.")
    ns = parser.parse_args()
    reg = ToolRegistry()
    profiles = ToolProfileManager(reg)
    if ns.list:
        if ns.profile:
            print(json.dumps(profiles.tools_for_profile(ns.profile), ensure_ascii=False, indent=2))
        else:
            print(json.dumps(reg.list_tools(ns.kit), ensure_ascii=False, indent=2))
        return
    if ns.profiles:
        print(json.dumps(profiles.list_profiles(), ensure_ascii=False, indent=2))
        return
    if ns.plan:
        engine = ExtremeEventWorkflowEngine(reg)
        if ns.event_id:
            print(json.dumps(engine.package_first_plan(ns.event_id, ns.question, ns.profile), ensure_ascii=False, indent=2))
        else:
            print(json.dumps(engine.plan(ns.question, profile=ns.profile), ensure_ascii=False, indent=2))
        return
    if not ns.tool:
        parser.error("tool name is required unless --list is used")
    kwargs = parse_tool_args(ns.args, ns.args_file)
    if ns.profile:
        engine = ExtremeEventWorkflowEngine(reg)
        print(json.dumps(engine.call_profile_tool(ns.profile, ns.tool, **kwargs), ensure_ascii=False, indent=2))
    else:
        print(json.dumps(reg.call(ns.tool, **kwargs), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
