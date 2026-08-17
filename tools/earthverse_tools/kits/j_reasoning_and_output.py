from __future__ import annotations
from typing import Any
from ..core import dispatch
KIT = 'J Reasoning and Output'
__all__ = [
    'plan_evidence_collection',
    'select_minimal_tool_subset',
    'route_to_hazard_workflow',
    'build_hazard_metric_matrix',
    'synthesize_multisource_evidence',
    'rank_response_priorities',
    'assemble_structured_answer_fields',
    'summarize_key_findings_table',
    'build_decision_brief_sections',
    'compute_weighted_hazard_score',
    'merge_tool_outputs_by_time',
    'normalize_answer_units_and_fields',
    'infer_task_reasoning_axes',
    'build_mechanism_competition_table',
    'reconstruct_event_process_stages',
    'evaluate_physical_consistency',
    'synthesize_compound_hazard_chain',
    'compare_visual_numeric_evidence',
    'calibrate_event_severity_profile',
    'derive_response_priority_rationale',
    'test_option_hypothesis_consistency',
    'extract_required_computation_targets',
    'map_task_to_required_tools',
    'build_metric_dependency_graph',
    'reconcile_point_grid_regional_scale',
    'parse_mcq_options_and_select',
]

def plan_evidence_collection(**kwargs: Any) -> dict[str, Any]:
    """plan_evidence_collection

Kit: J Reasoning and Output
Purpose: Generate a task-specific evidence plan from the question and manifest.
Inputs: question, manifest
Output: ordered plan
Used by: agent controller
"""
    return dispatch('plan_evidence_collection', **kwargs)

def select_minimal_tool_subset(**kwargs: Any) -> dict[str, Any]:
    """select_minimal_tool_subset

Kit: J Reasoning and Output
Purpose: Select the smallest tool subset likely to answer a task.
Inputs: question, manifest, tool_registry
Output: tool subset
Used by: router
"""
    return dispatch('select_minimal_tool_subset', **kwargs)

def route_to_hazard_workflow(**kwargs: Any) -> dict[str, Any]:
    """route_to_hazard_workflow

Kit: J Reasoning and Output
Purpose: Route a task to heat, flood, fire, cyclone, geophysical, urban or climate workflow.
Inputs: metadata, question
Output: workflow label
Used by: router
"""
    return dispatch('route_to_hazard_workflow', **kwargs)

def build_hazard_metric_matrix(**kwargs: Any) -> dict[str, Any]:
    """build_hazard_metric_matrix

Kit: J Reasoning and Output
Purpose: Assemble hazard, exposure, impact and process metrics into a task-specific matrix for downstream reasoning.
Inputs: metric_groups, dimensions?, event_metadata?
Output: hazard metric matrix JSON
Used by: multi-step reasoning tasks
"""
    return dispatch('build_hazard_metric_matrix', **kwargs)

def synthesize_multisource_evidence(**kwargs: Any) -> dict[str, Any]:
    """synthesize_multisource_evidence

Kit: J Reasoning and Output
Purpose: Combine physical, remote-sensing, exposure and report evidence into a structured finding.
Inputs: evidence_objects
Output: evidence synthesis
Used by: final reasoning
"""
    return dispatch('synthesize_multisource_evidence', **kwargs)

def rank_response_priorities(**kwargs: Any) -> dict[str, Any]:
    """rank_response_priorities

Kit: J Reasoning and Output
Purpose: Rank days, places, mechanisms or actions using provided metrics and weights.
Inputs: items, metrics, weights
Output: ranked output
Used by: priority tasks
"""
    return dispatch('rank_response_priorities', **kwargs)

def assemble_structured_answer_fields(**kwargs: Any) -> dict[str, Any]:
    """assemble_structured_answer_fields

Kit: J Reasoning and Output
Purpose: Assemble computed metrics, labels and selected option fields into a requested structured answer object.
Inputs: fields, metrics, labels?, selected_option?
Output: structured answer fields JSON
Used by: structured QA tasks
"""
    return dispatch('assemble_structured_answer_fields', **kwargs)

def summarize_key_findings_table(**kwargs: Any) -> dict[str, Any]:
    """summarize_key_findings_table

Kit: J Reasoning and Output
Purpose: Summarize the most important computed findings as rows with metric, value, unit and interpretation.
Inputs: findings, metrics?, interpretations?
Output: key findings table JSON
Used by: short-answer reasoning tasks
"""
    return dispatch('summarize_key_findings_table', **kwargs)

