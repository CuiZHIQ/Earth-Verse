# Langtang Mixed Avalanche-Obstruction Process Diagnosis

You are a mountain mass-movement analyst preparing a final mechanism diagnosis for Langtang avalanche/landslide. Use the local package as the only evidence source. The task is to diagnose whether local mass movement or obstruction evidence dominates over simple rainfall or image-change explanations.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `max_event_day_precip_mm`
- `precipitation_ratio`
- `radar_scene_balance`
- `diagnostic_diagnostic_test_margins.precip_below_ratio`
- `diagnostic_diagnostic_test_margins.radar_db_over`
- `diagnostic_diagnostic_test_margins.exposure_below_ratio`
- `exposure_scale_ratio`
- `component_evidence_scores.mixed_material_record`
- `component_evidence_scores.low_precip_ratio`
- `component_evidence_scores.paired_radar_change`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: mass-movement event anchor; local obstruction or slope-response signal; weather countercheck; simple-trigger rejection.
4. Compare the dominant explanation with at least two simpler alternatives and reject the alternatives using computed values.
5. State what the package evidence can and cannot prove.

Return exactly one JSON object with this top-level structure:

```json
{
  "answer": "<compact mechanism diagnosis>",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "<one sentence framing the physical question>",
  "computed_evidence": {},
  "mechanism_chain": [
    "<ordered physical or impact step>",
    "..."
  ],
  "decisive_evidence": "<which evidence carries the decision and why>",
  "rejected_simplifications": "<which simpler explanation fails and why>",
  "bounded_interpretation": "<what the evidence does not prove>"
}
```
