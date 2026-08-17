# Florida Keys Marine Heat-Stress Persistence and Coral-Rescue Triage Model

Use only the local event package for CSX-330. Select package-relative evidence for every value you use, and keep the final response focused on the computed process model rather than the file-search process.

Build a disaster-science process model for the 2023 Florida Keys marine heatwave and coral bleaching event. The model should connect satellite-derived sea-surface-temperature thresholds, persistence of heat stress, coral genetic-rescue pressure, local exposure, precipitation context, and remote-sensing disturbance context.

Use these definitions:

- `above_bleaching_c = peak_sst_c - bleaching_threshold_c`.
- `above_mmm_c = peak_sst_c - maximum_monthly_mean_sst_c`.
- `duration_days` is the inclusive day count from the first reported bleaching-threshold crossing through the reported peak SST date.
- `peak_equivalent_dhw_c_weeks = above_bleaching_c * duration_days / 7`.
- DHW severity band is `below_significant` below 4 C-weeks, `significant_not_severe` from 4 to below 8 C-weeks, and `severe_equivalent` at or above 8 C-weeks.
- `precip_consensus_mean_mm` is the mean of the event-window accumulated precipitation means from three gridded precipitation or reanalysis products in the package.
- `precip_spread_ratio = largest_precip_mean / smallest_precip_mean`.
- `minimum_rescue_fragments = 2 * (unique_elkhorn_individuals + unique_staghorn_individuals)`.
- `osm_emergency_facilities` is the count of package AOI OSM elements tagged as `amenity=fire_station`, `amenity=police`, or `amenity=shelter`.
- `remote_disturbance_norm = clip(((embedding_change_mean / 0.05) + (abs(dnbr_mean) / 0.10)) / 2, 0, 1)`.

Normalize and score as follows:

```text
thermal_dhw_norm = clip(peak_equivalent_dhw_c_weeks / 8, 0, 1)
duration_norm = clip(duration_days / 45, 0, 1)
hotspot_norm = clip(above_bleaching_c / 3, 0, 1)
mmm_anomaly_norm = clip(above_mmm_c / 4, 0, 1)
precip_norm = clip(precip_consensus_mean_mm / 250, 0, 1)
population_norm = clip(worldpop_population / 50000, 0, 1)
genetic_rescue_norm = clip(minimum_rescue_fragments / 1000, 0, 1)
facility_coordination_norm = clip(osm_emergency_facilities / 30, 0, 1)

marine_heat_stress_index =
100 * (0.40 * thermal_dhw_norm
     + 0.25 * duration_norm
     + 0.20 * hotspot_norm
     + 0.15 * mmm_anomaly_norm)

coral_rescue_priority_score =
100 * (0.40 * marine_heat_stress_index / 100
     + 0.25 * genetic_rescue_norm
     + 0.15 * population_norm
     + 0.10 * precip_norm
     + 0.10 * facility_coordination_norm)
```

Run two counterfactuals with all non-thermal context held fixed:

1. `storm_mixing_cool_peak`: reduce the reported peak SST by 1.5 C, keep the same threshold-to-peak duration, and recompute the DHW band, marine heat-stress index, and rescue-priority score.
2. `continued_hot_persistence`: increase the reported peak SST by 0.5 C, extend the threshold-duration by 14 days, and recompute the same outputs.

Set `answer_label` to `extreme_persistent_heat_stress_with_immediate_coral_rescue_priority` when the baseline DHW band is `severe_equivalent`, `marine_heat_stress_index >= 85`, and `coral_rescue_priority_score >= 85`; otherwise use `lower_priority_or_incomplete_heat_stress_signal`.

Return one JSON object, with no prose outside the JSON, using this structure:

```json
{
  "answer_label": "<label>",
  "source_paths": {
    "event_narrative": ["<package-relative path>", "..."],
    "heat_monitoring": ["<package-relative path>", "..."],
    "precipitation": ["<package-relative path>", "..."],
    "exposure_response": ["<package-relative path>", "..."],
    "remote_sensing": ["<package-relative path>", "..."],
    "geospatial_context": ["<package-relative path>", "..."]
  },
  "process_model": {
    "sst_anchors_c": {"maximum_monthly_mean": "<number>", "bleaching_threshold": "<number>", "peak": "<number>"},
    "event_timing": {"threshold_crossing_date": "<YYYY-MM-DD>", "peak_sst_date": "<YYYY-MM-DD>", "duration_days": "<integer>"},
    "thermal_exceedance": {"above_bleaching_c": "<number>", "above_mmm_c": "<number>", "peak_equivalent_dhw_c_weeks": "<number>", "dhw_severity_band": "<label>"}
  },
  "context_metrics": {
    "precipitation_mm": {"gpm_mean": "<number>", "chirps_mean": "<number>", "era5_mean": "<number>", "precip_consensus_mean": "<number>", "precip_spread_ratio": "<number>"},
    "exposure_response": {"worldpop_population": "<integer>", "osm_emergency_facilities": "<integer>", "unique_elkhorn_individuals": "<integer>", "unique_staghorn_individuals": "<integer>", "minimum_rescue_fragments": "<integer>", "forecast_persistence_chance_percent": ["<integer>", "<integer>"]},
    "remote_sensing": {"embedding_change_mean": "<number>", "dnbr_mean": "<number>", "remote_disturbance_norm": "<number>"}
  },
  "computed_metrics": {
    "normalizers": {"thermal_dhw_norm": "<number>", "duration_norm": "<number>", "hotspot_norm": "<number>", "mmm_anomaly_norm": "<number>", "precip_norm": "<number>", "population_norm": "<number>", "genetic_rescue_norm": "<number>", "facility_coordination_norm": "<number>"},
    "marine_heat_stress_index": "<number>",
    "coral_rescue_priority_score": "<number>"
  },
  "scenario_analysis": {
    "storm_mixing_cool_peak": {"peak_sst_c": "<number>", "duration_days": "<integer>", "peak_equivalent_dhw_c_weeks": "<number>", "dhw_severity_band": "<label>", "marine_heat_stress_index": "<number>", "coral_rescue_priority_score": "<number>", "priority_delta_from_baseline": "<number>"},
    "continued_hot_persistence": {"peak_sst_c": "<number>", "duration_days": "<integer>", "peak_equivalent_dhw_c_weeks": "<number>", "dhw_severity_band": "<label>", "marine_heat_stress_index": "<number>", "coral_rescue_priority_score": "<number>", "priority_delta_from_baseline": "<number>"}
  },
  "mechanism_chain": ["<short process statement>", "..."],
  "final_interpretation": "<one concise sentence>"
}
```

Round temperatures and DHW values to 2 decimals, precipitation means to 1 decimal, ratios and normalized values to 3 decimals, and index/priority scores to 2 decimals.
