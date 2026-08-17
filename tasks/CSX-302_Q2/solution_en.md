# Correct Answer

```json
{
  "source_paths": {
    "event_context": [
      "metadata/event.json",
      "data/event_reports/event_reports_003_Locked_event_anchor_June_2020_Saharan_dust_outbreak_to_Caribbean_and_U.S.json",
      "metadata/files.csv"
    ],
    "remote_sensing": [
      "data/remote_sensing/remote_sensing_005_pre.jpg",
      "data/remote_sensing/remote_sensing_006_event.jpg",
      "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json"
    ],
    "weather_and_precipitation": [
      "data/physical_hazard/physical_hazard_001_NASA_POWER_daily_point_sample.json",
      "data/physical_hazard/physical_hazard_002_Open-Meteo_archive_point_sample.json",
      "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json",
      "data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json",
      "data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json"
    ],
    "exposure_and_aoi": [
      "data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json",
      "data/exposure_impact/exposure_impact_004_OpenStreetMap_Overpass_bounded_AOI_slice.json",
      "data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json"
    ]
  },
  "process_model": {
    "event_window": {
      "start_date": "2020-06-14",
      "end_date": "2020-06-28",
      "duration_days": 15,
      "event_scene_offset_days": 7,
      "pre_scene_gap_days": 30
    },
    "mechanism_chain": [
      "official event context identifies a June 2020 Saharan dust outbreak reaching the Caribbean and United States",
      "paired true-color scenes show event-window haze/color change over the sampled sector",
      "low annual embedding change reduces the chance that the signal is persistent land-surface change",
      "mostly dry point records and moderate regional precipitation imply incomplete local rain scavenging",
      "wind, warm daily maxima, exposed population, roads, and critical amenities set the operational response load"
    ]
  },
  "computed_metrics": {
    "plume_visibility": {
      "brightness_delta": -2.888,
      "red_blue_delta": 1.358,
      "plume_visibility_norm": 0.534
    },
    "surface_confound_resistance": 0.536,
    "dry_scavenging_resistance": {
      "point_dry_fraction": 0.8,
      "regional_precip_mean_mm": 30.1,
      "value": 0.694
    },
    "transport_mixing": {
      "combined_wind_ms": 2.6,
      "archive_mean_daily_max_temperature_c": 20.5,
      "value": 0.469
    },
    "exposure_pressure": {
      "aoi_area_km2": 35714.8,
      "population": 49269.9,
      "population_density_per_km2": 1.4,
      "road_element_count": 973,
      "critical_amenity_count": 27,
      "access_sensitive_feature_count": 12,
      "value": 0.611
    },
    "baseline_dust_operational_stress_index": 57.2
  },
  "scenario_analysis": {
    "scenario_name": "warmer_windier_25pct_exposure_growth",
    "scenario_transport_mixing_norm": 0.563,
    "scenario_exposure_pressure_norm": 0.721,
    "scenario_index": 60.8,
    "scenario_delta": 3.6
  },
  "response_priorities": [
    {
      "rank": 1,
      "priority": "respiratory_health_and_visibility_alerting",
      "basis": "plume visibility, dry scavenging resistance, and exposed population make health messaging and visibility caution the leading action."
    },
    {
      "rank": 2,
      "priority": "road_and_access_corridor_monitoring",
      "basis": "the AOI contains many road elements and access-sensitive features that could be affected by haze-related visibility degradation."
    },
    {
      "rank": 3,
      "priority": "critical_facility_contingency_checks",
      "basis": "hospitals, schools, police, fire, and shelter amenities are present in the sampled sector and should be prepared for air-quality inquiries."
    }
  ],
  "final_interpretation": "The sampled sector shows a moderate dust-operational stress signal: transient haze/color change is supported by dry persistence and nontrivial exposure, while the scenario raises the index mainly through stronger mixing and higher exposed-load assumptions."
}
```

# Computation

The event context gives a 2020-06-14 to 2020-06-28 window, so the inclusive duration is 15 days. The manifest snapshot times place the pre-event scene on 2020-05-15 and the event scene on 2020-06-21, giving a 30-day pre-scene gap and a 7-day event-scene offset.

