# UAE-Dubai Arid Pluvial Runoff-Scale Diagnosis

You are a urban flood hydrometeorology analyst preparing a final mechanism diagnosis for April 2024 UAE and Dubai record rainfall flood. Use the local package as the only evidence source. The task is to reconstruct how rainfall concentration translates into pluvial or urban runoff pressure rather than a generic wet-period label.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `rainfall_ratios.eastern_less_than_24h_mm`
- `rainfall_ratios.dubai_airport_daily_mm`
- `rainfall_ratios.annual_midpoint_mm`
- `rainfall_ratios.eastern_less_than_24h_to_annual_midpoint`
- `rainfall_ratios.dubai_airport_daily_to_annual_midpoint`
- `rainfall_ratios.airport_to_eastern_less_than_24h`
- `rainfall_ratios.result`
- `runoff_equivalent`
- `scale_concentration.gridded_event_max_mm`
- `scale_concentration.gridded_event_mean_mm`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: rainfall burst or accumulation; duration/intensity or areal-load calculation; urban runoff or receptor context; single-number simplification rejection.
4. Compare the dominant explanation with at least two simpler alternatives and reject the alternatives using computed values.
5. State what the package evidence can and cannot prove.

Include a short physical derivation in the final JSON: When converting rainfall to runoff pressure, use V = rainfall_mm / 1000 * area_m2 and explain any runoff coefficient or normalized index.

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
