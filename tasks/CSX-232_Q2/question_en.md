# Earthquake Cascade Response-Stress Model

Use only the local CSX-232 event package. Select package-relative evidence for every evidence family used, including the evidence needed to localize the earthquake sequence before comparing shocks.

Model the 6-20 February 2023 Turkiye-Syria earthquake sequence as a compound response problem. For sequence calculations, use the event-specific ShakeMap geographic box from the local USGS event product to exclude unrelated global catalog entries before selecting the two largest local shocks.

Use these definitions, clipping every normalized term to `[0, 1]`:

- `moment_energy_ratio = 10 ** (1.5 * (second_largest_magnitude - largest_magnitude))`
- `dual_shock_gap_hours = hours between the two largest local shocks`
- `sequence_pressure = 100 * (0.30 * clip(largest_magnitude / 8) + 0.20 * clip(max_mmi / 10) + 0.20 * clip(max_slip_m / 12) + 0.15 * clip(moment_energy_ratio / 0.5) + 0.15 * clip((12 - dual_shock_gap_hours) / 12))`
- `first_day_precip_share = first_day_point_precip_mm / total_point_precip_mm`
- `freezing_night_fraction = count(min_daily_temperature_c < 0) / event_day_count`
- `gpm_spatial_contrast = (gpm_event_precip_mm_max - gpm_event_precip_mm_mean) / gpm_event_precip_mm_mean`
- `gridded_precip_load = (clip(gpm_event_precip_mm_mean / 40) + clip(era5_mean_event_precip_mm / 20)) / 2`
- `cold_wet_ground_stress = 100 * (0.35 * clip(max_mmi / 10) + 0.20 * clip(first_day_precip_share) + 0.15 * clip(gpm_spatial_contrast) + 0.15 * clip(freezing_night_fraction) + 0.15 * gridded_precip_load)`
- `red_alert_fraction = red_earthquake_alert_count / event_local_gdacs_earthquake_alert_count`, where event-local GDACS earthquake alerts are filtered with the same event-specific ShakeMap geographic box so unrelated global earthquake alerts are excluded.
- `osm_minor_road_share = count(tertiary, residential, unclassified, or service highway ways) / count(all sampled highway ways)`
- `osm_bridge_share = count(sampled highway ways tagged as bridge) / count(all sampled highway ways)`
- `exposure_access_load = 100 * (0.45 * clip(population_millions / 3) + 0.25 * clip(red_alert_fraction / 0.5) + 0.15 * clip(osm_minor_road_share) + 0.15 * clip(osm_bridge_share / 0.10))`
- `s1_spread_db = s1_max_db - s1_min_db`
- `s1_zero_centered_variability = 1 - abs(s1_mean_db) / s1_stddev_db`
- `s1_support_balance = min(pre_image_count, post_image_count) / max(pre_image_count, post_image_count)`
- `observation_disruption_signal = 100 * (0.45 * clip(s1_spread_db / 35) + 0.20 * clip(s1_zero_centered_variability) + 0.25 * clip(alphaearth_change_max / 0.6) + 0.10 * clip(s1_support_balance))`
- `compound_response_stress_index = 0.35 * sequence_pressure + 0.25 * cold_wet_ground_stress + 0.25 * exposure_access_load + 0.15 * observation_disruption_signal`

Then compute a wetter/colder response scenario in which first-day point precipitation increases by 25% while other point-precipitation days stay unchanged, GPM mean precipitation increases by 10%, GPM maximum precipitation increases by 15%, ERA5 mean precipitation increases by 10%, and the event has one additional freezing night, capped by the event-day count. Recompute only the cold/wet component and the compound index.

Priority class is `extreme_compound_response_stress` when the compound index is at least 80, `high_compound_response_stress` when it is at least 65, and `moderate_or_lower_compound_response_stress` otherwise.

Return only compact JSON with this structure:

```json
{
  "process_model": {
    "event_window": {},
    "rupture_sequence": {},
    "cold_wet_ground_stress": {},
    "exposure_access_load": {},
    "remote_sensing_disruption": {}
  },
  "computed_metrics": {
    "compound_response_stress_index": 0,
    "baseline_priority_class": ""
  },
  "scenario_analysis": {
    "scenario": "",
    "scenario_compound_response_stress_index": 0,
    "scenario_delta": 0,
    "priority_class": ""
  },
  "mechanism_chain": [],
  "source_paths": [],
  "final_interpretation": ""
}
```
