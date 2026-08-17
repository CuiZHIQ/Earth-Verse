# Typhoon Doksuri Remnant Rainfall Phase Segmentation

You are an event-timeline analyst segmenting the late July to early August 2023 rainfall process caused by Typhoon Doksuri remnants over Beijing, Hebei, Tianjin, and the Haihe river system. The task is to divide the event into physically meaningful phases with computed transition evidence.

Use only the local CSX-095 event package. Select package-relative evidence for hourly rainfall, daily rainfall, reported extreme rainfall anchors, and wind background.

Segment the event into these phases:

- sustained wet-hour rainfall phase;
- three-day concentration phase;
- report-calibrated extreme rainfall phase;
- wind-dominance rejection phase.

Compute:

- `wet_hour_fraction = wet_hours / window_hours`;
- `longest_wet_run_share = longest_wet_run_hours / wet_hours`;
- `peak_hour_share = peak_hour_mm / hourly_total_mm`;
- `wet_hour_mean_mm = hourly_total_mm / wet_hours`;
- `window_mean_mm_per_hour = hourly_total_mm / window_hours`;
- `max_3day_share = max_3day_daily_sum_mm / daily_total_mm`;
- `peak_day_share = peak_day_mm / daily_total_mm`;
- `daily_to_hourly_total_ratio = daily_total_mm / hourly_total_mm`;
- `report_avg_intensity_mm_per_hour = report_avg_mm / report_duration_hours`;
- `report_avg_to_hourly_total_ratio = report_avg_mm / hourly_total_mm`;
- `reservoir_to_report_avg_ratio = reservoir_mm / report_avg_mm`;
- `single_point_to_report_avg_ratio = single_point_max_mm / report_avg_mm`;
- `peak_wind_ms` and `wind_energy_proxy = peak_wind_ms^2`.

Return this JSON shape:

```json
{
  "target_family": "doksuri_rainfall_phase_segmentation",
  "phases": [
    {"phase": "sustained_wet_hour_rainfall", "time_window": "", "dominant_process": "", "computed_value": {}, "transition_basis": ""},
    {"phase": "three_day_concentration", "time_window": "", "dominant_process": "", "computed_value": {}, "transition_basis": ""},
    {"phase": "report_calibrated_extreme_rainfall", "time_window": "", "dominant_process": "", "computed_value": {}, "transition_basis": ""},
    {"phase": "wind_dominance_rejection", "time_window": "", "dominant_process": "", "computed_value": {}, "transition_basis": ""}
  ],
  "phase_checks": [
    {"row_id": "rainfall_persistence", "computed_value": {}, "result": ""},
    {"row_id": "three_day_concentration", "computed_value": {}, "result": ""},
    {"row_id": "report_intensity_alignment", "computed_value": {}, "result": ""},
    {"row_id": "wind_rejection", "computed_value": {}, "result": ""}
  ],
  "final_label": ""
}
```

Use `persistent_remnant_cyclone_rainfall_supported` only when the rainfall persistence, three-day concentration, report-intensity alignment, and wind rejection phases all support a rainfall-dominant remnant-cyclone timeline.
