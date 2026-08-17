# Final Answer

```json
{
  "answer_type": "poyang_heat_drought_lake_response_model",
  "source_paths": {
    "event_window": "data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json",
    "lake_report": "data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html",
    "heat_series": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "precipitation_products": [
      "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
      "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json",
      "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json"
    ],
    "remote_change_products": [
      "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json",
      "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json"
    ],
    "aoi_geometry": "data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json",
    "population": "data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json",
    "road_service_exposure": "data/exposure_impact/exposure_impact_005_OpenStreetMap_Overpass_bounded_AOI_slice.json"
  },
  "process_model": {
    "event_window": {
      "start": "2022-06-01",
      "end": "2022-08-31"
    },
    "lake_timeline": {
      "annual_high_date": "2022-06-23",
      "dry_season_start_date": "2022-08-06",
      "dry_season_early_by_days": 100,
      "level_start_m": 11.99,
      "level_end_date": "2022-08-30",
      "level_end_m": 8.96,
      "drop_m": 3.03,
      "drop_percent": 25.3,
      "level_span_days": 24,
      "drop_rate_m_per_day": 0.126,
      "drop_rate_cm_per_day": 12.6,
      "image_start_date": "2022-07-10",
      "image_end_date": "2022-08-27",
      "image_span_days": 48
    },
    "heat_stress": {
      "window_start": "2022-08-06",
      "window_end": "2022-08-30",
      "temperature_adjustment_c": 0.0,
      "longest_Tmax35_start": "2022-08-07",
      "longest_Tmax35_end": "2022-08-23",
      "longest_Tmax35_days": 17,
      "Tmax35_excess_C_day": 21.3,
      "hot_night_threshold_c": 28.0,
      "hot_night_count": 14,
      "hot_night_fraction": 0.824,
      "longest_apparent40_start": "2022-08-08",
      "longest_apparent40_end": "2022-08-23",
      "longest_apparent40_days": 16,
      "apparent40_excess_C_day": 27.1,
      "peak_apparent_date": "2022-08-20",
      "peak_apparent_c": 44.0
    },
    "precipitation_evidence": {
      "shared_start": "2022-06-01",
      "shared_end": "2022-07-16",
      "gpm_mean_mm": 519.7,
      "chirps_mean_mm": 387.6,
      "era5_mean_mm": 271.1,
      "gpm_minus_chirps_mm": 132.1,
      "gpm_to_chirps_ratio": 1.341,
      "gap_to_dry_season_start_days": 21,
      "gap_to_lake_image_days": 42,
      "gap_to_last_lake_level_days": 45,
      "interpretation": "precipitation_summaries_end_before_late_lake_drop_stage"
    },
    "remote_sensing_change": {
      "dnbr_pre_window": [
        "2022-04-02",
        "2022-05-25"
      ],
      "dnbr_post_window": [
        "2022-06-01",
        "2022-08-30"
      ],
      "dnbr_mean": 0.009274,
      "dnbr_max": 0.538638,
      "embedding_mean_change": 0.013761,
      "embedding_max_change": 0.250799,
      "dnbr_max_to_mean_ratio": 58.1,
      "embedding_max_to_mean_ratio": 18.2,
      "aoi_scale_signal": "weak_mean_change"
    },
    "spatial_exposure_context": {
      "weather_point": {
        "lat": 30.475,
        "lon": 112.526
      },
      "aoi_centroid": {
        "lat": 36.0,
        "lon": 120.5
      },
      "weather_to_aoi_distance_km": 962.4,
      "population": 2485012.3,
      "hospital_count": 24,
      "police_count": 28,
      "fire_station_count": 7,
      "shelter_count": 12,
      "critical_service_count": 71,
      "major_road_way_count": 170,
      "bridge_way_count": 29,
      "total_osm_elements": 1000,
      "spatial_transfer_caution": "large_weather_to_aoi_distance_do_not_treat_aoi_population_as_direct_poyang_impact_count"
    }
  },
  "computed_metrics": {
    "heat_persistence_index": 76.8,
    "lake_drop_index": 84.0,
    "late_precip_gap_index": 95.6,
    "remote_mean_change_index": 23.0,
    "exposure_service_index": 97.5,
    "response_priority_score": 85.9
  },
  "scenario_analysis": {
    "scenario_name": "plus_2C_and_10_day_continued_drop",
    "heat_stress": {
      "window_start": "2022-08-06",
      "window_end": "2022-08-30",
      "temperature_adjustment_c": 2.0,
      "longest_Tmax35_start": "2022-08-06",
      "longest_Tmax35_end": "2022-08-26",
      "longest_Tmax35_days": 21,
      "Tmax35_excess_C_day": 59.1,
      "hot_night_threshold_c": 28.0,
      "hot_night_count": 19,
      "hot_night_fraction": 0.905,
      "longest_apparent40_start": "2022-08-06",
      "longest_apparent40_end": "2022-08-26",
      "longest_apparent40_days": 21,
      "apparent40_excess_C_day": 65.3,
      "peak_apparent_date": "2022-08-20",
      "peak_apparent_c": 46.0
    },
    "lake_timeline": {
      "annual_high_date": "2022-06-23",
      "dry_season_start_date": "2022-08-06",
      "dry_season_early_by_days": 100,
      "level_start_m": 11.99,
      "level_end_date": "2022-08-30",
      "level_end_m": 8.96,
      "drop_m": 4.29,
      "drop_percent": 35.8,
      "level_span_days": 24,
      "drop_rate_m_per_day": 0.126,
      "drop_rate_cm_per_day": 12.6,
      "image_start_date": "2022-07-10",
      "image_end_date": "2022-08-27",
      "image_span_days": 48,
      "continued_drop_days": 10,
      "scenario_level_date": "2022-09-09",
      "scenario_level_m": 7.7
    },
    "computed_metrics": {
      "heat_persistence_index": 98.1,
      "lake_drop_index": 89.5,
      "late_precip_gap_index": 95.6,
      "remote_mean_change_index": 23.0,
      "exposure_service_index": 97.5,
      "response_priority_score": 95.0
    },
    "deltas_from_baseline": {
      "heat_persistence_index": 21.3,
      "lake_drop_index": 5.5,
      "response_priority_score": 9.1,
      "lake_level_m": -1.26,
      "drop_m": 1.26
    }
  },
  "response_priorities": [
    {
      "rank": 1,
      "priority": "protect_drinking_water_irrigation_and_shipping_access",
      "trigger_metrics": [
        "lake_drop_index",
        "scenario_level_m",
        "drop_rate_cm_per_day"
      ],
      "rationale": "The observed lake drop is rapid and the continued-drop scenario lowers the reported level by another 1.26 m."
    },
    {
      "rank": 2,
      "priority": "heat_health_and_power_reliability_operations",
      "trigger_metrics": [
        "heat_persistence_index",
        "hot_night_fraction",
        "peak_apparent_c"
      ],
      "rationale": "Persistent hot days, hot nights, and high apparent temperature coincide with the low-water stage and intensify demand and health stress."
    },
    {
      "rank": 3,
      "priority": "targeted_field_reconnaissance_before_using_aoi_exposure_as_lake_impact_load",
      "trigger_metrics": [
        "weather_to_aoi_distance_km",
        "remote_mean_change_index",
        "exposure_service_index"
      ],
      "rationale": "AOI service exposure is high but remote mean change is weak and the weather-to-AOI distance is large, so local deployment needs confirmation."
    }
  ],
  "mechanism_chain": [
    "Summer inflow did not produce the normal lake swelling described in the report.",
    "The late lake-drop window contains a 17-day Tmax >= 35 C sequence with frequent hot nights and high apparent temperature.",
    "Package precipitation products share an end date weeks before the reported late-August low-water observations.",
    "The report-based level sequence shows a 3.03 m decline over 24 days, while AOI mean remote-sensing change remains weak.",
    "The +2 C and 10-day continued-drop scenario raises the response score from high to very high."
  ],
  "final_interpretation": "Package evidence supports a high-priority heat-drought low-water response centered on water access and heat operations, with scenario conditions escalating the priority while AOI exposure must be used cautiously because spatial transfer uncertainty is large."
}
```

