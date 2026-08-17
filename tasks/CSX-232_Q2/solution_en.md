# Correct Answer

```json
{
  "process_model": {
    "event_window": {
      "start_date": "2023-02-06",
      "end_date": "2023-02-20",
      "duration_days": 15
    },
    "rupture_sequence": {
      "largest_magnitude": 7.8,
      "second_largest_magnitude": 7.5,
      "dual_shock_gap_hours": 9.121,
      "moment_energy_ratio": 0.355,
      "max_mmi": 9.537,
      "max_slip_m": 11.2122,
      "local_catalog_event_count": 9,
      "local_magnitude_5p5_or_larger_count": 9,
      "sequence_pressure": 81.26
    },
    "cold_wet_ground_stress": {
      "first_day_precip_mm": 31.4,
      "total_point_precip_mm": 34.7,
      "first_day_precip_share": 0.905,
      "cold_nights_below_0c": 14,
      "freezing_night_fraction": 0.933,
      "gpm_event_precip_mm_mean": 37.87,
      "gpm_event_precip_mm_max": 65.63,
      "gpm_spatial_contrast": 0.733,
      "era5_precipitation_sum_mm_mean": 19.06,
      "gridded_precip_load": 0.95,
      "cold_wet_ground_stress": 90.718
    },
    "exposure_access_load": {
      "global_earthquake_feature_count": 6,
      "event_local_earthquake_feature_count": 5,
      "excluded_global_earthquake_feature_count": 1,
      "red_alert_count": 2,
      "orange_alert_count": 3,
      "red_alert_fraction": 0.4,
      "population_millions": 2.526,
      "osm_sample_road_ways": 100,
      "osm_minor_road_ways": 74,
      "osm_bridge_road_ways": 8,
      "osm_minor_road_share": 0.74,
      "osm_bridge_share": 0.08,
      "exposure_access_load": 80.99
    },
    "remote_sensing_disruption": {
      "s1_pre_count": 85,
      "s1_post_count": 87,
      "s1_spread_db": 31.083,
      "s1_zero_centered_variability": 0.635,
      "s1_support_balance": 0.977,
      "alphaearth_change_max": 0.526,
      "observation_disruption_signal": 84.351
    }
  },
  "computed_metrics": {
    "compound_response_stress_index": 84.02,
    "baseline_priority_class": "extreme_compound_response_stress"
  },
  "scenario_analysis": {
    "scenario": "first-day precipitation +25%, GPM mean +10%, GPM maximum +15%, ERA5 mean precipitation +10%, and one additional freezing night",
    "scenario_first_day_precip_share": 0.922,
    "scenario_gpm_spatial_contrast": 0.812,
    "scenario_freezing_night_fraction": 1.0,
    "scenario_gridded_precip_load": 1.0,
    "scenario_cold_wet_ground_stress": 94.006,
    "scenario_compound_response_stress_index": 84.843,
    "scenario_delta": 0.823,
    "priority_class": "extreme_compound_response_stress"
  },
  "mechanism_chain": [
    "A regional earthquake sequence began with two large shocks only about 9.121 hours apart, so response demand was driven by both rupture severity and rapid sequencing.",
    "Strong shaking coincided with concentrated first-day precipitation, high freezing-night persistence, and gridded precipitation loads, increasing concern for cold-weather access and ground-stability complications.",
    "Population exposure above 2.5 million people, red GDACS alerts, and bridge/minor-road shares in the local OSM sample raise the operational access load.",
    "Sentinel-1 and annual embedding change statistics indicate heterogeneous surface-change signals rather than a uniform scene-wide offset."
  ],
  "source_paths": [
    "metadata/event.json",
    "data/event_reports/event_reports_001_Locked_anchor_NASA_disaster_activation.html",
    "data/event_reports/event_reports_002_Locked_event_anchor_2023_Turkiye-Syria_earthquake_sequence.json",
    "data/event_catalogs/event_catalogs_001_USGS_ComCat_earthquake_query.json",
    "data/event_catalogs/event_catalogs_003_GDACS_earthquake_alert_API.json",
    "data/event_catalogs/event_catalogs_006_USGS_event_GeoJSON_us6000jllz.json",
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_daily_point_sample.json",
    "data/physical_hazard/physical_hazard_002_NASA_POWER_daily_point_sample.json",
    "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
    "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json",
    "data/remote_sensing/remote_sensing_004_Sentinel-1_GRD_VV_pre_post_change.json",
    "data/exposure_impact/exposure_impact_002_OpenStreetMap_Overpass_small_AOI_sample.json",
    "data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json"
  ],
  "final_interpretation": "The package supports an extreme compound response-stress classification: paired major ruptures, cold wet ground conditions, high exposed population/access load, and heterogeneous remote-sensing change all reinforce the emergency-response burden."
}
```

