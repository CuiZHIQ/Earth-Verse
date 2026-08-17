# Monsoon-Typhoon Runoff and Access-Response Stress Model

Use only the local CSX-285 event package. Select package-relative evidence for every value you use, and combine multiple independent evidence streams where they are scientifically useful.

Build a compact disaster-science model for the September 2024 interaction between Typhoon Yagi and the southwest monsoon. The goal is to reconstruct whether the event produced an extreme compound runoff and access-response stress state, then test a wetter counterfactual. Treat mapped exposure, population, AOI, and remote-sensing values as package-derived operational indicators for this model, while keeping report-derived impact counts tied to the early AHA situation update represented in the package.

Use these definitions:

- `duration_days` is the inclusive count from the package event start date to end date.
- Treat the event-accumulated IMERG precipitation product as the primary satellite rainfall field, CHIRPS as an independent daily rainfall field, and ERA5-Land as the reanalysis rainfall field.
- `rainfall_loading_norm = clip(0.5 * (IMERG_mean_mm / 150) + 0.3 * (CHIRPS_mean_mm / 120) + 0.2 * (ERA5_Land_mean_mm / 100), 0, 1)`.
- `peak_concentration_norm = clip((IMERG_max_mm / IMERG_mean_mm - 1) / 4, 0, 1)`.
- `waterway_norm = clip(mapped_waterway_features / 250, 0, 1)`.
- `terrain_process_norm = 1.0` if the event narrative supports flash floods, landslides, and runoff or hillside-waterway-lowland sensitivity; `0.5` if it supports only two of those process elements; otherwise `0.0`.
- `hydro_trigger_index = 100 * (0.45 * rainfall_loading_norm + 0.20 * peak_concentration_norm + 0.20 * waterway_norm + 0.15 * terrain_process_norm)`.
- `road_bridge_sections_affected = reported_road_sections_affected + reported_bridge_sections_affected`.
- `implied_impassable_sections = road_bridge_sections_affected * (1 - reported_passable_pct / 100)`.
- `road_bridge_norm = clip(road_bridge_sections_affected / 200, 0, 1)`.
- `affected_norm = clip(reported_affected_people / 2500000, 0, 1)`.
- `displaced_norm = clip(reported_displaced_people / 50000, 0, 1)`.
- `critical_service_norm = clip(mapped_critical_amenities / 500, 0, 1)`, where critical amenities are schools, hospitals, shelters, police stations, and fire stations in the mapped exposure slice.
- `impassable_norm = clip(implied_impassable_sections / 60, 0, 1)`.
- `access_response_index = 100 * (0.30 * road_bridge_norm + 0.25 * affected_norm + 0.20 * displaced_norm + 0.15 * critical_service_norm + 0.10 * impassable_norm)`.
- `compound_priority_index = 0.60 * hydro_trigger_index + 0.40 * access_response_index`.
- Priority bands are `extreme` for `compound_priority_index >= 90`, `very_high` for `80-<90`, `high` for `70-<80`, and `moderate` below 70.

For the counterfactual, increase all three precipitation means and the IMERG maximum by 15%, increase reported displaced people by 20%, and reduce the passable share of affected road and bridge sections to 65%. Keep mapped exposure counts and reported affected population fixed. Recompute the indices and priority band.

Return one JSON object with this structure:

```json
{
  "process_model": {
    "event_window": {
      "start_date": "<YYYY-MM-DD>",
      "end_date": "<YYYY-MM-DD>",
      "duration_days": <integer>
    },
    "mechanism_chain": ["<3-5 concise process steps>"]
  },
  "computed_metrics": {
    "rainfall": {
      "imerg_mean_mm": <number>,
      "imerg_max_mm": <number>,
      "chirps_mean_mm": <number>,
      "chirps_max_mm": <number>,
      "era5_land_mean_mm": <number>,
      "era5_land_max_mm": <number>,
      "ensemble_mean_mm": <number>,
      "imerg_daily_mean_mm_day": <number>,
      "imerg_peak_to_mean_ratio": <number>,
      "chirps_to_imerg_mean_ratio": <number>,
      "era5_to_imerg_mean_ratio": <number>
    },
    "exposure_and_impact": {
      "affected_people": <integer>,
      "displaced_people": <integer>,
      "evacuation_centres": <integer>,
      "road_bridge_sections_affected": <integer>,
      "reported_passable_pct": <number>,
      "implied_impassable_sections": <number>,
      "mapped_road_features": <integer>,
      "mapped_waterway_features": <integer>,
      "mapped_critical_amenities": <integer>,
      "worldpop_population_context": <integer>
    },
    "surface_context": {
      "annual_embedding_cosine_change_mean": <number>,
      "annual_embedding_cosine_change_max": <number>,
      "interpretation_constraint": "<short caution about what this can and cannot prove>"
    }
  },
  "baseline_indices": {
    "rainfall_loading_norm": <number>,
    "peak_concentration_norm": <number>,
    "waterway_norm": <number>,
    "terrain_process_norm": <number>,
    "hydro_trigger_index": <number>,
    "road_bridge_norm": <number>,
    "affected_norm": <number>,
    "displaced_norm": <number>,
    "critical_service_norm": <number>,
    "impassable_norm": <number>,
    "access_response_index": <number>,
    "compound_priority_index": <number>,
    "priority_band": "<band>"
  },
  "scenario_analysis": {
    "scenario_imerg_mean_mm": <number>,
    "scenario_imerg_max_mm": <number>,
    "scenario_displaced_people": <integer>,
    "scenario_impassable_sections": <number>,
    "scenario_hydro_trigger_index": <number>,
    "scenario_access_response_index": <number>,
    "scenario_compound_priority_index": <number>,
    "scenario_delta_index_points": <number>,
    "scenario_priority_band": "<band>"
  },
  "response_priorities": [
    {"rank": 1, "focus": "<actionable operational focus>", "reason": "<computed evidence>"},
    {"rank": 2, "focus": "<actionable operational focus>", "reason": "<computed evidence>"},
    {"rank": 3, "focus": "<actionable operational focus>", "reason": "<computed evidence>"}
  ],
  "source_paths": ["<package-relative path>", "..."],
  "final_interpretation": "<one concise synthesis sentence>"
}
```

Round rainfall values and indices to one decimal place, ratios and normalized terms to three decimals unless a field is naturally an integer.
