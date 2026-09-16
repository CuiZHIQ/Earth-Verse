# Tropical Cyclone Freddy March Rain-Lag Threshold Proof

During Tropical Cyclone Freddy's March 2023 late southern Africa phase, hydrometeorology analysts need to check whether the southern Malawi rainfall and flood timing pass a deterministic multi-day rain-lag test rather than looking like a short rainfall spike or a local-wind-dominant signal.

Using the incident record's catalog timestamps, hourly precipitation and gust series, and cataloged Freddy peak wind, compute the threshold ledger for 2023-03-12 00:00 through 2023-03-14 23:00 in the package hourly timestamp basis. Compare GDACS catalog start/end timestamps on their UTC catalog basis.

Rules:

- `local_precip_mm` is total precipitation during the tested local window.
- `wettest_72h_mm` is the maximum rolling 72-hour precipitation total over the hourly series.
- `wettest_24_to_72_ratio` is maximum rolling 24-hour precipitation divided by maximum rolling 72-hour precipitation.
- `wet_run_hours` is the longest continuous run of hours in the hourly series with precipitation greater than 0.
- `flood_lag_days` is Malawi flood start minus Freddy tropical-cyclone end, in days.
- `gust_to_peak_wind_ratio` is maximum local hourly gust divided by the cataloged Freddy peak wind.
- Label the result `linked_multi_day_runoff_pulse` only when `local_precip_mm >= 100`, `abs(local_precip_mm - wettest_72h_mm) <= 0.05`, `wettest_24_to_72_ratio < 0.60`, `wet_run_hours >= 48`, `flood_lag_days <= 2.0`, and `gust_to_peak_wind_ratio < 0.35`; otherwise label it `threshold_mismatch`.

Return compact JSON only:

```json
{
  "answer": {
    "local_precip_mm": 0.0,
    "wettest_72h_mm": 0.0,
    "wettest_24_to_72_ratio": 0.0,
    "wet_run_hours": 0,
    "flood_lag_days": 0.0,
    "max_gust_kmh": 0.0,
    "gust_to_peak_wind_ratio": 0.0,
    "consequence_label": "<short label>"
  },
  "proof": "<one sentence threshold proof>"
}
```
