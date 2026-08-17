# Coastal Surge, Rainfall, and Wind Process Attribution Model

Use only the local event package for Hurricane Sandy's New York-New Jersey coastal flooding. Select package-relative evidence for every value you use.

Reconstruct whether the disaster process was dominated by coastal water-level forcing, short-duration rainfall/runoff, or local wind stress. Combine at least these evidence families where available in the package: official event narrative, coastal water-level/gage information, event-window point weather, gridded precipitation products, cyclone catalog context, and remote-sensing availability/status.

Compute the following:

1. `coastal_surge_index`

```text
coastal_surge_index =
100 * (0.40 * major_flood_share
     + 0.25 * return_level_share
     + 0.20 * surge_wave_report_share
     + 0.15 * mean_to_max_tide_ratio)
```

where `major_flood_share` is the fraction of coastal gages above major coastal flood elevation, `return_level_share` is the fraction above or near the FEMA 100-year water level, `surge_wave_report_share` is the fraction of required narrative anchors present, and `mean_to_max_tide_ratio` is the mean peak water level divided by the maximum peak water level.

For `surge_wave_report_share`, use five narrative anchors from the official event report: landfall near Brigantine, catastrophic surge on the New Jersey-New York coast, greatest inundation in New Jersey/New York/Connecticut, New York City metropolitan setting, and damaging waves.

2. `rainfall_runoff_index`

```text
rainfall_runoff_index =
100 * (0.30 * min(point_event_rain_mm / 100, 1)
     + 0.30 * min(gpm_mean_event_rain_mm / 100, 1)
     + 0.15 * min(era5_mean_event_rain_mm / 100, 1)
     + 0.15 * peak_hour_rain_share
     + 0.10 * wettest_6h_rain_share)
```

Also compute the precipitation-product spread ratio:

```text
precip_spread_ratio = chirps_mean_event_rain_mm / gpm_mean_event_rain_mm
```

3. `local_wind_stress_index`

```text
local_wind_stress_index =
100 * (0.55 * min(point_peak_wind_kmh / 100, 1)
     + 0.25 * wind_ge40_hour_share
     + 0.20 * min(point_peak_wind_kmh / catalog_peak_wind_kmh, 1))
```

4. `response_priority_score`

```text
response_priority_score =
100 * (0.45 * coastal_surge_index / 100
     + 0.20 * response_observation_norm
     + 0.15 * rainfall_runoff_index / 100
     + 0.10 * local_wind_stress_index / 100
     + 0.10 * surge_wave_report_share)
```

Use the package evidence on deployed/recovered storm-tide, wave, and rapid-deployment instruments plus surveyed high-water marks to compute:

```text
instrument_norm = min((storm_tide_sensor_count + wave_sensor_count + rapid_deployment_gage_count) / 50, 1)
high_water_mark_norm = min(high_water_mark_min_count / 300, 1)
response_observation_norm = 0.5 * instrument_norm + 0.5 * high_water_mark_norm
```

If a report gives high-water marks as "over N", treat `N` as a conservative lower-bound value named `high_water_mark_min_count`, not as an exact count.

Also compute:

```text
process_contrast = coastal_surge_index - max(rainfall_runoff_index, local_wind_stress_index)
```

5. `water_level_sensitivity`

Add a +0.60 m coastal water-level offset to the observed maximum tide. Report the scenario maximum in meters and feet, and the percent increase relative to the observed maximum tide in meters.

Return one valid JSON object with this schema:

```json
{
  "process_model": {
    "event_window": "",
    "dominant_process": "",
    "coastal_surge_index": 0,
    "rainfall_runoff_index": 0,
    "local_wind_stress_index": 0,
    "process_contrast": 0,
    "response_priority_score": 0
  },
  "computed_metrics": {
    "coastal_water_level": {},
    "rainfall": {},
    "wind": {},
    "response_observations": {},
    "remote_sensing_screening": {}
  },
  "scenario_analysis": {
    "water_level_offset_m": 0,
    "scenario_max_tide_m": 0,
    "scenario_max_tide_ft": 0,
    "max_tide_increase_percent": 0
  },
  "mechanism_chain": [],
  "source_paths": [],
  "final_interpretation": ""
}
```

Round index values and percentages to two decimals, shares and ratios to three decimals, meters to three decimals, feet and millimeters to two decimals, and wind speeds to two decimals.
