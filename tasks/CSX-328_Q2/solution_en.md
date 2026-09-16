# Correct Answer

```json
{
  "process_model": {
    "event": "2016 Great Barrier Reef marine heatwave and bleaching",
    "window": "2016-02-01/2016-05-31",
    "dominant_hazard_pathway": "marine_heat_stress_driven_coral_bleaching"
  },
  "source_paths": [
    "metadata/event.json",
    "data/event_reports/event_reports_003_Locked_event_anchor_2016_Great_Barrier_Reef_marine_heatwave_and_bleaching.json",
    "data/event_reports/event_reports_001_Locked_package_evidence_report.html",
    "data/other/other_001_NOAA_Coral_Reef_Watch_5km_products.html",
    "data/event_catalogs/event_catalogs_002_NOAA_OISST_PSL_ERDDAP_sea-surface_temperature_THREDDS_catalog_XML.xml",
    "data/physical_hazard/physical_hazard_001_NASA_POWER_daily_point_sample.json",
    "data/physical_hazard/physical_hazard_002_Open-Meteo_archive_point_sample.json",
    "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json",
    "data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json",
    "data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json"
  ],
  "computed_metrics": {
    "event_window_days": 121,
    "reef_length_km": 2300,
    "surveyed_reefs": 900,
    "escaped_bleaching_reefs": 68,
    "flyover_bleached_reefs": 832,
    "flyover_bleached_percent": 92.44,
    "reported_bleached_percent": 93,
    "severely_bleached_reefs": 316,
    "severe_observed_percent": 35.11,
    "sector_severe_bleaching_percent": {"north": 81, "central": 33, "south": 1},
    "spatial_concentration_norm": 0.8,
    "north_mortality_close_to_percent": 50,
    "sst_anomaly_c_range": [1.0, 2.0],
    "sst_anomaly_midpoint_c": 1.5,
    "north_sst_threshold_c": 30.0,
    "dhw_thresholds": {
      "widespread_bleaching_likely": 4,
      "significant_bleaching_and_death_possible": 8,
      "gap": 4
    },
    "annual_tourism_value_billion_aud": 5,
    "tourism_jobs": 70000,
    "jobs_per_billion_aud": 14000.0
  },
  "environmental_context": {
    "nasa_power_mean_t2m_c_first_15_days": 30.17,
    "nasa_power_total_precip_mm_first_15_days": 1.49,
    "nasa_power_mean_wind_ms_first_15_days": 5.53,
    "open_meteo_mean_tmax_c_first_15_days": 37.01,
    "open_meteo_dry_days_first_15_days": 15,
    "open_meteo_mean_wind_max_ms_first_15_days": 7.01,
    "era5_land_event_tmax_mean_c": 33.75,
    "gpm_event_precip_mean_mm": 633.35,
    "chirps_event_precip_mean_mm": 449.47,
    "gpm_to_chirps_precip_mean_ratio": 1.41,
    "sentinel2_dnbr_mean": 0.011,
    "worldpop_population_sum": 31011.46,
    "aoi_area_km2": 11864.18,
    "population_density_per_km2": 2.61,
    "crw_daily_5km_products_present": true,
    "crw_product_markers": [
      "SST",
      "SST Anomaly",
      "HotSpot",
      "Degree Heating Week",
      "Bleaching Alert Area"
    ],
    "oisst_2016_sst_mean_available": true,
    "oisst_2016_sst_anom_available": true
  },
  "scenario_analysis": {
    "formula": "100*(0.30*duration_norm + 0.25*thermal_norm + 0.20*bleached_extent_norm + 0.15*severe_fraction_norm + 0.10*spatial_concentration_norm)",
    "normalizers": {
      "duration_norm": 1.0,
      "thermal_norm": 0.75,
      "bleached_extent_norm": 0.924,
      "severe_fraction_norm": 0.351,
      "spatial_concentration_norm": 0.8
    },
    "baseline_bleaching_process_index": 80.51,
    "scenario_plus_0_5c_thermal_norm": 1.0,
    "scenario_plus_0_5c_process_index": 86.76,
    "scenario_delta": 6.25
  },
  "mechanism_chain": [
    "Persistent above-average sea-surface temperature produces accumulated coral heat stress.",
    "Bleaching extent is near-systemic in the surveyed reefs, while severe bleaching is concentrated in the north and central sectors.",
    "The northern sector crosses from bleaching concern toward mortality concern because the report describes close to 50 percent coral death there.",
    "Low mean dNBR and land-weather or precipitation layers are contextual checks, not the main causal pathway for this marine ecosystem event."
  ],
  "final_interpretation": "extreme_northern_reef_heat_stress_priority"
}
```

