# Saharan Dust Transport Stress and Downwind Exposure Model

Use only the local CSX-302 event package. Select package-relative evidence for every value you use.

Build a dust-transport stress model for the sampled downwind operational sector. The model should distinguish a transient atmospheric dust/haze signal from persistent surface change, account for rain scavenging and transport-weather support during the event window, and estimate the operational load on package-derived exposed people, roads, and critical facilities. Do not treat the sampled AOI as the full trans-Atlantic footprint; use it as the package's local exposure sector.

Use these formulas, with `clip(x, 0, 1)` limiting a value to the inclusive range from 0 to 1:

- `duration_days`: inclusive number of days in the event window.
- `event_scene_offset_days`: days from the event-window start to the event true-color scene.
- `pre_scene_gap_days`: days from the pre-event true-color scene to the event-window start.
- `brightness_delta`: event-scene mean brightness minus pre-event-scene mean brightness.
- `red_blue_delta`: event-scene `(red mean - blue mean)` minus pre-event-scene `(red mean - blue mean)`.
- `plume_visibility_norm = 0.65 * clip(abs(brightness_delta) / 5, 0, 1) + 0.35 * clip(max(red_blue_delta, 0) / 3, 0, 1)`.
- `surface_confound_resistance = 0.60 * (1 - clip(annual_embedding_mean / 0.10, 0, 1)) + 0.40 * (1 - clip(annual_embedding_max / 0.50, 0, 1))`.
- `point_dry_fraction`: mean of the two point-weather dry-day fractions, where a dry day has daily precipitation `< 0.1 mm`.
- `regional_precip_mean_mm`: mean of the gridded event-accumulated precipitation means from the two regional precipitation products.
- `dry_scavenging_resistance = 0.65 * point_dry_fraction + 0.35 * (1 - clip(regional_precip_mean_mm / 60, 0, 1))`.
- Convert the point archive wind-speed maximum from km/h to m/s. Compute `era5_vector_wind_ms = sqrt(mean_u10^2 + mean_v10^2)`.
- `combined_wind_ms = 0.50 * power_mean_wind_ms + 0.30 * archive_mean_wind_max_ms + 0.20 * era5_vector_wind_ms`.
- `temperature_support = clip((archive_mean_daily_max_temperature_c - 15) / 15, 0, 1)`.
- `transport_mixing_norm = 0.70 * clip(combined_wind_ms / 5, 0, 1) + 0.30 * temperature_support`.
- Estimate AOI area from the compact polygon as `(lat_span * 110.574) * (lon_span * 111.320 * cos(mid_lat_radians))`.
- Count all mapped road elements, mapped critical amenities (`hospital`, `clinic`, `doctors`, `fire_station`, `police`, `school`, `shelter`), and access-sensitive road features (`trunk` roads plus `bridge=yes` plus `mountain_pass=yes`) in the broader bounded AOI slice.
- `exposure_pressure_norm = 0.45 * clip(population / 100000, 0, 1) + 0.25 * clip(critical_amenity_count / 50, 0, 1) + 0.20 * clip(road_element_count / 1000, 0, 1) + 0.10 * clip(access_sensitive_feature_count / 20, 0, 1)`.
- `baseline_dust_operational_stress_index = 100 * (0.35 * plume_visibility_norm + 0.20 * dry_scavenging_resistance + 0.15 * transport_mixing_norm + 0.20 * exposure_pressure_norm + 0.10 * surface_confound_resistance)`.

Then run this scenario: mean wind inputs increase by 15%, archive mean daily maximum temperature increases by `2 C`, and population, critical amenities, roads, and access-sensitive features increase by 25%. Recompute `transport_mixing_norm`, `exposure_pressure_norm`, and the stress index; report the scenario delta relative to baseline.

Return only valid JSON with this structure:

```json
{
  "source_paths": {
    "event_context": [],
    "remote_sensing": [],
    "weather_and_precipitation": [],
    "exposure_and_aoi": []
  },
  "process_model": {
    "event_window": {
      "start_date": "",
      "end_date": "",
      "duration_days": 0,
      "event_scene_offset_days": 0,
      "pre_scene_gap_days": 0
    },
    "mechanism_chain": []
  },
  "computed_metrics": {
    "plume_visibility": {
      "brightness_delta": 0.0,
      "red_blue_delta": 0.0,
      "plume_visibility_norm": 0.0
    },
    "surface_confound_resistance": 0.0,
    "dry_scavenging_resistance": {
      "point_dry_fraction": 0.0,
      "regional_precip_mean_mm": 0.0,
      "value": 0.0
    },
    "transport_mixing": {
      "combined_wind_ms": 0.0,
      "archive_mean_daily_max_temperature_c": 0.0,
      "value": 0.0
    },
    "exposure_pressure": {
      "aoi_area_km2": 0.0,
      "population": 0.0,
      "population_density_per_km2": 0.0,
      "road_element_count": 0,
      "critical_amenity_count": 0,
      "access_sensitive_feature_count": 0,
      "value": 0.0
    },
    "baseline_dust_operational_stress_index": 0.0
  },
  "scenario_analysis": {
    "scenario_name": "warmer_windier_25pct_exposure_growth",
    "scenario_transport_mixing_norm": 0.0,
    "scenario_exposure_pressure_norm": 0.0,
    "scenario_index": 0.0,
    "scenario_delta": 0.0
  },
  "response_priorities": [],
  "final_interpretation": ""
}
```

Round index values and physical quantities to one decimal place where appropriate, normalized values to three decimals, and image deltas to three decimals.
