# Final Answer

```json
{
  "duration_days": 3,
  "annual_midpoint_mm": 170.0,
  "eastern_annual_ratio": 1.47,
  "airport_annual_ratio": 0.70,
  "airport_typical_annual_mm": 79.3,
  "max_gridded_precip_mm": 18.637,
  "report_to_grid_ratios": {
    "airport": 6.39,
    "eastern": 13.41
  },
  "final_label": "annual_scale_short_duration_rainfall_overload"
}
```

# Key Computations

The event window is 2024-04-15 through 2024-04-17 inclusive, so `duration_days = 3`.

The technical report gives the UAE annual rainfall context as 140-200 mm. The midpoint is:

`annual_midpoint_mm = (140.0 + 200.0) / 2 = 170.0 mm`

Rainfall-load ratios:

- Eastern UAE sub-24-hour report: `250.0 / 170.0 = 1.47`
- Dubai airport daily report: `119.0 / 170.0 = 0.70`
- Dubai airport typical annual rainfall implied by the 1.5x statement: `119.0 / 1.5 = 79.3 mm`

The gridded event maxima are ERA5-Land 12.758 mm, GPM IMERG 15.985 mm, and CHIRPS 18.637 mm, so:

- `max_gridded_precip_mm = 18.637`
- `airport_to_grid_ratio = 119.0 / 18.637 = 6.39`
- `eastern_to_grid_ratio = 250.0 / 18.637 = 13.41`

# Reasoning Path

The threshold diagnostic passes every required condition. The duration is exactly 3 days. The eastern UAE short-duration total is 1.47 times the national annual midpoint, exceeding the full-annual-load threshold. The Dubai airport daily total is 0.70 times that same midpoint, exceeding the half-annual-load threshold and implying a local typical annual value near 79.3 mm.

The gridded maximum of 18.637 mm is far below both report anchors, producing report-to-grid ratios of 6.39 for Dubai airport and 13.41 for eastern UAE. Those ratios pass the two contrast thresholds and rule out a conclusion based only on the gridded maximum as the compact event diagnosis.

# Computed Interpretation

The answer is `annual_scale_short_duration_rainfall_overload`: the computed diagnostic supports a short-duration rainfall event whose report-scale totals were annual-scale in an arid-climate context.

# Scoring Rubric

- 3 points: Correct final JSON shape and label. Full credit requires all requested fields and the label `annual_scale_short_duration_rainfall_overload`. Partial credit: 1-2 points for a near-complete JSON object with a semantically equivalent label but missing or renamed fields.
- 3 points: Correct event duration and annual midpoint. Full credit requires `duration_days = 3` and `annual_midpoint_mm = 170.0`. Partial credit: 1-2 points for only one correct value or a minor inclusive-date error.
- 4 points: Correct annual-normalized rainfall ratios. Full credit requires eastern ratio about 1.47 and airport ratio about 0.70 with formulas. Partial credit: 1-3 points for one correct ratio, swapped numerator context, or small rounding mistakes.
- 3 points: Correct airport typical annual rainfall calculation. Full credit requires `119.0 / 1.5 = 79.3 mm`. Partial credit: 1-2 points for identifying the multiplier but misrounding or omitting units.
- 3 points: Correct gridded maximum and report-to-grid ratios. Full credit requires 18.637 mm, airport ratio about 6.39, and eastern ratio about 13.41. Partial credit: 1-2 points for using the right maximum with one ratio error or choosing a lower gridded product by mistake.
- 3 points: Correct threshold logic. Full credit requires showing that all five pass conditions are satisfied. Partial credit: 1-2 points for the correct final pass state with incomplete or partially wrong inequality checks.
- 1 point: Concise computed interpretation. Full credit requires a short rainfall-load interpretation and no extra impact totals that are not derived from the requested calculations. Partial credit: no credit if the answer expands into broad incident narrative.
