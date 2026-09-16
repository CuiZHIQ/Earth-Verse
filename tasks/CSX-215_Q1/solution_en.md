# Final Answer

```json
{
  "process_model": "stagnant_winter_aerosol_exposure_load",
  "source_paths": {
    "event_window_and_report": [
      "metadata/event.json",
      "data/event_reports/event_reports_003_Locked_event_anchor_January_2013_Beijing-Tianjin-Hebei_severe_haze_episode.json",
      "data/event_reports/event_reports_001_Locked_anchor_report_NASA_Earth_Observatory.html"
    ],
    "meteorology_and_precipitation": [
      "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json",
      "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
      "data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json"
    ],
    "exposure_and_geospatial": [
      "data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json",
      "data/exposure_impact/exposure_impact_001_Overpass_small_roads_and_critical_amenities.json",
      "data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json",
      "data/exposure_impact/exposure_impact_003_OpenStreetMap_Overpass_bounded_AOI_slice.json"
    ],
    "imagery_and_process_context": [
      "data/remote_sensing/remote_sensing_002_pre.jpg",
      "data/remote_sensing/remote_sensing_003_event.jpg",
      "data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json",
      "data/event_catalogs/event_catalogs_003_NASA_EONET_wildfire_events.json"
    ]
  },
  "computed_metrics": {
    "window_days": 5,
    "event_pm25_ug_m3": 291,
    "peak_pm25_ug_m3": 886,
    "pm25_reference_ug_m3": 25,
    "event_pm25_ratio": 11.64,
    "peak_pm25_ratio": 35.44,
    "event_aqi": 341,
    "peak_aqi": 775,
    "era5_precip_mean_mm": 0.006,
    "gpm_precip_mean_mm": 0.335,
    "gpm_precip_max_mm": 1.185,
    "chirps_precip_mean_mm": 0.0,
    "era5_mean_wind_m_s": 1.378,
    "aoi_area_km2": 2030.2,
    "exposed_population": 2239926,
    "population_density_per_km2": 1103.3,
    "critical_amenities": 89,
    "hospitals": 25,
    "schools": 12,
    "emergency_services": 40,
    "major_response_roads": 170,
    "pre_event_mean_value": 0.726,
    "event_mean_value": 0.702,
    "true_color_darkening": 0.024
  },
  "process_components": {
    "pm25_ratio_norm": 0.976,
    "aqi_severity_norm": 0.972,
    "particle_severity_norm": 0.974,
    "wet_scavenging_deficit_norm": 0.989,
    "ventilation_stagnation_norm": 0.541,
    "meteorological_retention_norm": 0.787,
    "exposure_pressure_norm": 0.726,
    "remote_obscuration_norm": 0.943,
    "persistence_norm": 0.714
  },
  "scenario_analysis": {
    "baseline_index": 84.8,
    "baseline_load_million_person_ug_m3_days": 3259.09,
    "scenario_days": 7,
    "scenario_index": 89.1,
    "scenario_index_delta": 4.3,
    "scenario_load_million_person_ug_m3_days": 4562.73,
    "scenario_load_delta_million_person_ug_m3_days": 1303.64
  },
  "response_priorities": {
    "health_services_priority": 89.8,
    "traffic_visibility_priority": 89.4,
    "wet_weather_priority": 3.9,
    "top_priority": "health_services"
  },
  "mechanism_chain": [
    "The report and event anchor place a five-day severe haze episode over the Beijing-Tianjin-Hebei urban corridor, with PM2.5 at 291 ug/m3, a peak near 886 ug/m3, and AQI values in the hazardous range.",
    "Gridded precipitation is near zero while ERA5-Land mean wind is only about 1.38 m/s, so the event is best interpreted as particle accumulation under weak cleansing and limited ventilation rather than rain, heat, or surface-change forcing.",
    "WorldPop, OSM exposure, the AOI geometry, report visibility language, and the true-color image pair show a high-population, high-mobility exposure setting where delayed dispersion mainly increases health-service and visibility-management load."
  ],
  "final_interpretation": "The package supports a high-severity stagnant winter aerosol exposure event: the baseline index is 84.8, and two additional stagnant days would add about 1303.64 million person-ug/m3-days of PM2.5 burden while keeping health services as the leading response priority."
}
```

# Key Computations

