# Final Answer

```json
{
  "target_family": "doksuri_haihe_basin_routing_persistence_peak_ledger",
  "basin_routing_ledger": [
    {
      "row_id": "report_rain_load",
      "formula": "331.0/83.0; 1025.0/331.0; 331.0*1000; 1025.0*1000; 744.8/331.0",
      "computed_value": {
        "report_avg_intensity_mm_per_hour": 3.988,
        "max_to_avg_rainfall_ratio": 3.097,
        "avg_rain_volume_m3_per_km2": 331000.0,
        "max_point_rain_volume_m3_per_km2": 1025000.0,
        "reservoir_to_avg_ratio": 2.25
      },
      "threshold_or_test": "duration >= 72 h, average load >= 300000 m3/km2, max/avg > 2, and reservoir/avg > 2",
      "result": "pass_persistent_high_load"
    },
    {
      "row_id": "persistence_over_peak",
      "formula": "97.4/196.9; 161.3/196.9; 187.2/196.9; 187.2/17.5; 11/52; 97.29/220.61",
      "computed_value": {
        "wettest_24h_share": 0.495,
        "wettest_48h_share": 0.819,
        "wettest_72h_share": 0.951,
        "wettest_72h_to_1h_peak_ratio": 10.697,
        "wet_hours_ge_5_share_of_ge_1": 0.212,
        "daily_peak_share": 0.441
      },
      "threshold_or_test": "72h share >= 0.90, 72h/1h ratio >= 10, and daily peak share < 0.50",
      "result": "pass_persistence_dominates_peak"
    },
    {
      "row_id": "river_response_receptor_density",
      "formula": "river flag count = 1 + 1; 199/2031.312*100; 81/2031.312*100",
      "computed_value": {
        "river_response_flag_count": 2,
        "river_response_flags_possible": 2,
        "road_bridge_density_per_100km2": 9.797,
        "critical_facility_density_per_100km2": 3.988
      },
      "threshold_or_test": "2/2 river-response flags pass; density checks show receptor context",
      "result": "pass_river_response_with_receptor_density"
    },
    {
      "row_id": "wind_and_compact_grid_rejection",
      "formula": "38.5/3.6; (38.5/3.6)^2; 8.1955/196.9; 20.5586/196.9; 196.9/3.0849; 196.9/8.1955; 196.9/20.5586",
      "computed_value": {
        "peak_wind_ms": 10.694,
        "wind_energy_proxy": 114.371,
        "compact_event_max_to_point_total_ratio": 0.042,
        "compact_daily_max_to_point_total_ratio": 0.104,
        "point_total_to_compact_hourly_grid_max_ratio": 63.828,
        "point_total_to_compact_event_grid_max_ratio": 24.025,
        "point_total_to_compact_daily_grid_max_ratio": 9.578
      },
      "threshold_or_test": "peak wind < 15 m/s and compact-grid maxima are far below the point event total",
      "result": "reject_wind_control_and_low_grid_downgrade"
    },
    {
      "row_id": "sensor_context_check",
      "formula": "abs(-0.0410782699); scene counts = 2 and 8; embedding mean = 0.0067614112",
      "computed_value": {
        "pre_scene_count": 2,
        "post_scene_count": 8,
        "radar_mean_abs_change_db": 0.041,
        "embedding_mean_change": 0.00676
      },
      "threshold_or_test": "small mean-change metrics cannot replace the rainfall/routing proof",
      "result": "context_only_not_main_trigger"
    }
  ],
  "rejected_overreads": [
    "typhoon_wind_control",
    "release_or_retention_decisions_as_primary_trigger",
    "short_peak_hour_framing",
    "low_compact_gridded_rainfall_downgrade",
    "image_led_extent_as_hydrologic_proof",
    "mountain_gully_closures_as_dominant_basin_driver"
  ],
  "final_consistency_label": "basin_routed_persistent_rainfall_flood_supported"
}
```

# Key Computations

