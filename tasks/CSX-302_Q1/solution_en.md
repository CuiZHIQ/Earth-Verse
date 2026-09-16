# Correct Answer

```json
{
  "answer": "receptor_dust_signal_consistent",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "diagnose whether pollutant or aerosol burden persists over a receptor window after accounting for meteorology and removal modifiers",
  "computed_evidence": {
    "image_signal": {
      "dci_delta": 0.036578,
      "blue_drop_pp": 1.22
    },
    "confounders": {
      "pt_precip_mm": 3.3,
      "max_temp_c": 30.903,
      "surf_mean": 0.0251
    },
    "receptor_context": {
      "days": 15,
      "population": 49269.915
    },
    "component_evidence_scores": {
      "duration": 1.0,
      "image": 1.0,
      "blue": 1.0,
      "population": 0.985,
      "dry": 0.67,
      "surface": 0.498
    },
    "dust_receptor_index": 93.97,
    "diagnostic_diagnostic_test_result": {
      "passed_diagnostic_tests": 8,
      "label": "receptor_dust_signal_consistent"
    }
  },
  "mechanism_chain": [
    "pollutant or aerosol burden",
    "transport/stagnation duration",
    "rain or ventilation modifier",
    "receptor-context interpretation"
  ],
  "decisive_evidence": "Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.",
  "rejected_simplifications": "Reject ordinary-weather, rain-dominated, local-heat, or surface-change explanations if they fail to explain the receptor burden.",
  "bounded_interpretation": "Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package.",
  "formula_derivation": "Use an exposure-window concept: burden proxy times duration, with rain or ventilation acting as a removal/moderation term."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `image_signal.dci_delta`, `image_signal.blue_drop_pp`, `confounders.pt_precip_mm`, `confounders.max_temp_c`, `confounders.surf_mean`, `receptor_context.days`, `receptor_context.population`, `component_evidence_scores.duration`.
3. Use the computed values to build the ordered mechanism chain: pollutant or aerosol burden -> transport/stagnation duration -> rain or ventilation modifier -> receptor-context interpretation.
4. Weight decisive evidence against alternatives: Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.
5. Reject simpler explanations: Reject ordinary-weather, rain-dominated, local-heat, or surface-change explanations if they fail to explain the receptor burden.
6. Keep the interpretation bounded: Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package.

Formula/scaling note: Use an exposure-window concept: burden proxy times duration, with rain or ventilation acting as a removal/moderation term.

Key computed anchors from the package:

- `pre_image` = `{"width": 1024, "height": 768, "dci": 1.138175, "blue_water_fraction": 0.01863, "valid_fraction": 0.95554}`
- `event_image` = `{"width": 1024, "height": 768, "dci": 1.174754, "blue_water_fraction": 0.006413, "valid_fraction": 0.96123}`
- `unrounded` = `{"dci_delta": 0.036578471184026906, "blue_drop_pp": 1.2217203776041667, "point_precip_mm": 3.3000000000000003, "max_temp_c": 30.902993774414085, "surface_mean": 0.02507693877338612, "population": 49269.914585497914, "dust_receptor_index": 9`
- `gates` = `{"days_ge_14": true, "dci_delta_ge_0_03": true, "blue_drop_pp_ge_1": true, "point_precip_mm_le_5": true, "max_temp_c_lt_35": true, "surface_mean_le_0_05": true, "population_ge_10000": true, "dri_ge_75": true}`
- `formulas` = `{"dci": "mean((R+G)/(2*max(B,1))) for pixels with 20<mean(R,G,B)<245", "blue_water_fraction": "count(B>R+15 and B>G+5 and B>80)/all_pixels", "duration": "clip(window_days/14)", "image": "clip(dci_delta/0.03)", "blue": "clip(blue_drop_pp/1.0`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_June_2020_Saharan_dust_outbreak_to_Caribbean_and_U.S.json`
- `data/remote_sensing/remote_sensing_005_pre.jpg`
- `data/remote_sensing/remote_sensing_006_event.jpg`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/physical_hazard/physical_hazard_001_NASA_POWER_daily_point_sample.json`
- `data/physical_hazard/physical_hazard_002_Open-Meteo_archive_point_sample.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
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
