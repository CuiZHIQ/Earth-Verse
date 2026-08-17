# Southern California Snow-Level Stratification Analysis

You are a cold-region storm phase analyst preparing a final mechanism diagnosis for February 2023 Southern California winter storm. Use the local package as the only evidence source. The task is to determine whether the record supports persistent cold or elevation-stratified snow response rather than a brief visual snow proxy.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `basin_metrics.below0_h`
- `basin_metrics.fdh_c_h`
- `basin_metrics.gust_kmh`
- `basin_metrics.min_t_c`
- `basin_metrics.snow_cm`
- `basin_metrics.snow_h`
- `basin_metrics.wind_chill_c`
- `decision_rule`
- `process_alignment_result`
- `report_metrics.downtown_rain_in`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: event-window cold or storm anchor; temperature and phase calculation; elevation or wind context; warm-rain or image-only rejection.
4. Compare the dominant explanation with at least two simpler alternatives and reject the alternatives using computed values.
5. State what the package evidence can and cannot prove.

Include a short physical derivation in the final JSON: Use a phase-partition argument: compare temperature or snow-level evidence with elevation context to explain divergent basin and mountain response.

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
  "bounded_interpretation": "<what the evidence does not prove>",
  "formula_derivation": "<brief physical formula or scaling argument used in the diagnosis>"
}
```
