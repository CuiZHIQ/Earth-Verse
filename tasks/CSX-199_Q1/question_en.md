# Canadian Wildfire Burn-Smoke Signal Ledger

A technical review team is checking a compact numeric ledger for the May-September 2023 Canadian wildfires and smoke episode across North America. The test is whether the record is numerically strongest as a burn-and-smoke signal, rather than a rainfall, heat, or weak-signal reading.

Compute the ledger with these formulas:

- Report the full event window from the local event anchor, and separately report the physical-hazard diagnostic window used by the local precipitation and temperature products.
- `burn_index = dNBR_mean * 100 + dNBR_max * 10 + alpha_mean_change * 100`
- `burn_smoke = 2*(burn_index >= 40) + 1*(dNBR_mean >= 0.25) + 1*(dNBR_max >= 0.80) + 1*(alpha_mean_change >= 0.015) + 1*(smoke_air_quality_text) + 1*(smoke_health_text) + 1*(out_of_control_fire_text)`
- `rainfall = 1*(GPM_mean_mm >= 100) + 1*(CHIRPS_mean_mm >= 100) + 1*(ERA5_precip_mean_mm >= 150)`
- `heat = 1*(peak_Tmax_C >= 30) + 1*(mean_Tmax_C >= 25)`
- `weak_signal = 1*(burn_index < 25) + 1*(dNBR_mean < 0.10) + 1*(not smoke_air_quality_text) + 1*(not smoke_health_text)`
- `local_context = 1*(WorldPop_population < 250) + 1*(fire_station_count >= 1) + 1*(trunk_road_count >= 10)`

Use `local_context` only as a context score. The dominance margin is `burn_smoke - max(rainfall, heat, weak_signal)`. Set `answer` to `wildfire_burn_smoke_dominant` only if `burn_smoke >= 7` and the dominance margin is at least 5; otherwise set it to `threshold_not_met`. Set `severity_bin` from `burn_index`: `high` for at least 40, `moderate` for at least 25 and below 40, and `low` below 25.

Return compact JSON:

```json
{
  "target_family": "candidate_explanation_score_ledger",
  "event_window": {
    "start": "",
    "end": "",
    "days": 0
  },
  "hazard_window": {
    "start": "",
    "end": "",
    "days": 0
  },
  "metrics": {
    "burn_index": 0,
    "dnbr_mean": 0,
    "dnbr_max": 0,
    "alpha_mean_change": 0,
    "gpm_precip_mm": 0,
    "chirps_precip_mm": 0,
    "era5_precip_mm": 0,
    "peak_tmax_c": 0,
    "mean_tmax_c": 0,
    "worldpop_population": 0,
    "fire_station_count": 0,
    "trunk_road_count": 0
  },
  "text_gates": {
    "smoke_air_quality": false,
    "smoke_health": false,
    "out_of_control_fire": false
  },
  "scores": {
    "burn_smoke": 0,
    "rainfall": 0,
    "heat": 0,
    "weak_signal": 0,
    "local_context": 0
  },
  "score_comparison": {
    "dominant_signal": "",
    "secondary_signal": "",
    "margin": 0,
    "dominance_rule_pass": false
  },
  "severity_bin": "",
  "answer": "",
  "computed_consequence": "one sentence tied only to the ledger"
}
```
