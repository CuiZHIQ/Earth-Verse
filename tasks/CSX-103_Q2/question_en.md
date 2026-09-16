# Hurricane Sandy Coastal-Forcing Mechanism Competition

You are a coastal storm-surge analyst preparing a final mechanism diagnosis for Hurricane Sandy New York-New Jersey coastal flooding. Use the local package as the only evidence source. The task is to compare coastal water-level, pressure, wave, rainfall, and exposure evidence to identify the dominant flood forcing.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `required_fields`
- `required_flags.coastal_signal_passes`
- `required_flags.rainfall_only_passes`
- `required_flags.local_wind_only_passes`
- `canonical_values.state_count`
- `canonical_values.coastal_terms`
- `canonical_values.duration_ratio`
- `canonical_values.wettest_fraction`
- `canonical_values.local_wind_ratio`
- `canonical_values.grid_mean_mm`
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
