# Correct Answer

```json
{
  "answer": "elevation_stratified_marginal_basin_snow_and_mountain_snow",
  "bounded_interpretation": "The answer should not estimate exact snowpack volume, road closures, or complete infrastructure losses.",
  "computed_evidence": {
    "basin_metrics": {
      "below0_h": 0,
      "fdh_c_h": 0.0,
      "gust_kmh": 75.6,
      "min_t_c": 2.0,
      "snow_cm": 0.77,
      "snow_h": 3,
      "wind_chill_c": -0.1
    },
    "decision_rule": "Zero subfreezing hours and 0.0 C h at 90 m reject sustained basin freezing, but do not reject brief wet or mixed snow there or deep snow at 5000-7000 ft.",
    "process_alignment_result": "consistent",
    "report_metrics": {
      "downtown_rain_in": 4,
      "la_crescenta_snow_in": 2,
      "snow_5000_6000ft_ft": [
        1,
        3
      ],
      "snow_7000ft_ft": 8
    }
  },
  "decisive_evidence": "Thermal persistence, phase partition, and elevation contrast should outweigh image brightness or isolated precipitation values.",
  "formula_derivation": "Use a phase-partition argument: compare temperature or snow-level evidence with elevation context to explain divergent basin and mountain response.",
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
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `basin_metrics.below0_h`, `basin_metrics.fdh_c_h`, `basin_metrics.gust_kmh`, `basin_metrics.min_t_c`, `basin_metrics.snow_cm`, `basin_metrics.snow_h`, `basin_metrics.wind_chill_c`, `decision_rule`.
3. Use the computed values to build the ordered mechanism chain: event-window cold or storm anchor -> temperature and phase calculation -> elevation or wind context -> warm-rain or image-only rejection.
4. Weight decisive evidence against alternatives: Thermal persistence, phase partition, and elevation contrast should outweigh image brightness or isolated precipitation values.
5. Reject simpler explanations: Reject uniform warm-rain, uniform lowland-snow, or image-only explanations if the computed phase structure is stratified.
6. Keep the interpretation bounded: The answer should not estimate exact snowpack volume, road closures, or complete infrastructure losses.

Formula/scaling note: Use a phase-partition argument: compare temperature or snow-level evidence with elevation context to explain divergent basin and mountain response.

Key computed anchors from the package:

- `basin_metrics` = `{"below0_h": 0, "fdh_c_h": 0.0, "gust_kmh": 75.6, "min_t_c": 2.0, "snow_cm": 0.77, "snow_h": 3, "wind_chill_c": -0.1}`
- `diagnostic_point` = `{"elevation_m": 90.0, "latitude": 34.059753, "longitude": -118.2375}`
- `report_metrics` = `{"beverley_hills_rain_in": 6, "downtown_rain_in": 4, "la_crescenta_snow_in": 2, "snow_5000_6000ft_ft": [1, 3], "snow_7000ft_ft": 8}`
- `timing_checks` = `{"longest_snowfall_run_h": 2, "max_gust_time": "2023-02-25T02:00", "min_temperature_time": "2023-02-26T03:00", "min_wind_chill_time": "2023-02-24T01:00"}`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_February_2023_Southern_California_winter_storm.json`
- `data/event_reports/event_reports_004_01_Locked_package_evidence_report.html.html`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive_cold_variables.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