def build_decision_brief_sections(**kwargs: Any) -> dict[str, Any]:
    """build_decision_brief_sections

Kit: J Reasoning and Output
Purpose: Organize hazard diagnosis, mechanism, exposure, impact-chain and action-priority findings into named briefing sections.
Inputs: hazard_findings, mechanism_findings?, impact_findings?, action_findings?
Output: briefing section JSON
Used by: expert briefing tasks
"""
    return dispatch('build_decision_brief_sections', **kwargs)

def compute_weighted_hazard_score(**kwargs: Any) -> dict[str, Any]:
    """compute_weighted_hazard_score

Kit: J Reasoning and Output
Purpose: Compute a weighted score from normalized hazard, exposure, persistence, anomaly and infrastructure metrics.
Inputs: metrics, weights, normalization?
Output: weighted hazard score JSON
Used by: priority and severity tasks
"""
    return dispatch('compute_weighted_hazard_score', **kwargs)

def merge_tool_outputs_by_time(**kwargs: Any) -> dict[str, Any]:
    """merge_tool_outputs_by_time

Kit: J Reasoning and Output
Purpose: Merge time-indexed outputs from weather, hydrology, air-quality or report timeline tools into one chronological table.
Inputs: tool_outputs, time_key?
Output: merged chronological table JSON
Used by: temporal synthesis tasks
"""
    return dispatch('merge_tool_outputs_by_time', **kwargs)

def normalize_answer_units_and_fields(**kwargs: Any) -> dict[str, Any]:
    """normalize_answer_units_and_fields

Kit: J Reasoning and Output
Purpose: Normalize answer fields, units, dates and option letters before final reporting or comparison.
Inputs: answer_fields, unit_map?, field_aliases?
Output: normalized answer field JSON
Used by: structured QA tasks
"""
    return dispatch('normalize_answer_units_and_fields', **kwargs)

def infer_task_reasoning_axes(**kwargs: Any) -> dict[str, Any]:
    """infer_task_reasoning_axes

Kit: J Reasoning and Output
Purpose: Infer which deep reasoning axes a task requires: mechanism, severity, image-numeric fusion, impact chain, response priority, or physical consistency.
Inputs: question, metadata?, question_context?
Output: reasoning-axis plan JSON
Used by: tool router and judge planning
"""
    return dispatch('infer_task_reasoning_axes', **kwargs)

def build_mechanism_competition_table(**kwargs: Any) -> dict[str, Any]:
    """build_mechanism_competition_table

Kit: J Reasoning and Output
Purpose: Compare plausible disaster mechanisms and record supporting, contradicting and secondary evidence for each candidate.
Inputs: candidate_mechanisms, evidence_objects, required_axes?
Output: mechanism competition table
Used by: MCQ and causal diagnosis tasks
"""
    return dispatch('build_mechanism_competition_table', **kwargs)

def reconstruct_event_process_stages(**kwargs: Any) -> dict[str, Any]:
    """reconstruct_event_process_stages

Kit: J Reasoning and Output
Purpose: Reconstruct event phases from precursor forcing through hazard peak, exposure interaction and aftermath.
Inputs: timeline_evidence, metrics, reports?
Output: ordered process-stage reconstruction
Used by: phase reconstruction and briefing tasks
"""
    return dispatch('reconstruct_event_process_stages', **kwargs)

def evaluate_physical_consistency(**kwargs: Any) -> dict[str, Any]:
    """evaluate_physical_consistency

Kit: J Reasoning and Output
Purpose: Check whether a proposed answer is physically consistent with event forcing, indices, scale, timing and known hazard processes.
Inputs: proposed_answer, metrics, mechanism_rules, event_metadata
Output: physical-consistency verdict and failure modes
Used by: answer assembly and agent self-check
"""
    return dispatch('evaluate_physical_consistency', **kwargs)

def synthesize_compound_hazard_chain(**kwargs: Any) -> dict[str, Any]:
    """synthesize_compound_hazard_chain

Kit: J Reasoning and Output
Purpose: Build a driver-hazard-exposure-impact chain for compound or cascading events across multiple hazard components.
Inputs: drivers, hazard_components, exposure_metrics, impact_claims
Output: compound hazard-chain JSON
Used by: compound disaster tasks
"""
    return dispatch('synthesize_compound_hazard_chain', **kwargs)

