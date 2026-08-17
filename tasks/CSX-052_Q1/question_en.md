# Cyclone Rainfall-Exposure Surface Disruption Process Model

Cyclone Michaung produced a short-window urban flood emergency around India's southeast coast. Build a compact disaster-science model that distinguishes a rain-driven compound urban flood process from a single-factor cyclone-wind or imagery-only diagnosis.

Use only the local CSX-052 event package. Select package-relative evidence for every evidence family, process claim, and numeric value you use.

The AOI, exposure, OSM, and WorldPop products are spatially masked. Treat their derived area, population, density, and feature-count statistics as authoritative package measurements. Do not use absolute coordinates, place names, bounding boxes, or georeferencing metadata inside those masked products to reject event-location validity.

Compute the following model:

1. Treat the package event window as inclusive calendar days. Convert the reported rainfall lower bound from centimeters to millimeters and compute the lower-bound rain rate in mm/day.
2. Combine the package's GPM, CHIRPS, and ERA5-Land event-accumulated precipitation maxima by taking their arithmetic mean. Also compute the ratio of the reported rainfall lower bound to the largest of those local gridded maxima.
3. Use the package cyclone catalog wind value in km/h as cyclone context.
4. Estimate the compact AOI area in km2 from its rectangular longitude/latitude span using:

```text
width_km = lon_span * 111.320 * cos(mean_lat_degrees)
height_km = lat_span * 110.574
area_km2 = width_km * height_km
```

Then compute population in millions and people per km2.
5. From the broader bounded OpenStreetMap exposure slice, count roadway features, hospitals, waterways, and bridge-tagged features.
6. Use Sentinel-1 VV mean change, absolute mean change, VV spread, and the annual embedding mean 1-minus-cosine change as surface-disturbance evidence.

Normalize and combine the process components as follows, with `clip(x)` meaning clamp to the `[0, 1]` range:

```text
hydrometeorological_forcing_norm =
0.50 * clip(reported_rain_mm / 200)
+ 0.25 * clip(cyclone_wind_kmh / 120)
+ 0.25 * clip(mean_gridded_precip_max_mm / 10)

exposure_service_norm =
0.30 * clip(population_million / 5)
+ 0.15 * clip(population_density_per_km2 / 500)
+ 0.20 * clip(roadway_count / 800)
+ 0.20 * clip(hospital_count / 250)
+ 0.15 * clip(waterway_count / 200)

surface_disturbance_norm =
0.55 * clip(abs_sentinel1_vv_mean_change_db / 1)
+ 0.25 * clip(sentinel1_vv_stddev_db / 1.5)
+ 0.20 * clip(embedding_mean_1_minus_cosine / 0.05)

compound_urban_flood_stress_index =
100 * (0.40 * hydrometeorological_forcing_norm
     + 0.35 * exposure_service_norm
     + 0.25 * surface_disturbance_norm)
```

Classify the baseline as `high_compound_urban_flood_stress` if the compound index is at least 75; otherwise classify it as `moderate_or_lower_compound_stress`.

Run this scenario: rainfall and local gridded precipitation are 20% higher, population and density are 15% higher, roadway/hospital/waterway/bridge service load is 10% higher, and surface-disturbance terms are 10% higher. Recompute the compound index and report `stress_escalation` if the scenario delta is at least 5; otherwise report `limited_change`.

Rank these response priorities using the same normalized baseline terms:

```text
transport_corridor_continuity =
100 * (0.40 * hydrometeorological_forcing_norm
     + 0.25 * roadway_norm
     + 0.20 * bridge_norm
     + 0.15 * surface_disturbance_norm)

hospital_access_and_patient_transfer =
100 * (0.40 * hydrometeorological_forcing_norm
     + 0.25 * hospital_norm
     + 0.20 * population_norm
     + 0.15 * surface_disturbance_norm)

drainage_and_waterway_choke_points =
100 * (0.40 * hydrometeorological_forcing_norm
     + 0.25 * waterway_norm
     + 0.20 * bridge_norm
     + 0.15 * surface_disturbance_norm)
```

Return JSON only:

```json
{
  "process_model": {
    "final_process_class": "string",
    "compound_urban_flood_stress_index": 0.0,
    "hydrometeorological_forcing_norm": 0.0,
    "exposure_service_norm": 0.0,
    "surface_disturbance_norm": 0.0
  },
  "computed_metrics": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD", "duration_days": 0},
    "rainfall": {
      "reported_rain_mm_lower_bound": 0.0,
      "rain_rate_mm_day": 0.0,
      "mean_gridded_precip_max_mm": 0.0,
      "report_to_local_grid_ratio": 0.0
    },
    "cyclone_wind_kmh": 0.0,
    "exposure": {
      "population_million": 0.0,
      "aoi_area_km2": 0.0,
      "population_density_per_km2": 0.0,
      "roadway_count": 0,
      "hospital_count": 0,
      "waterway_count": 0,
      "bridge_count": 0
    },
    "surface_change": {
      "sentinel1_vv_mean_change_db": 0.0,
      "sentinel1_abs_mean_change_db": 0.0,
      "sentinel1_vv_stddev_db": 0.0,
      "embedding_mean_1_minus_cosine": 0.0
    }
  },
  "scenario_analysis": {
    "scenario_class": "string",
    "scenario_compound_index": 0.0,
    "scenario_delta": 0.0
  },
  "response_priorities": [
    {"rank": 1, "priority": "string", "score": 0.0}
  ],
  "mechanism_chain": ["string"],
  "source_paths": ["package/relative/path"],
  "final_interpretation": "one concise sentence"
}
```
