# Daytime Heat-Exposure Dominance Analysis

You are a heat-risk process analyst preparing a final mechanism diagnosis for 2015 India-Pakistan heat wave. Use the local package as the only evidence source. The task is to separate cumulative heat stress from a single peak-temperature story by combining thermal load, persistence, recovery, and contextual evidence.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `classification`
- `exposure_weighted_heat_load_m_person_c_day`
- `humid_heat_dominance_pass`
- `proof_result`
- `regional_heat_load_c_day`
- `regional_peak_tmax_c`
- `warm_night_ratio`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: event-window thermal forcing; accumulated heat-load calculation; persistence or recovery constraint; non-heat alternative rejection.
4. Compare the dominant explanation with at least two simpler alternatives and reject the alternatives using computed values.
5. State what the package evidence can and cannot prove.

Include a short physical derivation in the final JSON: Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units.

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