The event window is January 10-14, 2013 inclusive, so `window_days = 5`. The report gives PM2.5 of 291 ug/m3, peak PM2.5 of 886 ug/m3, a 25 ug/m3 reference level, event AQI of 341, and peak AQI of 775. Thus `event_pm25_ratio = 291 / 25 = 11.64` and `peak_pm25_ratio = 886 / 25 = 35.44`.

ERA5-Land mean precipitation is 0.006 mm, GPM mean precipitation is 0.335 mm, and CHIRPS mean precipitation is 0.0 mm. Their mean is 0.114 mm, so `wet_scavenging_deficit_norm = 1 - 0.114/10 = 0.989`. ERA5-Land mean wind speed is `sqrt(0.0599^2 + 1.3764^2) = 1.378 m/s`, giving `ventilation_stagnation_norm = 0.541` and `meteorological_retention_norm = 0.787`.

The AOI polygon spans 0.45 degrees by 0.45 degrees around latitude 36.0, giving about 2030.2 km2. WorldPop gives 2,239,925.775 people, so density is 1103.3 people/km2. Regex extraction from the OSM-like exposure files gives 89 critical amenities, including 25 hospitals, 12 schools, and 40 police or fire-station emergency-service points, plus 170 major response-road segments.

The true-color image pair has mean HSV value brightness of 0.726 before the episode and 0.702 during the episode after resizing to 128 x 96 pixels, so `true_color_darkening = 0.024`. Combined with report language describing haze obscuring the cities below, `remote_obscuration_norm = 0.943`.

The baseline process index is:

```text
100 * (0.32*0.974 + 0.20*0.787 + 0.18*0.726 + 0.15*0.714 + 0.15*0.943) = 84.8
```

The baseline population PM2.5 load is:

```text
2,239,925.775 * 291 * 5 / 1,000,000 = 3259.09 million person-ug/m3-days
```

With two additional stagnant days, the scenario uses seven days:

```text
scenario_load = 2,239,925.775 * 291 * 7 / 1,000,000 = 4562.73
scenario_delta = 4562.73 - 3259.09 = 1303.64
scenario_index = 89.1
```

# Reasoning Path

This is a winter aerosol-retention problem. The particle concentrations and AQI values establish the hazard intensity; the dry precipitation products and low ERA5-Land wind establish limited cleansing and ventilation; the population, OSM, and AOI layers convert the episode into an exposure-load problem; and the report plus true-color imagery support the visibility and transport consequences.

The Sentinel-2 dNBR and wildfire catalog context do not drive the index because they do not provide a burn-scar or wildfire mechanism for this episode. They are useful as process context: the disaster process is atmospheric particle accumulation over an urban corridor, not surface fire damage.

# Scoring Rubric

Total: 20 points.

- 3 points: Uses self-directed package discovery and cites package-relative paths across reports, weather/precipitation, exposure/geospatial, and remote-sensing or process-context sources. Partial credit for correct values with incomplete path citation.
- 3 points: Correctly extracts the event window and hazard intensity values: 5 days, 291 ug/m3, 886 ug/m3, 25 ug/m3, ratios 11.64 and 35.44, AQI 341 and 775. Partial credit for small rounding errors or one missing AQI/PM2.5 value.
- 3 points: Correctly computes meteorological retention: dry gridded precipitation values, ERA5 wind from u/v components, wet-scavenging deficit 0.989, ventilation stagnation 0.541, and retention 0.787. Partial credit for using the right evidence but one formula or unit error.
- 3 points: Correctly computes exposure metrics: AOI area about 2030.2 km2, population 2,239,926, density 1103.3/km2, 89 critical amenities, 25 hospitals, 12 schools, 40 emergency services, 170 major roads, and exposure pressure 0.726. Partial credit for plausible OSM extraction with minor count differences.
- 2 points: Correctly uses the true-color images and report visibility language to compute pre/event mean value, darkening about 0.024, and remote-obscuration norm 0.943. Partial credit for citing the imagery and using the report flag but not reproducing the exact image statistic.
- 3 points: Applies the process-index and two-day scenario formulas correctly, yielding baseline index 84.8, baseline load 3259.09, scenario index 89.1, and scenario load delta 1303.64. Partial credit for correct formulas with rounding or one intermediate error.
- 2 points: Computes response priorities and selects `health_services` as top priority, with health about 89.8, traffic visibility about 89.4, and wet weather about 3.9. Partial credit if the top two high priorities are identified but slightly misordered due to rounding.
- 1 point: Provides a concise mechanism chain and final interpretation grounded in aerosol retention, population exposure, and response pressure, without adding unsupported external loss totals or generic disaster commentary.
