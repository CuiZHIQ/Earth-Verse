# Uttarakhand Persistent Monsoon Mountain Hazard Chain

You are a mountain hydrometeorology analyst preparing a final mechanism diagnosis for June 2013 Uttarakhand Himalayan floods. Use the local package as the only evidence source. The task is to diagnose whether persistent rainfall over steep terrain supports a flood, debris, or landslide hazard chain rather than a short shower.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `required_tests`
- `key_metrics.wettest_72h_share`
- `key_metrics.wet_hour_fraction`
- `key_metrics.heavy_hour_share`
- `key_metrics.wettest_24h_to_72h_ratio`
- `key_metrics.outside_24h_share`
- `key_metrics.max_daily_to_mean_daily`
- `key_metrics.gpm_to_report_marker`
- `key_metrics.chirps_to_report_marker`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: persistent mountain rainfall; terrain-enhanced runoff or slope response; flood-landslide pathway; short-burst simplification rejection.
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