def compare_visual_numeric_evidence(**kwargs: Any) -> dict[str, Any]:
    """compare_visual_numeric_evidence

Kit: J Reasoning and Output
Purpose: Jointly interpret visual/remote-sensing cues and numeric indicators while separating what imagery can and cannot prove.
Inputs: image_summaries, numeric_metrics, question_context
Output: visual-numeric consistency report
Used by: image-numeric reasoning tasks
"""
    return dispatch('compare_visual_numeric_evidence', **kwargs)

def calibrate_event_severity_profile(**kwargs: Any) -> dict[str, Any]:
    """calibrate_event_severity_profile

Kit: J Reasoning and Output
Purpose: Convert peak, persistence, anomaly, spatial extent and exposure metrics into a calibrated event severity profile.
Inputs: hazard_metrics, baseline_metrics?, exposure_metrics?, thresholds?
Output: severity profile with calibrated labels
Used by: severity and index diagnosis tasks
"""
    return dispatch('calibrate_event_severity_profile', **kwargs)

def derive_response_priority_rationale(**kwargs: Any) -> dict[str, Any]:
    """derive_response_priority_rationale

Kit: J Reasoning and Output
Purpose: Derive a response-priority rationale from hazard timing, exposed systems, accessibility and cascading-risk indicators.
Inputs: hazard_metrics, exposure_metrics, impact_claims, candidate_actions
Output: ranked response rationale
Used by: ranking and emergency decision tasks
"""
    return dispatch('derive_response_priority_rationale', **kwargs)

def test_option_hypothesis_consistency(**kwargs: Any) -> dict[str, Any]:
    """test_option_hypothesis_consistency

Kit: J Reasoning and Output
Purpose: Treat each MCQ option as a hypothesis and compare its numeric, mechanism, timing and impact statements against computed metrics.
Inputs: options, metrics, mechanism_findings?, impact_findings?
Output: option hypothesis comparison JSON
Used by: MCQ reasoning tasks
"""
    return dispatch('test_option_hypothesis_consistency', **kwargs)

def extract_required_computation_targets(**kwargs: Any) -> dict[str, Any]:
    """extract_required_computation_targets

Kit: J Reasoning and Output
Purpose: Extract required variables, indices, thresholds, units and comparison targets from a question.
Inputs: question, metadata?
Output: required computation target JSON
Used by: tool planning tasks
"""
    return dispatch('extract_required_computation_targets', **kwargs)

def map_task_to_required_tools(**kwargs: Any) -> dict[str, Any]:
    """map_task_to_required_tools

Kit: J Reasoning and Output
Purpose: Map required computation targets and reasoning axes to concrete candidate tools.
Inputs: computation_targets, reasoning_axes?, tool_registry?
Output: required tool map JSON
Used by: tool routing tasks
"""
    return dispatch('map_task_to_required_tools', **kwargs)

def build_metric_dependency_graph(**kwargs: Any) -> dict[str, Any]:
    """build_metric_dependency_graph

Kit: J Reasoning and Output
Purpose: Build a dependency graph linking input files, intermediate metrics and final conclusions.
Inputs: input_files, computations, final_fields?
Output: metric dependency graph JSON
Used by: reproducible reasoning tasks
"""
    return dispatch('build_metric_dependency_graph', **kwargs)

def reconcile_point_grid_regional_scale(**kwargs: Any) -> dict[str, Any]:
    """reconcile_point_grid_regional_scale

Kit: J Reasoning and Output
Purpose: Compare point, gridded AOI, regional, and report-level metrics and return scale-aware interpretation cautions.
Inputs: source_metrics, event_scale?, question_context?
Output: scale reconciliation report
Used by: cross-scale reasoning tasks
"""
    return dispatch('reconcile_point_grid_regional_scale', **kwargs)

def parse_mcq_options_and_select(**kwargs: Any) -> dict[str, Any]:
    """parse_mcq_options_and_select

Kit: J Reasoning and Output
Purpose: Parse MCQ options, normalize option letters, and check that the selected answer matches the requested output format.
Inputs: question_text?, options?, selected?
Output: normalized options and selected letter
Used by: MCQ trajectory and evaluation
"""
    return dispatch('parse_mcq_options_and_select', **kwargs)
