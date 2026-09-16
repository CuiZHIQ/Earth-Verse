# Correct Answer

```json
{
  "answer": "compound_rainfall_load_localized_slope_failure_with_population_context",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "diagnose whether local mass movement or obstruction evidence dominates over simple rainfall or image-change explanations",
  "computed_evidence": {
    "rows": [
      {
        "row_id": "rainfall_load_gate",
        "formula": [
          "event_day_mean_mm = mean(65.60, 82.08)",
          "four_day_mean_mm = mean(389.10, 340.73)"
        ],
        "computed": {
          "event_day_mean_mm": 73.84,
          "four_day_mean_mm": 364.92,
          "event_day_margin_mm": 23.84,
          "four_day_margin_mm": 114.92
        },
        "diagnostic_test_result": "pass_compound_rainfall_load",
        "points": 2
      },
      {
        "row_id": "antecedent_load_gate",
        "formula": [
          "four_day_to_event_day_ratio = four_day_mean_mm / event_day_mean_mm",
          "event_day_share = event_day_mean_mm / four_day_mean_mm"
        ],
        "computed": {
          "four_day_to_event_day_ratio": 4.942,
          "event_day_share": 0.202
        },
        "diagnostic_test_result": "pass_multiday_antecedent_load",
        "points": 1
      },
      {
        "row_id": "surface_extent_gate",
        "formula": [
          "dnbr_local_to_mean_ratio = dnbr_max / dnbr_mean",
          "radar_abs_max_db = max(abs(radar_max_db), abs(radar_min_db))",
          "embedding_max_to_mean_ratio = embedding_max / embedding_mean"
        ],
        "computed": {
          "dnbr_max": 1.3848,
          "dnbr_mean": 0.0271,
          "dnbr_local_to_mean_ratio": 51.031,
          "radar_abs_max_db": 18.835,
          "radar_mean_db": 0.03,
          "embedding_max_to_mean_ratio": 14.467
        },
        "diagnostic_test_result": "pass_localized_high_contrast_disturbance",
        "points": 2
      },
      {
        "row_id": "exposure_context_gate",
        "formula": [
          "population_millions = mapped_population / 1000000"
        ],
        "computed": {
          "mapped_population": 6761902,
          "population_millions": 6.762
        },
        "diagnostic_test_result": "pass_population_context_not_loss",
        "points": 1
      }
    ],
    "process_alignment_evidence_score": 6,
    "evidence_score_max": 6,
    "final_label": "compound_rainfall_load_localized_slope_failure_with_population_context",
    "rejected_substitutions": [
      "event_day_only_spike",
      "broad_uniform_surface_damage",
      "exposure_as_loss_count",
      "image_only_diagnosis"
    ]
  },
  "mechanism_chain": [
    "mass-movement event anchor",
    "local obstruction or slope-response signal",
    "weather countercheck",
    "simple-trigger rejection"
  ],
  "decisive_evidence": "Mass-movement and obstruction evidence should dominate; precipitation and remote-sensing fields are modifiers or checks.",
  "rejected_simplifications": "Reject rainfall-only, exposure-only, or image-only explanations if the local slope or obstruction pathway is required.",
  "bounded_interpretation": "Do not infer exact failure volume, runout path, geotechnical plane, or all downstream impacts."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `rows`, `process_alignment_evidence_score`, `evidence_score_max`, `final_label`, `rejected_substitutions`.
3. Use the computed values to build the ordered mechanism chain: mass-movement event anchor -> local obstruction or slope-response signal -> weather countercheck -> simple-trigger rejection.
4. Weight decisive evidence against alternatives: Mass-movement and obstruction evidence should dominate; precipitation and remote-sensing fields are modifiers or checks.
5. Reject simpler explanations: Reject rainfall-only, exposure-only, or image-only explanations if the local slope or obstruction pathway is required.
6. Keep the interpretation bounded: Do not infer exact failure volume, runout path, geotechnical plane, or all downstream impacts.

Key computed anchors from the package:

- `event_date` = `2021-07-03`
- `event_day_point_precip_mm` = `{"open_meteo_mm": 65.6, "nasa_power_mm": 82.08}`
- `four_day_point_precip_totals_mm` = `{"open_meteo_mm": 389.1, "nasa_power_mm": 340.73}`
- `rainfall_metrics` = `{"event_day_mean_mm": 73.84, "four_day_mean_mm": 364.92, "event_day_margin_mm": 23.84, "four_day_margin_mm": 114.92, "four_day_to_event_day_ratio": 4.942, "event_day_share": 0.202}`
- `gridded_precip_context` = `{"event_maxima_mm": {"era5_land_max_mm": 65.1, "gpm_max_mm": 23.06, "chirps_max_mm": 74.74}, "mean_of_product_maxima_mm": 54.3, "max_to_min_product_ratio": 3.241, "products_with_max_at_least_50mm": 2}`
- `surface_extent_metrics` = `{"dnbr_max": 1.3848, "dnbr_mean": 0.0271, "dnbr_local_to_mean_ratio": 51.031, "radar_abs_max_db": 18.835, "radar_mean_db": 0.03, "embedding_max_to_mean_ratio": 14.467}`
- `exposure_context` = `{"mapped_population": 6761902, "population_millions": 6.762}`
- `consistency_score` = `6`

# Source Paths

- `metadata/event.json`
- `metadata/files.csv`
- `data/event_reports/event_reports_004_Locked_event_anchor_Atami_debris_flow.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_daily_weather_fill.json`
- `data/physical_hazard/physical_hazard_002_NASA_POWER_daily_weather_fill.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/remote_sensing/remote_sensing_004_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/remote_sensing/remote_sensing_005_Sentinel-1_GRD_VV_pre_post_change.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
