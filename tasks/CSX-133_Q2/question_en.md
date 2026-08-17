# Compound Passage Consistency Proof

A technical review team is checking the northern Viet Nam point record for Super Typhoon Yagi during 1-7 September 2024. Test whether the record satisfies a compound typhoon-passage label through explicit wind, pressure, rainfall, and timing inequalities rather than through a general storm explanation.

For local point metrics, use the full package hourly record for 2024-09-01 through 2024-09-07 inclusive. Use the GDACS catalog only for the catalog peak wind anchor and event metadata, not to truncate the local hourly series.

Compute the requested ledger and return JSON with exactly these five top-level keys:

```json
{
  "metrics": {
    "catalog_peak_wind_kmh": 0.0,
    "local_peak_gust_kmh": 0.0,
    "gust_energy_proxy_kmh2_per_1000": 0.0,
    "pressure_drop_hpa": 0.0,
    "event_precip_mm": 0.0,
    "wettest_24h_mm": 0.0,
    "rainfall_concentration_24h": 0.0,
    "peak_sync_lag_hours": 0
  },
  "threshold_tests": {
    "wind": false,
    "pressure": false,
    "rain_concentration": false,
    "timing": false
  },
  "conclusion": "<compound_typhoon_passage_consistent or compound_typhoon_passage_not_proven>",
  "rejected_alternative": "<single_driver_wind_or_rain, or none>",
  "proof": "<one or two sentences with formulas and inequalities>"
}
```

Use these definitions:

- `event_precip_mm` is total event-window precipitation.
- `wettest_24h_mm` is the maximum rolling 24-hour precipitation total.
- `rainfall_concentration_24h = wettest_24h_mm / event_precip_mm`.
- `gust_energy_proxy_kmh2_per_1000 = local_peak_gust_kmh^2 / 1000`.
- `pressure_drop_hpa = max pressure_msl - min pressure_msl`.
- `peak_sync_lag_hours` is the largest absolute time separation among the local peak gust, minimum pressure, and wettest hour.

Apply this decision rule: return `compound_typhoon_passage_consistent` only if local peak gust is at least 90 km/h, pressure drop is at least 20 hPa, rainfall concentration is at least 0.70, and `peak_sync_lag_hours` is at most 1 hour. Round wind, rainfall, pressure, and the energy proxy to one decimal place; round the rainfall concentration to three decimals.
