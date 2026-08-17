# Correct Answer

```json
{
  "answer": {
    "event_span_days": 110,
    "mean_precip_peak_ratio": 1.549,
    "precip_ratio_spread": 0.445,
    "surface_change_concentration_ratio": 15.734,
    "people_per_counted_facility": 14336.7,
    "rain_anomaly_midpoint_x": 5.5
  },
  "evidence_windows": {
    "event_window": {
      "start": "2022-06-14",
      "end": "2022-10-01"
    },
    "precipitation_evidence_window": {
      "start": "2022-06-14",
      "end": "2022-07-29"
    }
  },
  "score": 6,
  "class_label": "high_consistency_long_span_monsoon_flood_concentration"
}
```

# Computation Path

The locked dates run from 2022-06-14 through 2022-10-01, so the inclusive event span is 110 days. The precipitation-product evidence window is 2022-06-14 through 2022-07-29. The three precipitation ratios are:

- CHIRPS: 371.604 / 296.607 = 1.253
- GPM IMERG: 855.217 / 503.804 = 1.698
- ERA5-Land: 546.355 / 322.178 = 1.696

Their mean is 1.549 and their spread is 1.698 - 1.253 = 0.445. The annual surface-change concentration is 0.651 / 0.041374 = 15.734. The counted facility denominator is 1000 amenities, giving 14,336,658.681 / 1000 = 14,336.7 people per counted facility. The report phrase "five to six times" gives a midpoint of 5.5. All six threshold tests evaluate to 1, so the final score is 6 and the explicit class mapping gives `high_consistency_long_span_monsoon_flood_concentration`.

# Scoring Rubric

- 4 points: Correctly computes the inclusive 110-day event span and keeps the date arithmetic explicit.
- 4 points: Correctly computes all three precipitation evidence-window peak ratios, their 1.549 mean, and their 0.445 spread.
- 3 points: Correctly computes the 15.734 surface-change concentration ratio from the annual max and mean values.
- 3 points: Correctly derives the 1000 counted-facility denominator and 14,336.7 people-per-facility value from the population and amenity counts.
- 2 points: Correctly extracts the rainfall-anomaly midpoint of 5.5 from the report wording.
- 3 points: Correctly applies all six threshold tests and returns score 6 with the high-consistency class label under the explicit score-to-label rule.
- 1 point: Returns compact JSON with numeric units implied by field names and no extra prose outside the JSON answer.
