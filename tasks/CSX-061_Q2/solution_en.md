# Final Answer

The correct answer is `dual_threshold_high_concentration_rainfall`.

```json
{
  "record_hour": {
    "value_mm": 88.138,
    "threshold_mm": 75.0,
    "margin_mm": 13.138,
    "ratio_to_threshold": 1.175,
    "passes": true
  },
  "regional_total": {
    "value_mm": 254.0,
    "threshold_mm": 250.0,
    "margin_mm": 4.0,
    "ratio_to_threshold": 1.016,
    "passes": true
  },
  "concentration": {
    "record_hour_share_percent": 34.7,
    "classification": "high_hour_share"
  },
  "final_label": "dual_threshold_high_concentration_rainfall",
  "interpretation": "Ida's New York City calibration is supported by both a record-hour extreme and a storm-total lower-bound extreme, with the record hour alone equal to about one third of the regional reference."
}
```

# Key Computations

The technical report gives New York City's Central Park wettest hour as `3.47 in` and the northern Mid-Atlantic storm-total reference as just above `10 in`; the computation uses `10.0 in` as the lower-bound reference.

- Record hour: `3.47 in * 25.4 = 88.138 mm`.
- Record-hour margin: `88.138 - 75.0 = 13.138 mm`.
- Record-hour threshold ratio: `88.138 / 75.0 = 1.175`.
- Regional total reference: `10.0 in * 25.4 = 254.0 mm`.
- Regional-total margin: `254.0 - 250.0 = 4.0 mm`.
- Regional-total threshold ratio: `254.0 / 250.0 = 1.016`.
- Record-hour share: `88.138 / 254.0 * 100 = 34.7%`.

# Reasoning Path

Both rainfall thresholds pass: the Central Park record hour exceeds `75 mm`, and the storm-total reference exceeds `250 mm`. The record hour is also at least `30%` of the storm-total reference, so the concentration class is `high_hour_share`.

The final label is therefore `dual_threshold_high_concentration_rainfall`. A weaker label based only on storm-total accumulation would miss the concentration test, and a weaker label based only on the hourly burst would miss that the broader storm-total reference also clears its threshold.

# Computed Interpretation

The threshold-concentration diagnostic supports calibrating Ida in New York City as a short-duration extreme rainfall event embedded within a broader high-total rainfall episode.

# Scoring Rubric

- 3 points: Final label and pass states. Full credit requires `dual_threshold_high_concentration_rainfall`, both rainfall tests marked `true`, and `high_hour_share`. Partial credit: 1-2 points for the right severe-rainfall direction with one missing or mislabeled state.
- 4 points: Record-hour conversion and threshold arithmetic. Full credit requires `88.138 mm`, `13.138 mm`, ratio `1.175`, and comparison against `75 mm`. Partial credit: 2-3 points for correct conversion with a rounding or margin error; 1 point for recognizing the inches-to-millimeters conversion but using the wrong threshold comparison.
- 3 points: Regional-total conversion and threshold arithmetic. Full credit requires `254.0 mm`, `4.0 mm`, ratio `1.016`, and comparison against `250 mm`. Partial credit: 1-2 points for a correct conversion but incomplete margin or ratio reasoning.
- 3 points: Concentration calculation. Full credit requires `34.7%` and classification as `high_hour_share` using the `30%` rule. Partial credit: 1-2 points for computing the share approximately but omitting or misapplying the classification threshold.
- 3 points: Decision-rule reasoning. Full credit connects the two passed thresholds and the concentration class to the final label, and rejects a single-axis rainfall label. Partial credit: 1-2 points for reaching the final label without clearly showing all rule components.
- 2 points: Computed interpretation. Full credit gives one event-specific sentence tying the numbers to short-duration extreme rainfall embedded in a broader high-total episode. Partial credit: 1 point for a plausible interpretation that is too generic or not tied to the computed values.
- 2 points: Concise structured output. Full credit returns valid JSON with the requested fields and no extra planning material. Partial credit: 1 point for mostly correct fields with minor formatting issues.