# Key Computations

The event report gives a 2023-02-06 to 2023-02-20 window, or 15 inclusive days. The event-specific USGS product supplies the ShakeMap geographic box used to filter the broader catalog before selecting the local M7.8 and M7.5 shocks. Their gap is 9.121 hours, and `10 ** (1.5 * (7.5 - 7.8)) = 0.355`.

The rupture component is:

`100 * (0.30 * 7.8/8 + 0.20 * 9.537/10 + 0.20 * 11.2122/12 + 0.15 * 0.355/0.5 + 0.15 * (12 - 9.121)/12) = 81.260`.

The cold/wet component uses daily point precipitation, GPM, ERA5, and daily minimum temperature. First-day precipitation share is `31.4 / 34.7 = 0.905`; freezing persistence is `14 / 15 = 0.933`; GPM contrast is `(65.63 - 37.87) / 37.87 = 0.733`; gridded precipitation load is about `0.950`. These give `cold_wet_ground_stress = 90.718`.

Exposure/access combines WorldPop, GDACS, and the usable OSM road sample. The GDACS earthquake feed has 6 global earthquake entries in the package, but the event-specific ShakeMap box excludes 1 unrelated global earthquake alert, leaving 5 local earthquake alerts. The red alert fraction is therefore `2 / 5 = 0.400`; population is `2.526` million, minor-road share is `74 / 100 = 0.740`, and bridge share is `8 / 100 = 0.080`, giving `exposure_access_load = 80.990`.

Remote-sensing disruption combines Sentinel-1 and AlphaEarth summaries. Sentinel-1 spread is `14.887 - (-16.197) = 31.083 dB`; zero-centered variability is `1 - abs(-0.227) / 0.624 = 0.635`; support balance is `85 / 87 = 0.977`; AlphaEarth maximum change is `0.526`, giving `observation_disruption_signal = 84.351`.

The baseline index is:

`0.35 * 81.260 + 0.25 * 90.718 + 0.25 * 80.990 + 0.15 * 84.351 = 84.020`.

Under the wetter/colder scenario, the cold/wet component rises to `94.006`, and the compound index becomes `84.843`, a `0.823` increase. Both baseline and scenario exceed the `80` threshold for `extreme_compound_response_stress`.

# Scoring Rubric

- 3 points: Finds the relevant local package files independently and cites package-relative paths for the report, seismic, weather, precipitation, alert, exposure/access, and remote-sensing values used.
- 3 points: Uses the 2023-02-06 to 2023-02-20 event window, filters the broad earthquake catalog with the event-product ShakeMap geographic box, and extracts the paired M7.8/M7.5 sequence and 9.121 hour gap.
- 3 points: Correctly extracts and applies max MMI, finite-fault maximum slip, moment-energy ratio, local magnitude counts, and event-local GDACS red/orange alert counts after excluding unrelated global alerts.
- 3 points: Correctly computes precipitation concentration, freezing-night persistence, GPM spatial contrast, gridded precipitation load, and `cold_wet_ground_stress`.
- 3 points: Correctly computes WorldPop exposure, OSM road/bridge/minor-road shares, Sentinel-1 spread and balance, AlphaEarth change, and the exposure/access and observation scores.
- 3 points: Correctly applies clipping, weighted formulas, the scenario perturbation, scenario delta, and priority-class rule.
- 2 points: Provides a concise disaster-process interpretation tied to paired major ruptures, cold wet ground conditions, exposed population/access pressure, and heterogeneous remote-sensing change without unsupported claims.