# Key Computations

Use `data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json` for the package event window: 2022-06-01 to 2022-08-31. Use `data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html` for the lake process narrative, the July 10 and August 27 image dates, the August 6 dry-season threshold level of 11.99 m, the August 30 level of 8.96 m, and the statement that the dry-season threshold arrived roughly 100 days early.

Lake drop:

```text
drop_m = 11.99 - 8.96 = 3.03 m
drop_percent = 3.03 / 11.99 * 100 = 25.3%
drop_rate_m_per_day = 3.03 / 24 = 0.126 m/day
drop_rate_cm_per_day = 12.6 cm/day
image_span_days = 2022-08-27 - 2022-07-10 = 48 days
```

From `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`, restrict the heat run to 2022-08-06 through 2022-08-30. The longest `temperature_2m_max >= 35 C` run is 2022-08-07 through 2022-08-23, 17 days, with `sum(max(Tmax - 35, 0)) = 21.3 C-day`. Fourteen of those 17 days have `temperature_2m_min >= 28 C`, so the hot-night fraction is `14 / 17 = 0.824`. The longest `apparent_temperature_max >= 40 C` run is 2022-08-08 through 2022-08-23, 16 days, with 27.1 C-day apparent heat load and a 44.0 C peak on 2022-08-20.

Precipitation evidence uses `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`, `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`, and `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`. GPM and CHIRPS share 2022-06-01 to 2022-07-16. Their means are 519.7 mm and 387.6 mm, a spread of 132.1 mm and a GPM/CHIRPS ratio of 1.341. The shared end date is 21 days before the dry-season threshold, 42 days before the lake image, and 45 days before the last reported level. ERA5 mean precipitation is 271.1 mm over the same package period and is retained as a third precipitation context value.

