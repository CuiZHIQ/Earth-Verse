# Correct Answer

```json
{
  "answer": "dry_daytime_heat_dominant",
  "bounded_interpretation": "The package can diagnose local dry-heat stress but cannot estimate actual fire spread, burned assets, or health outcomes.",
  "computed_evidence": {
    "decision_rule": "dry true, humid false, persistent false -> dry_daytime_heat_dominant",
    "expected_values": {
      "exposure_load_million_person_C": 50.48,
      "peak_daily_apparent_c": 29.8,
      "peak_wet_bulb_c": 19.83,
      "regional_mean_tmax_c": 44.65,
      "regional_peak_tmax_c": 46.25,
      "warm_night_count": 3,
      "warm_night_max_run_days": 1
    },
    "failed_alternative": "humid_or_persistent_warm_night_dominance",
    "flags": {
      "dry_heat_extreme": true,
      "humid_heat_extreme": false,
      "persistent_warm_nights": false
    },
    "tolerances": {
      "apparent_c": 0.3,
      "exposure_load_million_person_C": 0.3,
      "regional_temperature_c": 0.5,
      "wet_bulb_c": 0.3
    }
  },
  "decisive_evidence": "The strongest evidence is the combination of hot daytime load and dry-air stress, with receptors treated as context rather than the trigger.",
  "mechanism_chain": [
    "hot daytime forcing",
    "dry-air or vapor-pressure stress",
    "rainfall moderation check",
    "exposure context"
  ],
  "mechanism_question": "test whether dry daytime heat and atmospheric dryness dominate the event instead of humid heat, rainfall, or exposure-only context",
  "rejected_simplifications": "Reject humid-heat dominance, rainfall moderation, and exposure-only explanations when meteorological forcing is stronger.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `decision_rule`, `expected_values.exposure_load_million_person_C`, `expected_values.peak_daily_apparent_c`, `expected_values.peak_wet_bulb_c`, `expected_values.regional_mean_tmax_c`, `expected_values.regional_peak_tmax_c`, `expected_values.warm_night_count`, `expected_values.warm_night_max_run_days`.
3. Use the computed values to build the ordered mechanism chain: hot daytime forcing -> dry-air or vapor-pressure stress -> rainfall moderation check -> exposure context.
4. Weight decisive evidence against alternatives: The strongest evidence is the combination of hot daytime load and dry-air stress, with receptors treated as context rather than the trigger.
5. Reject simpler explanations: Reject humid-heat dominance, rainfall moderation, and exposure-only explanations when meteorological forcing is stronger.
6. Keep the interpretation bounded: The package can diagnose local dry-heat stress but cannot estimate actual fire spread, burned assets, or health outcomes.

Key computed anchors from the package:

- `daily_wet_bulb_ge_20c_days` = `0`
- `event_name` = `2015 India-Pakistan heat wave`
- `expected_values` = `{"exposure_load_million_person_C": 50.48, "peak_daily_apparent_c": 29.8, "peak_wet_bulb_c": 19.83, "regional_mean_tmax_c": 44.65, "regional_peak_tmax_c": 46.25, "warm_night_count": 3, "warm_night_max_run_days": 1}`
- `final_label` = `dry_daytime_heat_dominant`
- `flags` = `{"dry_heat_extreme": true, "humid_heat_extreme": false, "persistent_warm_nights": false}`
- `peak_daily_apparent_date` = `2015-06-19`
- `peak_wet_bulb_time` = `2015-06-19T18:00`
- `population_millions` = `10.849`

# Source Paths

- `metadata/event.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
