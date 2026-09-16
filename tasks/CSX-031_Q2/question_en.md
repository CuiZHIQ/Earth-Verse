# East Asia 2016 Cold-Wave Persistence Mechanism Diagnosis

You are a cold-region storm phase analyst preparing a final mechanism diagnosis for January 2016 East Asia cold wave. Use the local package as the only evidence source. The task is to determine whether the record supports persistent cold or elevation-stratified snow response rather than a brief visual snow proxy.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `decision_rule`
- `diagnostic_diagnostic_test_tests.brief_cold_anomaly_pass`
- `diagnostic_diagnostic_test_tests.snow_ice_primary_pass`
- `diagnostic_diagnostic_test_tests.sustained_freezing_pass`
- `diagnostic_diagnostic_test_tests.wind_chill_only_pass`
- `evidence_synthesis.daily_below_freezing_run_days`
- `evidence_synthesis.event_snowfall_cm`
- `evidence_synthesis.freezing_degree_hours_c_h`
- `evidence_synthesis.freezing_run_hours`
- `evidence_synthesis.heating_degree_days_base18c`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: event-window cold or storm anchor; temperature and phase calculation; elevation or wind context; warm-rain or image-only rejection.
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