# Calculation Path

The package event anchor gives the 2016-02-01 through 2016-05-31 window. Counting both endpoints gives `121` days, so `duration_norm = min(121 / 120, 1) = 1.0`.

The event report describes the reef as 2,300 km long, with `900` reefs surveyed, `68` escaping bleaching, and `316` severely bleached. Thus `flyover_bleached_reefs = 900 - 68 = 832`, `flyover_bleached_percent = 832 / 900 * 100 = 92.44`, and `severe_observed_percent = 316 / 900 * 100 = 35.11`.

The sector severe-bleaching values are north `81%`, central `33%`, and south `1%`. The spatial concentration normalizer is `(81 - 1) / 100 = 0.8`. The same report gives close to `50%` coral death in northern diving surveys, so the interpretation should treat the northern sector as the strongest ecological-response priority, while avoiding extrapolating whole-reef mortality.

The report gives sea-surface temperatures `1-2 C` above average and exceeding `86 F` in the most affected northern areas. The midpoint is `(1 + 2) / 2 = 1.5 C`, and `86 F` converts to `(86 - 32) * 5 / 9 = 30.0 C`. The Degree Heating Week thresholds are `4` for widespread bleaching likely and `8` for significant bleaching and death possible, so the gap is `4`.

The supporting context shows warm and dry early-event land/atmospheric conditions in the point samples, event-period gridded temperature/precipitation context, daily 5 km coral heat-stress products and 2016 OISST SST datasets, low mean terrestrial dNBR, and population/geospatial context for the sampled AOI. These layers support situational interpretation, but the causal model remains marine thermal stress and coral bleaching.

The baseline index uses:

```text
duration_norm = 1.0
thermal_norm = min(1.5 / 2, 1) = 0.75
bleached_extent_norm = 832 / 900 = 0.924444...
severe_fraction_norm = 316 / 900 = 0.351111...
spatial_concentration_norm = 0.8
```

So:

```text
100 * (0.30*1.0 + 0.25*0.75 + 0.20*0.924444...
     + 0.15*0.351111... + 0.10*0.8)
= 80.51
```

For the warmer scenario, the anomaly midpoint becomes `2.0 C`, so `scenario_plus_0_5c_thermal_norm = min(2.0 / 2, 1) = 1.0`. The scenario index is `86.76`, and the scenario delta is `86.76 - 80.51 = 6.25`.

# Scoring Rubric (20 points)

- 3 points: Identifies relevant package files independently and cites package-relative paths across event reporting, hazard/product, remote-sensing, exposure, and geospatial evidence.
- 4 points: Correctly extracts the event window, inclusive day count, reef survey counts, bleaching counts, severe counts, sector percentages, and northern mortality statement.
- 4 points: Correctly handles thermal-stress values, including the SST anomaly midpoint, 86 F to 30.0 C conversion, Degree Heating Week thresholds, and threshold gap.
- 3 points: Synthesizes environmental and exposure context without misclassifying the event as flood, wind, burn-scar, or land-heat dominated.
- 4 points: Applies the process-index formula, clipping, rounding, and +0.5 C scenario correctly.
- 2 points: Provides a concise mechanism chain and final interpretation grounded in marine heat-stress persistence, severe northern concentration, and recovery pressure.
