# Correct Answer

```json
{
  "answer": "arid_pluvial_runoff_scale_consistent",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "reconstruct how rainfall concentration translates into pluvial or urban runoff pressure rather than a generic wet-period label",
  "computed_evidence": {
    "rainfall_ratios": {
      "eastern_less_than_24h_mm": 250.0,
      "dubai_airport_daily_mm": 119.0,
      "annual_midpoint_mm": 170.0,
      "eastern_less_than_24h_to_annual_midpoint": 1.47,
      "dubai_airport_daily_to_annual_midpoint": 0.7,
      "airport_to_eastern_less_than_24h": 0.48,
      "result": "short_window_load_exceeds_annual_midpoint"
    },
    "runoff_equivalent": [
      {
        "coefficient": 0.05,
        "runoff_depth_mm": 12.5,
        "runoff_volume_m3_per_km2": 12500.0
      },
      {
        "coefficient": 0.15,
        "runoff_depth_mm": 37.5,
        "runoff_volume_m3_per_km2": 37500.0
      },
      {
        "coefficient": 0.3,
        "runoff_depth_mm": 75.0,
        "runoff_volume_m3_per_km2": 75000.0
      }
    ],
    "scale_concentration": {
      "gridded_event_max_mm": 56.76,
      "gridded_event_mean_mm": 7.088,
      "gridded_max_to_mean": 8.01,
      "report_short_window_to_gridded_max": 4.4,
      "report_short_window_to_gridded_mean": 35.27,
      "result": "scale_mismatch_context_not_report_refutation"
    },
    "surface_change": {
      "radar_pre_count": 44,
      "radar_post_count": 39,
      "radar_scene_count_change_pct": -11.36,
      "radar_post_minus_pre_db_mean": 0.524,
      "embedding_change_mean": 0.0216,
      "embedding_change_max": 0.2791,
      "result": "surface_change_context_not_depth_calibration"
    },
    "population_normalized_midrunoff": {
      "mapped_population": 632943.1,
      "population_thousands": 632.94,
      "runoff_volume_c015_m3_per_km2": 37500.0,
      "runoff_volume_c015_m3_per_km2_per_1000_people": 59.25,
      "result": "population_normalizer_not_observed_loss"
    },
    "final_label": "arid_pluvial_runoff_scale_consistent",
    "rejected_substitutions": [
      "airport_only_denominator",
      "gridded_downgrade_of_report_rainfall",
      "surface_signal_depth_calibration",
      "population_normalizer_as_loss_total",
      "slow_routing_primary_process"
    ]
  },
  "mechanism_chain": [
    "rainfall burst or accumulation",
    "duration/intensity or areal-load calculation",
    "urban runoff or receptor context",
    "single-number simplification rejection"
  ],
  "decisive_evidence": "Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.",
  "rejected_simplifications": "Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.",
  "bounded_interpretation": "The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals.",
  "formula_derivation": "When converting rainfall to runoff pressure, use V = rainfall_mm / 1000 * area_m2 and explain any runoff coefficient or normalized index."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `rainfall_ratios.eastern_less_than_24h_mm`, `rainfall_ratios.dubai_airport_daily_mm`, `rainfall_ratios.annual_midpoint_mm`, `rainfall_ratios.eastern_less_than_24h_to_annual_midpoint`, `rainfall_ratios.dubai_airport_daily_to_annual_midpoint`, `rainfall_ratios.airport_to_eastern_less_than_24h`, `rainfall_ratios.result`, `runoff_equivalent`.
3. Use the computed values to build the ordered mechanism chain: rainfall burst or accumulation -> duration/intensity or areal-load calculation -> urban runoff or receptor context -> single-number simplification rejection.
4. Weight decisive evidence against alternatives: Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.
5. Reject simpler explanations: Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.
6. Keep the interpretation bounded: The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals.

Formula/scaling note: When converting rainfall to runoff pressure, use V = rainfall_mm / 1000 * area_m2 and explain any runoff coefficient or normalized index.

Key computed anchors from the package:

- `rainfall_ratios` = `{"eastern_less_than_24h_mm": 250.0, "dubai_airport_daily_mm": 119.0, "annual_midpoint_mm": 170.0, "eastern_less_than_24h_to_annual_midpoint": 1.47, "dubai_airport_daily_to_annual_midpoint": 0.7, "airport_to_eastern_less_than_24h": 0.48, "re`
- `scale_concentration` = `{"gridded_event_max_mm": 56.76, "gridded_event_mean_mm": 7.088, "gridded_max_to_mean": 8.01, "report_short_window_to_gridded_max": 4.4, "report_short_window_to_gridded_mean": 35.27, "result": "scale_mismatch_context_not_report_refutation"}`
- `surface_change` = `{"radar_pre_count": 44, "radar_post_count": 39, "radar_scene_count_change_pct": -11.36, "radar_post_minus_pre_db_mean": 0.524, "embedding_change_mean": 0.0216, "embedding_change_max": 0.2791, "result": "surface_change_context_not_depth_cali`
- `population_normalized_midrunoff` = `{"mapped_population": 632943.1, "population_thousands": 632.94, "runoff_volume_c015_m3_per_km2": 37500.0, "runoff_volume_c015_m3_per_km2_per_1000_people": 59.25, "result": "population_normalizer_not_observed_loss"}`
- `report_rainfall_anchors` = `{"eastern_less_than_24h_mm": 250.0, "dubai_airport_daily_mm": 119.0, "annual_low_mm": 140.0, "annual_high_mm": 200.0, "annual_midpoint_mm": 170.0, "jaxa_single_day_wide_area_threshold_mm": 100.0}`
- `answer_type` = `five_part_numeric_diagnostic`
- `tolerances` = `{"ratios": 0.02, "percentages": 0.05, "runoff_depth_mm": 0.1, "runoff_volume_m3_per_km2": 1.0, "embedding": 0.0002}`
- `decision_state` = `consistent_if_all_five_sections_pass`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_April_2024_UAE_and_Dubai_record_rainfall_flood.json`
- `data/event_reports/event_reports_004_01_Locked_package_evidence_report.html.html`
- `data/event_reports/event_reports_005_03_JAXA_GSMaP_quick_report_-_UAE_extreme_heavy_rainfall.html.html`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/remote_sensing/remote_sensing_005_Sentinel-1_GRD_VV_pre_post_change.json`
- `data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
