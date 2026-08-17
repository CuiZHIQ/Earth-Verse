# Final Answer

The computed final label is `source_transport_smoke_fit`.

```json
{
  "answer": "source_transport_smoke_fit",
  "window_days": 1,
  "metrics": {
    "source_flags": 3,
    "transport_flags": 4,
    "smoke_family_hits": 7,
    "local_precip_mm": 1.04,
    "regional_precip_mm": 5.34,
    "local_wind_kmh": 8.2,
    "tmax_c": 31.1,
    "tmax_ge_30c_run_days": 2,
    "eonet_events": 0,
    "burn_scar_status": "no_sufficient_scenes",
    "population_sum": 82984.1
  },
  "score_ledger": {
    "source_transport_smoke": 10,
    "local_catalog_fire": 1,
    "heat_only_weather": 1,
    "rainfall_clearing": 0,
    "burn_scar_mapping": 0,
    "margin_over_next": 9
  },
  "threshold_tests": {
    "source_transport_ge_8": true,
    "next_best_le_3": true,
    "local_precip_lt_2mm": true,
    "regional_precip_lt_10mm": true,
    "burn_scar_not_available": true
  },
  "decision_rule": "answer=source_transport_smoke_fit when source_transport_smoke>=8 and next_best<=3"
}
```

# Key Computations

The event window starts and ends on 2004-08-28, so the inclusive duration is `window_days = 1`.

In the event narrative, all three source flags are present: seasonal agricultural burning, charcoal production, and MODIS-detected fires. Four transport flags are also present: semi-permanent high pressure, counterclockwise recirculation, air recirculation, and Atlantic haze outflow. Exact event-narrative smoke-family term counts are `smoke = 5`, `smog = 1`, and `haze = 1`, so `smoke_family_hits = 7`.

The event-day local precipitation mean is `(1.10 + 0.97) / 2 = 1.04 mm`. The regional precipitation mean is `(3.14 + 5.64 + 7.25) / 3 = 5.34 mm`. Event-day Open-Meteo wind is `8.2 km/h`, event-day Tmax is `31.1 C`, and the longest run of days at or above 30 C is 2 days. The burn-scar summary status is `no_sufficient_scenes`, the wildfire catalog has 0 events, and the population total is `82,984.1`.

The source-plus-transport score is:

`3 source flags + 4 transport flags + 1 smoke-term pass + 1 dry/low-wind pass + 1 population-context pass = 10`.

The simpler candidate scores are `local_catalog_fire = 1`, `heat_only_weather = 1`, `rainfall_clearing = 0`, and `burn_scar_mapping = 0`. The next-best score is 1, so the margin is `10 - 1 = 9`.

# Reasoning Path

The text-derived flags form the main ledger signal: source and transport terms both pass strongly, and the event-narrative smoke-family count is above the threshold of 6. The weather fields do not create a high-precipitation clearing pattern because both local and regional precipitation means are below their thresholds, and the local wind value is below 10 km/h.

The heat-only label earns one point because Tmax exceeds 30 C, but the two-day warm run is below the three-day threshold and the smoke-family count is not low. The burn-scar label earns zero because there are no sufficient scenes and both pre-event and post-event scene counts are zero. The local catalog fire label earns only the source-flag point because the wildfire catalog count is zero and burn-scar mapping is not available.

The decision rule requires a source-plus-transport score of at least 8 and a next-best score of at most 3. The computed values meet both tests: `10 >= 8` and `1 <= 3`.

# Computed Interpretation

The ledger is numerically most consistent with `source_transport_smoke_fit`. That interpretation rests on a high text-flag score, light precipitation, weak local wind, unavailable burn-scar mapping, an empty wildfire catalog, and a population total above the context threshold. It does not convert the episode into measured PM2.5, ozone, health-outcome, runoff, or burn-severity quantities; those values are not demonstrated by the computed inputs.

# Scoring Rubric

Total: 20 points.

- 3 points: JSON shape and final label. Full credit for returning the requested top-level keys and `source_transport_smoke_fit`. Partial credit: 1-2 points for a mostly complete JSON object with a missing nested field or a label that is close but not exact.
- 4 points: Text flag extraction. Full credit for `source_flags = 3`, `transport_flags = 4`, and event-narrative `smoke_family_hits = 7`. Partial credit: 1-3 points for correct directionality with one or two count errors.
- 4 points: Weather and threshold metrics. Full credit for `local_precip_mm = 1.04`, `regional_precip_mm = 5.34`, `local_wind_kmh = 8.2`, `tmax_c = 31.1`, and `tmax_ge_30c_run_days = 2`. Partial credit: 1-3 points for using the correct variables with minor rounding or omission errors.
- 3 points: Catalog, burn-scar, and population metrics. Full credit for `eonet_events = 0`, `burn_scar_status = no_sufficient_scenes`, and `population_sum = 82984.1`. Partial credit: 1-2 points for two correct metrics or for correct qualitative use with imprecise numbers.
- 4 points: Candidate score ledger. Full credit for scores of 10, 1, 1, 0, and 0 with `margin_over_next = 9`. Partial credit: 1-3 points for applying the formula but missing one component or the margin.
- 2 points: Decision rule and interpretation. Full credit for applying `source_transport_smoke >= 8` and `next_best <= 3` and keeping the interpretation tied to computed values. Partial credit: 1 point for the right label without both threshold tests.
