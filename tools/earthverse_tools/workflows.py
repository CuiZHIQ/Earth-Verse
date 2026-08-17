from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .core import ToolRegistry
from .profiles import ToolProfileManager


@dataclass
class WorkflowPlan:
    profile: str
    tools: list[str]
    rationale: str
    steps: list[dict[str, Any]]


class ExtremeEventWorkflowEngine:
    """Plan and execute layered tool workflows for one benchmark task.

    The engine does not decide the scientific answer. It selects a bounded tool
    package and creates a trace scaffold that an agent or evaluator can follow.
    """

    def __init__(self, registry: ToolRegistry | None = None):
        self.registry = registry or ToolRegistry()
        self.profiles = ToolProfileManager(self.registry)

    def plan(self, question: str = "", metadata: dict[str, Any] | None = None, profile: str | None = None) -> dict[str, Any]:
        selected = self.profiles.get_profile(profile) if profile else self.profiles.route_profile(question, metadata)
        specs = [self.registry.describe(name) for name in selected["tools"] if name in self.registry.by_name]
        steps = []
        for i, spec in enumerate(specs, 1):
            steps.append({
                "step": i,
                "tool": spec["name"],
                "kit": spec["kit"],
                "purpose": spec["purpose"],
                "expected_output": spec["output"],
            })
        return WorkflowPlan(
            profile=selected["name"],
            tools=[s["name"] for s in specs],
            rationale=selected["description"],
            steps=steps,
        ).__dict__

    def package_first_plan(self, event_id: str, question: str = "", profile: str | None = None) -> dict[str, Any]:
        meta = self.registry.call("read_event_metadata", event_id=event_id)
        metadata = meta["data"] if meta["ok"] else {"event_id": event_id}
        plan = self.plan(question=question, metadata=metadata, profile=profile)
        plan["event_id"] = event_id
        plan["bootstrap_calls"] = [
            {"tool": "list_event_package_files", "kwargs": {"event_id": event_id}},
            {"tool": "read_event_metadata", "kwargs": {"event_id": event_id}},
            {"tool": "summarize_event_inventory", "kwargs": {"event_id": event_id}},
        ]
        return plan

    def run_bootstrap(self, event_id: str, question: str = "", profile: str | None = None) -> dict[str, Any]:
        plan = self.package_first_plan(event_id, question, profile)
        trace = []
        for call in plan["bootstrap_calls"]:
            trace.append({
                "tool": call["tool"],
                "kwargs": call["kwargs"],
                "result": self.registry.call(call["tool"], **call["kwargs"]),
            })
        return {"plan": plan, "trace": trace}

    def call_profile_tool(self, profile: str, tool_name: str, **kwargs: Any) -> dict[str, Any]:
        allowed = set(self.profiles.get_profile(profile)["tools"])
        if tool_name not in allowed:
            return {
                "tool": tool_name,
                "ok": False,
                "data": {},
                "warnings": [],
                "error": f"tool is not allowed in profile {profile}",
                "provenance": [],
            }
        return self.registry.call(tool_name, **kwargs)
