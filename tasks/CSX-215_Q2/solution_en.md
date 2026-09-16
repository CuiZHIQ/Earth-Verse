# Correct Answer

```json
{
  "answer": "haze_window_exposure_supported",
  "bounded_interpretation": "Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package.",
  "computed_evidence": {
    "computed_consequence": "dry_window_with_quantified_exposure_context",
    "diagnostic_tests": {
      "dry_guardrail": true,
      "exposure_slice_diagnostic_test": true,
      "report_pct_diagnostic_test": true,
      "window_match": true
    },
    "evidence_score": 4,
    "metrics": {
      "amenity_total": 69,
      "event_days": 5,
      "low_precip_products": 3,
      "people_per_amenity": 32462.7,
      "precip_max_mm": 0.335,
      "spike_mid_pct": 25.0
    }
  },
  "decisive_evidence": "Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.",
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
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `computed_consequence`, `diagnostic_tests.dry_guardrail`, `diagnostic_tests.exposure_slice_diagnostic_test`, `diagnostic_tests.report_pct_diagnostic_test`, `diagnostic_tests.window_match`, `evidence_score`, `metrics.amenity_total`, `metrics.event_days`.
3. Use the computed values to build the ordered mechanism chain: pollutant or aerosol burden -> transport/stagnation duration -> rain or ventilation modifier -> receptor-context interpretation.
4. Weight decisive evidence against alternatives: Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.
5. Reject simpler explanations: Reject ordinary-weather, rain-dominated, local-heat, or surface-change explanations if they fail to explain the receptor burden.
6. Keep the interpretation bounded: Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package.

Key computed anchors from the package:

- `amenity_counts` = `{"fire_stations": 7, "hospitals": 24, "police": 28, "schools": 10}`
- `event_name` = `January 2013 Beijing-Tianjin-Hebei severe haze episode`
- `event_window` = `{"end_date": "2013-01-14", "start_date": "2013-01-10"}`
- `hazard_family` = `air_pollution_smoke_heat`
- `population_sum` = `2239926`
- `precipitation_inputs_mm` = `{"chirps_mean": 0.0, "chirps_min": 0.0, "era5_mean": 0.00604, "era5_min": 0.00584, "gpm_mean": 0.335466, "gpm_min": 0.0}`
- `precipitation_windows_match` = `True`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_anchor_report_NASA_Earth_Observatory.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_January_2013_Beijing-Tianjin-Hebei_severe_haze_episode.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_003_OpenStreetMap_Overpass_bounded_AOI_slice.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
