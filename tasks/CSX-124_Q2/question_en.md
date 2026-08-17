# Cyclone Gabrielle Compound Rainfall-Wind Exposure Stress Model

Cyclone Gabrielle produced an unusual combination of concentrated rainfall, deep low pressure, damaging winds, coastal and river-drainage stress, and widespread emergency-management pressure across Aotearoa New Zealand in February 2023. Build a compact quantitative process model from the local event package that explains why this was a compound storm-impact problem rather than a single-parameter wind or rain event.

Use only the local event package for CSX-124. Select package-relative evidence for every value and qualitative process claim used in your answer.

Compute the following quantities and return one valid JSON object.

Definitions and formulas:

- `area_mean_precip_mm`: mean of the event-accumulated precipitation means from three gridded precipitation products.
- `aoi_area_km2`: estimate from the package AOI bounding polygon as `lat_span_deg * 111.32 * lon_span_deg * 111.32 * cos(mid_latitude_radians)`.
- `runoff_volume_proxy_million_m3`: `area_mean_precip_mm / 1000 * aoi_area_km2 * 1,000,000 / 1,000,000`.
- `population_rainfall_load_million_person_mm`: `population_sum * area_mean_precip_mm / 1,000,000`.
- `reported_station_to_area_ratio`: `reported maximum station rainfall / area_mean_precip_mm`.
- Count critical facilities from package infrastructure features with `amenity` equal to `school`, `hospital`, `fire_station`, or `police`.
- Count access assets as unique package infrastructure features that satisfy at least one of these conditions: `highway` is in `motorway`, `trunk`, `primary`, `secondary`, or `tertiary`; the feature is tagged as a bridge; or the feature has a tunnel tag. If one feature satisfies multiple conditions, count it once.
- `rainfall_stress = 0.45 * clip(area_mean_precip_mm / 100, 0, 1) + 0.35 * clip(wettest_24h_point_rain_mm / 150, 0, 1) + 0.20 * clip(reported_station_to_area_ratio / 7, 0, 1)`.
- `wind_pressure_stress = 0.45 * clip((point_peak_gust_kmh / 120)^2, 0, 1) + 0.35 * clip((1010 - point_min_pressure_hpa) / 30, 0, 1) + 0.20 * clip(point_max_24h_pressure_fall_hpa / 30, 0, 1)`.
- `exposure_access_stress = 0.50 * clip(population_sum / 350000, 0, 1) + 0.30 * clip(access_asset_count / 450, 0, 1) + 0.20 * clip(critical_facility_count / 35, 0, 1)`.
- `disturbance_context = clip(0.55 * (sar_mean_change_db / 2.5) + 0.45 * (annual_embedding_max_change / 0.5), 0, 1)`.
- `compound_storm_stress_index = 100 * (0.35 * rainfall_stress + 0.25 * wind_pressure_stress + 0.25 * exposure_access_stress + 0.15 * disturbance_context)`.

Scenario test: recompute the index for a warmer, wetter, windier emergency-planning scenario in which rainfall totals and gridded precipitation means increase by 12%, point peak gust increases by 15%, and exposed population increases by 10%. Keep pressure, infrastructure counts, AOI area, and remote-sensing terms unchanged; keep the station-to-area contrast unchanged because both station and gridded rainfall scale together. Report the scenario index and its delta from baseline.

Also compute three response priority scores and rank them from highest to lowest:

- `flood_slope_situational_awareness = 100 * (0.45 * rainfall_stress + 0.20 * clip(reported_station_to_area_ratio / 7, 0, 1) + 0.20 * disturbance_context + 0.15 * clip(population_sum / 350000, 0, 1))`
- `lifeline_access_continuity = 100 * (0.30 * wind_pressure_stress + 0.25 * clip(access_asset_count / 450, 0, 1) + 0.25 * clip(critical_facility_count / 35, 0, 1) + 0.20 * disturbance_context)`
- `evacuation_and_shelter_readiness = 100 * (0.30 * rainfall_stress + 0.20 * wind_pressure_stress + 0.25 * clip(population_sum / 350000, 0, 1) + 0.15 * clip(critical_facility_count / 35, 0, 1) + 0.10 * clip(access_asset_count / 450, 0, 1))`

Return JSON with this shape:

```json
{
  "process_model": "gabrielle_compound_rainfall_wind_exposure_stress",
  "source_paths": ["<package-relative path>", "..."],
  "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
  "computed_metrics": {
    "rainfall": {},
    "wind_pressure": {},
    "exposure_access": {},
    "remote_sensing": {},
    "compound_storm_stress_index": 0
  },
  "scenario_analysis": {
    "scenario": "+12% rainfall, +15% point gust, +10% exposed population",
    "scenario_index": 0,
    "delta_from_baseline": 0
  },
  "response_priorities": [
    {"rank": 1, "priority": "<name>", "score": 0}
  ],
  "mechanism_chain": ["<concise process step>", "..."],
  "final_interpretation": "<one concise sentence>"
}
```

Round normalized stresses and indices to three decimals, large physical totals to two decimals, and counts to integers.
