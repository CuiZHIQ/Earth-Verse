# Giant-Hail Severity Ledger

During the July 19-25, 2023 northern Italy severe hailstorms, a severe-convection reviewer is checking whether the event satisfies a hail-size/report-count severity ledger rather than a rainfall-load, wind-pressure, isolated-stone, or threshold-capped ledger.

Compute the following values from the event data:

- `diameter_ratio_vs_10cm = max_hail_cm / 10`
- `diameter_ratio_vs_previous_record = max_hail_cm / previous_record_cm`
- `world_record_fraction = max_hail_cm / cited_world_record_cm`
- `volume_proxy_vs_10cm = (max_hail_cm / 10)^3`
- `energy_proxy_vs_10cm = (max_hail_cm / 10)^4`
- `energy_proxy_vs_previous_record = (max_hail_cm / previous_record_cm)^4`
- `italy_report_share = italy_giant_hail_reports / total_giant_hail_reports`
- `gpm_spatial_concentration_ratio = event_gpm_precip_max_mm / event_gpm_precip_mean_mm`

Use these severity-ledger rules:

- the hail-size/report-count ledger passes if `max_hail_cm >= 10`, `total_giant_hail_reports >= 10`, `italy_report_share >= 0.75`, `energy_proxy_vs_10cm >= 8`, and `energy_proxy_vs_previous_record >= 1.5`;
- the rainfall-load ledger overrides only if point event rain is at least 100 mm, the wettest 24-hour point window is at least 75 mm, or `gpm_spatial_concentration_ratio >= 4`;
- the wind-pressure ledger overrides only if peak gust is at least 80 km/h or the start-to-minimum pressure fall is at least 25 hPa;
- the isolated-stone ledger fails when the report-spread test passes;
- the threshold-capped ledger fails when both nonlinear energy tests pass.

Return a concise JSON object with this shape:

```json
{
  "answer": "<ledger status>",
  "hail_size_proxies": {
    "max_hail_cm": 0,
    "diameter_ratio_vs_10cm": 0,
    "diameter_ratio_vs_previous_record": 0,
    "world_record_fraction": 0,
    "volume_proxy_vs_10cm": 0,
    "energy_proxy_vs_10cm": 0,
    "energy_proxy_vs_previous_record": 0
  },
  "report_spread": {
    "total_giant_hail_reports": 0,
    "italy_giant_hail_reports": 0,
    "italy_report_share": 0,
    "passes_spread_test": false
  },
  "context_overrides": {
    "rain_load_primary": false,
    "wind_pressure_primary": false,
    "point_event_precip_mm": 0,
    "wettest_24h_mm": 0,
    "gpm_spatial_concentration_ratio": 0,
    "peak_gust_kmh": 0,
    "pressure_fall_hpa": 0
  },
  "rejected_ledgers": ["<failed ledger labels>"],
  "proof_sentence": "<one sentence tying the pass/fail decisions to the numbers>"
}
```
