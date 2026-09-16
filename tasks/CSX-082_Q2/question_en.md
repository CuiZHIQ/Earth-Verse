# Storm Boris Multibasin Hydrologic Pressure Diagnosis

You are a river-flood routing analyst preparing a final mechanism diagnosis for Storm Boris Central and Eastern Europe floods. Use the local package as the only evidence source. The task is to test whether multiday rainfall loading translates into routed river or basin response instead of an instantaneous local anomaly.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `chain_evidence_synthesis`
- `rejected_alternative`
- `final_chain_label`
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
