# Marine Heat-Stress Persistence and Reef-Bleaching Severity Model

Use only the local CSX-328 event package. Select package-relative evidence for every value used.

Reconstruct the disaster process behind the 2016 Great Barrier Reef marine heatwave and bleaching event as a multi-source ecological stress model. Your answer should combine event reporting, marine heat-stress product context, physical hazard context, remote-sensing context, exposure/geospatial context, and the reef-impact observations.

Compute the following quantities:

- inclusive event-window days;
- reef survey bleaching extent and severe-bleaching fraction;
- north-central-south severe-bleaching structure, with `spatial_concentration_norm = (north severe percent - south severe percent) / 100`;
- SST anomaly range, midpoint in degrees C, the Celsius value of the reported northern 86 F threshold, and the Degree Heating Week threshold gap;
- supporting environmental context from short-window land/atmospheric samples, gridded precipitation/temperature summaries, daily coral heat-stress product context, a terrestrial dNBR product, population, and AOI area;
- baseline and warmer-scenario bleaching-process scores.

Use these normalizers:

```text
duration_norm = min(window_days / 120, 1)
thermal_norm = min(sst_anomaly_midpoint_c / 2, 1)
bleached_extent_norm = flyover_bleached_reefs / surveyed_reefs
severe_fraction_norm = severely_bleached_reefs / surveyed_reefs
spatial_concentration_norm = (north_severe_percent - south_severe_percent) / 100
```

Then compute:

```text
bleaching_process_index =
100 * (0.30 * duration_norm
     + 0.25 * thermal_norm
     + 0.20 * bleached_extent_norm
     + 0.15 * severe_fraction_norm
     + 0.10 * spatial_concentration_norm)
```

For the scenario, add `0.5 C` to the SST anomaly midpoint before recomputing `thermal_norm` and the index. Round percentages, temperatures, ratios, areas, and index values to two decimals unless a field is explicitly a normalized value, in which case round to three decimals.

Return only JSON with this structure:

```json
{
  "process_model": {
    "event": "",
    "window": "YYYY-MM-DD/YYYY-MM-DD",
    "dominant_hazard_pathway": ""
  },
  "source_paths": [],
  "computed_metrics": {
    "event_window_days": 0,
    "reef_length_km": 0,
    "surveyed_reefs": 0,
    "escaped_bleaching_reefs": 0,
    "flyover_bleached_reefs": 0,
    "flyover_bleached_percent": 0.0,
    "reported_bleached_percent": 0,
    "severely_bleached_reefs": 0,
    "severe_observed_percent": 0.0,
    "sector_severe_bleaching_percent": {"north": 0, "central": 0, "south": 0},
    "spatial_concentration_norm": 0.0,
    "north_mortality_close_to_percent": 0,
    "sst_anomaly_c_range": [0.0, 0.0],
    "sst_anomaly_midpoint_c": 0.0,
    "north_sst_threshold_c": 0.0,
    "dhw_thresholds": {
      "widespread_bleaching_likely": 0,
      "significant_bleaching_and_death_possible": 0,
      "gap": 0
    },
    "annual_tourism_value_billion_aud": 0,
    "tourism_jobs": 0,
    "jobs_per_billion_aud": 0.0
  },
  "environmental_context": {
    "nasa_power_mean_t2m_c_first_15_days": 0.0,
    "nasa_power_total_precip_mm_first_15_days": 0.0,
    "nasa_power_mean_wind_ms_first_15_days": 0.0,
    "open_meteo_mean_tmax_c_first_15_days": 0.0,
    "open_meteo_dry_days_first_15_days": 0,
    "open_meteo_mean_wind_max_ms_first_15_days": 0.0,
    "era5_land_event_tmax_mean_c": 0.0,
    "gpm_event_precip_mean_mm": 0.0,
    "chirps_event_precip_mean_mm": 0.0,
    "gpm_to_chirps_precip_mean_ratio": 0.0,
    "sentinel2_dnbr_mean": 0.0,
    "worldpop_population_sum": 0.0,
    "aoi_area_km2": 0.0,
    "population_density_per_km2": 0.0,
    "crw_daily_5km_products_present": true,
    "crw_product_markers": [],
    "oisst_2016_sst_mean_available": true,
    "oisst_2016_sst_anom_available": true
  },
  "scenario_analysis": {
    "formula": "",
    "normalizers": {
      "duration_norm": 0.0,
      "thermal_norm": 0.0,
      "bleached_extent_norm": 0.0,
      "severe_fraction_norm": 0.0,
      "spatial_concentration_norm": 0.0
    },
    "baseline_bleaching_process_index": 0.0,
    "scenario_plus_0_5c_thermal_norm": 0.0,
    "scenario_plus_0_5c_process_index": 0.0,
    "scenario_delta": 0.0
  },
  "mechanism_chain": [],
  "final_interpretation": ""
}
```
