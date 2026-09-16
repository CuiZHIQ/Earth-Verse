# Gorkha Shallow Seismic Dominance Diagnosis

You are a seismic impact-pattern analyst preparing a final mechanism diagnosis for 2015 Gorkha earthquake. Use the local package as the only evidence source. The task is to diagnose whether seismic forcing and patchy coseismic response dominate over weather or generic exposure context.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `computed_values.ancillary_values.main_tsunami`
- `computed_values.ancillary_values.major_tsunami_sum`
- `computed_values.ancillary_values.s1_post`
- `computed_values.ancillary_values.s1_pre`
- `computed_values.ancillary_values.s1_vv_mean_db`
- `computed_values.impact_values.deaths`
- `computed_values.impact_values.injuries`
- `computed_values.impact_values.intensity_x`
- `computed_values.impact_values.population`
- `computed_values.main_values.cdi`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: earthquake magnitude/depth anchor; seismic dominance or patchiness metric; secondary product checks; non-seismic rejection.
4. Compare the dominant explanation with at least two simpler alternatives and reject the alternatives using computed values.
5. State what the package evidence can and cannot prove.

Include a short physical derivation in the final JSON: Where magnitude is used, note that seismic energy scales approximately with 10^(1.5M), so magnitude differences are physically nonlinear.

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
