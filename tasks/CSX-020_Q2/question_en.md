# Black Summer Dry-Heat Fire-Weather Exposure Chain

You are a dry-heat and fire-weather analyst preparing a final mechanism diagnosis for 2019-2020 Australian extreme heat during Black Summer. Use the local package as the only evidence source. The task is to test whether dry daytime heat and atmospheric dryness dominate the event instead of humid heat, rainfall, or exposure-only context.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `label`
- `evidence_score`
- `heat_load_c_days_gt35`
- `warm_nights_ge18c`
- `dryness_evidence_synthesis.peak_vpd_kpa`
- `dryness_evidence_synthesis.hot_dry_hours`
- `dryness_evidence_synthesis.hot_humid_hours`
- `exposure_evidence_synthesis.population`
- `exposure_evidence_synthesis.critical_amenities`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: hot daytime forcing; dry-air or vapor-pressure stress; rainfall moderation check; exposure context.
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