Remote-sensing change uses AOI mean values, not maxima. `data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json` gives mean dNBR 0.009274 and maximum 0.538638. `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json` gives mean embedding change 0.013761 and maximum 0.250799. The mean-change index is low:

```text
remote_mean_change_index =
100 * (0.50 * min(0.009274 / 0.05, 1)
     + 0.50 * min(0.013761 / 0.05, 1))
= 23.0
```

Exposure context uses `data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json`, `data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json`, and `data/exposure_impact/exposure_impact_005_OpenStreetMap_Overpass_bounded_AOI_slice.json`. The weather point is 30.475, 112.526 and the compact AOI centroid is 36.000, 120.500, giving a 962.4 km separation. This is why AOI exposure is useful as planning context but not a direct Poyang impact population count. The AOI population is 2,485,012.3. The bounded OSM slice has 24 hospitals, 28 police stations, 7 fire stations, 12 shelters, 71 critical services, 170 major road ways, and 29 bridge ways.

Baseline indices:

```text
heat_persistence_index =
100 * (0.40 * 17/21 + 0.25 * 21.3/30 + 0.20 * 0.824 + 0.15 * 27.1/40)
= 76.8

lake_drop_index =
100 * (0.45 * 12.6/15 + 0.35 * 25.3/30 + 0.20 * 100/120)
= 84.0

late_precip_gap_index =
100 * (0.50 * 45/45 + 0.30 * 42/45 + 0.20 * 132.1/150)
= 95.6

exposure_service_index =
100 * (0.45 * 2485012.3/2500000 + 0.25 * 71/75 + 0.20 * 170/175 + 0.10 * 29/30)
= 97.5

response_priority_score =
0.35 * 76.8 + 0.30 * 84.0 + 0.15 * 95.6 + 0.20 * 97.5
= 85.9
```

