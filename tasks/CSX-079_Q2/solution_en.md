# Final Answer

Correct answer: `moisture_transport_terrain_official_burden_chain_consistent`.

```json
{
  "target_family": "central_chile_flood_uncertainty_propagation",
  "uncertainty_propagation": [
    {
      "evidence_stream": "rainfall_duration_load",
      "computed_values": {
        "event_precip_total_mm": 133.8,
        "wet_hours": 78,
        "longest_wet_run_hours": 69,
        "max_1h_precip_mm": 6.8,
        "max_72h_precip_mm": 132.9,
        "max_1h_share_of_total": 0.0508,
        "max_72h_share_of_total": 0.9933,
        "max_72h_to_max_1h_ratio": 19.54,
        "max_wind_speed_kmh": 30.6
      },
      "robust_conclusion": "The rainfall signal is a sustained multi-day load, not a one-hour burst.",
      "uncertainty_limit": "Hourly values constrain timing at one point and do not by themselves map flood depth.",
      "rejected_alternative": "hourly_cloudburst_controls_chain"
    },
    {
      "evidence_stream": "terrain_amplification",
      "computed_values": {
        "el_paico_rain_mm_nearly": 80,
        "foothills_rain_mm_as_much_as": 370,
        "foothill_to_valley_ratio": 4.625,
        "orographic_multiplier_claim_range": [5, 10],
        "snow_meters_reported_at_least": 2,
        "annual_precipitation_from_atmospheric_rivers_percent_range": [45, 60],
        "regions_named": ["Maule", "Nuble", "Biobio"]
      },
      "robust_conclusion": "The terrain contrast is strong enough to support orographic amplification of the moist-flow rainfall load.",
      "uncertainty_limit": "The point ratio and reported multiplier describe terrain contrast, not basin-wide uniform rainfall.",
      "rejected_alternative": "uniform_point_rainfall_or_snowmelt_dominance"
    },
    {
      "evidence_stream": "official_people_burden",
      "computed_values": {
        "deaths": 3,
        "sheltered": 1265,
        "isolated": 42392,
        "evacuated": 31863,
        "official_people_burden": 75520,
        "isolated_to_evacuated_ratio": 1.33
      },
      "robust_conclusion": "Official people counts document a large burden consistent with the rainfall-terrain chain.",
      "uncertainty_limit": "These are reported burden counts and do not replace the physical rainfall mechanism.",
      "rejected_alternative": "official_counts_replace_rainfall_mechanism"
    },
    {
      "evidence_stream": "official_housing_alert_burden",
      "computed_values": {
        "homes_damaged_or_destroyed_total": 21885,
        "homes_severe_or_destroyed": 2813,
        "homes_severe_or_destroyed_share": 0.1285,
        "homes_under_evaluation": 1509,
        "emergency_alert_activations": 170
      },
      "robust_conclusion": "Housing and alert counts support a broad official burden context.",
      "uncertainty_limit": "They are administrative counts, not a direct hydrologic trigger or depth observation.",
      "rejected_alternative": "official_counts_replace_rainfall_mechanism"
    },
    {
      "evidence_stream": "surface_change_context",
      "computed_values": {
        "event_minus_pre_brown_water_fraction": 0.1087,
        "event_minus_pre_brown_water_percentage_points": 10.87,
        "event_minus_pre_bright_cloud_or_snow_fraction": 0.0211,
        "event_minus_pre_blue_water_fraction": -0.0077,
        "sentinel1_post_minus_pre_db_mean": -0.2497,
        "sentinel1_pre_count": 6,
        "sentinel1_post_count": 8,
        "alphaearth_annual_change_mean": 0.0624
      },
      "robust_conclusion": "Surface-change metrics provide contextual support for disturbed wet surfaces.",
      "uncertainty_limit": "Image fractions and radar differences do not directly quantify flood depth or losses.",
      "rejected_alternative": "imagery_quantifies_depth_or_loss"
    },
    {
      "evidence_stream": "exposure_context",
      "computed_values": {
        "compact_study_area_population_sum": 56343.3,
        "osm_element_count": 1000
      },
      "robust_conclusion": "Exposure layers describe receptors near the study area.",
      "uncertainty_limit": "Exposure layers are denominator context and not observed losses.",
      "rejected_alternative": "exposure_layers_measure_observed_losses"
    }
  ],
  "evidence_stream_checks": [
    {"row_id": "rainfall_duration_load", "computed_values": {"event_precip_total_mm": 133.8, "wet_hours": 78, "longest_wet_run_hours": 69, "max_72h_share_of_total": 0.9933}, "pass_fail": "pass", "rejected_alternative": "hourly_cloudburst_controls_chain"},
    {"row_id": "terrain_amplification", "computed_values": {"foothill_to_valley_ratio": 4.625, "orographic_multiplier_claim_range": [5, 10]}, "pass_fail": "pass", "rejected_alternative": "uniform_point_rainfall_or_snowmelt_dominance"},
    {"row_id": "official_people_burden", "computed_values": {"official_people_burden": 75520, "isolated_to_evacuated_ratio": 1.33}, "pass_fail": "context_pass", "rejected_alternative": "official_counts_replace_rainfall_mechanism"},
    {"row_id": "official_housing_alert_burden", "computed_values": {"homes_damaged_or_destroyed_total": 21885, "homes_severe_or_destroyed_share": 0.1285, "emergency_alert_activations": 170}, "pass_fail": "context_pass", "rejected_alternative": "official_counts_replace_rainfall_mechanism"},
    {"row_id": "surface_change_context", "computed_values": {"event_minus_pre_brown_water_percentage_points": 10.87, "sentinel1_post_minus_pre_db_mean": -0.2497}, "pass_fail": "context_pass", "rejected_alternative": "imagery_quantifies_depth_or_loss"},
    {"row_id": "exposure_context", "computed_values": {"compact_study_area_population_sum": 56343.3, "osm_element_count": 1000}, "pass_fail": "context_pass", "rejected_alternative": "exposure_layers_measure_observed_losses"}
  ],
  "fragile_links": [
    "surface_change_context cannot be converted into flood depth",
    "exposure_context cannot be converted into observed losses"
  ],
  "final_consistency_label": "moisture_transport_terrain_official_burden_chain_consistent"
}
```

