#!/usr/bin/env python3
"""Build the official benchmark report from LLM judge output and capability labels."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any


CORE_SCORE_KEYS = [
    "answer_correctness_score",
    "llm_rubric_score",
]

OFFICIAL_SCORE_KEYS = CORE_SCORE_KEYS

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

TOOL_TRACE_SUMMARY_FIELDS = [
    "summary_type",
    "name",
    "tool",
    "value_count",
    "total_rows",
    "excluded_rows",
    "mean",
    "median",
    "p25",
    "p75",
    "min",
    "max",
    "call_count",
    "success_count",
    "error_count",
    "success_rate",
    "task_count_with_tool",
    "mean_calls_per_official_task",
    "evidence_file_reference_count",
    "unique_evidence_file_count",
]

STRICT_CORRECT_THRESHOLD = 95.0

METRIC_DEFINITIONS = {
    "answer_correctness_score": "Partial-credit final-answer correctness against GT.",
    "llm_rubric_score": "Independent process-only 20-point solution-rubric score converted to percent.",
    "mean_score": "Simple unweighted mean of answer_correctness_score and llm_rubric_score.",
}

RATIONALE_KEYS = [
    "answer_correctness",
    "llm_rubric",
]


SOLVER_FAILURE_VERDICTS = {"solver_error_scored_zero"}


def is_solver_failure(row: dict[str, Any]) -> bool:
    verdict = str(row.get("verdict", "")).strip().lower()
    if verdict == "judge_error":
        return False
    run_status = str(row.get("run_status", "")).strip().lower()
    return verdict in SOLVER_FAILURE_VERDICTS or run_status not in {"", "ok"}


def is_official_scored(row: dict[str, Any]) -> bool:
    return str(row.get("verdict", "")).strip().lower() != "judge_error"


def read_csv(path: Path, *, required: bool = True) -> list[dict[str, str]]:
    if not path.exists():
        if required:
            raise FileNotFoundError(path)
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def resolve_path(path: str) -> Path:
    raw = Path(path)
    return raw.resolve() if raw.is_absolute() else (Path.cwd() / raw).resolve()


def resolve_optional_path(path: str) -> Path | None:
    return resolve_path(path) if path else None


def path_string(path: Path | None) -> str:
    return str(path) if path else ""


def score_value(row: dict[str, Any], key: str) -> float:
    raw = row.get(key, "")
    if raw in ("", None):
        raise KeyError(key)
    try:
        value = float(raw)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"invalid score for {key}: {raw!r}") from exc
    return round(max(0.0, min(value, 100.0)), 2)


def optional_float(row: dict[str, Any], key: str) -> float | str:
    raw = row.get(key, "")
    if raw in ("", None):
        return ""
    try:
        return round(float(raw), 2)
    except (TypeError, ValueError):
        return ""


def parse_json_value(value: Any, default: Any) -> Any:
    if isinstance(value, (dict, list)):
        return value
    if value in ("", None):
        return default
    try:
        return json.loads(str(value))
    except (TypeError, json.JSONDecodeError):
        return default


def unit_score(row: dict[str, Any]) -> float | None:
    raw = row.get("answer_units_score", "")
    if raw not in ("", None):
        try:
            return round(max(0.0, min(float(raw), 100.0)), 2)
        except (TypeError, ValueError):
            return None
    try:
        total = float(row.get("answer_units_total") or 0)
        correct = float(row.get("answer_units_correct") or 0)
    except (TypeError, ValueError):
        return None
    if total <= 0:
        return None
    return round(max(0.0, min(100.0 * correct / total, 100.0)), 2)


def strict_correct(row: dict[str, Any], threshold: float = STRICT_CORRECT_THRESHOLD) -> bool:
    score = unit_score(row)
    return score is not None and score >= threshold


def split_dimensions(raw: str) -> list[str]:
    return [part.strip() for part in str(raw or "").replace("|", ";").split(";") if part.strip()]


def mean(values: list[float]) -> float:
    return round(statistics.fmean(values), 2) if values else 0.0


def percentile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return round(ordered[0], 2)
    idx = (len(ordered) - 1) * p
    low = int(idx)
    high = min(low + 1, len(ordered) - 1)
    weight = idx - low
    return round(ordered[low] * (1 - weight) + ordered[high] * weight, 2)


def summary_stats(values: list[float]) -> dict[str, float | str]:
    if not values:
        return {"mean": "", "median": "", "p25": "", "p75": "", "min": "", "max": ""}
    return {
        "mean": mean(values),
        "median": round(statistics.median(values), 2),
        "p25": percentile(values, 0.25),
        "p75": percentile(values, 0.75),
        "min": round(min(values), 2),
        "max": round(max(values), 2),
    }


def diagnostic_mean(rows: list[dict[str, Any]], key: str) -> float | str:
    values = numeric_values(rows, key)
    return mean(values) if values else ""


def normalize_rows(
    judge_rows: list[dict[str, str]],
    metadata_rows: list[dict[str, str]],
    dimension_rows: list[dict[str, str]] | None = None,
) -> list[dict[str, Any]]:
    metadata_by_id = {row.get("task_id", ""): row for row in metadata_rows if row.get("task_id")}
    dimensions_by_id = {row.get("task_id", ""): row for row in dimension_rows or [] if row.get("task_id")}
    out: list[dict[str, Any]] = []
    missing: list[str] = []

    for row in judge_rows:
        task_id = row.get("task_id", "").strip()
        if not task_id:
            raise ValueError("judge CSV contains a row without task_id")
        metadata = metadata_by_id.get(task_id, {})
        dimension_info = dimensions_by_id.get(task_id, {})
        dimension_labels = split_dimensions(dimension_info.get("dimension_labels", ""))
        item: dict[str, Any] = {
            "task_id": task_id,
            "event_id": row.get("event_id") or metadata.get("event_id") or task_id.split("_")[0],
            "task_type": row.get("task_type") or metadata.get("task_type", ""),
            "task_subtype": row.get("task_subtype") or metadata.get("task_subtype", ""),
            "primary_dimension": dimension_info.get("primary_dimension", ""),
            "dimension_labels": ";".join(dimension_labels),
            "scoring_source": "llm_judge_core_scores_plus_capability_labels",
            "verdict": row.get("verdict", ""),
            "raw_judge_verdict": row.get("raw_judge_verdict", ""),
            "run_status": row.get("run_status") or metadata.get("run_status", ""),
            "answer_units_total": row.get("answer_units_total", ""),
            "answer_units_correct": row.get("answer_units_correct", ""),
            "answer_units_score": row.get("answer_units_score", ""),
            "answer_unit_flags": row.get("answer_unit_flags", ""),
            "rubric_points_total": row.get("rubric_points_total", ""),
            "rubric_points_earned": row.get("rubric_points_earned", ""),
            "rubric_points_score": row.get("rubric_points_score", ""),
            "rubric_points_criteria": row.get("rubric_points_criteria", ""),
            "rubric_points_notes": row.get("rubric_points_notes", ""),
            "raw_mean_score": row.get("raw_mean_score", ""),
            "mean_cap": row.get("mean_cap", ""),
            "applied_caps": row.get("applied_caps", ""),
        }
        for key in PROCESS_DIAGNOSTIC_KEYS:
            item[key] = optional_float(row, key)
        for key in PROCESS_TEXT_KEYS:
            item[key] = row.get(key, "")
        for key in TOOL_TRACE_JSON_KEYS:
            item[key] = row.get(key, "")
        values: list[float] = []
        for key in OFFICIAL_SCORE_KEYS:
            try:
                value = score_value(row, key)
            except KeyError:
                missing.append(f"{task_id}:{key}")
                value = 0.0
            item[key] = value
        rubric_points_score = optional_float(row, "rubric_points_score")
        if rubric_points_score != "":
            item["llm_rubric_score"] = rubric_points_score
        if is_solver_failure(item):
            for key in OFFICIAL_SCORE_KEYS:
                item[key] = 0.0
            item["answer_units_score"] = 0.0
            item["answer_units_correct"] = 0
            item["rubric_points_earned"] = 0.0
            item["rubric_points_score"] = 0.0
        values = [float(item[key]) for key in OFFICIAL_SCORE_KEYS]
        item["llm_rubric_trace_score"] = item["llm_rubric_score"]
        item["mean_score"] = mean(values)
        for key in RATIONALE_KEYS:
            item[f"rationale_{key}"] = row.get(f"rationale_{key}", "")
        item["one_sentence_rationale"] = row.get("one_sentence_rationale", "")
        item["official_scored"] = "yes" if is_official_scored(item) else "no"
        item["strict_correct_95"] = "yes" if is_official_scored(item) and strict_correct(item) else "no"
        out.append(item)

    if missing:
        preview = ", ".join(missing[:20])
        suffix = " ..." if len(missing) > 20 else ""
        raise ValueError("Official report requires core judge score columns. Missing: " + preview + suffix)
    return out


def summarize(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    scored_rows = [row for row in rows if is_official_scored(row)]
    for metric in [*OFFICIAL_SCORE_KEYS, "mean_score"]:
        values = [float(row[metric]) for row in scored_rows]
        out.append({
            "metric": metric,
            "count": len(values),
            "total_rows": len(rows),
            "excluded_rows": len(rows) - len(scored_rows),
            **summary_stats(values),
        })
    return out


def process_diagnostics_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    scored_rows = [row for row in rows if is_official_scored(row)]
    metric_keys = [*PROCESS_DIAGNOSTIC_KEYS, "llm_rubric_trace_score"]
    for metric in metric_keys:
        values: list[float] = []
        for row in scored_rows:
            raw = row.get(metric, "")
            if raw in ("", None):
                continue
            try:
                values.append(float(raw))
            except (TypeError, ValueError):
                continue
        out.append({
            "metric": metric,
            "count": len(values),
            "total_rows": len(rows),
            "excluded_rows": len(rows) - len(scored_rows),
            **summary_stats(values),
        })
    return out


def tool_trace_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    scored_rows = [row for row in rows if is_official_scored(row)]
    out: list[dict[str, Any]] = []
    for item in process_diagnostics_summary(rows):
        out.append({
            "summary_type": "overall_metric",
            "name": item["metric"],
            "tool": "__all__",
            "value_count": item["count"],
            "total_rows": item["total_rows"],
            "excluded_rows": item["excluded_rows"],
            "mean": item["mean"],
            "median": item["median"],
            "p25": item["p25"],
            "p75": item["p75"],
            "min": item["min"],
            "max": item["max"],
            "call_count": "",
            "success_count": "",
            "error_count": "",
            "success_rate": "",
            "task_count_with_tool": "",
            "mean_calls_per_official_task": "",
            "evidence_file_reference_count": "",
            "unique_evidence_file_count": "",
        })

    tool_totals: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "call_count": 0,
        "success_count": 0,
        "error_count": 0,
        "task_count_with_tool": 0,
        "evidence_file_reference_count": 0,
        "unique_evidence_files": set(),
    })
    per_task_tool_counts: list[dict[str, int]] = []
    for row in scored_rows:
        summaries = parse_json_value(row.get("tool_usage_summary"), [])
        if not isinstance(summaries, list):
            summaries = []
        seen_tools: set[str] = set()
        per_row_counts: dict[str, int] = {}
        for entry in summaries:
            if not isinstance(entry, dict):
                continue
            tool = str(entry.get("tool", "")).strip() or "__unknown__"
            stats = tool_totals[tool]
            call_count = int(float(entry.get("call_count") or 0))
            success_count = int(float(entry.get("success_count") or 0))
            error_count = int(float(entry.get("error_count") or 0))
            evidence_refs = int(float(entry.get("evidence_file_reference_count") or 0))
            unique_evidence_count = int(float(entry.get("unique_evidence_file_count") or 0))
            stats["call_count"] += call_count
            stats["success_count"] += success_count
            stats["error_count"] += error_count
            stats["evidence_file_reference_count"] += evidence_refs
            evidence_files = entry.get("evidence_files", [])
            if isinstance(evidence_files, list):
                for evidence_file in evidence_files:
                    stats["unique_evidence_files"].add(str(evidence_file))
            else:
                for idx in range(unique_evidence_count):
                    stats["unique_evidence_files"].add(f"{row.get('task_id', '')}:{tool}:{idx}")
            seen_tools.add(tool)
            per_row_counts[tool] = per_row_counts.get(tool, 0) + call_count
        for tool in seen_tools:
            tool_totals[tool]["task_count_with_tool"] += 1
        per_task_tool_counts.append(per_row_counts)

    for tool, stats in sorted(tool_totals.items()):
        values = [float(counts.get(tool, 0)) for counts in per_task_tool_counts]
        call_count = int(stats["call_count"])
        success_count = int(stats["success_count"])
        out.append({
            "summary_type": "tool",
            "name": tool,
            "tool": tool,
            "value_count": len(values),
            "total_rows": len(rows),
            "excluded_rows": len(rows) - len(scored_rows),
            "mean": mean(values),
            "median": round(statistics.median(values), 2) if values else 0.0,
            "p25": percentile(values, 0.25),
            "p75": percentile(values, 0.75),
            "min": round(min(values), 2) if values else 0.0,
            "max": round(max(values), 2) if values else 0.0,
            "call_count": call_count,
            "success_count": success_count,
            "error_count": int(stats["error_count"]),
            "success_rate": round(100.0 * success_count / call_count, 2) if call_count else "",
            "task_count_with_tool": int(stats["task_count_with_tool"]),
            "mean_calls_per_official_task": round(call_count / len(scored_rows), 2) if scored_rows else 0.0,
            "evidence_file_reference_count": int(stats["evidence_file_reference_count"]),
            "unique_evidence_file_count": len(stats["unique_evidence_files"]),
        })
    return out


def numeric_values(rows: list[dict[str, Any]], key: str) -> list[float]:
    values: list[float] = []
    for row in rows:
        raw = row.get(key, "")
        if raw in ("", None):
            continue
        try:
            values.append(float(raw))
        except (TypeError, ValueError):
            continue
    return values


def group_score_summary(subset: list[dict[str, Any]], total_count: int) -> dict[str, Any]:
    scored_subset = [row for row in subset if is_official_scored(row)]
    strict_subset = [row for row in scored_subset if strict_correct(row)]
    unit_scores = [score for row in scored_subset if (score := unit_score(row)) is not None]
    return {
        "task_count": total_count,
        "official_scored_count": len(scored_subset),
        "excluded_count": total_count - len(scored_subset),
        "strict_correct_95_count": len(strict_subset),
        "strict_accuracy_95": round(100.0 * len(strict_subset) / len(scored_subset), 2) if scored_subset else 0.0,
        "mean_unit_accuracy": mean(unit_scores),
        "mean_answer_correctness_score": mean([float(row["answer_correctness_score"]) for row in scored_subset]),
        "mean_llm_rubric_score": mean([float(row["llm_rubric_score"]) for row in scored_subset]),
        "mean_score": mean([float(row["mean_score"]) for row in scored_subset]),
        "mean_tool_call_count": diagnostic_mean(scored_subset, "tool_call_count"),
        "mean_llm_call_round_count": diagnostic_mean(scored_subset, "llm_call_round_count"),
        "mean_latency_s": diagnostic_mean(scored_subset, "latency_s"),
        "mean_prompt_tokens": diagnostic_mean(scored_subset, "prompt_tokens"),
        "mean_completion_tokens": diagnostic_mean(scored_subset, "completion_tokens"),
        "mean_total_tokens": diagnostic_mean(scored_subset, "total_tokens"),
        "mean_cached_prompt_tokens": diagnostic_mean(scored_subset, "cached_prompt_tokens"),
        "mean_estimated_cost_usd": diagnostic_mean(scored_subset, "estimated_cost_usd"),
        "mean_file_read_call_count": diagnostic_mean(scored_subset, "file_read_call_count"),
        "mean_unique_evidence_file_count": diagnostic_mean(scored_subset, "unique_evidence_file_count"),
        "mean_python_exec_count": diagnostic_mean(scored_subset, "python_exec_count"),
        "mean_forced_finalization_rate": diagnostic_mean(
            scored_subset, "forced_finalization_rate"
        ),
        "mean_llm_rubric_trace_score": mean([float(row["llm_rubric_trace_score"]) for row in scored_subset]),
    }


def strict_accuracy_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    scored_rows = [row for row in rows if is_official_scored(row)]
    correct_rows = [row for row in scored_rows if strict_correct(row)]
    unit_scores = [score for row in scored_rows if (score := unit_score(row)) is not None]
    return {
        "metric": "strict_answer_accuracy_at_95",
        "threshold": STRICT_CORRECT_THRESHOLD,
        "correct_count": len(correct_rows),
        "official_scored_count": len(scored_rows),
        "total_rows": len(rows),
        "excluded_rows": len(rows) - len(scored_rows),
        "accuracy": round(100.0 * len(correct_rows) / len(scored_rows), 2) if scored_rows else 0.0,
        "mean_unit_accuracy": mean(unit_scores),
        "median_unit_accuracy": round(statistics.median(unit_scores), 2) if unit_scores else 0.0,
    }


def by_task_type(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row.get("task_type", "")].append(row)
    out: list[dict[str, Any]] = []
    for task_type, subset in sorted(grouped.items()):
        item: dict[str, Any] = {
            "task_type": task_type,
            **group_score_summary(subset, len(subset)),
        }
        out.append(item)
    return out


def by_dimension(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    unlabelled: list[dict[str, Any]] = []
    for row in rows:
        labels = split_dimensions(row.get("dimension_labels", ""))
        if not labels:
            unlabelled.append(row)
            continue
        for label in labels:
            grouped[label].append(row)

    out: list[dict[str, Any]] = []
    for label, subset in sorted(grouped.items()):
        out.append({
            "dimension": label,
            "tagged_count": len(subset),
            **{key: value for key, value in group_score_summary(subset, len(subset)).items() if key != "task_count"},
        })

    if unlabelled:
        out.append({
            "dimension": "__unlabelled__",
            "tagged_count": len(unlabelled),
            **{key: value for key, value in group_score_summary(unlabelled, len(unlabelled)).items() if key != "task_count"},
        })
    return out


def metric_schema() -> dict[str, Any]:
    return {
        "schema_version": "official_core_label_report_v4",
        "score_range": "Core judge scores and label-group means are 0-100. Higher is better.",
        "core_judge_metrics": OFFICIAL_SCORE_KEYS,
        "metric_definitions": METRIC_DEFINITIONS,
        "capability_dimension_scores": "Seven capability-dimension metrics are grouped by task_sets/dimension_labels.csv. A task contributes to each of its 1-3 labels.",
        "capability_dimensions": [
            "quantitative_calculation",
            "physical_mechanism",
            "spatiotemporal_process",
            "multi_source_evidence",
            "causal_chain",
            "ranking_decision",
            "remote_sensing_geospatial",
        ],
        "tool_trace_summary": {
            "latency_s": "Wall-clock seconds recorded for the solver run in trajectory.json when available.",
            "tool_call_count": "Number of tool calls recorded in trajectory.json.",
            "tool_success_count": "Number of recorded tool calls with ok=true.",
            "tool_error_count": "Number of recorded tool calls without ok=true.",
            "tool_success_rate": "100 * tool_success_count / tool_call_count when tool calls exist.",
            "agent_step_count": "Number of distinct recorded tool-call step ids.",
            "llm_call_round_count": "Number of raw model-call usage records in trajectory.json.",
            "prompt_tokens": "Sum of prompt tokens across raw_usage records in trajectory.json.",
            "completion_tokens": "Sum of completion tokens across raw_usage records in trajectory.json.",
            "total_tokens": "Sum of total tokens across raw_usage records, or prompt + completion when total is missing.",
            "cached_prompt_tokens": "Sum of cached prompt tokens reported in raw_usage.prompt_tokens_details.cached_tokens when available.",
            "estimated_cost_usd": "Estimated solver cost in USD from token counts and configured pricing. Blank when pricing is not configured.",
            "file_read_call_count": "Interactive runs: number of direct file-inspection calls such as read_text_file, summarize_table_or_json, inspect_image. Direct prompt-context runs: number of local text evidence files embedded into the prompt context.",
            "unique_evidence_file_count": "Number of unique evidence files attached to tool calls.",
            "evidence_file_reference_count": "Total evidence-file references attached to tool calls before deduplication.",
            "list_files_call_count": "Number of package file-listing calls.",
            "search_call_count": "Number of package search calls.",
            "python_exec_count": "Number of Python execution calls.",
            "forced_finalization_rate": "Per task this is 100 for a budget-forced final answer and 0 for normal model completion; the report mean is the forced-finalization percentage.",
            "research_budget_seconds": "Maximum package-tool research time before finalization begins.",
            "total_budget_seconds": "Maximum total solve time including forced finalization.",
            "termination_reason": "Per-task terminal state such as model_final, round_limit, or research_time_limit.",
            "llm_rubric_trace_score": "Alias of llm_rubric_score, produced by the independent process judge from solution/rubric and visible trace without ground truth.",
        },
        "mean_score": "Simple unweighted mean of answer_correctness_score and llm_rubric_score. Capability-dimension metrics are reported separately instead of being folded into this mean.",
        "strict_answer_accuracy_at_95": "A task is counted correct only when answer_units_score is at least 95. Solver timeouts and protocol-format failures remain in the denominator with zero credit; judge infrastructure failures are excluded.",
        "dimension_accuracy": "Dimension accuracy is tag based. A manually labelled task contributes to each of its 1-3 dimension labels. For each dimension, strict_accuracy_95 = tagged tasks with answer_units_score >= 95 divided by officially scored tagged tasks.",
        "excluded_from_official_metrics": [
            "runtime/API failure counters",
            "format-failure counters",
            "binary pass/fail metrics",
            "deterministic exact-match hard-scoring metrics",
            "legacy detailed heuristic metrics",
            "legacy five free-form earth-science judge subscores",
        ],
        "diagnostic_policy": "Tool, trace, latency, token, and configured-cost diagnostics are reported together in the tool_trace_summary table of official_report.json for trace analysis and agent-efficiency comparisons. They are not included in official answer correctness or mean_score.",
        "policy": [
            "Core answer and rubric scores come from the LLM judge CSV.",
            "Capability-dimension metrics come from manual task labels plus strict answer-unit correctness.",
            "Solver timeouts and protocol-format failures receive zero answer, rubric, and unit scores and remain in every applicable denominator.",
            "Only judge infrastructure failures marked judge_error are excluded from official aggregate means.",
            "The report does not derive correctness from exact string matching, field overlap, threshold gates, or legacy hard scorers.",
            "JSON extraction may expose the model answer, but substantive scoring is semantic and rubric-aware.",
            "Solver failure counts remain diagnostics rather than separate paper metrics, while their affected tasks receive zero quality credit.",
        ],
        "paper_table_recommendation": "Model | Strict Acc@95 | Answer | Rubric/Trace | Mean Core | Quant | Mechanism | Spatiotemporal | Multi-source | Causal | Ranking | Remote sensing | Tool calls | File reads | LLM rounds | Tokens | Latency | Cost",
    }


def write_schema(path: Path) -> None:
    write_json(path, metric_schema())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the official core, capability-dimension, and process-diagnostic benchmark report.")
    parser.add_argument("--judge-csv", default="reports/judge/per_task_judge_scores.csv")
    parser.add_argument("--metadata-csv", default="", help="Optional CSV with task metadata columns such as task_type/task_subtype/run_status.")
    parser.add_argument("--dimension-labels-csv", default="task_sets/dimension_labels.csv", help="Optional task dimension label CSV.")
    parser.add_argument("--detailed-csv", default="", help="Deprecated alias for --metadata-csv; used only for metadata if supplied.")
    parser.add_argument("--out-dir", default="reports/final")
    parser.add_argument("--out-file", default="", help="Single JSON report path. Defaults to <out-dir>/official_report.json.")
    parser.add_argument("--legacy-csv", action="store_true", help="Also write the old multi-file CSV/JSON report artifacts.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    metadata_arg = args.metadata_csv or args.detailed_csv
    judge_csv_path = resolve_path(args.judge_csv)
    metadata_path = resolve_optional_path(metadata_arg)
    dimension_labels_path = resolve_optional_path(args.dimension_labels_csv)
    judge_rows = read_csv(judge_csv_path)
    metadata_rows = read_csv(metadata_path, required=False) if metadata_path else []
    dimension_rows = read_csv(dimension_labels_path, required=False) if dimension_labels_path else []
    rows = normalize_rows(judge_rows, metadata_rows, dimension_rows)

    out_dir = resolve_path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = resolve_path(args.out_file) if args.out_file else out_dir / "official_report.json"
    per_task_fields = [
        "task_id",
        "event_id",
        "task_type",
        "task_subtype",
        "primary_dimension",
        "dimension_labels",
        "scoring_source",
        "verdict",
        "raw_judge_verdict",
        "run_status",
        "official_scored",
        "answer_units_total",
        "answer_units_correct",
        "answer_units_score",
        "answer_unit_flags",
        "strict_correct_95",
        "rubric_points_total",
        "rubric_points_earned",
        "rubric_points_score",
        "rubric_points_criteria",
        "rubric_points_notes",
        *OFFICIAL_SCORE_KEYS,
        "mean_score",
        "raw_mean_score",
        "mean_cap",
        "applied_caps",
        *PROCESS_DIAGNOSTIC_KEYS,
        *PROCESS_TEXT_KEYS,
        *TOOL_TRACE_JSON_KEYS,
        "llm_rubric_trace_score",
        *[f"rationale_{key}" for key in RATIONALE_KEYS],
        "one_sentence_rationale",
    ]
    group_fields = [
        "official_scored_count",
        "excluded_count",
        "strict_correct_95_count",
        "strict_accuracy_95",
        "mean_unit_accuracy",
        "mean_answer_correctness_score",
        "mean_llm_rubric_score",
        "mean_score",
        "mean_tool_call_count",
        "mean_llm_call_round_count",
        "mean_latency_s",
        "mean_prompt_tokens",
        "mean_completion_tokens",
        "mean_total_tokens",
        "mean_cached_prompt_tokens",
        "mean_estimated_cost_usd",
        "mean_file_read_call_count",
        "mean_unique_evidence_file_count",
        "mean_python_exec_count",
        "mean_forced_finalization_rate",
        "mean_llm_rubric_trace_score",
    ]
    core_metric_summary = summarize(rows)
    trace_summary = tool_trace_summary(rows)
    strict_summary = strict_accuracy_summary(rows)
    task_type_scores = by_task_type(rows)
    dimension_scores = by_dimension(rows)
    scored_rows = [row for row in rows if is_official_scored(row)]

    report = {
        "schema_version": "official_single_report_v2",
        "inputs": {
            "judge_csv": str(judge_csv_path),
            "metadata_csv": path_string(metadata_path),
            "dimension_labels_csv": path_string(dimension_labels_path),
        },
        "summary": {
            "tasks": len(rows),
            "official_scored_tasks": len(scored_rows),
            "excluded_tasks": len(rows) - len(scored_rows),
            "core_metrics": len(OFFICIAL_SCORE_KEYS),
            "mean_score": mean([float(row["mean_score"]) for row in scored_rows]),
            "mean_scores": {
                key: mean([float(row[key]) for row in scored_rows])
                for key in OFFICIAL_SCORE_KEYS
            },
            "strict_answer_accuracy_at_95": strict_summary,
        },
        "tables": {
            "core_scores_per_task": rows,
            "core_metric_summary": core_metric_summary,
            "tool_trace_summary": trace_summary,
            "strict_accuracy_summary": strict_summary,
            "scores_by_task_type": task_type_scores,
            "capability_dimension_scores": dimension_scores,
        },
        "metric_schema": metric_schema(),
        "report_file": str(out_file),
    }
    write_json(out_file, report)

    if args.legacy_csv:
        write_csv(out_dir / "official_core_scores_per_task.csv", rows, per_task_fields)
        write_csv(out_dir / "official_core_metric_summary.csv", core_metric_summary, ["metric", "count", "total_rows", "excluded_rows", "mean", "median", "p25", "p75", "min", "max"])
        write_csv(out_dir / "official_tool_trace_summary.csv", trace_summary, TOOL_TRACE_SUMMARY_FIELDS)
        write_csv(out_dir / "official_strict_accuracy_summary.csv", [strict_summary], ["metric", "threshold", "correct_count", "official_scored_count", "total_rows", "excluded_rows", "accuracy", "mean_unit_accuracy", "median_unit_accuracy"])
        write_csv(out_dir / "official_scores_by_task_type.csv", task_type_scores, ["task_type", "task_count", *group_fields])
        write_csv(out_dir / "official_capability_dimension_scores.csv", dimension_scores, ["dimension", "tagged_count", *group_fields])
        write_schema(out_dir / "official_metric_schema.json")

    console_summary = {
        **report["summary"],
        "report_file": str(out_file),
        "legacy_csv_written": bool(args.legacy_csv),
    }
    print(json.dumps(console_summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
