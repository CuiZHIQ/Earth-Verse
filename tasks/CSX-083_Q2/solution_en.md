# Final Answer

```json
{
  "target_family": "doksuri_haihe_rainfall_runoff_routing_score_ledger",
  "score_ledger": [
    {
      "row_id": "rainfall_persistence_load",
      "formula": "event_total=sum(hourly_precip_mm); wettest_72h_fraction=max_72h_sum/event_total; wet_hours_share=wet_hours/window_hours; longest_wet_run=max_consecutive(precip_mm>0)",
      "computed_values": {
        "event_total_mm": 196.9,
        "window_hours": 120,
        "wettest_72h_mm": 187.2,
        "wettest_72h_fraction": 0.951,
        "wet_hours": 84,
        "wet_hours_share": 0.700,
        "longest_wet_run_hours": 78
      },
      "threshold_or_test": "pass if event_total>=150 mm, wettest_72h_fraction>=0.90, wet_hours_share>=0.60, and longest_wet_run>=48 h",
      "result": "pass_persistent_rainfall_load"
    },
    {
      "row_id": "peak_hour_concentration_test",
      "formula": "peak_hour_fraction=max_hourly_precip_mm/event_total; peak_to_72h=max_hourly_precip_mm/wettest_72h_mm",
      "computed_values": {
        "max_hourly_mm": 17.5,
        "max_hour_time_utc": "2023-07-31T18:00",
        "peak_hour_fraction": 0.089,
        "peak_to_72h_ratio": 0.093
      },
      "threshold_or_test": "single-hour control is rejected when both ratios are below 0.10",
      "result": "reject_peak_hour_control"
    },
    {
      "row_id": "report_total_transfer_test",
      "formula": "report_total_mm/comparison_total_or_grid_max_mm",
      "computed_values": {
        "report_total_mm": 744.8,
        "report_to_hourly_point_total_ratio": 3.78,
        "report_to_daily_point_total_ratio": 3.38,
        "report_to_daily_grid_max_ratio": 9.26,
        "report_to_satellite_grid_max_ratio": 12.79
      },
      "threshold_or_test": "uniform transfer is rejected when point ratios exceed 3 and grid-max ratios exceed 5",
      "result": "reject_uniform_report_total_transfer"
    },
    {
      "row_id": "runoff_equivalent_load",
      "formula": "mean_intensity=744.8/83; mm_per_day=mean_intensity*24; runoff_m3_per_km2=rainfall_mm*C*1000",
      "computed_values": {
        "duration_hours": 83.0,
        "mean_intensity_mm_per_h": 8.97,
        "mean_intensity_mm_per_day": 215.4,
        "runoff_m3_per_km2_at_C_0_50": 372400,
        "runoff_m3_per_km2_at_C_0_70": 521360
      },
      "threshold_or_test": "pass if duration>=72 h, mean_intensity>=8 mm/h, and C=0.50 runoff exceeds 300000 m3/km2",
      "result": "pass_severe_runoff_load"
    },
    {
      "row_id": "wind_and_image_dominance_test",
      "formula": "max_wind_kmh<50 and abs(radar_vv_mean_change_db)<0.1 and embedding_change_mean<0.05",
      "computed_values": {
        "max_wind_kmh": 38.5,
        "radar_vv_mean_change_db": -0.0142,
        "embedding_change_mean": 0.0175
      },
      "threshold_or_test": "wind and image dominance are rejected when all three low-signal tests pass",
      "result": "reject_wind_or_image_dominance"
    }
  ],
  "final_label": "persistent_remnant_rainfall_runoff_haihe_routing"
}
```

# Key Computations

- Rainfall persistence: 196.9 mm over 120 hours; 187.2 mm fell in the wettest 72-hour window, so the 72-hour share is 187.2 / 196.9 = 0.951. There were 84 wet hours, a wet-hour share of 0.700, and the longest wet run was 78 hours.
- Peak-hour test: the largest hour was 17.5 mm at 2023-07-31T18:00 UTC. Its share of the event total is 17.5 / 196.9 = 0.089, and its share of the wettest 72-hour total is 17.5 / 187.2 = 0.093.
- Report-total transfer test: the 744.8 mm report total is 3.78 times the hourly point total, 3.38 times the daily point total, 9.26 times the daily grid maximum, and 12.79 times the satellite grid maximum.
- Runoff-equivalent load: 744.8 mm over 83 hours gives 8.97 mm/h and 215.4 mm/day. A runoff coefficient of 0.50 gives 372400 m3/km2; a coefficient of 0.70 gives 521360 m3/km2.
- Wind and image checks: maximum wind is 38.5 km/h, mean radar VV change is -0.0142 dB, and mean embedding change is 0.0175.

# Reasoning Path

The persistence row passes because the event total, 72-hour concentration, wet-hour share, and longest wet run all exceed the required thresholds. That makes the rainfall load a multiday forcing rather than a brief spike.

The peak-hour row rejects single-hour control because both concentration ratios are below 0.10. The largest hour matters locally, but it does not dominate the accumulated rainfall ledger.

The report-total row rejects transferring the 744.8 mm report maximum uniformly across the broader comparison domain. The ratios are too large, especially against gridded maxima, so that number should be treated as an extreme local anchor.

The runoff row passes because the report-scale duration, mean intensity, and runoff-equivalent depths are all high enough to support severe runoff loading. The wind and image row rejects a wind-led or image-led diagnosis because those summary values stay below the dominance thresholds.

# Computed Interpretation

The compact diagnosis is `persistent_remnant_rainfall_runoff_haihe_routing`: multiday Doksuri remnant rainfall supplied the runoff load, while river routing through the Haihe system explains why the event cannot be reduced to peak-hour rainfall, wind, or image-change summaries.

# Scoring Rubric

- 3 points: Returns the requested compact JSON structure with the target family, five required row IDs, formulas, computed values, tests, row results, and final label. Partial credit: 1-2 points for valid JSON with missing rows or incomplete row fields.
- 4 points: Correctly computes the rainfall persistence row: 196.9 mm, 187.2 mm, 0.951, 84 wet hours, 0.700 wet-hour share, and 78-hour longest wet run, with the correct pass result. Partial credit: 2-3 points for mostly correct values with one threshold or unit error.
- 3 points: Correctly computes the peak-hour ratios 0.089 and 0.093 from 17.5 mm and rejects single-hour control. Partial credit: 1-2 points for the right rejection with incomplete ratio work.
- 3 points: Correctly computes the four report-total ratios 3.78, 3.38, 9.26, and 12.79 and rejects uniform report-total transfer. Partial credit: 1-2 points for using only point comparisons or only grid comparisons.
- 3 points: Correctly derives 8.97 mm/h, 215.4 mm/day, 372400 m3/km2, and 521360 m3/km2, and applies the severe-runoff threshold. Partial credit: 1-2 points for correct intensity or volume computation but not both.
- 2 points: Correctly applies the wind and image dominance test using 38.5 km/h, -0.0142 dB, and 0.0175. Partial credit: 1 point for using only wind or only image values.
- 2 points: Gives the final label `persistent_remnant_rainfall_runoff_haihe_routing` and keeps the interpretation tied to the computed ledger rather than adding exact loss or management-sequence assertions. Partial credit: 1 point for a correct label with a loose interpretation, or a correct interpretation with a noncanonical label.
