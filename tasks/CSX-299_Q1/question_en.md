# Patagonian Dust-Streamer Dry-Transport Check

A technical reviewer is testing a rule for the February 6, 2020 Patagonian dust streamers: the event has dry wind-lofting conditions when all precipitation products are below 1.0 mm and the ERA5-Land mean wind-vector speed is at least 1.5 m/s. The NASA report transport-distance statement should be treated as report-context evidence for dust-streamer scale, not as same-day measured transport for the February 6 numeric window. The local PM/dust time series is used only to determine whether a measured particulate burden is available.

Compute:

- `pmax_mm = max(ERA5-Land mean event precipitation, GPM mean event precipitation, CHIRPS mean event precipitation)`.
- `dry_count = count of those three means below 1.0 mm`.
- `wind_m_s = sqrt(u_mean^2 + v_mean^2)` from mean 10 m wind components.
- `transport_km_lb`, the report-context lower-bound transport distance.
- `pm_obs_frac = non-null entries in PM10, PM2.5, and dust / total PM10, PM2.5, and dust hourly entries`.

Return compact JSON exactly with:

```json
{
  "evidence_windows": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "precip_wind_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "transport_report_context_date": "YYYY-MM-DD_or_report_context"
  },
  "pmax_mm": 0.0,
  "dry_count": 0,
  "wind_m_s": 0.0,
  "transport_km_lb": 0,
  "pm_obs_frac": 0.0,
  "conclusion": ""
}
```

Round numeric values to three decimals except `dry_count` and `transport_km_lb`. Use `dry_wind_conditions_with_report_context_transport_not_measured_pm` only when the dry and wind tests pass, the report-context transport lower bound passes, and `pm_obs_frac` equals 0; otherwise use `rule_not_satisfied`.