# Key Computations

Rainfall totals are `133.8 mm` across `78` wet hours, with a `69 h` longest wet run. The `72 h` window contains `132.9 / 133.8 = 0.9933` of the event total, while the strongest hour contributes only `6.8 / 133.8 = 0.0508`. The foothill-to-valley rainfall ratio is `370 / 80 = 4.625`.

Official people burden is `1265 + 42392 + 31863 = 75520`, and the isolated-to-evacuated ratio is `42392 / 31863 = 1.33`. Housing burden totals `19072 + 2789 + 24 = 21885`, with severe or destroyed share `(2789 + 24) / 21885 = 0.1285`. Brown-water fraction rises by `0.2447 - 0.1360 = 0.1087`, or `10.87` percentage points.

# Reasoning Path

The robust part of the explanation is the rainfall-duration, terrain-amplification, and official-burden chain. The fragile parts are the image and exposure streams: they support context but cannot be promoted into flood depth, road failure, housing loss, or observed population loss. The final label is therefore a bounded consistency result, not an image-derived damage estimate.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the required uncertainty-propagation structure, six evidence streams, six stream checks, fragile links, and final label. Partial credit for the right label with one missing stream.
- 4 points: Computes rainfall duration/load values correctly: total, wet hours, longest wet run, peak windows, peak shares, 72 h/1 h ratio, and wind context. Partial credit for correct totals with one missing ratio.
- 3 points: Computes terrain amplification and report context correctly, including the 4.625 foothill/valley ratio and 5-10x multiplier range. Partial credit for the ratio without the multiplier context.
- 4 points: Computes official people and housing burden values correctly. Partial credit for either people or housing arithmetic alone.
- 3 points: Computes surface and exposure context values correctly while keeping their role bounded. Partial credit for correct image values without the exposure context.
- 2 points: Rejects the five overinterpretations using evidence-specific limits. Partial credit for at least three correct rejections.
- 1 point: Keeps the answer concise and does not turn context layers into loss, depth, or response claims.
