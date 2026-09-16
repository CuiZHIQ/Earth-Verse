# Correct Answer

```json
{
  "answer": "sustained_freezing_cold",
  "bounded_interpretation": "The answer should not estimate exact snowpack volume, road closures, or complete infrastructure losses.",
  "computed_evidence": {
    "decision_rule": "label sustained_freezing_cold when daily run >= 3 days and hourly freezing run >= 48 hours",
    "diagnostic_diagnostic_test_tests": {
      "brief_cold_anomaly_pass": false,
      "snow_ice_primary_pass": false,
      "sustained_freezing_pass": true,
      "wind_chill_only_pass": false
    },
    "evidence_synthesis": {
      "daily_below_freezing_run_days": 3,
      "event_snowfall_cm": 9.87,
      "freezing_degree_hours_c_h": 177.4,
      "freezing_run_hours": 60,
      "heating_degree_days_base18c": 124.2,
      "min_tmin_c": -6.3,
      "min_wind_chill_c": -17.1,
      "wind_chill_amplification_c": 10.8
    },
    "tolerances": {
      "degree_hours": 1.0,
      "run_hours": 1,
      "snow_cm": 0.1,
      "temperature_c": 0.3
    }
  },
  "decisive_evidence": "Thermal persistence, phase partition, and elevation contrast should outweigh image brightness or isolated precipitation values.",
  "mechanism_chain": [
    "event-window cold or storm anchor",
    "temperature and phase calculation",
    "elevation or wind context",
    "warm-rain or image-only rejection"
  ],
  "mechanism_question": "determine whether the record supports persistent cold or elevation-stratified snow response rather than a brief visual snow proxy",
  "rejected_simplifications": "Reject uniform warm-rain, uniform lowland-snow, or image-only explanations if the computed phase structure is stratified.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `decision_rule`, `diagnostic_diagnostic_test_tests.brief_cold_anomaly_pass`, `diagnostic_diagnostic_test_tests.snow_ice_primary_pass`, `diagnostic_diagnostic_test_tests.sustained_freezing_pass`, `diagnostic_diagnostic_test_tests.wind_chill_only_pass`, `evidence_synthesis.daily_below_freezing_run_days`, `evidence_synthesis.event_snowfall_cm`, `evidence_synthesis.freezing_degree_hours_c_h`.
3. Use the computed values to build the ordered mechanism chain: event-window cold or storm anchor -> temperature and phase calculation -> elevation or wind context -> warm-rain or image-only rejection.
4. Weight decisive evidence against alternatives: Thermal persistence, phase partition, and elevation contrast should outweigh image brightness or isolated precipitation values.
5. Reject simpler explanations: Reject uniform warm-rain, uniform lowland-snow, or image-only explanations if the computed phase structure is stratified.
6. Keep the interpretation bounded: The answer should not estimate exact snowpack volume, road closures, or complete infrastructure losses.

Key computed anchors from the package:

- `answer` = `sustained_freezing_cold`
- `brief_cold_anomaly_pass` = `False`
- `daily_below_freezing_run_days` = `3`
- `event_snowfall_cm` = `9.87`
- `freezing_degree_hours_c_h` = `177.4`
- `freezing_run_hours` = `60`
- `heating_degree_days_base18c` = `124.2`
- `min_tmin_c` = `-6.3`

# Source Paths

- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive_cold_variables.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
