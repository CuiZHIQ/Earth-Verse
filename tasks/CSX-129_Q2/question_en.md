# Hurricane Ian Compound-Load Index Check

A tropical-cyclone analyst is checking a numeric diagnosis for Hurricane Ian near the Fort Myers area during September 23-30, 2022. Compute the local wind-rain-pressure load from the technical record and test the pass rule below.

Definitions:

- `peak_gust_kmh`: maximum hourly 10 m wind gust, rounded to one decimal.
- `gust_hours_ge119`: count of hourly gust values at or above 119 km/h.
- `event_precip_mm`: sum of hourly precipitation over the event window, rounded to one decimal.
- `wettest_24h_mm`: largest rolling sum across any 24 consecutive hourly precipitation values, rounded to one decimal.
- `min_pressure_hpa`: minimum hourly mean sea-level pressure, rounded to one decimal.
- `pressure_deficit_hpa`: `1013.25 - min_pressure_hpa`, rounded to two decimals.
- `wind_gate`: `peak_gust_kmh >= 150` and `gust_hours_ge119 >= 6`.
- `rain_gate`: `wettest_24h_mm >= 100` and `event_precip_mm >= 150`.
- `pressure_gate`: `min_pressure_hpa <= 970` and `pressure_deficit_hpa >= 40`.
- `low_coastal_gate`: point elevation is at most 10 m and `min_pressure_hpa <= 970`.
- `gate_count`: count of true gates among `wind_gate`, `rain_gate`, `pressure_gate`, and `low_coastal_gate`.
- `compound_index`: `peak_gust_kmh/150 + wettest_24h_mm/100 + event_precip_mm/150 + pressure_deficit_hpa/40 + (10 - elevation_m)/10`, rounded to three decimals.

The diagnosis passes when `gate_count == 4` and `compound_index >= 5.0`. If it passes, use `answer = "compound_wind_rain_pressure_load_pass"`, `threshold_result = "pass_compound_load"`, and `rejected_alternative = "single_driver_only"`. If it fails, use `answer = "compound_load_fail"`, `threshold_result = "fail_compound_load"`, and `rejected_alternative = "compound_threshold_not_met"`.

Return this compact JSON shape:

```json
{
  "answer": "<short computed diagnosis label>",
  "metrics": {
    "peak_gust_kmh": 0.0,
    "gust_hours_ge119": 0,
    "event_precip_mm": 0.0,
    "wettest_24h_mm": 0.0,
    "min_pressure_hpa": 0.0,
    "pressure_deficit_hpa": 0.0,
    "elevation_m": 0.0
  },
  "gates": {
    "wind": false,
    "rain": false,
    "pressure": false,
    "low_coastal": false
  },
  "gate_count": 0,
  "compound_index": 0.0,
  "threshold_result": "<pass/fail label>",
  "rejected_alternative": "<short computed consequence>"
}
```
