# Doksuri Haihe Basin Rainfall Persistence Ledger

A technical hydrology team is reviewing the July 29-August 2, 2023 Typhoon Doksuri flood affecting Beijing, Tianjin, Hebei, and the Haihe basin. The proposed diagnosis is that the inland flood signal is supported by persistent basin rainfall and routed river response, rather than by a short burst, wind forcing, or a weak gridded-rainfall signal.

Compute the consistency ledger from the incident record and return JSON only. Use the row IDs below exactly.

Use these variable aliases in formulas:

- `report_avg_rainfall_mm`, `report_duration_hours`, `report_single_point_max_rainfall_mm`, `reservoir_site_rainfall_mm`
- `point_event_total_mm`, `point_max_1h_mm`, `point_max_24h_mm`, `point_max_48h_mm`, `point_max_72h_mm`, `wet_hours_ge_1mm`, `wet_hours_ge_5mm`
- `daily_event_total_mm`, `daily_max_day_precip_mm`, `peak_wind_kmh`
- `compact_hourly_grid_max_mm`, `compact_event_grid_max_mm`, `compact_daily_grid_max_mm`
- `river_swelling_flag`, `bridge_damage_flag`, `analysis_area_km2`, `road_bridge_elements`, `critical_facility_elements`
- `pre_scene_count`, `post_scene_count`, `radar_mean_change_db`, `embedding_mean_change`

Required tests:

- Report rain load: compute average intensity, maximum-to-average rainfall ratio, rain volume per square kilometer for the average and point maximum, and reservoir-to-average ratio.
- Persistence over peak: compute the 24h, 48h, and 72h shares of the point event total, the 72h-to-1h ratio, the share of hours at or above 5 mm among hours at or above 1 mm, and the daily peak share.
- River response and receptor density: compute the two river-response flags as a pass count, plus road/bridge and critical-facility densities per 100 km2.
- Wind and compact-grid rejection: convert peak wind to m/s, square it as a wind-energy proxy, and compare compact-grid maxima with the point event total.
- Sensor context check: report the pre/post scene counts and small mean-change metrics only as supporting context; closure and management counts must not become the main trigger.

Set `final_consistency_label` to `basin_routed_persistent_rainfall_flood_supported` only if the report rain-load, persistence-over-peak, and river-response rows pass while wind control, low compact-grid downgrade, image-led extent, release/retention trigger, short peak-hour framing, and mountain-gully dominance are rejected by the computed ledger.

Return JSON in this shape:

```json
{
  "target_family": "doksuri_haihe_basin_routing_persistence_peak_ledger",
  "basin_routing_ledger": [
    {"row_id": "report_rain_load", "formula": "", "computed_value": {}, "threshold_or_test": "", "result": ""},
    {"row_id": "persistence_over_peak", "formula": "", "computed_value": {}, "threshold_or_test": "", "result": ""},
    {"row_id": "river_response_receptor_density", "formula": "", "computed_value": {}, "threshold_or_test": "", "result": ""},
    {"row_id": "wind_and_compact_grid_rejection", "formula": "", "computed_value": {}, "threshold_or_test": "", "result": ""},
    {"row_id": "sensor_context_check", "formula": "", "computed_value": {}, "threshold_or_test": "", "result": ""}
  ],
  "rejected_overreads": ["..."],
  "final_consistency_label": "<computed_label>"
}
```
