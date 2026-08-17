# Hunga Tonga Surface-Change Consistency Test

A technical review is checking whether the Hunga Tonga event-window numbers satisfy a surface-change rule with a weather-null guardrail.

Compute these quantities:

- `s1_abs_change_db = max(abs(vv_change_min), abs(vv_change_max))`
- `s1_signal_to_std = s1_abs_change_db / vv_change_stdDev`
- `optical_peak_to_mean = optical_change_max / optical_change_mean`
- `event_precip_max_mm = max(event_day_gridded_precip_max, event_day_reanalysis_precip_sum_max)`
- `coverage_balance = min(pre_count, post_count) / max(pre_count, post_count)`
- `event_anchor_score = I(alert_score >= 3.0) + I(plume_height_km >= 40.0)`

Apply these gates:

- `all_weather_gate`: `s1_abs_change_db >= 10`, `s1_signal_to_std >= 10`, `pre_count >= 10`, `post_count >= 10`, and `coverage_balance >= 0.8`
- `optical_support_gate`: `optical_change_max >= 0.5` and `optical_peak_to_mean >= 10`
- `weather_null_gate`: `event_precip_max_mm < 1.0`
- `event_anchor_gate`: `event_anchor_score == 2`

Set `final_label` to `event_window_surface_change_weather_null_pass` when all four gates pass; otherwise use `event_window_surface_change_weather_null_fail`.

Return compact JSON:

```json
{
  "target_family": "hunga_tonga_surface_change_weather_null_consistency",
  "metrics": {
    "s1_abs_change_db": 0.0,
    "s1_signal_to_std": 0.0,
    "optical_peak_to_mean": 0.0,
    "event_precip_max_mm": 0.0,
    "coverage_balance": 0.0,
    "event_anchor_score": 0
  },
  "gates": {
    "all_weather_gate": false,
    "optical_support_gate": false,
    "weather_null_gate": false,
    "event_anchor_gate": false
  },
  "final_label": "<label>",
  "computed_consequence": "<short consequence derived from the gates>"
}
```
