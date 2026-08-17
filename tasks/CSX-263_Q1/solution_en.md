# Correct Answer

```json
{
  "process_model": {
    "event": "2015 Indonesian drought, peat fires and transboundary haze",
    "mechanism": "El Nino-amplified drying of peatlands enabled persistent fires, low smoke and carbon monoxide transport, and downwind population-service exposure.",
    "baseline_priority": 77.34,
    "scenario_priority": 82.08,
    "priority_delta": 4.74
  },
  "evidence_scope": {
    "point_weather": "Antecedent plus fire-season dryness and wind diagnostic for the available local/downwind context, not a sole source-region fire locator.",
    "gridded_hazard_products": "Overlapping precipitation and heat summaries used for regional process consistency across products.",
    "receptor_load_products": "Masked WorldPop and OSM-derived counts used as authoritative receptor/service-load statistics for the package context.",
    "remote_sensing": "Sentinel scene-pair availability is an observability constraint, not evidence of absent burning."
  },
  "computed_metrics": {
    "event_window": "2015-09-01 to 2015-10-31",
    "event_days": 61,
    "hazard_overlap_window": "2015-09-01 to 2015-10-16",
    "hazard_overlap_days": 46,
    "coverage_fraction_pct": 75.41,
    "point_weather_days": 60,
    "low_rain_threshold_mm_day": 1.0,
    "dry_day_share_pct": 41.67,
    "longest_low_rain_run_days": 8,
    "longest_low_rain_run_start": "2015-08-21",
    "longest_low_rain_run_end": "2015-08-28",
    "mean_point_precip_mm_day": 3.7,
    "heat_tail_c": 8.25,
    "mean_overlap_wind_mps": 4.42,
    "gpm_precip_cv": 0.499,
    "chirps_precip_cv": 0.348,
    "gridded_mean_gap_pct": 8.15,
    "gpm_low_tail_norm": 0.833,
    "chirps_low_tail_norm": 0.058,
    "scene_pair_ready": 0,
    "sentinel_pre_count": 0,
    "sentinel_post_count": 1,
    "population_sum": 510700.36,
    "osm_element_count": 1000,
    "critical_service_count": 395,
    "network_element_count": 549,
    "pop_per_osm_element": 510.7
  },
  "baseline_indices": {
    "dry_persistence_index": 65.13,
    "rainfall_structure_index": 66.34,
    "heat_transport_index": 79.41,
    "receptor_load_index": 90.48,
    "observability_constraint_index": 100.0,
    "compound_haze_response_priority": 77.34
  },
  "scenario_analysis": {
    "scenario_name": "warmer_drier_higher_exposure",
    "precipitation_multiplier": 0.85,
    "heat_tail_increase_c": 2.0,
    "wind_multiplier": 1.1,
    "population_multiplier": 1.1,
    "dry_persistence_index": 68.46,
    "rainfall_structure_index": 69.25,
    "heat_transport_index": 93.37,
    "receptor_load_index": 94.74,
    "compound_haze_response_priority": 82.08,
    "priority_delta": 4.74
  },
  "mechanism_chain": [
    "Strong seasonal drying and an 8-day low-rain run lower peat moisture.",
    "Spatially uneven rainfall leaves dry pockets even when regional means differ across products.",
    "A warm regional tail and moderate near-surface wind support smoke persistence and transport.",
    "Incomplete dNBR scene pairing limits burn-scar confirmation, so true-color remote sensing and weather-exposure evidence carry more operational weight.",
    "Population, schools, shelters, hospitals, police, fire stations, roads, and waterways make haze a receptor and service-continuity problem."
  ],
  "source_paths": [
    "metadata/event.json",
    "data/event_reports/event_reports_001_Locked_anchor_NASA_Earth_Observatory.html",
    "data/event_reports/event_reports_002_Locked_event_anchor_2015_Indonesian_drought_peat_fires_and_transboundary_haze.json",
    "data/physical_hazard/physical_hazard_001_Open-Meteo_daily_weather_fill.json",
    "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json",
    "data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json",
    "data/exposure_impact/exposure_impact_003_OpenStreetMap_Overpass_bounded_AOI_slice.json",
    "data/remote_sensing/remote_sensing_001_pre.jpg",
    "data/remote_sensing/remote_sensing_002_event.jpg"
  ],
  "final_interpretation": "The baseline priority is high, and the warmer-drier scenario raises it further because drought persistence, heat transport, and receptor load intensify while burn-scar scene pairing remains unavailable; the receptor-load and point-weather terms should be read as package-context diagnostics rather than standalone fire-source locators."
}
```

