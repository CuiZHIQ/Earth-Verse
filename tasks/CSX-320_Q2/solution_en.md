# Correct Answer

```json
{
  "target_family": "mendenhall_glof_release_precip_radar_gate_consistency",
  "metrics": {
    "release_mcm": 55.267,
    "crest_excess_ft": 1.02,
    "flow_floor_m3s": 934.456,
    "precip_mean_max_mm": 0.1239,
    "radar_span_db": 42.9976,
    "coverage_balance": 0.6
  },
  "gates": {
    "release_gate": true,
    "river_gate": true,
    "rainfall_guardrail": true,
    "radar_context_gate": true
  },
  "answer": "mendenhall_glof_release_precip_radar_gate_pass",
  "computed_consequence": "rainfall_trigger_rejected_release_gate_passes"
}
```

# Computation Path

The release conversion is `14.6 * 3.785411784 = 55.267` million cubic meters, so the `release_gate` passes the 50 MCM threshold.

The river severity checks are `15.99 - 14.97 = 1.02 ft` and `33000 * 0.028316846592 = 934.456 m3/s`. Both satisfy the river gate.

The rainfall guardrail uses the maximum mean precipitation across the event-window summaries: `max(0.000097, 0.1239299, 0) = 0.1239 mm`, with the daily mean absent. This is below 1.0 mm, so the rainfall guardrail passes.

The radar context calculation is `21.0028 - (-21.9947) = 42.9976 dB`, and the coverage balance is `min(10, 6) / max(10, 6) = 0.6`. The pre/post counts, span, and balance all pass the radar context gate.

Because all four gates pass, the compact consequence is that rainfall is rejected by the guardrail while the release, river, and corridor-change gates pass.

# Scoring Rubric

- 4 points: Returns compact JSON with `target_family`, `metrics`, `gates`, `answer`, and `computed_consequence`.
- 5 points: Computes the numeric anchors correctly: 55.267 MCM, 1.02 ft, 934.456 m3/s, 0.1239 mm, 42.9976 dB, and 0.6 coverage balance.
- 4 points: Applies the four threshold gates correctly and reports `mendenhall_glof_release_precip_radar_gate_pass`.
- 3 points: Shows the component formulas for release conversion, crest excess, streamflow conversion, precipitation maximum, radar span, and coverage balance.
- 2 points: Derives the rainfall-trigger rejection from `precip_mean_max_mm < 1.0` together with passing release and river gates.
- 1 point: Keeps the computed consequence short and tied to the gates.
- 1 point: Avoids treating radar context, annual surface change, population context, or amenity counts as loss accounting.
