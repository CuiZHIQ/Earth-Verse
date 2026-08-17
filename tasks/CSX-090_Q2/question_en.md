# Derna Flood-Wave Amplification Chain Diagnosis

You are a dam-area flood cascade analyst preparing a final mechanism diagnosis for Storm Daniel Derna flood. Use the local package as the only evidence source. The task is to connect rainfall or report anchors to a localized dam-area cascade and downstream flood-wave pathway.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `derivation_evidence_synthesis`
- `rejected_overreads`
- `final_process_alignment_label`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: storm or rainfall loading; dam-area pathway or storage release; downstream flood-wave amplification; regional-rainfall-only rejection.
4. Compare the dominant explanation with at least two simpler alternatives and reject the alternatives using computed values.
5. State what the package evidence can and cannot prove.

Include a short physical derivation in the final JSON: When amplification is used, express it as a ratio or difference between upstream forcing and downstream response indicators.

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
