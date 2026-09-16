# Hong Kong Cold-Surge Numeric Ledger

For the January 23-24, 2016 Hong Kong cold-wave episode, compute a compact cold-stress ledger that distinguishes sustained cold plus wind from a snow-accumulation interpretation.

Use the 48 hourly records from 2016-01-23T00:00 through 2016-01-24T23:00. Apply these definitions:

- `cold_load_c_h = sum(max(0, 7 - temperature_c))`
- `hours_le_7c = count(temperature_c <= 7)`
- `longest_run_h = longest consecutive hourly run with temperature_c <= 7`
- `overlap_h = count(temperature_c <= 7 and gust_kmh >= 55)`
- `wind_chill_c = 13.12 + 0.6215*T - 11.37*V^0.16 + 0.3965*T*V^0.16`, where `T` is temperature in C and `V` is 10 m wind speed in km/h
- the snow-depth gate passes only when maximum snow depth is greater than 0 m and total snowfall is at least 1 cm

Return compact JSON in this shape:

```json
{
  "event_window": "start_hour/end_hour",
  "temperature": {
    "min_c": 0.0,
    "hours_le_7c": 0,
    "longest_run_h": 0,
    "cold_load_c_h": 0.0
  },
  "wind": {
    "peak_gust_kmh": 0.0,
    "overlap_h": 0,
    "min_wind_chill_c": 0.0
  },
  "snow": {
    "total_cm": 0.0,
    "max_depth_m": 0.0,
    "passes_depth_gate": false
  },
  "final_label": "snake_case_label"
}
```

Round temperatures, cold load, and gust speed to one decimal place; round wind chill to two decimals and snowfall to two decimals.
