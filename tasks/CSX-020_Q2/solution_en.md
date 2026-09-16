# Correct Answer

```json
{
  "answer": "compound_dry_heat_fire_weather_exposure_supported",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "test whether dry daytime heat and atmospheric dryness dominate the event instead of humid heat, rainfall, or exposure-only context",
  "computed_evidence": {
    "label": "compound_dry_heat_fire_weather_exposure_supported",
    "evidence_score": 6,
    "heat_load_c_days_gt35": 36.9,
    "warm_nights_ge18c": 5,
    "dryness_evidence_synthesis": {
      "peak_vpd_kpa": 7.62,
      "hot_dry_hours": 75,
      "hot_humid_hours": 0
    },
    "exposure_evidence_synthesis": {
      "population": 344722,
      "critical_amenities": 81
    }
  },
  "mechanism_chain": [
    "hot daytime forcing",
    "dry-air or vapor-pressure stress",
    "rainfall moderation check",
    "exposure context"
  ],
  "decisive_evidence": "The strongest evidence is the combination of hot daytime load and dry-air stress, with receptors treated as context rather than the trigger.",
  "rejected_simplifications": "Reject humid-heat dominance, rainfall moderation, and exposure-only explanations when meteorological forcing is stronger.",
  "bounded_interpretation": "The package can diagnose local dry-heat stress but cannot estimate actual fire spread, burned assets, or health outcomes."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `label`, `evidence_score`, `heat_load_c_days_gt35`, `warm_nights_ge18c`, `dryness_evidence_synthesis.peak_vpd_kpa`, `dryness_evidence_synthesis.hot_dry_hours`, `dryness_evidence_synthesis.hot_humid_hours`, `exposure_evidence_synthesis.population`.
3. Use the computed values to build the ordered mechanism chain: hot daytime forcing -> dry-air or vapor-pressure stress -> rainfall moderation check -> exposure context.
4. Weight decisive evidence against alternatives: The strongest evidence is the combination of hot daytime load and dry-air stress, with receptors treated as context rather than the trigger.
5. Reject simpler explanations: Reject humid-heat dominance, rainfall moderation, and exposure-only explanations when meteorological forcing is stronger.
6. Keep the interpretation bounded: The package can diagnose local dry-heat stress but cannot estimate actual fire spread, burned assets, or health outcomes.

Key computed anchors from the package:

- `event_name` = `2019-2020 Australian extreme heat during Black Summer`
- `event_window` = `{"start": "2019-12-01", "end": "2020-01-31", "days": 62}`
- `thresholds` = `{"heat_load_c_days_gt35": 30.0, "warm_nights_ge18c": 3, "peak_vpd_kpa": 6.0, "hot_dry_hours": 24, "hot_humid_hours_max": 1, "population_min": 300000, "critical_amenities_min": 50}`
- `computed_values` = `{"heat_load_c_days_gt35": 36.9, "warm_nights_ge18c": 5, "peak_vpd_kpa": 7.62, "hot_dry_hours": 75, "hot_humid_hours": 0, "population": 344722, "critical_amenities": 81}`
- `test_passes` = `{"heat_load": true, "warm_nights": true, "dry_air": true, "hot_dry": true, "humid_countercheck": true, "exposure": true}`
- `tolerances` = `{"heat_load_c_days_gt35": 0.2, "peak_vpd_kpa": 0.05, "hot_dry_hours": 1, "population": 100}`

# Source Paths

- `metadata/event.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_003_Overpass_small_roads_and_critical_amenities.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
