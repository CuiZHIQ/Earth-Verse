# Correct Answer

```json
{
  "answer": "daytime_heat_exposure_dominant",
  "bounded_interpretation": "The result is a package-scale heat mechanism diagnosis, not exact mortality, outage, damage, or full regional attribution.",
  "computed_evidence": {
    "classification": "daytime_heat_exposure_dominant",
    "exposure_weighted_heat_load_m_person_c_day": 2322.1,
    "humid_heat_dominance_pass": false,
    "proof_result": "passes_daytime_heat_exposure_rule",
    "regional_heat_load_c_day": 214.0,
    "regional_peak_tmax_c": 46.25,
    "warm_night_ratio": 0.049
  },
  "decisive_evidence": "Accumulated heat load, duration, and exposure scaling carry the mechanism decision; rainfall or image signals only test competing explanations.",
  "formula_derivation": "Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units.",
  "mechanism_chain": [
    "event-window thermal forcing",
    "accumulated heat-load calculation",
    "persistence or recovery constraint",
    "non-heat alternative rejection"
  ],
  "mechanism_question": "separate cumulative heat stress from a single peak-temperature story by combining thermal load, persistence, recovery, and contextual evidence",
  "rejected_simplifications": "Reject peak-only, rainfall-led, and image-primary explanations when the computed heat-load chain is stronger.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `classification`, `exposure_weighted_heat_load_m_person_c_day`, `humid_heat_dominance_pass`, `proof_result`, `regional_heat_load_c_day`, `regional_peak_tmax_c`, `warm_night_ratio`.
3. Use the computed values to build the ordered mechanism chain: event-window thermal forcing -> accumulated heat-load calculation -> persistence or recovery constraint -> non-heat alternative rejection.
4. Weight decisive evidence against alternatives: Accumulated heat load, duration, and exposure scaling carry the mechanism decision; rainfall or image signals only test competing explanations.
5. Reject simpler explanations: Reject peak-only, rainfall-led, and image-primary explanations when the computed heat-load chain is stronger.
6. Keep the interpretation bounded: The result is a package-scale heat mechanism diagnosis, not exact mortality, outage, damage, or full regional attribution.

Formula/scaling note: Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units.

Key computed anchors from the package:

- `exposed_population_m` = `10.85`
- `hazard_days` = `46`
- `max_apparent_temperature_c` = `29.8`
- `max_wet_bulb_c` = `19.83`
- `point_daily_record_count` = `61`
- `regional_mean_tmax_c` = `44.65`
- `thresholds` = `{"apparent_temperature_c": 40.0, "exposed_population_m": 5.0, "exposure_weighted_heat_load_m_person_c_day": 1000.0, "peak_tmax_c": 45.0, "regional_heat_load_c_day": 100.0, "wet_bulb_c": 30.0}`
- `warm_night_count_tmin_ge_16c` = `3`

# Source Paths

- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
