# Mediterranean Compound Atmospheric Stress Diagnosis

You are a air-quality exposure analyst preparing a final mechanism diagnosis for Mediterranean heatwave wildfire smoke and dust episode. Use the local package as the only evidence source. The task is to diagnose whether pollutant or aerosol burden persists over a receptor window after accounting for meteorology and removal modifiers.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `event_days`
- `heat_load_c_day`
- `peak_heat_margin_c`
- `ventilation_ratio`
- `airborne_alignment_count`
- `final_label`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: pollutant or aerosol burden; transport/stagnation duration; rain or ventilation modifier; receptor-context interpretation.
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
