# Stagnant Winter Aerosol Exposure-Load Reconstruction

Use only the local CSX-215 event package. Select package-relative evidence needed to distinguish a stagnant winter aerosol episode from other disaster processes.

Build a disaster-science reconstruction of the January 10-14, 2013 Beijing-Tianjin-Hebei severe haze episode as a stagnant winter aerosol exposure event. Cite package-relative source paths for every value you use.

Compute the following quantities:

1. Event-window, concentration, and AQI metrics:
   - inclusive event-window days;
   - event PM2.5 concentration, peak PM2.5 concentration, and the PM2.5 reference concentration reported in the package;
   - event and peak PM2.5 ratios to that reference concentration;
   - event AQI and peak AQI.

2. Meteorological retention metrics:
   - event-window precipitation from ERA5-Land, GPM, and CHIRPS gridded precipitation summaries;
   - ERA5-Land mean wind speed from the mean u and v 10 m components;
   - `wet_scavenging_deficit_norm = 1 - min(mean(era5_precip_mean_mm, gpm_precip_mean_mm, chirps_precip_mean_mm) / 10, 1)`;
   - `ventilation_stagnation_norm = clip((3 - era5_mean_wind_m_s) / 3, 0, 1)`;
   - `meteorological_retention_norm = 0.55 * wet_scavenging_deficit_norm + 0.45 * ventilation_stagnation_norm`.

3. Exposure and response-load metrics:
   - AOI area in km2 from the package AOI polygon, using 111.32 km per degree latitude and `111.32 * cos(latitude_midpoint)` km per degree longitude;
   - exposed population, population density, critical-amenity counts, hospital count, school count, emergency-service count, and major response-road segment count. Use package-local exposure evidence and make a defensible extraction when a mapped feature record is semi-structured;
   - `exposure_pressure_norm = 0.55 * min(population_density_per_km2 / 1500, 1) + 0.25 * min(critical_amenities / 120, 1) + 0.20 * min(major_response_roads / 250, 1)`.

4. Remote-sensing support:
   - compute the mean HSV value brightness for the pre-event and event true-color images after resizing each to 128 x 96 pixels;
   - `true_color_darkening = pre_event_mean_value - event_mean_value`;
   - set `report_haze_visibility_flag` from report language describing the haze obscuring cities below;
   - `remote_obscuration_norm = clip(0.70 * report_haze_visibility_flag + 0.30 * min(true_color_darkening / 0.03, 1), 0, 1)`.

5. Process index and scenario:
   - `pm25_ratio_norm = clip(0.60 * (event_pm25_ratio / 12) + 0.40 * (peak_pm25_ratio / 36), 0, 1)`;
   - `aqi_severity_norm = clip(0.50 * (event_aqi / 350) + 0.50 * (peak_aqi / 800), 0, 1)`;
   - `particle_severity_norm = 0.65 * pm25_ratio_norm + 0.35 * aqi_severity_norm`;
   - `persistence_norm = min(window_days / 7, 1)`;
   - `stagnant_aerosol_exposure_index = 100 * (0.32 * particle_severity_norm + 0.20 * meteorological_retention_norm + 0.18 * exposure_pressure_norm + 0.15 * persistence_norm + 0.15 * remote_obscuration_norm)`;
   - `population_pm25_load_million_person_ug_m3_days = population * event_pm25_ug_m3 * window_days / 1,000,000`;
   - for a two-day delayed-dispersal scenario, recompute the population PM2.5 load and the process index with `scenario_days = window_days + 2` and `scenario_persistence_norm = min(scenario_days / 7, 1)`, keeping other terms unchanged.

6. Response priorities:
   - `health_services_priority = 100 * (0.52 * particle_severity_norm + 0.24 * exposure_pressure_norm + 0.14 * min(hospitals / 30, 1) + 0.10 * respiratory_spike_flag)`;
   - `traffic_visibility_priority = 100 * (0.35 * remote_obscuration_norm + 0.25 * particle_severity_norm + 0.25 * min(major_response_roads / 250, 1) + 0.15 * report_haze_visibility_flag)`;
   - `wet_weather_priority = 100 * (0.50 * (1 - wet_scavenging_deficit_norm) + 0.30 * min(gpm_precip_mean_mm / 10, 1) + 0.20 * min(gpm_precip_max_mm / 10, 1))`.

Round ratios and normalized values to three decimals, index and priority scores to one decimal, population to the nearest person, area and density to one decimal, and population PM2.5 loads to two decimals.

Return one JSON object:

```json
{
  "process_model": "stagnant_winter_aerosol_exposure_load",
  "source_paths": {
    "event_window_and_report": [],
    "meteorology_and_precipitation": [],
    "exposure_and_geospatial": [],
    "imagery_and_process_context": []
  },
  "computed_metrics": {
    "window_days": 0,
    "event_pm25_ug_m3": 0,
    "peak_pm25_ug_m3": 0,
    "pm25_reference_ug_m3": 0,
    "event_pm25_ratio": 0,
    "peak_pm25_ratio": 0,
    "event_aqi": 0,
    "peak_aqi": 0,
    "era5_precip_mean_mm": 0,
    "gpm_precip_mean_mm": 0,
    "gpm_precip_max_mm": 0,
    "chirps_precip_mean_mm": 0,
    "era5_mean_wind_m_s": 0,
    "aoi_area_km2": 0,
    "exposed_population": 0,
    "population_density_per_km2": 0,
    "critical_amenities": 0,
    "hospitals": 0,
    "schools": 0,
    "emergency_services": 0,
    "major_response_roads": 0,
    "pre_event_mean_value": 0,
    "event_mean_value": 0,
    "true_color_darkening": 0
  },
  "process_components": {
    "pm25_ratio_norm": 0,
    "aqi_severity_norm": 0,
    "particle_severity_norm": 0,
    "wet_scavenging_deficit_norm": 0,
    "ventilation_stagnation_norm": 0,
    "meteorological_retention_norm": 0,
    "exposure_pressure_norm": 0,
    "remote_obscuration_norm": 0,
    "persistence_norm": 0
  },
  "scenario_analysis": {
    "baseline_index": 0,
    "baseline_load_million_person_ug_m3_days": 0,
    "scenario_days": 0,
    "scenario_index": 0,
    "scenario_index_delta": 0,
    "scenario_load_million_person_ug_m3_days": 0,
    "scenario_load_delta_million_person_ug_m3_days": 0
  },
  "response_priorities": {
    "health_services_priority": 0,
    "traffic_visibility_priority": 0,
    "wet_weather_priority": 0,
    "top_priority": "short_label"
  },
  "mechanism_chain": [
    "short evidence-grounded step",
    "short evidence-grounded step",
    "short evidence-grounded step"
  ],
  "final_interpretation": "one concise disaster-science conclusion"
}
```
