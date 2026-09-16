# Correct Answer

```json
{
  "answer": "derna_flood_wave_amplification_supported",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "connect rainfall or report anchors to a localized dam-area cascade and downstream flood-wave pathway",
  "computed_evidence": {
    "derivation_evidence_synthesis": [
      {
        "row_id": "rainfall_persistence",
        "formula": "local_wettest_24h_mm/local_hourly_total_mm; local_wettest_6h_mm/local_hourly_total_mm; local_longest_wet_run_hours/local_wet_hours_ge_0p1mm",
        "computed_value": {
          "wettest_24h_share_of_local_total": 0.976,
          "wettest_6h_share_of_local_total": 0.547,
          "longest_wet_run_share_of_wet_hours": 0.906
        },
        "diagnostic_diagnostic_test_or_test": "24h share near-total, 6h share above one-half, wet-run share above 0.9",
        "result": "local rainfall was concentrated and persistent enough to support a rainfall trigger"
      },
      {
        "row_id": "cross_source_rainfall_support",
        "formula": "regional_gridded_max_mm/contrasting_gridded_max_mm; regional_gridded_mean_mm/reanalysis_mean_mm; independent_daily_total_mm/local_hourly_total_mm; regional_gridded_max_mm/local_wettest_24h_mm",
        "computed_value": {
          "regional_to_contrasting_max_ratio": 24.95,
          "regional_to_reanalysis_mean_ratio": 1.41,
          "independent_daily_to_local_total_ratio": 1.6,
          "regional_max_to_local_24h_ratio": 2.05,
          "reported_rainfall_range_mm": [
            150,
            240
          ],
          "reported_al_bayda_daily_record_mm": 414.1
        },
        "diagnostic_diagnostic_test_or_test": "independent and regional rainfall support exceed local-only and contrasting-grid explanations",
        "result": "multiple rainfall sources support a severe regional rainfall trigger, but regional rain alone does not prove neighborhood losses"
      },
      {
        "row_id": "flood_wave_depth_amplification",
        "formula": "regional_gridded_max_mm/1000; reported_wave_height_m_min/regional_rain_depth_m to reported_wave_height_m_max/regional_rain_depth_m",
        "computed_value": {
          "regional_rain_depth_m": 0.15044,
          "wave_to_regional_rain_depth_ratio_range": [
            19.94,
            46.53
          ],
          "independent_daily_depth_m": 0.12033,
          "wave_to_independent_daily_depth_ratio_range": [
            24.93,
            58.17
          ]
        },
        "diagnostic_diagnostic_test_or_test": "reported 3-7 m wave is tens of times the event rainfall depth",
        "result": "direct rainfall depth or urban ponding alone is not sufficient; flood-wave amplification through dam failure is required"
      },
      {
        "row_id": "wadi_dam_exposure_coupling",
        "formula": "bridge_features + destroyed_highway_features + waterway_features; exposed_population/linear_infrastructure_marker_count",
        "computed_value": {
          "long_narrow_wadi_reported": true,
          "two_dams_collapsed": true,
          "second_dam_distance_km": 1,
          "linear_infrastructure_marker_count": 12,
          "exposure_context_per_linear_marker": 4676.1,
          "exposed_population": 56113.05,
          "reported_derna_population_context": 90000
        },
        "diagnostic_diagnostic_test_or_test": "routing and dam facts true, with nonzero linear infrastructure and population context",
        "result": "the confined wadi, nearby second dam, and exposed infrastructure context support a routed flood-wave pathway"
      },
      {
        "row_id": "remote_disturbance_context",
        "formula": "radar pre/post counts and post-minus-pre VV mean; annual embedding change maximum",
        "computed_value": {
          "radar_pre_count": 18,
          "radar_post_count": 14,
          "radar_vv_post_minus_pre_db_mean": -1.108,
          "radar_vv_post_minus_pre_db_min": -10.254,
          "radar_vv_post_minus_pre_db_max": 8.505,
          "embedding_annual_change_mean": 0.0175,
          "embedding_annual_change_max": 0.2047
        },
        "diagnostic_diagnostic_test_or_test": "surface-change context may support disturbance but cannot replace the hydraulic process alignment check",
        "result": "remote metrics are supporting context only"
      }
    ],
    "rejected_overreads": [
      "direct pluvial or urban ponding alone cannot explain a 3-7 m wave that is tens of times the rainfall depth",
      "coastal setting or exposure alone does not supply the upstream wadi and two-dam amplification chain",
      "regional rainfall maxima cannot be transferred directly into neighborhood loss ranks",
      "image summaries do not establish exact breach time, outflow hydrograph, parcel depth, casualty attribution, final death toll, or building-by-building structural loss"
    ],
    "final_process_alignment_label": "rainfall_triggered_dam_breach_flood_wave_supported"
  },
  "mechanism_chain": [
    "storm or rainfall loading",
    "dam-area pathway or storage release",
    "downstream flood-wave amplification",
    "regional-rainfall-only rejection"
  ],
  "decisive_evidence": "The mechanism must connect forcing with pathway amplification; rainfall magnitude alone is not a complete explanation.",
  "rejected_simplifications": "Reject regional-rainfall-only or exposure-only explanations if they do not explain the cascade pathway.",
  "bounded_interpretation": "Do not estimate breach hydrographs, exact wave heights, engineering fault, or complete loss totals unless sourced.",
  "formula_derivation": "When amplification is used, express it as a ratio or difference between upstream forcing and downstream response indicators."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `derivation_evidence_synthesis`, `rejected_overreads`, `final_process_alignment_label`.
3. Use the computed values to build the ordered mechanism chain: storm or rainfall loading -> dam-area pathway or storage release -> downstream flood-wave amplification -> regional-rainfall-only rejection.
4. Weight decisive evidence against alternatives: The mechanism must connect forcing with pathway amplification; rainfall magnitude alone is not a complete explanation.
5. Reject simpler explanations: Reject regional-rainfall-only or exposure-only explanations if they do not explain the cascade pathway.
6. Keep the interpretation bounded: Do not estimate breach hydrographs, exact wave heights, engineering fault, or complete loss totals unless sourced.

Formula/scaling note: When amplification is used, express it as a ratio or difference between upstream forcing and downstream response indicators.

Key computed anchors from the package:

- `rainfall` = `{"local_hourly_total_mm": 75.2, "local_wettest_1h_mm": 9.3, "local_wettest_6h_mm": 41.1, "local_wettest_24h_mm": 73.4, "local_wet_hours_ge_0p1mm": 32, "local_longest_wet_run_hours": 29, "local_hourly_record_hours": 48, "independent_daily_to`
- `reported` = `{"wmo_rainfall_range_mm": [150, 240], "wmo_al_bayda_daily_record_mm": 414.1, "two_dams_collapsed": true, "long_narrow_wadi": true, "second_dam_distance_km": 1, "flood_wave_height_m_range": [3, 7], "derna_population_context": 90000}`
- `exposure_context` = `{"exposed_population": 56113.05, "linear_features": {"elements": 1000, "highway_features": 968, "major_road_features": 57, "destroyed_highway_features": 3, "bridge_features": 6, "amenity_features": 6, "school_features": 2, "police_features"`
- `remote_sensing` = `{"radar_pre_count": 18, "radar_post_count": 14, "radar_vv_post_minus_pre_db_mean": -1.108, "radar_vv_post_minus_pre_db_min": -10.254, "radar_vv_post_minus_pre_db_max": 8.505, "embedding_annual_change_mean": 0.0175, "embedding_annual_change_`

# Source Paths

- `metadata/event.json`
- `data/event_catalogs/event_catalogs_001_GDACS_event_list_GeoJSON_API.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_Storm_Daniel_Derna_flood.json`
- `data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Storm_aftermath_in_Derna_Libya.html`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`
- `data/physical_hazard/physical_hazard_004_NASA_POWER_daily_point_weather_API.json`
- `data/physical_hazard/physical_hazard_005_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_006_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json`
- `data/remote_sensing/remote_sensing_004_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/remote_sensing/remote_sensing_005_Sentinel-1_GRD_VV_pre_post_change.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
