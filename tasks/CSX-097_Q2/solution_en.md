# Final Answer

```json
{
  "target_family": "yagi_rainfall_persistence_threshold_proof",
  "rainfall_metrics": {
    "event_total_mm": 373.0,
    "wettest_72h_share": 0.5236,
    "wettest_5day_share": 0.7525,
    "peak_hour_share": 0.0477,
    "wet_day_fraction_ge10mm": 0.8333,
    "mean_hourly_precip_rate_mm_h": 1.295
  },
  "daily_corroboration": {
    "daily_to_hourly_total_ratio": 1.0424,
    "daily_72h_share": 0.5595,
    "daily_5day_share": 0.8711,
    "daily_5day_to_wettest_day_ratio": 2.856,
    "hourly_5day_to_wettest_day_ratio": 2.359
  },
  "gridded_concentration": {
    "era5_max_to_mean_ratio": 2.259,
    "gpm_max_to_mean_ratio": 4.6,
    "chirps_max_to_mean_ratio": 1.702,
    "gpm_max_to_chirps_max_ratio": 2.23,
    "gpm_max_to_era5_max_ratio": 2.798
  },
  "threshold_results": {
    "hourly_persistence": "pass",
    "daily_corroboration": "pass",
    "gridded_concentration": "pass"
  },
  "rejected_readings": [
    "short_peak_burst",
    "wind_only",
    "single_grid_max_as_regional_loss"
  ],
  "final_label": "persistent_multi_day_rainfall_cascade_supported"
}
```

# Key Computations

Hourly rainfall record, with hourly precipitation first grouped into calendar-day totals for the 3-day and 5-day window calculations:

- Event total = 373.0 mm over 288 hours.
- Wettest 72-hour load = 195.3 mm, so 195.3 / 373.0 = 0.5236.
- Wettest calendar-day 5-day load = 280.7 mm, so 280.7 / 373.0 = 0.7525.
- Peak hour = 17.8 mm, so 17.8 / 373.0 = 0.0477.
- Wet days at or above 10 mm = 10 of 12 days, so 10 / 12 = 0.8333.
- Mean hourly rate = 373.0 / 288 = 1.295 mm/h.

Independent daily rainfall record:

- Daily total = 388.82 mm, so daily/hourly total ratio = 388.82 / 373.0 = 1.0424.
- Daily wettest 72-hour load = 217.54 mm, so 217.54 / 388.82 = 0.5595.
- Daily wettest 5-day load = 338.72 mm, so 338.72 / 388.82 = 0.8711.
- Daily 5-day/wettest-day ratio = 338.72 / 118.6 = 2.856.
- Hourly 5-day/wettest-day ratio = 280.7 / 119.0 = 2.359.

Gridded precipitation concentration:

- ERA5-Land max/mean = 129.122 / 57.158 = 2.259.
- GPM IMERG max/mean = 361.275 / 78.542 = 4.600.
- CHIRPS max/mean = 161.988 / 95.192 = 1.702.
- GPM maximum relative to CHIRPS maximum = 361.275 / 161.988 = 2.230.
- GPM maximum relative to ERA5-Land maximum = 361.275 / 129.122 = 2.798.

# Reasoning Path

The hourly persistence test passes because the wettest 72 hours contain more than half of the event rainfall, the wettest 5 days contain more than 70%, the single peak hour remains below 6% of the event total, and most days are wet. This combination rules against a short peak-hour burst as the main rainfall structure.

The independent daily series corroborates the same conclusion. Its total is within 4.24% of the hourly total, its wettest 72-hour and 5-day shares exceed the persistence thresholds, and both 5-day-to-wettest-day ratios are above 2. This means the persistence result is not an artifact of only one temporal aggregation.

The gridded precipitation summaries pass the concentration test: every max/mean ratio is above 1.5 and the GPM ratio is above 3. These values show localized high rainfall embedded within a broader multi-day event, but the grid maxima should be used as concentration checks, not as direct regional loss denominators.

# Computed Interpretation

The computed label is `persistent_multi_day_rainfall_cascade_supported`: multi-day rainfall loading is the dominant quantitative signal, with gridded concentration adding a compatible high-rainfall pattern. The calculations reject `short_peak_burst`, `wind_only`, and `single_grid_max_as_regional_loss` readings.

# Scoring Rubric

- 3 points: Correct final label and JSON target family. Full credit requires `persistent_multi_day_rainfall_cascade_supported` and the requested top-level fields. Partial credit: 1-2 points for a compatible label with missing or mislabeled fields.
- 4 points: Correct hourly rainfall persistence metrics. Full credit requires event total, 72-hour share, 5-day share, peak-hour share, wet-day fraction, and mean hourly rate within tolerance. Partial credit: 1-3 points for mostly correct arithmetic with one or two missing metrics or minor rounding errors.
- 4 points: Correct daily corroboration metrics. Full credit requires total ratio, daily 72-hour share, daily 5-day share, and both 5-day-to-wettest-day ratios within tolerance. Partial credit: 1-3 points for correct daily totals but incomplete ratio logic.
- 3 points: Correct gridded concentration calculations. Full credit requires all three max/mean ratios and both GPM-to-other-maximum ratios within tolerance. Partial credit: 1-2 points for using the right formula but omitting one or more ratios.
- 3 points: Correct threshold decisions. Full credit requires all three threshold rows marked pass and tied to the stated inequalities. Partial credit: 1-2 points for the right overall direction but incomplete inequality checks.
- 2 points: Correct rejection of weaker readings. Full credit requires rejecting short peak-hour burst, wind-only, and single-grid-maximum-as-loss readings from the computed values. Partial credit: 1 point for rejecting only one or two of them.
- 1 point: Concise structured answer without extra realized-loss escalation. Full credit requires JSON-only style or an equivalently compact structured answer. Partial credit: 0.5 points for a clear answer with extra prose that does not change the conclusion.
