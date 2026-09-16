#!/usr/bin/env python3
"""Run the EarthVerse LLM judge.

The current scoring design is deliberately small:

1. Compare the model answer against the ground truth and assign partial credit.
2. Grade the answer against the task's own rubric.

Capability-dimension scores are derived later by scripts/report.py from manual
task labels and strict answer-unit correctness.
No deterministic exact-match scorer, binary pass/fail metric, runtime-error
rate, or JSON-format error rate is part of the core benchmark score. A solver
run that fails to produce an answer is nevertheless scored as a zero answer;
only judge infrastructure failures are excluded.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


OFFICIAL_SCORE_KEYS = [
    "answer_correctness_score",
    "llm_rubric_score",
]

RATIONALE_KEYS = [
    "answer_correctness",
    "llm_rubric",
]

SUPPORT_SCORE_KEYS: list[str] = []

SCORE_DEFINITIONS = {
    "answer_correctness_score": (
        "0-100 partial-credit correctness of the final answer against computed_gt/primary_gt. "
        "For multi-field JSON answers, estimate the fraction of required answer elements, "
        "labels, numeric values, units, orderings, and conclusions that are correct."
    ),
    "llm_rubric_score": (
        "0-100 task-rubric score converted from the task's own 20-point rubric "
        "in solution_en.md. Compare the model answer and trace against the "
        "solution process and rubric criteria, assign earned_points out of 20, "
        "then set llm_rubric_score = earned_points / 20 * 100."
    ),
}

FILE_READ_TOOLS = {
    "read_text_file",
    "summarize_table_or_json",
    "inspect_image",
    "browser.open",
    "browser.summarize",
}
DIRECT_CONTEXT_TOOLS = {
    "build_direct_prompt_context",
    "build_compact_local_context",
    "read_selected_files",
}
LIST_TOOLS = {"list_package_files", "browser.list"}
SEARCH_TOOLS = {"search_package_files", "browser.search"}
PYTHON_TOOLS = {"python_exec", "browser.python"}
PROCESS_DIAGNOSTIC_KEYS = [
    "latency_s",
    "tool_call_count",
    "tool_success_count",
    "tool_error_count",
    "tool_success_rate",
    "agent_step_count",
    "llm_call_round_count",
    "prompt_tokens",
    "completion_tokens",
    "total_tokens",
    "cached_prompt_tokens",
    "estimated_cost_usd",
    "file_read_call_count",
    "unique_evidence_file_count",
    "evidence_file_reference_count",
    "list_files_call_count",
    "search_call_count",
    "python_exec_count",
    "forced_finalization_rate",
    "research_budget_seconds",
    "total_budget_seconds",
]
PROCESS_TEXT_KEYS = ["termination_reason", "solver_error_type"]
TOOL_TRACE_JSON_KEYS = ["tool_usage_summary"]


def read_text(path: Path, default: str = "") -> str:
    if not path.exists():
        return default
    return path.read_text(encoding="utf-8-sig", errors="replace")


def read_json(path: Path, default: Any | None = None) -> Any:
    if not path.exists():
        return {} if default is None else default
    text = read_text(path)
    if not text.strip():
        return {} if default is None else default
    return json.loads(text)


def extract_rubric(solution_text: str) -> str:
    markers = ["## Scoring Rubric", "## Rubric", "# Scoring Rubric", "Scoring Rubric"]
    for marker in markers:
        idx = solution_text.find(marker)
        if idx >= 0:
            return solution_text[idx: idx + 3500]
    return ""


def compact_text(text: str, max_chars: int) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 80] + "\n...[TRUNCATED]..."


def is_empty_answer(value: Any) -> bool:
    return value in (None, "", [], {})


def build_messages(task_dir: Path, run_dir: Path) -> list[dict[str, str]]:
    task_id = task_dir.name
    gt = read_json(task_dir / "computed_gt.json", {})
    trajectory = read_json(run_dir / "trajectory.json", {})
    question = read_text(task_dir / "question_en.md")
    solution = read_text(task_dir / "solution_en.md")
    rubric = extract_rubric(solution)
    answer_md = read_text(run_dir / "answer.md")
    tool_trace = read_text(run_dir / "tool_trace.md")
    run_notes = read_text(run_dir / "run_notes.md")

    trajectory_final_answer = trajectory.get("final_answer")
    answer_fallback_used = is_empty_answer(trajectory_final_answer)
    final_answer_for_judge = answer_md if answer_fallback_used else trajectory_final_answer
    task_metadata = {
        "task_id": task_id,
        "task_type": gt.get("task_type"),
        "task_subtype": gt.get("task_subtype"),
        "target_family": gt.get("target_family"),
        "schema_version": gt.get("schema_version"),
        "answer_fallback_used": answer_fallback_used,
        "model_answer_type": trajectory.get("answer_type"),
    }

    user_payload = f"""
Evaluate this model response for an extreme-event evidence-and-reasoning
benchmark. Make one combined evaluation and produce two core 0-100 scores.
Capability-dimension metrics are computed later from manual task labels and
answer-unit correctness.

### Required Output Scores
```json
{json.dumps(SCORE_DEFINITIONS, ensure_ascii=False, indent=2)}
```

### Calibration Rules
- Do not emit binary 0/100 pass-fail metrics unless the answer truly deserves
  that endpoint. Partial credit is expected.
- `answer_correctness_score` is the direct partial-credit comparison between
  the model's final answer and the ground truth. If the task has multiple JSON
  fields or multiple required claims, score the fraction that is correct.
- Treat the answer as a set of answer units. Units include required JSON fields,
  labels, categorical decisions, numeric values with units/tolerances, ordered
  items, listed alternatives, stage boundaries, and required one-sentence
  conclusions. Missing required fields count wrong. Noncanonical labels count
  wrong unless the question explicitly allows free-form labels. Correct prose
  cannot compensate for a missing required structured field.
