# April 2022 Iraq Dust-Storm Wind-Rain Threshold Check

A technical analyst is checking whether the 7-10 April 2022 Iraq dust-storm event is represented by onset wind support followed by wet moderation. Use the daily point meteorology and regional precipitation summaries as package-derived threshold diagnostics for the event window, not as measured loss, closure, admission, or exact footprint evidence.

For each date, compute:

- `wind_ratio = min(point_wind_m_s / 4.5, companion_wind_km_h / 22.0)`
- `rain_ratio = min(point_precip_mm / 10.0, companion_precip_mm / 10.0)`

A paired wind-support day has `wind_ratio >= 1.0`. A paired rain-moderation day has `rain_ratio >= 1.0`. The late-window wind revival test is true only if 2022-04-10 has `wind_ratio >= 1.0`. Compute the mean of the three regional event-precipitation mean values as `regional_mean_mm`.

Set `answer` to `onset_wind_supported_then_wet_moderated` only when exactly one paired wind-support day occurs at event onset, exactly one paired rain-moderation day occurs later, the rain peak follows the wind peak by one day, and the late-window wind revival test is false. Otherwise use `threshold_not_met`.

Return compact JSON:

```json
{
  "answer": "<computed_label>",
  "wind_pair_days": 0,
  "wind_peak": {"date": "YYYY-MM-DD", "ratio": 0.0},
  "rain_pair_days": 0,
  "rain_peak": {"date": "YYYY-MM-DD", "ratio": 0.0},
  "lag_days": 0,
  "late_pair": false,
  "regional_mean_mm": 0.0
}
```
