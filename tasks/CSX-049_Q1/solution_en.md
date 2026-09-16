# Final Answer

```json
{
  "answer_label": "short_window_high_contrast_pluvial_flood_signature",
  "event_window_days": 2,
  "precip_max_mm": {
    "era5": 10.82,
    "gpm": 18.36,
    "chirps": 18.05
  },
  "max_to_mean_ratios": {
    "era5": 6.8,
    "gpm": 9.18,
    "chirps": 127.19
  },
  "satellite_max_disagreement_percent": 1.72,
  "report_flag_count": 6,
  "score_0_to_6": 6,
  "computed_interpretation": "The two-day Ida record has concentrated precipitation maxima across products, close GPM-CHIRPS peak agreement, and six independent disruption flags."
}
```

# Key Computations

The locked event window runs from 2021-09-01 through 2021-09-02, so the inclusive duration is 2 days.

Precipitation maxima are 10.819 mm for ERA5-Land, 18.360 mm for GPM IMERG, and 18.047 mm for CHIRPS. The corresponding max-to-mean ratios are:

- ERA5-Land: `10.819 / 1.591 = 6.80`
- GPM IMERG: `18.360 / 2.000 = 9.18`
- CHIRPS: `18.047 / 0.142 = 127.19`

The GPM-CHIRPS event-maximum disagreement is:

`abs(18.360 - 18.047) / mean(18.360, 18.047) * 100 = 1.72%`.

The report text contains all six impact flags: road shutdowns, public transit disruption, flight cancellations, stranded cars, high-water rescues, and flash-flood emergency statements.

# Reasoning Path

The six-part diagnostic score has six possible points. The event passes the two-day-window test, the ERA5 >= 10 mm test, the paired GPM/CHIRPS >= 18 mm test, the three-product max-to-mean-ratio >= 5 test, the report-flag-count >= 5 test, and the GPM-CHIRPS disagreement <= 5% test.

Because all six tests pass, the deterministic label is `short_window_high_contrast_pluvial_flood_signature`. A diffuse-rainfall label is weaker because the ratios show high spatial or temporal contrast within the event summaries rather than uniform accumulation.

# Computed Interpretation

The computation supports a compact pluvial-flood signature: concentrated two-day rainfall maxima align with multiple independent disruption signals.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the requested compact JSON fields and the final label `short_window_high_contrast_pluvial_flood_signature`.
- 4 points: Computes precipitation maxima correctly for ERA5, GPM, and CHIRPS, with at most 0.05 mm error after rounding.
- 4 points: Computes all three max-to-mean ratios correctly, including the very high CHIRPS ratio.
- 3 points: Computes the GPM-CHIRPS maximum disagreement percent and applies the <= 5% agreement test correctly.
- 3 points: Counts the six report flags correctly and ties them to the computed diagnostic score without adding uncomputed loss claims.
- 2 points: Applies all six decision tests and reports `score_0_to_6 = 6`.
- 1 point: Keeps the interpretation concise and derived from the calculations.
