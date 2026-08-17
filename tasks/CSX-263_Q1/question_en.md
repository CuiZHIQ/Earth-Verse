# Peat-Fire Haze Process Stress and Response Priority Model

Using only the local package, reconstruct a process-based response-priority model for the 2015 Indonesian drought, peat fires, and cross-border haze. Your final answer must cite package-relative evidence for every evidence family you use.

Use the event narrative to explain the physical pathway: El Nino-amplified drying, peat combustion, smoke and carbon monoxide transport, and downwind receptor exposure. Then compute the numeric model below from local package data.

Definitions:

- `clip01(x) = max(0, min(1, x))`
- Use the full available point-weather daily series for antecedent plus fire-season drying.
- Use the event start through the last common available date in the gridded hazard products for overlap wind and coverage calculations.
- Treat a low-rain day as point daily precipitation `<= 1 mm/day`.
- Count critical services in the OSM slice as amenities tagged `school`, `shelter`, `hospital`, `police`, or `fire_station`.
- Count network elements as OSM elements tagged `highway` plus elements tagged `waterway`.
- A Sentinel dNBR scene pair is ready only if both the pre-event and post-event counts are at least 1.

Compute these baseline terms:

```text
dry_persistence_norm =
clip01(0.40 * (dry_day_share_pct / 50)
     + 0.30 * (longest_low_rain_run_days / 10)
     + 0.30 * (1 - min(mean_point_precip_mm_day / 5, 1)))

rainfall_structure_norm =
0.40 * clip01(mean(GPM_CV, CHIRPS_CV) / 0.5)
+ 0.35 * mean(1 - min(GPM_min_mm / 50, 1),
              1 - min(CHIRPS_min_mm / 50, 1))
+ 0.25 * (1 - min(gridded_mean_gap_pct / 25, 1))

GPM_CV = GPM_stdDev_mm / GPM_mean_mm
CHIRPS_CV = CHIRPS_stdDev_mm / CHIRPS_mean_mm
gridded_mean_gap_pct =
100 * abs(GPM_mean_mm - CHIRPS_mean_mm) / mean(GPM_mean_mm, CHIRPS_mean_mm)

heat_transport_norm =
0.65 * clip01((regional_tmax_max_c - regional_tmax_mean_c) / 10)
+ 0.35 * clip01(mean_overlap_point_wind_mps / 6)

receptor_load_norm =
0.35 * clip01(WorldPop_population / 600000)
+ 0.30 * clip01(critical_service_count / 400)
+ 0.20 * clip01(network_element_count / 600)
+ 0.15 * clip01(population_per_osm_element / 600)

observability_constraint_norm = 1 - scene_pair_ready

compound_haze_response_priority =
100 * (0.30 * dry_persistence_norm
     + 0.20 * rainfall_structure_norm
     + 0.15 * heat_transport_norm
     + 0.25 * receptor_load_norm
     + 0.10 * observability_constraint_norm)
```

Also compute a warmer-drier higher-exposure scenario:

- Multiply point-weather precipitation by `0.85`.
- Scale gridded precipitation amounts by `0.85`; this leaves product CV and mean-gap terms unchanged but changes the low-rain tail term.
- Add `2.0 C` to the regional heat-tail term.
- Multiply overlap mean wind by `1.10`.
- Multiply exposed population by `1.10`; leave OSM counts and Sentinel scene availability unchanged.
- Recompute the same indices and report `priority_delta = scenario_priority - baseline_priority`.

Return only valid JSON with this schema:

```json
{
  "process_model": {
    "event": "",
    "mechanism": "",
    "baseline_priority": 0.0,
    "scenario_priority": 0.0,
    "priority_delta": 0.0
  },
  "evidence_scope": {
    "point_weather": "",
    "gridded_hazard_products": "",
    "receptor_load_products": "",
    "remote_sensing": ""
  },
  "computed_metrics": {
    "event_window": "",
    "event_days": 0,
    "hazard_overlap_window": "",
    "hazard_overlap_days": 0,
    "coverage_fraction_pct": 0.0,
    "point_weather_days": 0,
    "low_rain_threshold_mm_day": 0.0,
    "dry_day_share_pct": 0.0,
    "longest_low_rain_run_days": 0,
    "longest_low_rain_run_start": "",
    "longest_low_rain_run_end": "",
    "mean_point_precip_mm_day": 0.0,
    "heat_tail_c": 0.0,
    "mean_overlap_wind_mps": 0.0,
    "gpm_precip_cv": 0.0,
    "chirps_precip_cv": 0.0,
    "gridded_mean_gap_pct": 0.0,
    "gpm_low_tail_norm": 0.0,
    "chirps_low_tail_norm": 0.0,
    "scene_pair_ready": 0,
    "sentinel_pre_count": 0,
    "sentinel_post_count": 0,
    "population_sum": 0.0,
    "osm_element_count": 0,
    "critical_service_count": 0,
    "network_element_count": 0,
    "pop_per_osm_element": 0.0
  },
  "baseline_indices": {
    "dry_persistence_index": 0.0,
    "rainfall_structure_index": 0.0,
    "heat_transport_index": 0.0,
    "receptor_load_index": 0.0,
    "observability_constraint_index": 0.0,
    "compound_haze_response_priority": 0.0
  },
  "scenario_analysis": {
    "scenario_name": "warmer_drier_higher_exposure",
    "dry_persistence_index": 0.0,
    "rainfall_structure_index": 0.0,
    "heat_transport_index": 0.0,
    "receptor_load_index": 0.0,
    "compound_haze_response_priority": 0.0,
    "priority_delta": 0.0
  },
  "mechanism_chain": [],
  "source_paths": [],
  "final_interpretation": ""
}
```
