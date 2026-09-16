# Mocoa Threshold Ledger Consistency Check

For the 31 March to 1 April 2017 Mocoa event, a technical review team is checking whether two rapid affected-zone products form a numerically consistent threshold ledger. Use the event window, mapped envelope, area-normalized affected-zone counts, satellite observation counts, satellite change ranges, and event precipitation summary to compute the ledger.

Compute the following metrics and return only JSON:

```json
{
  "mapped_extent_bbox_km2": 0.0,
  "window_ledger": {
    "event_window_days_inclusive": 0,
    "days_04apr_after_window_end": 0,
    "days_10apr_after_window_end": 0,
    "product_spacing_days": 0
  },
  "area_and_exposure_ratios": {
    "road_density_04apr_km_per_km2": 0.0,
    "road_density_10apr_km_per_km2": 0.0,
    "road_density_ratio_10apr_to_04apr": 0.0,
    "building_density_04apr_per_km2": 0.0,
    "building_density_10apr_per_km2": 0.0,
    "building_density_ratio_10apr_to_04apr": 0.0
  },
  "satellite_change_metrics": {
    "radar_to_optical_observation_ratio": 0.0,
    "radar_change_range_db": 0.0,
    "optical_change_range": 0.0,
    "radar_to_optical_change_range_ratio": 0.0
  },
  "rainfall_concentration_ratio": 0.0,
  "threshold_gates": {
    "mapped_area_25_to_40_km2": "<pass/fail>",
    "window_spacing_3_to_9_days": "<pass/fail>",
    "road_density_ratio_at_least_1_2": "<pass/fail>",
    "building_density_ratio_below_0_5": "<pass/fail>",
    "radar_obs_ratio_at_least_4": "<pass/fail>",
    "radar_change_ratio_at_least_20": "<pass/fail>",
    "precip_concentration_at_least_30": "<pass/fail>"
  },
  "final": {
    "label": "<compact label>",
    "passed_gate_count": 0,
    "interpretation": "<one sentence>"
  }
}
```

Use km2 for mapped area. Compute the bounding-box area as `width_km * height_km`, with `width_km = (max_lon - min_lon) * 111.320 * cos(mid_lat)` and `height_km = (max_lat - min_lat) * 110.574`. Treat the event window as inclusive when counting `event_window_days_inclusive`. Use calendar-day differences for the April products: April 4 minus April 1 is 3 days, April 10 minus April 1 is 9 days, and April 10 minus April 4 is 6 days. Treat the radar and optical summaries as package-provided observation-count and change-range summaries for the ledger. Compute rainfall concentration as event maximum precipitation divided by event mean precipitation. Round numeric outputs to three decimals. Use `mapped_extent_thresholds_pass` only if all gates pass; otherwise use `mapped_extent_thresholds_fail`. Keep the interpretation to one sentence tied to the computed threshold ledger.
