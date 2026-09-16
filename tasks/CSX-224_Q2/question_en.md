# Rainfall-Runout Coupled Landslide Response Model

Use only the local CSX-224 event package. Select package-relative evidence for every value you use.

Build a compact disaster-science model for the 14 August 2017 Freetown landslide-mudflow that links antecedent rainfall, hillslope/runout mechanics, remote-sensing observability, and emergency response load. The model should distinguish the physical trigger from the urban exposure conditions that amplified consequences.

Return one JSON object with this structure:

```json
{
  "source_paths": [],
  "process_model": {
    "event_window": "",
    "mechanism_chain": [],
    "hazard_classification": ""
  },
  "computed_metrics": {
    "rainfall_loading": {
      "event_day_point_mm": 0,
      "point_rainfall_min_mm": 0,
      "point_rainfall_max_mm": 0,
      "point_rainfall_disagreement_ratio": 0,
      "regional_mean_mm": 0,
      "multi_sensor_mean_mm": 0,
      "point_to_multi_sensor_ratio": 0,
      "reported_period_total_mm": 0,
      "reported_period_norm_ratio": 0,
      "event_day_share_of_period_pct": 0,
      "rainfall_trigger_index": 0
    },
    "hillslope_runout": {
      "runout_km_min": 0,
      "forest_loss_km2": 0,
      "forest_loss_pct": 0,
      "city_growth_ratio": 0,
      "runout_to_aoi_short_side_pct": 0,
      "hillslope_runout_index": 0
    },
    "observability": {
      "radar_scene_balance": 0,
      "radar_mean_change_db": 0,
      "radar_change_to_std_ratio": 0,
      "optical_scene_count_total": 0,
      "event_cloud_fraction": 0,
      "observability_constraint_index": 0
    },
    "response_load": {
      "population_million": 0,
      "reported_deaths": 0,
      "reported_displaced": 0,
      "critical_facility_nodes": 0,
      "school_nodes": 0,
      "major_road_features": 0,
      "waterway_features": 0,
      "response_load_index": 0
    },
    "compound_process_index": 0,
    "risk_state": ""
  },
  "scenario_analysis": {
    "scenario_name": "",
    "assumption_changes": [],
    "scenario_rainfall_trigger_index": 0,
    "scenario_hillslope_runout_index": 0,
    "scenario_response_load_index": 0,
    "scenario_compound_process_index": 0,
    "compound_delta": 0
  },
  "response_priorities": [],
  "final_interpretation": ""
}
```

Use these formulas and rounding rules:

- `multi_sensor_mean_mm` is the mean of the event-day regional rainfall means from the available gridded precipitation products used in the model.
- `event_day_point_mm` is the maximum available event-day point rainfall sample, used as an upper-bound trigger stress value; also report the minimum and maximum point samples and their max/min disagreement ratio.
- `point_to_multi_sensor_ratio = event_day_point_mm / multi_sensor_mean_mm`.
- `event_day_share_of_period_pct = event_day_point_mm / reported_period_total_mm * 100`.
- `rainfall_trigger_index = 100 * (0.40 * min(event_day_point_mm / 300, 1) + 0.25 * min(regional_mean_mm / 150, 1) + 0.25 * min(reported_period_norm_ratio / 4, 1) + 0.10 * min(event_day_share_of_period_pct / 25, 1))`.
- `forest_loss_km2 = forest_area_1986_km2 - forest_area_2015_km2`.
- `forest_loss_pct = forest_loss_km2 / forest_area_1986_km2 * 100`.
- `city_growth_ratio = current_city_population / 1986_city_population`.
- `runout_to_aoi_short_side_pct = runout_km_min / min(aoi_north_south_km, aoi_east_west_km) * 100`.
- `hillslope_runout_index = 100 * (0.30 * topographic_failure_norm + 0.25 * min(runout_km_min / 5, 1) + 0.20 * min(forest_loss_pct / 60, 1) + 0.15 * min(city_growth_ratio / 2.5, 1) + 0.10 * valley_flood_coupling_norm)`, where `topographic_failure_norm` is 1 only if the report supports hillside failure, mountainous terrain, and stream-valley flow, otherwise use the fraction supported; `valley_flood_coupling_norm` is 1 when the source describes the mudflow entering flood-filled valleys, otherwise 0.
- `radar_scene_balance = min(pre_event_radar_count, post_event_radar_count) / max(pre_event_radar_count, post_event_radar_count)`.
- `radar_change_to_std_ratio = abs(radar_mean_change_db) / radar_change_std_db`.
- `observability_constraint_index = 100 * (0.30 * radar_scene_balance + 0.30 * min(abs(radar_mean_change_db) / 1.5, 1) + 0.20 * min(event_cloud_fraction, 1) + 0.20 * optical_gap_norm)`, where `optical_gap_norm` is 1 if there are zero usable optical scenes and 0 otherwise.
- Count `critical_facility_nodes` as hospital, police, fire-station, and shelter nodes in the bounded exposure data.
- Count `major_road_features` as primary, secondary, tertiary, and trunk highway features; count `waterway_features` as stream plus river features.
- `impact_severity_norm = mean(min(reported_deaths / 1200, 1), min(reported_displaced / 4000, 1), min(reported_home_damage_usd_million / 20, 1))`.
- `response_load_index = 100 * (0.22 * min(population / 1500000, 1) + 0.18 * min(critical_facility_nodes / 50, 1) + 0.15 * min(school_nodes / 120, 1) + 0.15 * min(major_road_features / 175, 1) + 0.10 * min(waterway_features / 60, 1) + 0.20 * impact_severity_norm)`.
- `compound_process_index = 0.35 * rainfall_trigger_index + 0.30 * hillslope_runout_index + 0.15 * observability_constraint_index + 0.20 * response_load_index`.
- `risk_state` is `severe_compound_landslide_response_load` when the compound index is at least 75, `elevated_compound_landslide_response_load` for 60 to below 75, and `moderate_compound_landslide_response_load` below 60.

Scenario: recompute the model for a future wet-season stress case in which event-day point rainfall rises by 20%, regional mean rainfall rises by 20%, the period rainfall anomaly rises from 3.0 to 3.6 times normal, dense forest remaining falls to 45 km2, population and mapped exposure features used in the response-load index rise by 20%, and reported impact magnitudes rise by 15%. Keep runout distance, radar/optical conditions, and the AOI dimensions unchanged. Report `compound_delta = scenario_compound_process_index - compound_process_index`.

Round rainfall depths and percentages to 2 decimals, ratios to 2 decimals, counts to integers, and index values to 2 decimals. The `response_priorities` array should contain exactly three concise operational priorities ordered from highest to lowest urgency and grounded in the computed metrics.
