# Hurricane Ida Rainfall Threshold-Concentration Diagnostic

A hydrometeorology team is calibrating the September 1-2, 2021 Hurricane Ida rainfall-flood episode in New York City and the northern Mid-Atlantic. The team needs a compact threshold-concentration diagnostic that distinguishes a short-duration rainfall burst from a broader storm-total signal.

Using the technical record, compute the Central Park record-hour rainfall in millimeters, compute the northern Mid-Atlantic "just above 10 inches" storm-total reference as a conservative lower-bound value of 10.0 inches, test both against the thresholds below, and quantify how concentrated the record hour was relative to the storm-total reference.

Return JSON only, using this schema:

```json
{
  "record_hour": {
    "value_mm": 0.0,
    "threshold_mm": 75.0,
    "margin_mm": 0.0,
    "ratio_to_threshold": 0.0,
    "passes": "<boolean>"
  },
  "regional_total": {
    "value_mm": 0.0,
    "threshold_mm": 250.0,
    "margin_mm": 0.0,
    "ratio_to_threshold": 0.0,
    "passes": "<boolean>"
  },
  "concentration": {
    "record_hour_share_percent": 0.0,
    "classification": "<short label>"
  },
  "final_label": "<short label>",
  "interpretation": "<one sentence tied to the computed values>"
}
```

Rules:

- Convert inches to millimeters with `25.4 mm/in`.
- Compare the Central Park wettest-hour rainfall with the `75 mm` record-hour threshold.
- Compare the northern Mid-Atlantic storm-total reference with the `250 mm` storm-total threshold.
- Compute `record_hour_share_percent = record_hour_mm / regional_total_reference_mm * 100`.
- Use `high_hour_share` when the record hour is at least `30%` of the storm-total reference; otherwise use `lower_hour_share`.
- Set `final_label` to `dual_threshold_high_concentration_rainfall` only when both rainfall thresholds pass and the concentration classification is `high_hour_share`; otherwise use the most specific failed-threshold label implied by the calculations.
