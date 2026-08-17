# Correct Answer

```json
{
  "answer": "cross_scale_flood_transition_supported",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "reconstruct how rainfall concentration translates into pluvial or urban runoff pressure rather than a generic wet-period label",
  "computed_evidence": {
    "transition_evidence_synthesis": [
      {
        "row_id": "regional_multiday_accumulation",
        "formula": [
          "event_hours = 7 * 24",
          "regional_mean_average_mm = mean(426.100, 256.635, 214.341)",
          "average_max_mean_ratio = mean(product_max_mm / product_mean_mm)"
        ],
        "computed_values": {
          "event_hours": 168,
          "regional_product_means_mm": {
            "gpm_mm": 426.1,
            "chirps_mm": 256.635,
            "era5_land_mm": 214.341
          },
          "regional_mean_average_mm": 299.025,
          "average_max_mean_ratio": 1.185
        },
        "diagnostic_diagnostic_test_result": "pass: all three regional means exceed 200 mm and the ensemble mean is about 299.025 mm",
        "rejected_overread": "regional_accumulation_only"
      },
      {
        "row_id": "zhengzhou_record_burst",
        "formula": [
          "201.9 - 198.5",
          "201.9 / 198.5",
          "201.9 / 23.3"
        ],
        "computed_values": {
          "station_one_hour_mm": 201.9,
          "previous_record_mm": 198.5,
          "record_margin_mm": 3.4,
          "record_ratio": 1.017128,
          "station_to_point_peak_ratio": 8.665
        },
        "diagnostic_diagnostic_test_result": "pass: Zhengzhou exceeded the previous mainland one-hour record",
        "rejected_overread": "point_series_downgrades_station_record"
      },
      {
        "row_id": "point_persistence_and_concentration",
        "formula": [
          "wet_hours / 168",
          "heavy_hours_ge_10mm / 168",
          "max_24h / event_total",
          "max_72h / event_total"
        ],
        "computed_values": {
          "point_event_total_mm": 332.2,
          "wet_hours": 137,
          "wet_hour_fraction": 0.815476,
          "heavy_hours_ge_10mm": 3,
          "heavy_hour_fraction": 0.017857,
          "rolling_24h_mm": 172.5,
          "rolling_24h_fraction": 0.519266,
          "rolling_72h_mm": 283.9,
          "rolling_72h_fraction": 0.854606
        },
        "diagnostic_diagnostic_test_result": "pass: sustained wetness plus strong 24-hour and 72-hour concentration",
        "rejected_overread": "city_burst_only"
      },
      {
        "row_id": "northern_short_duration_context",
        "formula": [
          "260.0 / 2"
        ],
        "computed_values": {
          "xinxiang_two_hour_total_mm": 260.0,
          "xinxiang_rate_mm_per_hour": 130.0
        },
        "diagnostic_diagnostic_test_result": "pass: northern Henan also shows a short-duration extreme",
        "rejected_overread": "meteorological_rarity_only"
      },
      {
        "row_id": "urban_receptor_context",
        "formula": [
          "population_millions = population_sum / 1000000",
          "feature_share = count / 1000"
        ],
        "computed_values": {
          "population_millions": 11.097,
          "highway_share": 0.635,
          "bridge_share": 0.16,
          "critical_amenity_share": 0.055,
          "building_share": 0.296
        },
        "diagnostic_diagnostic_test_result": "pass: dense receptor context is present",
        "rejected_overread": "receptor_density_as_loss_metric"
      },
      {
        "row_id": "surface_change_context",
        "formula": [
          "mean Sentinel-1 VV post-minus-pre dB",
          "mean AlphaEarth annual 1-minus-cosine change"
        ],
        "computed_values": {
          "sentinel_vv_change_db": 0.854,
          "alphaearth_annual_surface_change_mean": 0.0446
        },
        "diagnostic_diagnostic_test_result": "context: nonzero surface-change metrics are present",
        "rejected_overread": "surface_signal_as_depth_or_loss_metric"
      }
    ],
    "rejected_alternatives": [
      "city_burst_only",
      "regional_accumulation_only",
      "point_series_downgrades_station_record",
      "receptor_density_as_loss_metric",
      "surface_signal_as_depth_or_loss_metric",
      "meteorological_rarity_only"
    ],
    "final_process_alignment_label": "cross_scale_flood_transition_consistent"
  },
  "mechanism_chain": [
    "rainfall burst or accumulation",
    "duration/intensity or areal-load calculation",
    "urban runoff or receptor context",
    "single-number simplification rejection"
  ],
  "decisive_evidence": "Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.",
  "rejected_simplifications": "Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.",
  "bounded_interpretation": "The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `transition_evidence_synthesis`, `rejected_alternatives`, `final_process_alignment_label`.
3. Use the computed values to build the ordered mechanism chain: rainfall burst or accumulation -> duration/intensity or areal-load calculation -> urban runoff or receptor context -> single-number simplification rejection.
4. Weight decisive evidence against alternatives: Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.
5. Reject simpler explanations: Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.
6. Keep the interpretation bounded: The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals.

Key computed anchors from the package:

- `event_hours` = `168`
- `station_one_hour_mm` = `201.9`
- `previous_record_mm` = `198.5`
- `record_margin_mm` = `3.4`
- `record_ratio` = `1.017128`
- `point_event_total_mm` = `332.2`
- `point_max_hourly_mm` = `23.3`
- `point_max_time` = `2021-07-20T02:00`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_July_2021_Henan_Zhengzhou_extreme_rainfall_and_flood.json`
- `data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Flooding_in_Central_China.html`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`
- `data/physical_hazard/physical_hazard_005_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_007_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_009_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_006_OpenStreetMap_Overpass_bounded_AOI_slice.json`
- `data/remote_sensing/remote_sensing_004_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/remote_sensing/remote_sensing_006_Sentinel-1_GRD_VV_pre_post_change.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
