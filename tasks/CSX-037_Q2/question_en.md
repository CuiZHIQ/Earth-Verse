# Hong Kong Cold-Process Fingerprint

During the January 2016 Hong Kong cold wave, a climatology review team needs a compact 23-24 January cold-process fingerprint that separates lowland air temperature, wind-chill exposure, and report-coded high-ground ice signals.

Compute these five fields from the package-local Open-Meteo cold-variable hourly series; use the official report only for the three high-ground ice text flags. For wind chill, use `WC = 13.12 + 0.6215*T - 11.37*V^0.16 + 0.3965*T*V^0.16` with `T` in deg C and 10 m wind speed `V` in km/h, applying the formula only where `T <= 10 C` and `V > 4.8 km/h`; otherwise keep the measured air temperature.

- `lowland_freezing_load_c_hours = sum(max(0 - T2m_hourly, 0))`
- `min_temp_threshold_anomaly_c = min(T2m_hourly) - 10`
- `severe_cold_duration_hours_le_5c = count(T2m_hourly <= 5)`
- `wind_chill_freezing_load_c_hours = sum(max(0 - wind_chill_hourly, 0))`
- `high_ground_ice_report_score_0to3 = freezing_rain_flag + icing_flag + slippery_or_icy_road_flag`

The report-score flags are binary text indicators from the official event report. Return only compact JSON in this form:

```json
{
  "answer": {
    "lowland_freezing_load_c_hours": 0.0,
    "min_temp_threshold_anomaly_c": 0.0,
    "severe_cold_duration_hours_le_5c": 0,
    "wind_chill_freezing_load_c_hours": 0.0,
    "high_ground_ice_report_score_0to3": 0
  },
  "interpretation": "<one sentence linking the numeric fingerprint to the cold-process profile>"
}
```
