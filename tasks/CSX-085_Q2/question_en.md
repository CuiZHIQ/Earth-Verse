# Super Typhoon Yagi Rainfall Persistence and Service-Disruption Diagnosis

You are a tropical-cyclone flood analyst preparing a final mechanism diagnosis for Super Typhoon Yagi floods. Use the local package as the only evidence source. The task is to diagnose whether cyclone rainfall persistence and service-context evidence dominate over wind-only severity.

Work as an interactive tool-agent: inspect the package root, choose the files that contain the event anchor and quantitative evidence, read or search those files, run calculations when needed, and record the evidence that supports each intermediate value. Do not rely on web search or hidden answers.

Required reasoning:

1. Establish the event window and the physical process being tested.
2. Recompute the package-derived evidence fields needed for the final answer, including:
- `computed_metrics.gdacs_peak_wind_kmh`
- `computed_metrics.gdacs_peak_wind_ms`
- `computed_metrics.gdacs_alert_level`
- `computed_metrics.openmeteo_event_precip_mm`
- `computed_metrics.nasa_power_event_precip_mm`
- `computed_metrics.daily_hourly_total_agreement_ratio`
- `computed_metrics.openmeteo_wettest_72h_mm`
- `computed_metrics.openmeteo_wettest_24h_mm`
- `computed_metrics.openmeteo_wet_hours`
3. Organize the result as a causal mechanism, not as a pass/fail table. The chain must cover: cyclone rainfall persistence; regional flood loading; service or receptor context; wind-only rejection.
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
