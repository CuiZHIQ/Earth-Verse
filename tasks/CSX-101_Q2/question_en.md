# North Sea 1953 Surge Amplification Process Analysis

You are a coastal storm-surge analyst preparing a final mechanism diagnosis for 1953 North Sea storm surge flood. Use the local package as the only evidence source. The task is to compare coastal water-level, pressure, wave, rainfall, and exposure evidence to identify the dominant flood forcing.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `surge_proof.pressure_gap.inverse_barometer_m`
- `surge_proof.pressure_gap.reported_surge_m`
- `surge_proof.pressure_gap.surge_to_inverse_barometer_ratio`
- `surge_proof.pressure_gap.inverse_barometer_fraction_of_surge`
- `surge_proof.pressure_gap.pressure_only_test`
- `surge_proof.synoptic_forcing.storm_deepening_mb`
- `surge_proof.synoptic_forcing.ridge_to_low_gradient_mb`
- `surge_proof.synoptic_forcing.gradient_to_deepening_ratio`
- `surge_proof.synoptic_forcing.force_10_11_northerly_winds_reported`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: storm pressure or wind forcing; surge/wave water-level amplification; coastal exposure context; rainfall-only rejection.
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
