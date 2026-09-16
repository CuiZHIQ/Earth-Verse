# Correct Answer

```json
{
  "answer": "localized_dam_area_cascade_consistent",
  "bounded_interpretation": "Do not estimate breach hydrographs, exact wave heights, engineering fault, or complete loss totals unless sourced.",
  "computed_evidence": {
    "decision_rule": "consistent if score >= 4 and areal rainfall agreement plus process flags pass",
    "evidence_score": 5,
    "final_label": "localized_dam_area_cascade_consistent",
    "max_evidence_score": 5,
    "required_rows": [
      "local_damage_concentration",
      "service_damage_per_impacted_village",
      "areal_rainfall_agreement",
      "point_weather_contrast",
      "dam_cascade_process_flags"
    ],
    "tolerances": {
      "count": 0,
      "percent": 0.1,
      "ratio": 0.01
    }
  },
  "decisive_evidence": "The mechanism must connect forcing with pathway amplification; rainfall magnitude alone is not a complete explanation.",
  "mechanism_chain": [
    "storm or rainfall loading",
    "dam-area pathway or storage release",
    "downstream flood-wave amplification",
    "regional-rainfall-only rejection"
  ],
  "mechanism_question": "connect rainfall or report anchors to a localized dam-area cascade and downstream flood-wave pathway",
  "rejected_simplifications": "Reject regional-rainfall-only or exposure-only explanations if they do not explain the cascade pathway.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `decision_rule`, `evidence_score`, `final_label`, `max_evidence_score`, `required_rows`, `tolerances.count`, `tolerances.percent`.
3. Use the computed values to build the ordered mechanism chain: storm or rainfall loading -> dam-area pathway or storage release -> downstream flood-wave amplification -> regional-rainfall-only rejection.
4. Weight decisive evidence against alternatives: The mechanism must connect forcing with pathway amplification; rainfall magnitude alone is not a complete explanation.
5. Reject simpler explanations: Reject regional-rainfall-only or exposure-only explanations if they do not explain the cascade pathway.
6. Keep the interpretation bounded: Do not estimate breach hydrographs, exact wave heights, engineering fault, or complete loss totals unless sourced.

Key computed anchors from the package:

- `destroyed_village_share` = `0.286`
- `event_window_days` = `24`
- `final_label` = `localized_dam_area_cascade_consistent`
- `gpm_chirps_mean_agreement_pct` = `99.06`
- `gpm_max_to_nasa_power_wettest_day_ratio` = `15.91`
- `gpm_mean_to_nasa_power_total_ratio` = `2.988`
- `gpm_mean_to_open_meteo_total_ratio` = `46.985`
- `local_severe_to_wider_impacted_ratio` = `0.161`

# Source Paths

- `data/event_reports/event_reports_003_Locked_event_anchor_2024_Sudan_floods_and_Arba_at_Dam_flood.json`
- `data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Floods_swamp_Sudan.html`
- `data/other/other_001_UN_Geneva_OCHA_-_Flooding_from_Sudan_dam_collapse_worsens_humanitarian_crisis.html`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`
- `data/physical_hazard/physical_hazard_004_NASA_POWER_daily_point_weather_API.json`
- `data/physical_hazard/physical_hazard_005_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_007_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_009_CHIRPS_daily_event_accumulated_precipitation.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