Image means from the paired true-color scenes are:

- pre-event brightness `136.551`, event brightness `133.663`, so `brightness_delta = -2.888`;
- pre-event red-minus-blue `9.017`, event red-minus-blue `10.375`, so `red_blue_delta = 1.358`;
- `plume_visibility_norm = 0.65 * (2.888 / 5) + 0.35 * (1.358 / 3) = 0.534`.

The annual embedding-change mean is `0.0251` and maximum is `0.3917`, so `surface_confound_resistance = 0.60 * (1 - 0.0251 / 0.10) + 0.40 * (1 - 0.3917 / 0.50) = 0.536`.

The point-weather dry-day fractions are `11/15 = 0.733` from NASA POWER and `13/15 = 0.867` from the archive record, giving `point_dry_fraction = 0.800`. The GPM and CHIRPS regional precipitation means are `25.031 mm` and `35.255 mm`, so their mean is `30.143 mm`, rounded to `30.1 mm`. Thus `dry_scavenging_resistance = 0.65 * 0.800 + 0.35 * (1 - 30.143 / 60) = 0.694`.

The transport inputs are NASA POWER mean wind `2.483 m/s`, archive mean wind maximum `13.033 km/h = 3.620 m/s`, and ERA5 vector wind `sqrt(1.153^2 + 0.265^2) = 1.183 m/s`. The weighted wind is `2.564 m/s`, rounded to `2.6 m/s`. Archive mean daily maximum temperature is `20.513 C`, rounded to `20.5 C`, so `transport_mixing_norm = 0.469`.

The compact AOI polygon gives an area of `35714.8 km2`. WorldPop gives `49269.9` people, or `1.4 people/km2`. The broader bounded AOI slice contains `973` mapped road elements, `27` critical amenities, and `12` access-sensitive road features. Therefore `exposure_pressure_norm = 0.611`.

Baseline:

```text
100 * (0.35 * 0.534
     + 0.20 * 0.694
     + 0.15 * 0.469
     + 0.20 * 0.611
     + 0.10 * 0.536)
= 57.2
```

Scenario:

Increasing all wind inputs by 15%, temperature by `2 C`, and exposure counts by 25% gives `scenario_transport_mixing_norm = 0.563` and `scenario_exposure_pressure_norm = 0.721`.

```text
100 * (0.35 * 0.534
     + 0.20 * 0.694
     + 0.15 * 0.563
     + 0.20 * 0.721
     + 0.10 * 0.536)
= 60.8
```

The scenario delta is `60.8 - 57.2 = 3.6`.

# Reasoning Path

The event is a trans-Atlantic Saharan dust outbreak, but the package's computable exposure evidence is a sampled local AOI. The answer therefore treats the AOI as a downwind operational sector rather than as the full dust footprint. The paired imagery supplies the transient haze/color signal, annual embedding-change statistics reduce the chance of confusing that signal with persistent surface change, weather and precipitation records describe rainout and transport support, and population/OSM/AOI data translate the atmospheric signal into operational load.

# Scoring Rubric

- 3 points: Finds the relevant package evidence without being given exact filenames and cites package-relative paths for event context, imagery, weather, precipitation, exposure, and AOI geometry.
- 3 points: Correctly extracts the event window, scene dates, image dimensions, brightness delta, red-blue delta, and plume-visibility normalization.
- 4 points: Correctly computes surface-confound resistance, point dry-day fractions, regional precipitation mean, dry-scavenging resistance, wind conversion, ERA5 vector wind, and transport-mixing normalization.
- 3 points: Correctly estimates AOI area, population density, road elements, critical amenities, access-sensitive features, and exposure-pressure normalization.
- 3 points: Applies the weighted baseline index and warmer, windier, 25 percent exposure-growth scenario with correct scenario delta.
- 2 points: Explains the chain from trans-Atlantic dust/haze expression through low local rainout, transport support, and sampled operational exposure without claiming the AOI is the full plume footprint.
- 2 points: Returns valid JSON matching the requested schema, rounds values appropriately, and keeps response priorities grounded in the computed metrics.