- In `answer_units.wrong_or_missing`, prefix each important error with one of:
  `critical_label`, `numeric_value`, `formula`, `missing_field`, `schema`,
  `source_evidence`, `unit`, `ordering`, or `reasoning`. Use these prefixes
  especially for wrong final labels, wrong mechanism decisions, wrong numeric
  values, missing required JSON keys, and non-reproducible formulas.
- Be strict. A score above 90 requires a nearly complete, evidence-backed answer
  with correct final fields and no material unsupported shortcut. A score of
  75-89 means mostly correct with meaningful omissions. A score of 50-74 means
  partially correct. A score below 50 means the answer is mostly wrong,
  unsupported, or missing key fields.
- `llm_rubric_score` must come from the task's own 20-point rubric in
  `solution_en.md`. Compare the model answer and trace against the solution
  process and each rubric criterion, assign `earned_points` out of 20, and
  convert it to percent as `earned_points / 20 * 100`.
- Fill `rubric_points.criteria` with the visible rubric items. Preserve the
  rubric's point allocation when it is explicit. If the rubric text is
  malformed or does not sum exactly to 20, normalize your criterion max-points
  so `rubric_points.total` is 20 while keeping the original intent.
- Do not invent extra credit outside the solution rubric. Penalize lucky final
  answers that skip required source selection, calculation, evidence
  provenance, schema fields, or reasoning steps when the rubric requires them.
- Treat each rubric criterion as result-dependent unless its wording is
  explicitly process-only. If a criterion requires a correct calculation,
  comparison, mechanism conclusion, ranking, label, or structured output, the
  model must lose rubric credit when that corresponding result is wrong or
  missing, even when it attempted the expected method.
- A plausible narrative, many tool calls, or reading the right files is not by
  itself a correct solution process. Award high rubric credit only when the
  cited evidence, intermediate values, transformations, and rubric-required
  conclusions are mutually consistent with the ground truth and solution.
- Calibrate the two scores together without making them identical. A rubric
  score more than 20 points above answer correctness should be exceptional and
  justified criterion by criterion; this is not a hard numerical cap. Such a
  gap is reasonable only when the task rubric genuinely rewards substantial,
  independently correct process work despite a limited final-answer error.
- The code will trust `rubric_points.earned` as the source of
  `llm_rubric_score`; make the points and rationale consistent.
- A wrong final label, selected option, mechanism decision, threshold result, or
  required classification is a material error. Deduct credit in proportion to
  the answer units affected; do not apply a fixed score ceiling.
- If required numeric values or formulas are materially wrong, answer
  correctness and rubric credit should reflect that error unless most numerical
  fields are independently correct.
- JSON extraction is allowed only to read the model output. Substantive
  correctness, numeric tolerance, semantic equivalence, evidence sufficiency,
  and rubric credit must be judged by you.
- Spatially masked OSM, WorldPop, AOI, and exposure products are authoritative
  for their derived statistics. Do not reject a package because masked
  coordinate, place-name, bounding-box, or georeferencing metadata looks unlike
  the event location.
- Use only the local package evidence, ground truth, task solution, rubric, and
  model trace supplied below. Do not rely on web knowledge.

### Task Metadata
```json
{json.dumps(task_metadata, ensure_ascii=False, indent=2)}
```

### Question
```text
{compact_text(question, 5000)}
```

### Ground Truth
```json
{json.dumps(gt.get("primary_gt", gt), ensure_ascii=False, indent=2)}
```

### Solution And Rubric
```text
{compact_text(solution, 6000)}
```

### Extracted Rubric
```text
{compact_text(rubric, 3500)}
```

### Model Final Answer
If `answer_fallback_used` is true in the metadata, treat the answer.md content
as the model's final answer for grading.

```json
{json.dumps(final_answer_for_judge, ensure_ascii=False, indent=2)}
```

### Model answer.md
```text
{compact_text(answer_md, 3500)}
```

### Model Tool Trace
```text
{compact_text(tool_trace, 6000)}
```

### Model Run Notes
```text
{compact_text(run_notes, 1500)}
```

