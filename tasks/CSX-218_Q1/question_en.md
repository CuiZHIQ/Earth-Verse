# Angola Smoke-Transport Candidate Score Ledger

An analyst is auditing the late-August 2004 Angola fire-and-smoke episode. Build a numeric candidate score ledger from the event narrative, daily weather fills, regional precipitation summaries, burn-scar availability, the wildfire catalog, and the population summary. The goal is to test whether the data fit a source-plus-transport smoke state better than four simpler labels: local catalog fire, heat-only weather, rainfall clearing, or burn-scar mapping.

Return a JSON object with exactly these keys:

```json
{
  "answer": "short_label",
  "window_days": 0,
  "metrics": {
    "source_flags": 0,
    "transport_flags": 0,
    "smoke_family_hits": 0,
    "local_precip_mm": 0.0,
    "regional_precip_mm": 0.0,
    "local_wind_kmh": 0.0,
    "tmax_c": 0.0,
    "tmax_ge_30c_run_days": 0,
    "eonet_events": 0,
    "burn_scar_status": "short_status",
    "population_sum": 0.0
  },
  "score_ledger": {
    "source_transport_smoke": 0,
    "local_catalog_fire": 0,
    "heat_only_weather": 0,
    "rainfall_clearing": 0,
    "burn_scar_mapping": 0,
    "margin_over_next": 0
  },
  "threshold_tests": {
    "source_transport_ge_8": false,
    "next_best_le_3": false,
    "local_precip_lt_2mm": false,
    "regional_precip_lt_10mm": false,
    "burn_scar_not_available": false
  },
  "decision_rule": "short_rule"
}
```

Use these rules:

- `window_days` is the inclusive event-window duration.
- `source_flags` counts seasonal agricultural burning, charcoal production, and MODIS-detected fires. `transport_flags` counts semi-permanent high pressure, counterclockwise recirculation, air recirculation, and Atlantic haze outflow.
- `smoke_family_hits` is the exact total of `smoke`, `smog`, and `haze` terms in the event narrative only; do not count page navigation, boilerplate, or unrelated background articles.
- `local_precip_mm` is the mean of event-day Open-Meteo and NASA POWER precipitation. `regional_precip_mm` is the mean of ERA5-Land, GPM, and CHIRPS event precipitation means. `local_wind_kmh` and `tmax_c` come from event-day Open-Meteo, and `tmax_ge_30c_run_days` is the longest Open-Meteo run of days at or above 30 C in the filled daily series.
- `source_transport_smoke = source_flags + transport_flags + smoke_term_pass + dry_low_wind_pass + population_context_pass`, where `smoke_term_pass` is 1 when event-narrative `smoke_family_hits >= 6`, `dry_low_wind_pass` is 1 when local precipitation is below 2 mm, regional precipitation is below 10 mm, and local wind is below 10 km/h, and `population_context_pass` is 1 when population is at least 50,000.
- `local_catalog_fire = 1` when at least two source flags are present, plus 3 if the wildfire catalog has at least one event, plus 2 if burn-scar mapping has sufficient scenes.
- `heat_only_weather = 1` when event-day Tmax is at least 30 C, plus 1 when the warm run is at least 3 days, plus 1 when smoke-family hits are below 3.
- `rainfall_clearing = 2` when local precipitation is at least 10 mm, plus 2 when regional precipitation is at least 10 mm, plus 1 when the GPM max/mean precipitation ratio is at most 5.
- `burn_scar_mapping = 5` when burn-scar mapping has sufficient scenes, plus 1 each for nonzero pre-event and post-event scene counts.
- Set `answer` to `source_transport_smoke_fit` only when `source_transport_smoke >= 8` and the next-best candidate score is at most 3; otherwise set it to `mixed_or_low_fit`.
