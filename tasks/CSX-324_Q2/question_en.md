# Arabian Sea Sustained Marine Heat-Stress Diagnosis

You are a marine heatwave ecosystem analyst preparing a final mechanism diagnosis for 2023 Indian Ocean/Arabian Sea marine heatwave context. Use the local package as the only evidence source. The task is to diagnose whether sustained sea-surface thermal stress dominates over land-weather or generic coastal context.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `evidence_synthesis_values.crw_core_product_count`
- `evidence_synthesis_values.crw_core_product_ratio`
- `evidence_synthesis_values.dhw_proxy_c_weeks`
- `evidence_synthesis_values.duration_days`
- `evidence_synthesis_values.evidence_score`
- `evidence_synthesis_values.land_counter_passes`
- `evidence_synthesis_values.sst_anom_hits_2023`
- `land_counter_values.dnbr_abs_mean`
- `land_counter_values.embedding_mean`
- `land_counter_values.gpm_peak_mean_ratio`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: sea-surface thermal anomaly; duration or persistence; land-context countercheck; marine-stress conclusion.
4. Compare the dominant explanation with at least two simpler alternatives and reject the alternatives using computed values.
5. State what the package evidence can and cannot prove.

Include a short physical derivation in the final JSON: Use thermal excess times duration, analogous to degree-heating accumulation where supported by package fields.

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