The report average rainfall is 331.0 mm over 83.0 h, so the average intensity is `331.0 / 83.0 = 3.988 mm/h`. The single-point maximum of 1025.0 mm is `1025.0 / 331.0 = 3.097` times the report average. Water-load equivalents are `331.0 * 1000 = 331000 m3/km2` and `1025.0 * 1000 = 1025000 m3/km2`. The reservoir site rainfall ratio is `744.8 / 331.0 = 2.25`.

For the point hourly series, the event total is 196.9 mm. The wettest-window shares are `97.4 / 196.9 = 0.495`, `161.3 / 196.9 = 0.819`, and `187.2 / 196.9 = 0.951`. The 72h-to-1h ratio is `187.2 / 17.5 = 10.697`. There are 11 hours at or above 5 mm among 52 hours at or above 1 mm, giving `0.212`. The daily peak share is `97.29 / 220.61 = 0.441`.

Both river-response flags are true, giving `2/2`. With an analysis area of 2031.312 km2, road/bridge density is `199 / 2031.312 * 100 = 9.797 per 100 km2`, and critical-facility density is `81 / 2031.312 * 100 = 3.988 per 100 km2`. Peak wind is `38.5 / 3.6 = 10.694 m/s`, with wind-energy proxy `114.371`. Compact-grid maxima are only `0.042` and `0.104` of the point event total, while the point total is 63.828, 24.025, and 9.578 times the compact hourly, event, and daily grid maxima.

# Reasoning Path

The report rain-load row passes because the event duration exceeds 72 hours, the average water load exceeds 300000 m3/km2, the point maximum is more than twice the average, and the reservoir ratio is greater than 2. The persistence row also passes: 95.1% of the point event total is captured in the wettest 72 hours, the 72h load is more than ten times the one-hour peak, and the daily peak share remains below 0.50. These tests make a short peak-hour explanation too weak.

The river-response row passes because the two report-derived river indicators are both present, while the receptor-density calculations provide context rather than a separate trigger. The wind row rejects wind control because 10.694 m/s is below the 15 m/s test threshold. The compact-grid ratios reject a low-gridded-rainfall downgrade because the point series and report values show a much stronger local persistent-rain signal than the coarse compact maxima.

# Computed Interpretation

The compact interpretation is: persistent high rainfall over several days, combined with report-confirmed river response, supports the basin-routed inland flood label; wind, short-hour peak framing, and compact-grid downgrade are rejected by the computed ledger.

# Scoring Rubric

- 3 points: Required JSON schema and final label. Full credit returns the target family, all five required ledger rows, rejected-overread list, and `basin_routed_persistent_rainfall_flood_supported`. Partial credit: 1-2 points for a mostly correct shape with one missing row or a minor label mismatch; 0 points if the response is not a ledger-style answer.
- 4 points: Report rain-load calculations. Full credit gives 3.988 mm/h, 3.097, 331000 and 1025000 m3/km2, and 2.25 with correct tests. Partial credit: 2-3 points for most values with a rounding or unit slip; 1 point for using the right variables but missing derived load or ratio logic.
- 4 points: Persistence-over-peak proof. Full credit gives 0.495, 0.819, 0.951, 10.697, 0.212, and 0.441 with pass logic. Partial credit: 2-3 points for correct window shares but incomplete threshold reasoning; 1 point for only identifying that the 72h window dominates.
- 3 points: River response and receptor-density checks. Full credit gives 2/2 river flags plus 9.797 road/bridge and 3.988 critical-facility elements per 100 km2. Partial credit: 1-2 points for the correct river flags but one density missing or miscomputed.
- 3 points: Wind and compact-grid rejection. Full credit uses 10.694 m/s, 114.371, and the compact-grid contrast ratios to reject wind control and low-grid downgrade. Partial credit: 1-2 points for only the wind calculation or only the compact-grid comparison.
- 2 points: Rejected overreads. Full credit rejects at least four named overreads, including release/retention trigger and short peak-hour framing, and treats the sensor row as context only. Partial credit: 1 point for rejecting only two or three overreads or omitting the sensor-context limitation.
- 1 point: Concise calculation-led interpretation. Full credit keeps the final label tied to the computed ledger and avoids broad event narration. Partial credit: no partial credit for this item; prose that drifts away from the calculations earns 0 points.