# Key Computations

The event report fixes the event period as 2015-09-01 to 2015-10-31, or 61 inclusive days. The hazard-data overlap used for wind and gridded products is 2015-09-01 to 2015-10-16, or 46 days, so coverage is `100 * 46 / 61 = 75.41%`.

The point-weather series has 60 daily precipitation values. Of these, 25 are `<= 1 mm/day`, giving `41.67%`; the longest low-rain run is 8 days from 2015-08-21 to 2015-08-28, and mean point precipitation is `222.0 / 60 = 3.70 mm/day`. Therefore:

```text
dry_persistence_norm =
0.40 * (41.67 / 50) + 0.30 * (8 / 10) + 0.30 * (1 - 3.70 / 5)
= 0.6513
dry_persistence_index = 65.13
```

For rainfall structure, the GPM CV is `115.41345 / 231.10754 = 0.499`; the CHIRPS CV is `87.26987 / 250.73282 = 0.348`. The gridded mean gap is `8.15%`, and the low-tail terms are `0.833` for GPM and `0.058` for CHIRPS. The weighted rainfall structure index is `66.34`.

ERA5-Land gives a heat tail of `38.79063 - 30.54140 = 8.25 C`. Mean overlap point wind is `15.92 km/h / 3.6 = 4.42 m/s`, so the heat-transport index is `79.41`. Sentinel dNBR has no complete pre/post pair (`pre_count = 0`, `post_count = 1`), giving scene readiness `0` and observability constraint `100.0`.

WorldPop gives `510700.36` people. The OSM slice has 1000 elements, 395 critical services, and 549 highway/waterway network elements, so `population_per_osm_element = 510.70`. The receptor-load index is `90.48`.

The baseline response priority is:

```text
100 * (0.30 * 0.6513
     + 0.20 * 0.6634
     + 0.15 * 0.7941
     + 0.25 * 0.9048
     + 0.10 * 1.0000)
= 77.34
```

Under the warmer-drier higher-exposure scenario, the recomputed subindices are 68.46 for dry persistence, 69.25 for rainfall structure, 93.37 for heat transport, and 94.74 for receptor load. The scenario priority is `82.08`, so `priority_delta = 82.08 - 77.34 = 4.74`.

# Reasoning Path

The NASA event narrative describes thick peat, El Nino dryness, intentionally set agricultural fires, low smoke layers, carbon monoxide, and downwind air-quality impacts across Southeast Asia. The model therefore combines drying and rainfall heterogeneity with heat and wind transport, then weights the exposed population and service network. The missing Sentinel dNBR scene pair is treated as an operational monitoring constraint rather than as proof that burn impacts were absent.

# Scoring Rubric

- 3 points: Self-directed package discovery, package-relative path citations, and bounded evidence-scope statements across event report, timing metadata, point weather, gridded rainfall, ERA5-Land, Sentinel, population, OSM, geospatial, and remote-sensing evidence.
- 4 points: Correct event timing, hazard-data overlap, dry-day share, longest low-rain run, mean precipitation, and dry persistence index.
- 3 points: Correct GPM and CHIRPS CVs, low-tail terms, mean-gap percentage, and rainfall structure index.
- 3 points: Correct heat-tail calculation, km/h to m/s wind conversion, heat-transport index, and Sentinel scene-pair interpretation.
- 4 points: Correct population, critical service count, network count, people per OSM element, receptor-load index, baseline response priority, and interpretation of receptor products as package-context load statistics.
- 3 points: Correct warmer-drier scenario recomputation and concise peat-fire haze mechanism interpretation.
