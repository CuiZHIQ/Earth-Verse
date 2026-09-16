# Giant-Hail Convective Stress and Response-Load Model

Use only the local CSX-144 event package. Select package-relative evidence for every value and qualitative process claim used in the final JSON.

Construct a process model for the July 2023 northern Italy severe hailstorms as a coupled giant-hail, storm-environment, exposed-service, and landscape-change problem. Your answer must be valid JSON.

Compute the following inputs from the package:

- Event start date, event end date, and inclusive duration in days.
- Confirmed maximum hailstone diameter in centimeters.
- Event-window precipitation summaries from usable gridded or aggregate products, then report the maximum cross-source precipitation value in millimeters. For the process model, use the event accumulated precipitation product that gives both peak and mean event precipitation over the package domain.
- Maximum 10 m wind speed over the event window in kilometers per hour from the usable aggregate weather product, converting vector components from meters per second to kilometers per hour when needed.
- Maximum 2 m temperature over the event window in degrees Celsius from the usable aggregate product.
- Exposed population, counts of schools, fire stations, police facilities, and hospitals, and the total critical-service count from those four amenity types.
- Approximate area of the package AOI polygon in square kilometers using `111.32^2 * abs(delta_lon) * abs(delta_lat) * cos(mean_latitude_radians)`, then compute population density.
- Annual embedding mean and maximum `1 - cosine` change.

Use these formulas, clipping every normalized term to `[0, 1]`:

```text
duration_days = inclusive calendar days from start through end
precip_concentration = event_precip_peak_mm / event_precip_mean_mm

hail_severity_norm = clip((hail_cm - 5) / 15)
precip_peak_norm = clip(event_precip_peak_mm / 50)
precip_concentration_norm = clip(precip_concentration / 3)
wind_norm = clip(max_wind_kmh / 50)
thermal_norm = clip(max_temp_c / 35)

storm_environment_norm =
  0.35 * precip_peak_norm
+ 0.25 * precip_concentration_norm
+ 0.20 * wind_norm
+ 0.20 * thermal_norm

population_norm = clip(exposed_population / 1000000)
critical_facility_norm = clip(critical_service_count / 75)
exposure_norm = 0.60 * population_norm + 0.40 * critical_facility_norm

landscape_change_norm =
  0.70 * clip(embedding_change_max / 0.60)
+ 0.30 * clip(embedding_change_mean / 0.06)

hail_response_load_index =
  100 * (0.40 * hail_severity_norm
       + 0.25 * storm_environment_norm
       + 0.25 * exposure_norm
       + 0.10 * landscape_change_norm)
```

Then compute a `warm_wet_exposure_push` scenario:

- Keep hail size and landscape change unchanged.
- Increase event precipitation peak and mean by 15 percent.
- Increase maximum wind by 10 percent.
- Increase maximum temperature by 2 degrees C.
- Increase exposed population and every critical-service amenity count by 20 percent.
- Recompute the same normalized components, scenario index, and scenario delta from baseline.

Also rank three response priorities using the baseline normalized terms:

```text
roof_and_outdoor_object_safety =
  100 * (0.55 * hail_severity_norm
       + 0.25 * critical_facility_norm
       + 0.20 * population_norm)

drainage_and_debris_clearance =
  100 * (0.45 * precip_peak_norm
       + 0.25 * precip_concentration_norm
       + 0.15 * wind_norm
       + 0.15 * population_norm)

critical_service_continuity =
  100 * (0.40 * critical_facility_norm
       + 0.25 * hail_severity_norm
       + 0.20 * landscape_change_norm
       + 0.15 * population_norm)
```

Return JSON with this structure:

```json
{
  "source_paths": {
    "event_window": [],
    "hail_report": [],
    "weather": [],
    "exposure": [],
    "geospatial_context": [],
    "remote_sensing": []
  },
  "event_window": {
    "start_date": "",
    "end_date": "",
    "duration_days": 0
  },
  "computed_metrics": {
    "hail_cm": 0,
    "precipitation_mm": {},
    "event_precip_peak_mm": 0,
    "event_precip_mean_mm": 0,
    "precip_concentration": 0,
    "max_wind_kmh": 0,
    "max_temp_c": 0,
    "exposed_population": 0,
    "population_density_per_km2": 0,
    "critical_service_counts": {},
    "embedding_change": {}
  },
  "process_model": {
    "component_norms": {},
    "hail_response_load_index": 0
  },
  "scenario_analysis": {
    "scenario_name": "warm_wet_exposure_push",
    "component_norms": {},
    "hail_response_load_index": 0,
    "delta_from_baseline": 0
  },
  "response_priorities": [
    {"rank": 1, "priority": "", "score": 0}
  ],
  "mechanism_chain": [],
  "final_interpretation": ""
}
```

Round source values to sensible precision, normalized terms to 3 decimals, and index or priority scores to 2 decimals.
