# Correct Answer

```json
{
  "answer": "smoke_health_exposure_window",
  "bounded_interpretation": "Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package.",
  "computed_evidence": {
    "computed_consequence": "10/10 smoke-health score using gridded heat, precipitation consensus, large exposure, and low surface-change counter-scores.",
    "diagnostic_tests": {
      "dry_window": true,
      "hazard_family": true,
      "heat_context": true,
      "low_rainfall": true,
      "low_surface_change": true,
      "population": true,
      "report_text": true
    },
    "evidence_scores": {
      "burnscar_map": 0,
      "heat_only": 2,
      "rainfall_or_flood": 0,
      "smoke_health": 10
    },
    "metrics": {
      "dnbr_mean": -0.1268,
      "embedding_change_mean": 0.0215,
      "era5_tmax_max_c": 40.5,
      "era5_tmax_mean_c": 36.6,
      "exposed_population": 3703791,
      "precip_consensus_mean_mm": 12.8,
      "window_days": 16
    },
    "window": "2021-03-26/2021-04-10"
  },
  "decisive_evidence": "Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.",
  "formula_derivation": "Use an exposure-window concept: burden proxy times duration, with rain or ventilation acting as a removal/moderation term.",
  "mechanism_chain": [
    "pollutant or aerosol burden",
    "transport/stagnation duration",
    "rain or ventilation modifier",
    "receptor-context interpretation"
  ],
  "mechanism_question": "diagnose whether pollutant or aerosol burden persists over a receptor window after accounting for meteorology and removal modifiers",
  "rejected_simplifications": "Reject ordinary-weather, rain-dominated, local-heat, or surface-change explanations if they fail to explain the receptor burden.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `computed_consequence`, `diagnostic_tests.dry_window`, `diagnostic_tests.hazard_family`, `diagnostic_tests.heat_context`, `diagnostic_tests.low_rainfall`, `diagnostic_tests.low_surface_change`, `diagnostic_tests.population`, `diagnostic_tests.report_text`.
3. Use the computed values to build the ordered mechanism chain: pollutant or aerosol burden -> transport/stagnation duration -> rain or ventilation modifier -> receptor-context interpretation.
4. Weight decisive evidence against alternatives: Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.
5. Reject simpler explanations: Reject ordinary-weather, rain-dominated, local-heat, or surface-change explanations if they fail to explain the receptor burden.
6. Keep the interpretation bounded: Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package.

Formula/scaling note: Use an exposure-window concept: burden proxy times duration, with rain or ventilation acting as a removal/moderation term.

Key computed anchors from the package:

- `event_name` = `Kathmandu wildfire smoke air pollution episode`
- `flood_wording_present` = `False`
- `hazard_family` = `air_pollution_smoke_heat`
- `icimod_text_hits` = `7`
- `nasa_text_hits` = `4`
- `precipitation_means_mm` = `{"chirps": 19.388, "era5": 6.97, "gpm": 12.136}`
- `scoring_formula` = `1*hazard + 2*report_text + 2*dry_window + 1*heat_context + 2*population + 1*low_rainfall + 1*low_surface_change`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_Kathmandu_wildfire_smoke_air_pollution_episode.json`
- `data/event_reports/event_reports_004_Locked_anchor_report_ICIMOD.html`
- `data/other/other_001_NASA_Earth_Observatory_A_Fierce_Fire_Season_in_Nepal.html`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
