# Central Chile Atmospheric-River Rainfall Routing Diagnosis

You are a river-flood routing analyst preparing a final mechanism diagnosis for August 2023 central Chile atmospheric-river floods. Use the local package as the only evidence source. The task is to test whether multiday rainfall loading translates into routed river or basin response instead of an instantaneous local anomaly.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `computed_values.foothill_to_el_paico_ratio`
- `computed_values.foothill_to_nasa_power_ratio`
- `computed_values.foothill_to_open_meteo_ratio`
- `computed_values.nasa_power_first_3_day_share_percent`
- `computed_values.open_meteo_first_72h_share_percent`
- `computed_values.open_meteo_max_hour_share_percent`
- `computed_values.rain_peak_to_sediment_plume_lag_days`
- `decision_tests.lagged_river_routing`
- `decision_tests.sustained_early_rainfall`
- `decision_tests.terrain_amplification`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: multiday rainfall loading; basin or terrain routing; river-response timing; instantaneous simplification rejection.
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
