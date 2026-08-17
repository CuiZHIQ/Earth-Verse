# Sahel Heat-Stress Persistence and Response-Load Model

Use only the local event package for `CSX-018`. Select package-relative evidence for every value you use.

Reconstruct the five-day March-April 2024 Sahel heat episode as an operational heat-stress problem, combining event narrative, local hourly heat data, gridded hazard summaries, population exposure, mapped critical services and roads, geospatial context, and remote-sensing surface-change context.

Compute Stull wet-bulb temperature for each hourly air-temperature and relative-humidity pair:

```text
T_w = T atan(0.151977 sqrt(RH + 8.313659)) + atan(T + RH)
      - atan(RH - 1.676331) + 0.00391838 RH^1.5 atan(0.023101 RH)
      - 4.686035
```

Use these derived quantities:

- `hours_apparent_ge40c`: count of hourly apparent-temperature values at or above 40.0 C.
- `apparent_degree_hours_ge40c`: sum of `max(apparent_temperature_c - 40.0, 0)` across the event window.
- `warm_night_count`: count of event-window daily minimum temperatures at or above 27.0 C.
- `aoi_area_km2`: approximate polygon area from the package AOI using 111.32 km per longitude degree times `cos(mean_latitude)` and 110.574 km per latitude degree.
- `school_count`: mapped OSM elements with `amenity=school`.
- `health_facility_count`: mapped OSM elements with `amenity` in `hospital`, `clinic`, `doctors`, or `pharmacy`.
- `shelter_count`: mapped OSM elements with `amenity=shelter`.
- `major_road_way_count`: mapped OSM ways whose `highway` tag is `trunk`, `primary`, `secondary`, or `tertiary`.

Normalize with `clip(x, 0, 1)`:

```text
peak_apparent_norm = clip((max_apparent_temperature_c - 35.0) / 10.0, 0, 1)
apparent_duration_norm = clip(hours_apparent_ge40c / 40.0, 0, 1)
night_relief_loss_norm = warm_night_count / event_nights
population_norm = clip(aoi_population / 200000.0, 0, 1)
critical_service_norm = clip((school_count + 2 * health_facility_count + shelter_count) / 15.0, 0, 1)
transport_exposure_norm = clip(major_road_way_count / 60.0, 0, 1)
degree_hour_norm = clip(apparent_degree_hours_ge40c / 30.0, 0, 1)
land_surface_change_norm = clip(((annual_embedding_change_mean / 0.05) + (abs(mean_dnbr) / 0.02)) / 2.0, 0, 1)
land_surface_stability = 1.0 - land_surface_change_norm
```

Compute:

```text
persistent_heat_response_index =
100 * (0.26 * peak_apparent_norm
     + 0.20 * apparent_duration_norm
     + 0.18 * night_relief_loss_norm
     + 0.16 * population_norm
     + 0.12 * critical_service_norm
     + 0.08 * transport_exposure_norm)

response_priority_score =
100 * (0.36 * degree_hour_norm
     + 0.22 * night_relief_loss_norm
     + 0.18 * population_norm
     + 0.14 * critical_service_norm
     + 0.10 * transport_exposure_norm)
```

Then run a future same-pattern heat scenario by adding `+1.0 C` to the hourly air temperature, hourly apparent temperature, and daily minimum temperature series, leaving relative humidity and exposure fixed. Recompute the heat metrics and both scores; report the deltas from baseline.

Return one JSON object:

```json
{
  "process_model": {
    "event_window": {"start_date": "<YYYY-MM-DD>", "end_date": "<YYYY-MM-DD>", "event_nights": <integer>},
    "mechanism_chain": ["<concise process step>", "<concise process step>", "<concise process step>"],
    "source_paths": {
      "event_context": ["<package-relative path>", "..."],
      "heat_hazard": ["<package-relative path>", "..."],
      "exposure_and_access": ["<package-relative path>", "..."],
      "surface_context": ["<package-relative path>", "..."]
    }
  },
  "computed_metrics": {
    "max_air_temperature_c": <number>,
    "max_apparent_temperature_c": <number>,
    "max_wbt_c": <number>,
    "hours_apparent_ge40c": <integer>,
    "apparent_degree_hours_ge40c": <number>,
    "warm_night_count": <integer>,
    "aoi_population": <number>,
    "aoi_area_km2": <number>,
    "population_density_per_km2": <number>,
    "school_count": <integer>,
    "health_facility_count": <integer>,
    "shelter_count": <integer>,
    "major_road_way_count": <integer>,
    "gridded_temperature_max_c": <number>,
    "gpm_mean_precip_mm": <number>,
    "chirps_mean_precip_mm": <number>,
    "land_surface_change_norm": <number>,
    "land_surface_stability": <number>
  },
  "normalized_inputs": {
    "peak_apparent_norm": <number>,
    "apparent_duration_norm": <number>,
    "night_relief_loss_norm": <number>,
    "population_norm": <number>,
    "critical_service_norm": <number>,
    "transport_exposure_norm": <number>,
    "degree_hour_norm": <number>
  },
  "indices": {
    "persistent_heat_response_index": <number>,
    "response_priority_score": <number>
  },
  "scenario_analysis": {
    "warming_c": 1.0,
    "future_max_apparent_temperature_c": <number>,
    "future_hours_apparent_ge40c": <integer>,
    "future_apparent_degree_hours_ge40c": <number>,
    "future_warm_night_count": <integer>,
    "future_persistent_heat_response_index": <number>,
    "future_response_priority_score": <number>,
    "persistent_heat_response_index_delta": <number>,
    "response_priority_score_delta": <number>
  },
  "final_interpretation": "<one concise disaster-science interpretation>"
}
```
