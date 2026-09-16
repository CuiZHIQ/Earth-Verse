# Correct Answer

```json
{
  "process_model": {
    "event_window_days": 1,
    "mechanism_chain": [
      "A one-day rainfall trigger produced a 68.2 mm gridded peak and at least 39.0 mm at the drier point sample.",
      "The triggering rain arrived 21 days after the Thomas Fire, with mean dNBR about 2.95 times the annual surface-change mean.",
      "Debris flows traveled at least 3.0 km along five main runout paths across alluvial fans.",
      "The exposed AOI contains about 120050 people, 52 critical facilities, and 947 mapped road ways, so response load extends beyond the hillslope source area."
    ]
  },
  "computed_metrics": {
    "rainfall_trigger": {
      "grid_peak_product": "GPM",
      "grid_peak_mm": 68.2,
      "grid_peak_mean_mm": 52.1,
      "grid_peak_to_mean_ratio": 1.31,
      "spatial_concentration_product": "CHIRPS",
      "spatial_concentration_ratio": 4.52,
      "point_precip_floor_mm": 39.0,
      "point_precip_ceiling_mm": 62.4,
      "grid_peak_to_point_floor_ratio": 1.75,
      "rainfall_trigger_norm": 0.91
    },
    "burn_scar_conditioning": {
      "fire_lag_days": 21,
      "fire_area_km2": 1140,
      "dnbr_mean": 0.26,
      "dnbr_max": 1.578,
      "annual_change_mean": 0.088,
      "annual_change_max": 0.412,
      "dnbr_mean_to_annual_change_ratio": 2.95,
      "dnbr_max_to_annual_change_ratio": 3.83,
      "burn_conditioning_norm": 0.89
    },
    "runout_and_exposure": {
      "runout_km_min": 3.0,
      "runout_paths": 5,
      "fatalities": 23,
      "homes_damaged_min": 400,
      "population_exposed": 120050,
      "critical_facilities": 52,
      "road_ways": 947,
      "fatalities_per_100k_population": 19.16,
      "critical_facilities_per_100k_population": 43.32,
      "damaged_homes_per_runout_path_min": 80.0,
      "runout_exposure_norm": 0.92,
      "impact_norm": 0.87
    },
    "process_scores": {
      "post_fire_debris_flow_process_index": 90.44,
      "process_label": "very_high_post_fire_debris_flow_coupling",
      "response_priority_score": 82.85,
      "response_priority_label": "high_response_priority"
    }
  },
  "scenario_analysis": {
    "assumptions": {
      "daily_rainfall_multiplier": 1.15,
      "population_multiplier": 1.2,
      "critical_facility_multiplier": 1.25,
      "spatial_pattern_and_reported_impact_held_constant": true
    },
    "scenario_grid_peak_mm": 78.4,
    "scenario_population_exposed": 144060,
    "scenario_critical_facilities": 65.0,
    "scenario_rainfall_trigger_norm": 0.97,
    "scenario_runout_exposure_norm": 0.97,
    "scenario_process_index": 94.06,
    "scenario_response_priority_score": 91.58,
    "process_index_delta": 3.62,
    "response_priority_delta": 8.74,
    "priority_label_shift": "high_response_priority_to_extreme_escalation_priority"
  },
  "source_paths": [
    "data/event_reports/event_reports_001_Locked_anchor_USGS_data_release.html",
    "data/event_reports/event_reports_002_Locked_event_anchor_2018_Montecito_post-fire_debris_flows.json",
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_daily_point_sample.json",
    "data/physical_hazard/physical_hazard_002_NASA_POWER_daily_point_sample.json",
    "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json",
    "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json",
    "data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json",
    "data/exposure_impact/exposure_impact_004_OpenStreetMap_Overpass_bounded_AOI_slice.json"
  ],
  "final_interpretation": "The package supports a very high post-fire debris-flow coupling: intense one-day rainfall arrived only 21 days after the Thomas Fire, burn-scar metrics are much stronger than annual background surface change, and multi-kilometer runout crossed populated alluvial-fan corridors with dense road and critical-facility exposure."
}
```

# Key Computations

The event anchor gives 2018-01-09 to 2018-01-09, so the inclusive event window is `1` day. The report text gives a three-week burn lag, the `1140 km2` Thomas Fire, runout over `3 km`, `5` main runout paths, `23` fatalities, and over `400` damaged homes; conservative lower-bound values are used for runout and damaged homes.

For precipitation, the largest gridded maximum is `68.2 mm`, with same-source mean `52.1 mm`, so `68.2 / 52.1 = 1.31`. The strongest spatial concentration is `62.8 / 13.9 = 4.52`. The two point precipitation samples are `62.4 mm` and `39.0 mm`, giving `68.2 / 39.0 = 1.75`.

For burn conditioning, `dnbr_mean / annual_change_mean = 0.260 / 0.088 = 2.95`, and `dnbr_max / annual_change_max = 1.578 / 0.412 = 3.83`. Critical facilities are counted from amenities tagged `school`, `fire_station`, `hospital`, `police`, or `shelter`; road ways are mapped ways with a `highway` tag.

The baseline normalized components are:

```text
rainfall_trigger_norm = 0.91
burn_conditioning_norm = 0.89
runout_exposure_norm = 0.92
impact_norm = 0.87
post_fire_debris_flow_process_index = 90.44
response_priority_score = 82.85
```

Under the stress scenario, the gridded rainfall peak becomes `78.4 mm`, population becomes `144060`, and critical facilities become `65.0`. This raises the process index to `94.06` and the response-priority score to `91.58`, shifting the priority label from `high_response_priority` to `extreme_escalation_priority`.

# Scoring Rubric

- 3 points: Finds the relevant event report, precipitation, burn-scar, annual-change, population, and map-exposure records, and cites package-relative paths for values used.
- 3 points: Extracts the one-day event window, 21-day burn lag, 1140 km2 fire area, at least 3 km runout, five runout paths, 23 fatalities, and at least 400 damaged homes.
- 3 points: Computes gridded peak rainfall, same-source mean ratio, largest spatial concentration ratio, point rainfall floor/ceiling, grid-to-point ratio, and rainfall-trigger normalization.
- 3 points: Uses dNBR and annual surface-change statistics to compute burn-severity ratios and burn-conditioning normalization.
- 3 points: Counts population, critical facilities, road ways, and impact rates, then derives runout-exposure and impact normalizations.
- 4 points: Applies the specified weighted formulas, reports baseline process and response scores, recomputes the wetter/higher-exposure scenario, and gives deltas and label shift.
- 1 point: Provides valid JSON and a concise mechanism-based interpretation tied to rainfall, burn conditioning, runout, and exposure.