Scenario: add 2.0 C to daily maximum, minimum, and apparent temperatures in the late lake-drop window. The longest `Tmax >= 35 C` run becomes 2022-08-06 through 2022-08-26, 21 days, with 59.1 C-day heat load and 19 hot nights, so the hot-night fraction is 0.905. The apparent heat run also becomes 21 days, with 65.3 C-day load and a 46.0 C peak. Continue the observed lake drop rate for 10 days after 2022-08-30:

```text
additional_drop_m = (3.03 / 24) * 10 = 1.26 m
scenario_level_m = 8.96 - 1.26 = 7.70 m
scenario_drop_m = 11.99 - 7.70 = 4.29 m
scenario_drop_percent = 4.29 / 11.99 * 100 = 35.8%
```

The scenario heat index rises to 98.1, lake-drop index to 89.5, and response score to 95.0. The response-score delta is 9.1 points.

# Reasoning Path

1. Inspect the package inventory to locate reports, daily weather, precipitation summaries, remote-sensing change statistics, AOI geometry, WorldPop population, and bounded OSM exposure files.
2. Read the event window from the locked anchor and use the Poyang report for lake dates, water levels, early dry-season timing, and affected sectors.
3. Compute late-window heat persistence from daily maximum, minimum, and apparent temperatures.
4. Compare GPM, CHIRPS, and ERA5 precipitation means and measure their shared-window gap to the lake dates.
5. Use mean dNBR and mean embedding change for AOI-scale surface change, retaining maxima only to show that isolated maxima are not the mean-change conclusion.
6. Count AOI services and road elements, compute the weather-to-AOI distance, and treat that distance as a transfer uncertainty.
7. Apply the baseline formulas, then repeat heat and lake-drop formulas for the +2 C and 10-day continued-drop scenario.
8. Rank response priorities from the resulting physical stress, water-level trajectory, service exposure, and uncertainty.

# Scoring Rubric

Total: 20 points.

1. Self-directed package discovery and citations, 2 points: finds the relevant report, heat, precipitation, remote-sensing, AOI, population, and OSM exposure records without visible filename hints, and cites package-relative paths.
2. Lake timeline and drop dynamics, 3 points: extracts the event window, image dates, dry-season start, lake levels, 3.03 m drop, 25.3 percent decline, 24-day span, and 12.6 cm/day mean drop rate.
3. Heat-stress sequence calculations, 3 points: computes the late-window 17-day Tmax >= 35 C run, 21.3 C-day heat load, 14 hot nights, 0.824 hot-night fraction, 16-day apparent >= 40 C run, 27.1 C-day apparent load, and 44.0 C peak.
4. Precipitation evidence and timing gap, 3 points: compares GPM, CHIRPS, and ERA5 summaries, including 519.7 mm, 387.6 mm, 271.1 mm, 132.1 mm product spread, 1.341 GPM/CHIRPS ratio, and the 21/42/45 day gaps to lake dates.
5. Remote-sensing and exposure synthesis, 3 points: uses mean dNBR and mean embedding change rather than maxima, computes the weak remote-change index, summarizes AOI population and OSM service/road counts, and flags the 962.4 km spatial transfer uncertainty.
6. Indices and response-priority model, 3 points: applies the specified formulas with clipping and rounding to produce baseline indices and a response priority score near 85.9.
7. Future scenario analysis, 2 points: applies the +2 C adjustment and 10-day continued lake drop to obtain scenario heat, lake level near 7.70 m, scenario response score near 95.0, and correct deltas.
8. Mechanism chain and operational interpretation, 1 point: gives a concise process explanation and response priorities grounded in the computed metrics, without generic disaster commentary.
