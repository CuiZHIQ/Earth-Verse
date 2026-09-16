# Correct Answer

```json
{
  "answer": "score_6_of_6",
  "ledger": {
    "score_0_to_6": 6,
    "cloud_ratio": 5.52,
    "bright_ratio": 14.89,
    "reported_24h_rain_floor_mm": 680,
    "max_grid_precip_mm": 62.18,
    "grid_product_max_spread_mm": 11.76,
    "report_to_grid_ratio": 10.94,
    "report_marker_count": 5,
    "low_change_component": 1,
    "wind_penalty": 0
  },
  "label": "storm_obscured_localized_rain_slope_failure"
}
```

# Computation Path

The storm true-color image has a cloud-like share of 0.5304 and a bright share of 0.4639. The pre-date image has a cloud-like share of 0.0961 and a bright share of 0.0311. The ratios are therefore `0.5304 / 0.0961 = 5.52` and `0.4639 / 0.0311 = 14.89`, giving 2 obscuration points.

The three gridded event precipitation maxima are 62.18 mm, 50.42 mm, and 52.45 mm, so the maximum is 62.18 mm and the cross-product maximum-value spread is 11.76 mm. The report gives a 24-hour rainfall floor of 680 mm; `680 / 62.18 = 10.94`, giving 2 rainfall points.

The report marker count is 5. The annual cosine-change mean is 0.062 and the dNBR mean is -0.060, so the low-change component is 1. The maximum daily wind inside the February 18-21 event window is 22.7 km/h, so the wind term is 0. The ledger is `2 + 2 + 1 + 1 - 0 = 6`.

# Scoring Rubric

- 4 points: Computes the storm/pre cloud-like and bright-pixel ratios from the RGB thresholds.
- 4 points: Computes the gridded precipitation maximum, cross-product maximum-value spread, and reported-rainfall-to-grid ratio.
- 4 points: Counts the five report markers and applies the threshold formula.
- 3 points: Uses the annual cosine mean, dNBR mean, and event-window maximum daily wind value correctly.
- 3 points: Returns the requested JSON fields with units implied by field names and rounding consistent with the answer.
- 2 points: Shows how the component subtotal and wind term produce `score_6_of_6`.