Return only valid JSON with exactly this structure:
{{
  "task_id": "{task_id}",
  "scores": {{
    "answer_correctness_score": 0,
    "llm_rubric_score": 0
  }},
  "answer_units": {{
    "total": 0,
    "correct": 0,
    "wrong_or_missing": ["short descriptions of incorrect answer units"],
    "notes": "brief note on how units were counted"
  }},
  "rubric_points": {{
    "total": 20,
    "earned": 0,
    "criteria": [
      {{
        "name": "criterion name from the solution rubric",
        "max_points": 0,
        "earned_points": 0,
        "reason": "brief criterion-specific reason"
      }}
    ],
    "notes": "brief note on how the 20-point rubric was applied"
  }},
  "mean_score": 0,
  "verdict": "incorrect | partial | mostly_correct | correct",
  "rationale": {{
    "answer_correctness": "",
    "llm_rubric": ""
  }},
  "critical_errors": [],
  "missing_answer_elements": [],
  "unsupported_overclaims": [],
  "one_sentence_rationale": ""
}}
"""

    system = (
        "You are a strict but fair evaluator for a local extreme-event benchmark. "
        "Your job is to judge answer correctness and task-rubric quality. "
        "Use partial 0-100 scores, avoid "
        "old deterministic exact matching, and return only valid JSON."
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user_payload}]


def collect_metadata(task_dir: Path, run_dir: Path) -> dict[str, Any]:
    gt = read_json(task_dir / "computed_gt.json", {})
    trajectory = read_json(run_dir / "trajectory.json", {})
    task_id = task_dir.name
    process = trace_process_diagnostics(trajectory)
    final_answer = trajectory.get("final_answer", {})
    error_text = final_answer.get("error", "") if isinstance(final_answer, dict) else ""
    solver_error_type = str(trajectory.get("error_type", "")).strip()
    if not solver_error_type and error_text:
        solver_error_type = str(error_text).partition(":")[0].strip()
    return {
        "event_id": gt.get("event_id") or trajectory.get("event_id") or task_id.split("_")[0],
        "task_type": gt.get("task_type", ""),
        "task_subtype": gt.get("task_subtype", ""),
        "target_family": gt.get("target_family", ""),
        "schema_version": gt.get("schema_version", ""),
        "run_status": trajectory.get("run_status", ""),
        "answer_type": trajectory.get("answer_type", ""),
        "evidence_boundary": trajectory.get("evidence_boundary", ""),
        "solver_error_type": solver_error_type,
        **process,
    }


def has_scoreable_final_answer(run_dir: Path) -> bool:
    trajectory = read_json(run_dir / "trajectory.json", {})
    final_answer = trajectory.get("final_answer")
    if is_empty_answer(final_answer):
        final_answer = read_text(run_dir / "answer.md")
    text = str(final_answer or "").strip()
    return bool(text) and not text.startswith("[Agent error:")


def trace_process_diagnostics(trajectory: Any) -> dict[str, Any]:
    if not isinstance(trajectory, dict):
        trajectory = {}
    raw_tool_calls = trajectory.get("tool_calls", [])
    tool_calls = raw_tool_calls if isinstance(raw_tool_calls, list) else []
    if not tool_calls and isinstance(trajectory.get("tool_call_records"), list):
        tool_calls = trajectory["tool_call_records"]
    raw_usage = trajectory.get("raw_usage", [])
    llm_rounds = raw_usage if isinstance(raw_usage, list) else []

    if tool_calls:
        tool_count = len(tool_calls)
    else:
        try:
            tool_count = max(0, int(raw_tool_calls))
        except (TypeError, ValueError):
            tool_count = 0
    success_count = 0
    file_read_count = 0
    evidence_reference_count = 0
    evidence_files: set[str] = set()
    step_ids: set[str] = set()
    list_count = 0
    search_count = 0
    python_count = 0
    tool_stats: dict[str, dict[str, Any]] = {}

    for idx, call in enumerate(tool_calls, start=1):
        if not isinstance(call, dict):
            continue
        tool_name = str(call.get("tool", "")).strip() or "__unknown__"
        stats = tool_stats.setdefault(tool_name, {
            "tool": tool_name,
            "call_count": 0,
            "success_count": 0,
            "error_count": 0,
            "evidence_file_reference_count": 0,
            "_evidence_files": set(),
            "_steps": [],
        })
        stats["call_count"] += 1
        if call.get("ok") is True:
            success_count += 1
            stats["success_count"] += 1
        else:
            stats["error_count"] += 1
        call_evidence = call.get("evidence_files", [])
        if tool_name in DIRECT_CONTEXT_TOOLS and isinstance(call_evidence, list):
            file_read_count += len(call_evidence)
        elif tool_name in FILE_READ_TOOLS:
            file_read_count += 1
        if tool_name in LIST_TOOLS:
            list_count += 1
        if tool_name in SEARCH_TOOLS:
            search_count += 1
        if tool_name in PYTHON_TOOLS:
            python_count += 1
        if call.get("step") not in (None, ""):
            step_ids.add(str(call.get("step")))
            try:
                stats["_steps"].append(float(call.get("step")))
            except (TypeError, ValueError):
                stats["_steps"].append(float(idx))
        else:
            step_ids.add(str(idx))
            stats["_steps"].append(float(idx))
        if isinstance(call_evidence, list):
            for evidence_file in call_evidence:
                evidence_reference_count += 1
                evidence_files.add(str(evidence_file))
                stats["evidence_file_reference_count"] += 1
                stats["_evidence_files"].add(str(evidence_file))

    error_count = max(0, tool_count - success_count) if tool_calls else 0
    tool_usage_summary: list[dict[str, Any]] = []
    for tool_name, stats in sorted(tool_stats.items()):
        tool_call_count = int(stats["call_count"])
        tool_success_count = int(stats["success_count"])
        tool_steps = stats["_steps"]
        tool_evidence_files = stats["_evidence_files"]
        tool_usage_summary.append({
            "tool": tool_name,
            "call_count": tool_call_count,
            "success_count": tool_success_count,
            "error_count": int(stats["error_count"]),
            "success_rate": round(100.0 * tool_success_count / tool_call_count, 2) if tool_call_count else "",
            "evidence_file_reference_count": int(stats["evidence_file_reference_count"]),
            "unique_evidence_file_count": len(tool_evidence_files),
            "evidence_files": sorted(tool_evidence_files),
            "first_step": round(min(tool_steps), 3) if tool_steps else "",
            "last_step": round(max(tool_steps), 3) if tool_steps else "",
        })
    if llm_rounds:
        llm_round_count = len(llm_rounds)
    elif isinstance(trajectory.get("raw_messages"), list):
        llm_round_count = sum(
            1
            for message in trajectory["raw_messages"]
            if isinstance(message, dict) and message.get("role") == "assistant"
        )
    else:
        try:
            llm_round_count = max(0, int(trajectory.get("main_assistant_turns") or 0))
        except (TypeError, ValueError):
            llm_round_count = 0

    forced_raw = trajectory.get("forced_finalization", None)
    if forced_raw is None:
        forced_finalization_rate: float | str = ""
    else:
        forced_finalization_rate = 100.0 if bool(forced_raw) else 0.0
    return {
        "latency_s": numeric_or_blank(trajectory.get("latency_s")),
        "tool_call_count": tool_count,
        "tool_success_count": success_count,
        "tool_error_count": error_count,
        "tool_success_rate": round(100.0 * success_count / tool_count, 2) if tool_count else "",
        "agent_step_count": len(step_ids),
        "llm_call_round_count": llm_round_count,
        **usage_diagnostics(trajectory),
        "file_read_call_count": file_read_count,
        "unique_evidence_file_count": len(evidence_files),
        "evidence_file_reference_count": evidence_reference_count,
        "list_files_call_count": list_count,
        "search_call_count": search_count,
        "python_exec_count": python_count,
        "forced_finalization_rate": forced_finalization_rate,
        "research_budget_seconds": numeric_or_blank(trajectory.get("max_research_seconds")),
        "total_budget_seconds": numeric_or_blank(
            trajectory.get("max_total_seconds", trajectory.get("max_task_wall_seconds"))
        ),
        "termination_reason": str(trajectory.get("termination_reason", "")),
        "tool_usage_summary": tool_usage_summary,
    }


def numeric_or_blank(value: Any) -> float | str:
    try:
        return round(float(value), 6)
    except (TypeError, ValueError):
        return ""


def usage_diagnostics(trajectory: dict[str, Any]) -> dict[str, Any]:
    raw_usage = trajectory.get("raw_usage", [])
    usage_items = raw_usage if isinstance(raw_usage, list) else [raw_usage] if isinstance(raw_usage, dict) else []
    usage_items = [
        usage
        for usage in usage_items
        if isinstance(usage, dict)
        and any(key in usage for key in ("prompt_tokens", "completion_tokens", "total_tokens"))
    ]
    if not usage_items:
        return {
            "prompt_tokens": "",
            "completion_tokens": "",
            "total_tokens": "",
            "cached_prompt_tokens": "",
            "estimated_cost_usd": "",
        }
    prompt_tokens = 0
    completion_tokens = 0
    total_tokens = 0
    cached_prompt_tokens = 0
    for usage in usage_items:
        if not isinstance(usage, dict):
            continue
        prompt_tokens += int(float(usage.get("prompt_tokens") or 0))
        completion_tokens += int(float(usage.get("completion_tokens") or 0))
        total_tokens += int(float(usage.get("total_tokens") or 0))
        details = usage.get("prompt_tokens_details")
        if isinstance(details, dict):
            cached_prompt_tokens += int(float(details.get("cached_tokens") or 0))
    if not total_tokens:
        total_tokens = prompt_tokens + completion_tokens
    cost = estimate_cost_usd(
        model=str(trajectory.get("model", "")),
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        cached_prompt_tokens=cached_prompt_tokens,
    )
    return {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
        "cached_prompt_tokens": cached_prompt_tokens,
        "estimated_cost_usd": cost,
    }


def estimate_cost_usd(
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    cached_prompt_tokens: int,
) -> float | str:
    pricing = pricing_for_model(model)
    if not pricing:
        return ""
    try:
        input_per_m = float(pricing["input_per_million_tokens"])
        output_per_m = float(pricing["output_per_million_tokens"])
    except (KeyError, TypeError, ValueError):
        return ""
    cached_raw = pricing.get("cached_input_per_million_tokens")
    cached_per_m = None
    if cached_raw not in (None, ""):
        try:
            cached_per_m = float(cached_raw)
        except (TypeError, ValueError):
            cached_per_m = None
    cached = min(max(cached_prompt_tokens, 0), max(prompt_tokens, 0))
    uncached = max(prompt_tokens - cached, 0)
    if cached_per_m is None:
        input_cost = prompt_tokens * input_per_m / 1_000_000
    else:
        input_cost = (uncached * input_per_m + cached * cached_per_m) / 1_000_000
    output_cost = completion_tokens * output_per_m / 1_000_000
    return round(input_cost + output_cost, 8)


def pricing_for_model(model: str) -> dict[str, Any]:
    env_pricing = {
        "input_per_million_tokens": os.environ.get("EVAL_INPUT_COST_PER_MILLION_TOKENS"),
        "output_per_million_tokens": os.environ.get("EVAL_OUTPUT_COST_PER_MILLION_TOKENS"),
        "cached_input_per_million_tokens": os.environ.get("EVAL_CACHED_INPUT_COST_PER_MILLION_TOKENS"),
    }
    if env_pricing["input_per_million_tokens"] and env_pricing["output_per_million_tokens"]:
        return env_pricing
    path = Path(os.environ.get("EVAL_MODEL_PRICING_JSON", "configs/model_pricing.json"))
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {}
    models = data.get("models", data) if isinstance(data, dict) else {}
    if not isinstance(models, dict):
        return {}
    return models.get(model) or models.get(model.replace("/", "__")) or {}


def extract_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    if not text:
        raise json.JSONDecodeError("empty judge response", text, 0)
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    decoder = json.JSONDecoder()

    def candidates(source: str, offset: int = 0) -> list[tuple[int, int, dict[str, Any]]]:
        found: list[tuple[int, int, dict[str, Any]]] = []
        for match in re.finditer(r"\{", source):
            try:
                value, consumed = decoder.raw_decode(source[match.start():])
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                found.append((offset + match.start(), consumed, value))
        return found

    found: list[tuple[int, int, dict[str, Any]]] = []
    for fenced in re.finditer(r"```(?:json)?\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE):
        found.extend(candidates(fenced.group(1), fenced.start(1)))
    found.extend(candidates(text))
    if found:
        required = [item for item in found if "scores" in item[2] and "task_id" in item[2]]
        pool = required or found
        return max(pool, key=lambda item: (item[1], item[0]))[2]
    raise json.JSONDecodeError("no JSON object found in judge response", text, 0)


def call_openai_compatible_raw(
    messages: list[dict[str, str]],
    model: str,
    base_url: str,
    api_key: str,
    timeout: int,
    use_response_format: bool = True,
) -> dict[str, Any]:
    url = base_url.rstrip("/") + "/chat/completions"
    payload: dict[str, Any] = {"model": model, "messages": messages}
    temperature_raw = os.environ.get("OPENAI_TEMPERATURE", "").strip()
    if temperature_raw:
        payload["temperature"] = float(temperature_raw)
    max_tokens_raw = os.environ.get("OPENAI_MAX_TOKENS", "").strip()
    if max_tokens_raw:
        payload["max_tokens"] = int(max_tokens_raw)
    if use_response_format:
        payload["response_format"] = {"type": "json_object"}
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8")
    parsed = json.loads(raw)
    content = parsed["choices"][0]["message"]["content"]
    return extract_json_object(content)


def clamp_score(value: Any) -> float:
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        numeric = 0.0
    return round(max(0.0, min(numeric, 100.0)), 2)


def infer_verdict(mean_score: float) -> str:
    if mean_score >= 85:
        return "correct"
    if mean_score >= 70:
        return "mostly_correct"
    if mean_score >= 40:
        return "partial"
    return "incorrect"


def normalize_string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    if value in (None, ""):
        return []
    return [str(value)]


def normalize_answer_units(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {"total": 0, "correct": 0, "unit_score": None, "wrong_or_missing": [], "notes": ""}
    try:
        total = int(float(value.get("total", 0) or 0))
    except (TypeError, ValueError):
        total = 0
    try:
        correct = int(float(value.get("correct", 0) or 0))
    except (TypeError, ValueError):
        correct = 0
    total = max(0, total)
    correct = max(0, min(correct, total)) if total else 0
    unit_score = round(100.0 * correct / total, 2) if total else None
    return {
        "total": total,
        "correct": correct,
        "unit_score": unit_score,
        "wrong_or_missing": normalize_string_list(value.get("wrong_or_missing")),
        "notes": str(value.get("notes", "")),
    }


def normalize_rubric_points(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {"total": 20.0, "earned": None, "score": None, "criteria": [], "notes": ""}
    try:
        total = float(value.get("total", 20) or 20)
    except (TypeError, ValueError):
        total = 20.0
    if total <= 0:
        total = 20.0
    try:
        earned = float(value.get("earned", 0) or 0)
    except (TypeError, ValueError):
        earned = 0.0
    earned = max(0.0, min(earned, total))

    criteria: list[dict[str, Any]] = []
    raw_criteria = value.get("criteria", [])
    if isinstance(raw_criteria, list):
        for item in raw_criteria:
            if not isinstance(item, dict):
                continue
            try:
                max_points = float(item.get("max_points", 0) or 0)
            except (TypeError, ValueError):
                max_points = 0.0
            try:
                earned_points = float(item.get("earned_points", 0) or 0)
            except (TypeError, ValueError):
                earned_points = 0.0
            max_points = max(0.0, max_points)
            earned_points = max(0.0, min(earned_points, max_points)) if max_points else max(0.0, earned_points)
            criteria.append({
                "name": str(item.get("name", "")),
                "max_points": round(max_points, 3),
                "earned_points": round(earned_points, 3),
                "reason": str(item.get("reason", "")),
            })

    return {
        "total": round(total, 3),
        "earned": round(earned, 3),
        "score": round(100.0 * earned / total, 2),
        "criteria": criteria,
        "notes": str(value.get("notes", "")),
    }


def answer_unit_flags(answer_units: dict[str, Any]) -> dict[str, bool]:
    text = " ".join(answer_units.get("wrong_or_missing") or []).lower()
    return {
        "critical_label": any(
            term in text
            for term in [
                "critical_label",
                "final label",
                "final_label",
                "answer label",
                "answer_label",
                "classification",
                "selected option",
                "mechanism decision",
                "threshold result",
                "threshold_result",
                "winning label",
                "winner",
            ]
        ),
        "numeric_formula": any(
            term in text
            for term in [
                "numeric_value",
                "numeric",
                "formula",
                "calculation",
                "wrong value",
                "ratio",
                "unit",
                "derived",
                "metric",
            ]
        ),
        "missing_schema": any(
            term in text
            for term in [
                "missing_field",
                "missing field",
                "missing required",
                "schema",
                "json key",
                "required field",
            ]
        ),
    }


def require_complete_judge_shape(result: dict[str, Any]) -> None:
    scores = result.get("scores")
    if not isinstance(scores, dict) or any(key not in scores for key in OFFICIAL_SCORE_KEYS):
        raise ValueError("judge response is missing required score fields")

    answer_units = result.get("answer_units")
    if not isinstance(answer_units, dict):
        raise ValueError("judge response is missing answer_units")
    try:
        unit_total = int(float(answer_units.get("total", 0)))
        int(float(answer_units["correct"]))
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("judge response has invalid answer_units") from exc
    if unit_total <= 0:
        raise ValueError("judge response must enumerate at least one answer unit")

    rubric_points = result.get("rubric_points")
    if not isinstance(rubric_points, dict):
        raise ValueError("judge response is missing rubric_points")
    try:
        float(rubric_points["earned"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("judge response has invalid rubric_points.earned") from exc
    if not isinstance(rubric_points.get("criteria"), list) or not rubric_points["criteria"]:
        raise ValueError("judge response must include rubric_points.criteria")


def validate_judge_result(task_id: str, result: dict[str, Any]) -> dict[str, Any]:
    require_complete_judge_shape(result)
    result["task_id"] = result.get("task_id") or task_id
    raw_scores = result.get("scores") if isinstance(result.get("scores"), dict) else result
    scores = {key: clamp_score(raw_scores.get(key, 0)) for key in OFFICIAL_SCORE_KEYS}
    answer_units = normalize_answer_units(result.get("answer_units"))
    rubric_points = normalize_rubric_points(result.get("rubric_points"))
    if rubric_points["score"] is not None:
        scores["llm_rubric_score"] = rubric_points["score"]
    flags = answer_unit_flags(answer_units)
    answer_scale_normalized = False
    if (
        0 < scores["answer_correctness_score"] <= 1
        and answer_units["unit_score"] is not None
        and answer_units["unit_score"] > 1
    ):
        scores["answer_correctness_score"] = round(
            scores["answer_correctness_score"] * 100.0, 2
        )
        answer_scale_normalized = True
    if answer_units["unit_score"] is not None and answer_units["unit_score"] < scores["answer_correctness_score"]:
        scores["answer_correctness_score"] = answer_units["unit_score"]
    applied_caps: list[dict[str, Any]] = []
    raw_mean_score = round(sum(scores.values()) / len(OFFICIAL_SCORE_KEYS), 2)
    mean_cap = 100.0
    mean_score = raw_mean_score
    result["scores"] = scores
    result["mean_score"] = mean_score
    result["raw_mean_score"] = raw_mean_score
    result["mean_cap"] = mean_cap
    result["answer_units"] = answer_units
    result["rubric_points"] = rubric_points
    result["answer_unit_flags"] = flags
    result["answer_score_scale_normalized"] = answer_scale_normalized
    result["applied_caps"] = applied_caps
    result["raw_judge_verdict"] = str(result.get("verdict", ""))
    result["verdict"] = infer_verdict(mean_score)
    rationale = result.get("rationale") if isinstance(result.get("rationale"), dict) else {}
    result["rationale"] = {key: str(rationale.get(key, "")) for key in RATIONALE_KEYS}
    result["critical_errors"] = normalize_string_list(result.get("critical_errors"))
    result["missing_answer_elements"] = normalize_string_list(result.get("missing_answer_elements"))
    result["unsupported_overclaims"] = normalize_string_list(result.get("unsupported_overclaims"))
    result["one_sentence_rationale"] = str(result.get("one_sentence_rationale", ""))
    return result


def judge_error_result(task_id: str, exc: BaseException) -> dict[str, Any]:
    return {
        "task_id": task_id,
        "scores": {key: 0.0 for key in OFFICIAL_SCORE_KEYS},
        "answer_units": {"total": 0, "correct": 0, "unit_score": None, "wrong_or_missing": [], "notes": ""},
        "rubric_points": {"total": 20.0, "earned": None, "score": None, "criteria": [], "notes": ""},
        "answer_unit_flags": {},
        "applied_caps": [],
        "raw_mean_score": 0.0,
        "mean_cap": 0.0,
        "mean_score": 0.0,
        "verdict": "judge_error",
        "rationale": {key: "" for key in RATIONALE_KEYS},
        "critical_errors": [str(exc)],
        "missing_answer_elements": [],
        "unsupported_overclaims": [],
        "one_sentence_rationale": "Judge call failed.",
    }


def solver_error_zero_result(task_id: str, metadata: dict[str, Any]) -> dict[str, Any]:
    result = {
        "task_id": task_id,
        "scores": {key: 0.0 for key in OFFICIAL_SCORE_KEYS},
        "answer_units": {
            "total": 0,
            "correct": 0,
            "unit_score": 0.0,
            "wrong_or_missing": ["No valid final answer was produced."],
            "notes": "Solver timeout or protocol failure is scored as zero.",
        },
        "rubric_points": {
            "total": 20.0,
            "earned": 0.0,
            "score": 0.0,
            "criteria": [],
            "notes": "No rubric credit is awarded without a valid final answer.",
        },
        "answer_unit_flags": {},
        "applied_caps": [],
        "raw_mean_score": 0.0,
        "mean_cap": 0.0,
        "mean_score": 0.0,
        "verdict": "solver_error_scored_zero",
        "rationale": {key: "" for key in RATIONALE_KEYS},
        "critical_errors": ["Solver run did not complete and is scored as zero."],
        "missing_answer_elements": ["Valid final answer"],
        "unsupported_overclaims": [],
        "one_sentence_rationale": "Solver run failed, so all answer and rubric credit is zero.",
    }
    result.update(metadata)
    return result


def judge_one(
    task_dir: Path,
    pred_root: Path,
    model: str,
    base_url: str,
    api_key: str,
    timeout: int,
    use_response_format: bool,
    retries: int,
) -> dict[str, Any]:
    task_id = task_dir.name
    run_dir = pred_root / task_id
    metadata = collect_metadata(task_dir, run_dir)
    scoreable_invalid = (
        metadata.get("run_status") not in ("", "ok")
        and has_scoreable_final_answer(run_dir)
    )
    if metadata.get("run_status") not in ("", "ok") and not scoreable_invalid:
        return solver_error_zero_result(task_id, metadata)
    retryable = (urllib.error.URLError, KeyError, TypeError, ValueError, json.JSONDecodeError, OSError)

    def call_stage(messages: list[dict[str, str]]) -> dict[str, Any]:
        last_exc: BaseException | None = None
        for attempt in range(retries + 1):
            try:
                return call_openai_compatible_raw(
                    messages,
                    model,
                    base_url,
                    api_key,
                    timeout,
                    use_response_format=use_response_format,
                )
            except retryable as exc:
                last_exc = exc
                if attempt < retries:
                    time.sleep(min(2.0 * (attempt + 1), 8.0))
        assert last_exc is not None
        raise last_exc

    try:
        combined_result = call_stage(build_messages(task_dir, run_dir))
        combined_result["judge_protocol"] = "single_combined_answer_and_rubric_v1"
        combined_result["judge_call_count"] = 1
        validated = validate_judge_result(task_id, combined_result)
        validated.update(metadata)
        validated["scoreable_invalid_final"] = scoreable_invalid
        return validated
    except retryable as exc:
        last_exc = exc
    failed = judge_error_result(task_id, last_exc)
    failed.update(metadata)
    return failed


def write_csv(path: Path, results: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "task_id",
        "event_id",
        "task_type",
        "task_subtype",
        "target_family",
        "schema_version",
        "run_status",
        "answer_type",
        "evidence_boundary",
        "judge_protocol",
        "judge_call_count",
        "scoreable_invalid_final",
        "answer_score_scale_normalized",
        *PROCESS_DIAGNOSTIC_KEYS,
        *PROCESS_TEXT_KEYS,
        *TOOL_TRACE_JSON_KEYS,
        "answer_units_total",
        "answer_units_correct",
        "answer_units_score",
        "answer_unit_flags",
        "rubric_points_total",
        "rubric_points_earned",
        "rubric_points_score",
        "rubric_points_criteria",
        "rubric_points_notes",
        *OFFICIAL_SCORE_KEYS,
        "raw_mean_score",
        "mean_cap",
        "mean_score",
        "applied_caps",
        "judge_status",
        "excluded_from_official",
        "verdict",
        "raw_judge_verdict",
        *[f"rationale_{key}" for key in RATIONALE_KEYS],
        "critical_errors",
        "missing_answer_elements",
        "unsupported_overclaims",
        "one_sentence_rationale",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for result in sorted(results, key=lambda item: item.get("task_id", "")):
            scores = result.get("scores", {})
            rationale = result.get("rationale", {})
            row: dict[str, Any] = {"task_id": result.get("task_id", "")}
            answer_units = result.get("answer_units", {}) if isinstance(result.get("answer_units"), dict) else {}
            rubric_points = result.get("rubric_points", {}) if isinstance(result.get("rubric_points"), dict) else {}
            for key in [
                "event_id",
                "task_type",
                "task_subtype",
                "target_family",
                "schema_version",
                "run_status",
                "answer_type",
                "evidence_boundary",
                "judge_protocol",
                "judge_call_count",
                "scoreable_invalid_final",
                "answer_score_scale_normalized",
                *PROCESS_DIAGNOSTIC_KEYS,
                *PROCESS_TEXT_KEYS,
                *TOOL_TRACE_JSON_KEYS,
            ]:
                value = result.get(key, "")
                row[key] = json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else value
            row["answer_units_total"] = answer_units.get("total", "")
            row["answer_units_correct"] = answer_units.get("correct", "")
            row["answer_units_score"] = "" if answer_units.get("unit_score") is None else answer_units.get("unit_score")
            row["answer_unit_flags"] = json.dumps(result.get("answer_unit_flags", {}), ensure_ascii=False)
            row["rubric_points_total"] = rubric_points.get("total", "")
            row["rubric_points_earned"] = "" if rubric_points.get("earned") is None else rubric_points.get("earned")
            row["rubric_points_score"] = "" if rubric_points.get("score") is None else rubric_points.get("score")
            row["rubric_points_criteria"] = json.dumps(rubric_points.get("criteria", []), ensure_ascii=False)
            row["rubric_points_notes"] = rubric_points.get("notes", "")
            row.update({key: scores.get(key, 0) for key in OFFICIAL_SCORE_KEYS})
            row["raw_mean_score"] = result.get("raw_mean_score", result.get("mean_score", 0))
            row["mean_cap"] = result.get("mean_cap", "")
            row["mean_score"] = result.get("mean_score", 0)
            row["applied_caps"] = json.dumps(result.get("applied_caps", []), ensure_ascii=False)
            verdict = str(result.get("verdict", ""))
            if verdict == "judge_error":
                row["judge_status"] = "judge_error"
            elif verdict == "solver_error_scored_zero":
                row["judge_status"] = "solver_error_scored_zero"
            else:
                row["judge_status"] = "ok"
            row["excluded_from_official"] = verdict == "judge_error"
            row["verdict"] = result.get("verdict", "")
            row["raw_judge_verdict"] = result.get("raw_judge_verdict", "")
            row.update({f"rationale_{key}": rationale.get(key, "") for key in RATIONALE_KEYS})
            for key in ["critical_errors", "missing_answer_elements", "unsupported_overclaims"]:
                row[key] = json.dumps(result.get(key, []), ensure_ascii=False)
            row["one_sentence_rationale"] = result.get("one_sentence_rationale", "")
            writer.writerow(row)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the official core LLM judge.")
    parser.add_argument("--task-dir", default="tasks")
    parser.add_argument("--pred-dir", default="outputs/interactive_tool_agent/gpt-5.5")
    parser.add_argument("--submission-dir", default="", help="Alias for --pred-dir when scoring an external submission directory.")
    parser.add_argument("--out-dir", default="reports/judge")
    parser.add_argument("--task-id", action="append", default=[])
    parser.add_argument(
        "--rejudge-task-id",
        action="append",
        default=[],
        help="With --resume, recompute this task even when a prior result exists.",
    )
    parser.add_argument("--task-file", default="", help="Newline-separated task ids to judge.")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume an interrupted atomic .tmp run and judge only unfinished or judge-error tasks.",
    )
    parser.add_argument(
        "--no-response-format",
        action="store_true",
        help="Do not send response_format=json_object. Use this for OpenAI-compatible gateways that reject it.",
    )
    return parser.parse_args()


def prepare_atomic_out_dir(out_dir: Path, resume: bool = False) -> Path:
    tmp_dir = out_dir.with_name(out_dir.name + ".tmp")
    if resume:
        if tmp_dir.exists():
            return tmp_dir
        if out_dir.exists():
            shutil.copytree(out_dir, tmp_dir)
            return tmp_dir
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir(parents=True, exist_ok=True)
    return tmp_dir


def dedupe_results(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for result in results:
        task_id = str(result.get("task_id") or "").strip()
        if not task_id:
            continue
        if task_id in latest:
            del latest[task_id]
        latest[task_id] = result
    return list(latest.values())


def load_existing_results(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    results: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            results.append(value)
    return dedupe_results(results)


def completed_result_ids(
    results: list[dict[str, Any]], force_rejudge_ids: set[str] | None = None
) -> set[str]:
    forced = force_rejudge_ids or set()
    return {
        str(result.get("task_id"))
        for result in results
        if result.get("verdict") != "judge_error"
        and str(result.get("task_id")) not in forced
    }


def commit_atomic_out_dir(work_dir: Path, out_dir: Path, aggregate: dict[str, Any]) -> None:
    failed_dir = out_dir.with_name(out_dir.name + ".failed")
    if failed_dir.exists():
        shutil.rmtree(failed_dir)
    protects_existing = (
        out_dir.exists()
        and (out_dir / "per_task_judge_scores.csv").exists()
        and aggregate.get("official_scored_count", 0) == 0
        and aggregate.get("judge_error_count", 0) > 0
    )
    if protects_existing:
        work_dir.rename(failed_dir)
        raise SystemExit(
            f"Judge produced zero official scored rows with judge errors; preserved existing outputs in {out_dir} "
            f"and wrote failed attempt to {failed_dir}."
        )
    if out_dir.exists():
        shutil.rmtree(out_dir)
    work_dir.rename(out_dir)


def load_task_ids(path: Path | None) -> set[str]:
    if not path:
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()}


def mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 4) if values else 0.0


def main() -> None:
    args = parse_args()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set. Set it in the environment before running LLM judge.")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    model = os.environ.get("OPENAI_MODEL", "gpt-5.5")
    task_root = Path(args.task_dir)
    pred_root = Path(args.submission_dir or args.pred_dir)
    out_dir = Path(args.out_dir)
    work_dir = prepare_atomic_out_dir(out_dir, resume=args.resume)
    task_dirs = [p for p in sorted(task_root.iterdir()) if p.is_dir() and (p / "computed_gt.json").exists()]
    force_rejudge_ids = set(args.rejudge_task_id)
    wanted = (
        set(args.task_id)
        | force_rejudge_ids
        | load_task_ids(Path(args.task_file) if args.task_file else None)
    )
    if wanted:
        task_dirs = [p for p in task_dirs if p.name in wanted]
    if args.limit > 0:
        task_dirs = task_dirs[: args.limit]

    jsonl_path = work_dir / "per_task_judge_scores.jsonl"
    results = load_existing_results(jsonl_path) if args.resume else []
    completed_ids = completed_result_ids(results, force_rejudge_ids)
    task_dirs = [task_dir for task_dir in task_dirs if task_dir.name not in completed_ids]
    workers = max(1, args.workers)
    with jsonl_path.open("a" if args.resume else "w", encoding="utf-8") as jsonl:
        if workers == 1:
            for idx, task_dir in enumerate(task_dirs, start=1):
                result = judge_one(
                    task_dir,
                    pred_root,
                    model,
                    base_url,
                    api_key,
                    args.timeout,
                    use_response_format=not args.no_response_format,
                    retries=args.retries,
                )
                results.append(result)
                jsonl.write(json.dumps(result, ensure_ascii=False) + "\n")
                jsonl.flush()
                print(f"[{idx}/{len(task_dirs)}] {task_dir.name}: {result.get('mean_score')} {result.get('verdict')}")
                if args.sleep:
                    time.sleep(args.sleep)
        else:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                future_map = {
                    executor.submit(
                        judge_one,
                        task_dir,
                        pred_root,
                        model,
                        base_url,
                        api_key,
                        args.timeout,
                        not args.no_response_format,
                        args.retries,
                    ): task_dir
                    for task_dir in task_dirs
                }
                completed = 0
                for future in as_completed(future_map):
                    task_dir = future_map[future]
                    completed += 1
                    try:
                        result = future.result()
                    except Exception as exc:
                        result = judge_error_result(task_dir.name, exc)
                    results.append(result)
                    jsonl.write(json.dumps(result, ensure_ascii=False) + "\n")
                    jsonl.flush()
                    print(f"[{completed}/{len(task_dirs)}] {task_dir.name}: {result.get('mean_score')} {result.get('verdict')}")

    results = sorted(dedupe_results(results), key=lambda result: str(result.get("task_id", "")))
    with jsonl_path.open("w", encoding="utf-8") as jsonl:
        for result in results:
            jsonl.write(json.dumps(result, ensure_ascii=False) + "\n")
    write_csv(work_dir / "per_task_judge_scores.csv", results)
    valid_results = [
        result
        for result in results
        if result.get("verdict") != "judge_error"
    ]
    aggregate = {
        "schema_version": "official_core_judge_v3",
        "judge_model": model,
        "judge_base_url": base_url,
        "count": len(results),
        "judge_error_count": sum(1 for result in results if result.get("verdict") == "judge_error"),
        "solver_error_scored_zero_count": sum(
            1 for result in results if result.get("verdict") == "solver_error_scored_zero"
        ),
        "official_scored_count": len(valid_results),
        "mean_score": mean([float(result.get("mean_score", 0)) for result in valid_results]),
        "mean_scores": {
            key: mean([float(result.get("scores", {}).get(key, 0)) for result in valid_results])
            for key in OFFICIAL_SCORE_KEYS
        },
        "process_diagnostics_official_scored": {
            key: mean([
                float(result.get(key, 0) or 0)
                for result in valid_results
                if result.get(key, "") != ""
            ])
            for key in PROCESS_DIAGNOSTIC_KEYS
        },
        "mean_llm_rubric_trace_score_official_scored": mean([
            float(result.get("scores", {}).get("llm_rubric_score", 0))
            for result in valid_results
        ]),
    }
    (work_dir / "aggregate_judge_scores.json").write_text(json.dumps(aggregate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    commit_atomic_out_dir(work_dir, out_dir, aggregate)
    print(json.dumps(aggregate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
