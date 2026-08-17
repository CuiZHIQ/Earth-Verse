# UAE Rainfall Load Diagnostic

A hydrometeorology team is checking an index-based diagnosis for the April 15-17, 2024 UAE and Dubai record rainfall flood. The proposed conclusion is that the event passes an annual-scale, short-duration rainfall-overload test: an eastern UAE sub-24-hour total exceeded the midpoint of the country's typical annual rainfall range, the Dubai airport daily total was still at least half of that annual midpoint, and the gridded event maxima are much smaller than the report-scale totals.

Using the technical record, compute a compact proof diagnostic. Infer the event duration, the annual rainfall midpoint, the two report-to-annual ratios, the Dubai airport typical annual rainfall implied by its reported multiplier, the largest gridded accumulated precipitation total, and the airport/eastern report-to-grid ratios. Apply these pass conditions:

- `duration_days == 3`
- `eastern_annual_ratio >= 1.0`
- `airport_annual_ratio >= 0.5`
- `airport_to_grid_ratio >= 5.0`
- `eastern_to_grid_ratio >= 10.0`

Return only JSON:

```json
{
  "duration_days": "<integer>",
  "annual_midpoint_mm": "<number>",
  "eastern_annual_ratio": "<number>",
  "airport_annual_ratio": "<number>",
  "airport_typical_annual_mm": "<number>",
  "max_gridded_precip_mm": "<number>",
  "report_to_grid_ratios": {
    "airport": "<number>",
    "eastern": "<number>"
  },
  "final_label": "<short_label>"
}
```
