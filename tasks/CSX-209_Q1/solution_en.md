# Correct Answer

```json
{
  "answer": "severe_co_haze_exposure_with_partial_rain_clearing",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "diagnose whether pollutant or aerosol burden persists over a receptor window after accounting for meteorology and removal modifiers",
  "computed_evidence": {
    "pollutant_load": {
      "usual_co_ppb": 100,
      "peak_co_ppb": 1300,
      "co_multiplier": 13.0,
      "co_excess_ppb": 1200
    },
    "meteo_clearing": {
      "meteo_start": "2015-09-01",
      "meteo_end": "2015-10-16",
      "meteo_days": 46,
      "rain_clearing_fraction": 0.674,
      "weak_wind_fraction": 0.761,
      "dry_stagnation_fraction": 0.261
    },
    "visibility_proxy": {
      "gray_haze_delta_pp": 7.86,
      "mean_luminance_delta": 6.09
    },
    "exposure_index": {
      "population": 410885,
      "co_population_index": 53.42,
      "compound_exposure_index": 72.65
    },
    "diagnostic_diagnostic_tests": {
      "co_severe": true,
      "visual_haze_increase": true,
      "large_compound_exposure": true,
      "partial_rain_clearing": true
    },
    "final_label": "severe_co_haze_exposure_with_partial_rain_clearing"
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
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `pollutant_load.usual_co_ppb`, `pollutant_load.peak_co_ppb`, `pollutant_load.co_multiplier`, `pollutant_load.co_excess_ppb`, `meteo_clearing.meteo_start`, `meteo_clearing.meteo_end`, `meteo_clearing.meteo_days`, `meteo_clearing.rain_clearing_fraction`.
3. Use the computed values to build the ordered mechanism chain: pollutant or aerosol burden -> transport/stagnation duration -> rain or ventilation modifier -> receptor-context interpretation.
4. Weight decisive evidence against alternatives: Burden, duration, and receptor context carry the diagnosis; precipitation or surface products are modifiers or counterchecks.
5. Reject simpler explanations: Reject ordinary-weather, rain-dominated, local-heat, or surface-change explanations if they fail to explain the receptor burden.
6. Keep the interpretation bounded: Do not infer individual dose, clinical outcomes, emissions inventory, or source apportionment beyond the package.

Key computed anchors from the package:

- `pollutant_load` = `{"usual_co_ppb": 100, "peak_co_ppb": 1300, "co_multiplier": 13.0, "co_excess_ppb": 1200}`
- `meteo_clearing` = `{"daily_span_start": "2015-09-01", "daily_span_end": "2015-10-16", "meteo_days": 46, "rain_clearing_days": 31, "weak_wind_days": 35, "dry_stagnation_days": 12, "rain_clearing_fraction": 0.6739130434782609, "weak_wind_fraction": 0.7608695652`
- `visibility_proxy` = `{"pre_image": {"valid_fraction": 0.8697357177734375, "mean_luminance": 102.16847908004235, "gray_haze_fraction": 0.4541834067264338, "bright_fraction": 0.26932782446475667, "low_contrast_fraction": 0.9390603343918315}, "event_image": {"vali`
- `exposure_index` = `{"population": 410884.77942285844, "co_population_index": 53.4150213249716, "compound_exposure_index": 72.6454074133291}`
- `thresholds` = `{"co_severe": true, "visual_haze_increase": true, "large_compound_exposure": true, "partial_rain_clearing": true}`
- `final_label` = `severe_co_haze_exposure_with_partial_rain_clearing`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_September-October_2015_Singapore_haze_from_Indonesian_peat_and_forest.json`
- `data/event_reports/event_reports_001_Locked_anchor_report_NASA_Earth_Observatory.html`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_daily_weather_fill.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/remote_sensing/remote_sensing_002_pre.jpg`
- `data/remote_sensing/remote_sensing_003_event.jpg`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
