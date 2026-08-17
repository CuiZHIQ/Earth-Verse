# Correct Answer

```json
{
  "answer": "compound_atmospheric_stress_pass",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "diagnose whether pollutant or aerosol burden persists over a receptor window after accounting for meteorology and removal modifiers",
  "computed_evidence": {
    "event_days": 9,
    "heat_load_c_day": 22.025,
    "peak_heat_margin_c": 0.426,
    "ventilation_ratio": 0.817,
    "airborne_alignment_count": 3,
    "final_label": "compound_atmospheric_stress_pass"
  },
  "mechanism_chain": [
    "pollutant or aerosol burden",
    "transport/stagnation duration",
    "rain or ventilation modifier",
    "receptor-context interpretation"
  ],
  "decisive_evidence": "Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.",
  "rejected_simplifications": "Reject ordinary-weather, rain-dominated, local-heat, or surface-change explanations if they fail to explain the receptor burden.",
  "bounded_interpretation": "Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `event_days`, `heat_load_c_day`, `peak_heat_margin_c`, `ventilation_ratio`, `airborne_alignment_count`, `final_label`.
3. Use the computed values to build the ordered mechanism chain: pollutant or aerosol burden -> transport/stagnation duration -> rain or ventilation modifier -> receptor-context interpretation.
4. Weight decisive evidence against alternatives: Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.
5. Reject simpler explanations: Reject ordinary-weather, rain-dominated, local-heat, or surface-change explanations if they fail to explain the receptor burden.
6. Keep the interpretation bounded: Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package.

Key computed anchors from the package:

- `temporal_window` = `{"start_date": "2023-07-17", "end_date": "2023-07-25", "event_days_inclusive": 9}`
- `temperature` = `{"tmax_peak_c": 30.426049804687523, "tmax_mean_c": 27.447185522912548, "heat_load_c_day": 22.024669706212933, "peak_heat_margin_c": 0.42604980468752274}`
- `wind` = `{"u10_mean_ms": 2.429117360672204, "v10_mean_ms": 0.3208548912675745, "mean_wind_vector_ms": 2.450216115604789, "ventilation_ratio": 0.8167387052015963}`
- `airborne_flags` = `{"heat_report_flag": 1, "dust_forecast_date": "2023-07-19", "dust_forecast_inside_window_flag": 1, "wildfire_article_flag": 1, "smoke_anchor_flag": 1, "wildfire_smoke_flag": 1, "airborne_alignment_count": 3, "text_scope": "Heat and dust are`
- `competing_metric_ratios` = `{"precipitation_peak_to_mean_ratio": 2.7671752338448368, "burn_change_peak_to_mean_ratio": 11.26366511922435, "annual_surface_change_peak_to_mean_ratio": 14.969275042515314}`
- `threshold_tests` = `{"heat_load_pass": true, "peak_heat_pass": true, "low_ventilation_pass": true, "airborne_alignment_pass": true}`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_anchor_report_Copernicus_Atmosphere.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_Mediterranean_heatwave_wildfire_smoke_and_dust_episode.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_009_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
