# Yagi Rainfall Persistence Threshold Proof

During 7-18 September 2024, Super Typhoon Yagi moved inland after landfall in northern Viet Nam and was followed by flooding and landslides across parts of mainland Southeast Asia. A hydrometeorology review team needs a compact calculation showing whether the rainfall record is better described as a persistent multi-day basin loading episode than as a short peak-hour burst.

Compute the threshold proof from the event-window precipitation diagnostics. Use the hourly rainfall series, the independent daily rainfall series, and gridded precipitation summaries to derive:

For the hourly series, first group hourly precipitation into calendar-day totals over the event window. Then compute the 72-hour and 5-day loads as rolling 3-calendar-day and 5-calendar-day sums over those daily totals. Do not use arbitrary-offset rolling 120-hour windows for the `wettest_5day_share` field.

- hourly event total rainfall, wettest 72-hour share, wettest 5-day share, peak-hour share, wet-day fraction, and mean hourly rainfall rate;
- independent daily total ratio against the hourly total, daily 72-hour share, daily 5-day share, and both 5-day-to-wettest-day ratios;
- gridded max-to-mean concentration ratios for the three precipitation summaries and the largest-grid maximum relative to the other two maxima;
- one final label that follows from the threshold tests.

Use these pass tests:

- hourly persistence passes when 72-hour share >= 0.50, 5-day share >= 0.70, peak-hour share <= 0.06, and wet-day fraction >= 0.75;
- daily corroboration passes when the daily/hourly total ratio is within 0.90-1.15, daily 72-hour share >= 0.50, daily 5-day share >= 0.70, and both 5-day-to-wettest-day ratios exceed 2;
- gridded concentration passes when all three max-to-mean ratios exceed 1.5 and at least one exceeds 3.

Return JSON only:

```json
{
  "target_family": "yagi_rainfall_persistence_threshold_proof",
  "rainfall_metrics": {
    "event_total_mm": 0,
    "wettest_72h_share": 0,
    "wettest_5day_share": 0,
    "peak_hour_share": 0,
    "wet_day_fraction_ge10mm": 0,
    "mean_hourly_precip_rate_mm_h": 0
  },
  "daily_corroboration": {
    "daily_to_hourly_total_ratio": 0,
    "daily_72h_share": 0,
    "daily_5day_share": 0,
    "daily_5day_to_wettest_day_ratio": 0,
    "hourly_5day_to_wettest_day_ratio": 0
  },
  "gridded_concentration": {
    "era5_max_to_mean_ratio": 0,
    "gpm_max_to_mean_ratio": 0,
    "chirps_max_to_mean_ratio": 0,
    "gpm_max_to_chirps_max_ratio": 0,
    "gpm_max_to_era5_max_ratio": 0
  },
  "threshold_results": {
    "hourly_persistence": "",
    "daily_corroboration": "",
    "gridded_concentration": ""
  },
  "rejected_readings": [],
  "final_label": ""
}
```
