# Central Andes Snow Phase Ledger

For the January 27-February 4, 2021 Central Andes high-terrain storm, compute a compact phase-state ledger from the local hourly and daily weather series. The aim is to test whether the series supports sustained snow accumulation followed by refreeze and wind stress, rather than a brief visual coating or a warm rain-only reading.

Use the diagnostic weather point in the local event package. Apply these definitions:

- `snow_total_cm = sum(daily snowfall)`
- `snow_days = count(daily snowfall > 0)`
- `longest_snow_run_h = longest consecutive hourly run with snowfall > 0`
- `max_depth_m = max(hourly snow_depth)`
- `depth_retention_ratio = max_depth_m / (snow_total_cm / 100)`
- `snow_weighted_temp_c = sum(hourly temperature_c * hourly snowfall_cm) / sum(hourly snowfall_cm)`
- `snow_le_1c_cm = sum(hourly snowfall_cm where hourly temperature_c <= 1)`
- `freezing_level_proxy_m = elevation_m + temperature_c / 0.0065`
- `subzero_h = count(hourly temperature_c < 0)`
- `post_snow_subzero_h = count(hourly temperature_c < 0 after the final hour with snowfall > 0)`
- `freezing_degree_hours_c_h = sum(max(0, -hourly temperature_c))`
- `wind_chill_c = 13.12 + 0.6215*T - 11.37*V^0.16 + 0.3965*T*V^0.16`, where `T` is temperature in C and `V` is 10 m wind speed in km/h

Return compact JSON in this shape:

```json
{
  "event_window": "start_date/end_date",
  "snow": {
    "total_cm": 0.0,
    "peak_day_cm": 0.0,
    "peak_day": "YYYY-MM-DD",
    "snow_days": 0,
    "longest_run_h": 0,
    "max_depth_m": 0.0,
    "depth_retention_ratio": 0.0
  },
  "phase": {
    "snow_weighted_temp_c": 0.0,
    "freezing_level_during_snow_m": 0,
    "freezing_level_coldest_m": 0,
    "snow_le_1c_cm": 0.0
  },
  "cold_wind": {
    "subzero_h": 0,
    "post_snow_subzero_h": 0,
    "freezing_degree_hours_c_h": 0.0,
    "peak_gust_kmh": 0.0,
    "min_wind_chill_c": 0.0
  },
  "final_label": "snake_case_label"
}
```

Use `sustained_high_terrain_snow_then_refreeze_wind` when all five gates pass: total snow at least 50 cm, longest snowfall run at least 24 h, maximum snow depth at least 0.20 m, freezing-degree hours at least 20 C h, and minimum wind chill at or below -5 C. Otherwise use `weak_or_warm_snow_signal`.

Round snowfall and depth-retention values to two decimals, temperature and freezing-degree hours to one decimal, freezing-level proxies to the nearest meter, gust speed to one decimal, and wind chill to two decimals.
