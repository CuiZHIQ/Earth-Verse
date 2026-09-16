# Correct Answer

```json
{
  "answer_label": "extreme_persistent_heat_stress_with_immediate_coral_rescue_priority",
  "source_paths": {
    "event_narrative": ["data/event_reports/event_reports_001_Locked_package_evidence_report.html"],
    "heat_monitoring": ["data/event_reports/event_reports_001_Locked_package_evidence_report.html", "data/other/other_001_NOAA_Coral_Reef_Watch_5km_products.html"],
    "precipitation": ["data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json", "data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json", "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json"],
    "exposure_response": ["data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json", "data/exposure_impact/exposure_impact_003_OpenStreetMap_Overpass_bounded_AOI_slice.json", "data/event_reports/event_reports_001_Locked_package_evidence_report.html", "data/exposure_impact/exposure_impact_001_ReefBase_Allen_Coral_Atlas_protected_areas.html"],
    "remote_sensing": ["data/remote_sensing/remote_sensing_002_Google_Satellite_Embedding_annual_cosine-change_stats.json", "data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json"],
    "geospatial_context": ["data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json", "data/geospatial_context/geospatial_context_003_04_nominatim.json.json"]
  },
  "process_model": {
    "sst_anchors_c": {"maximum_monthly_mean": 29.63, "bleaching_threshold": 30.63, "peak": 33.6},
    "event_timing": {"threshold_crossing_date": "2023-06-14", "peak_sst_date": "2023-07-13", "duration_days": 30},
    "thermal_exceedance": {"above_bleaching_c": 2.97, "above_mmm_c": 3.97, "peak_equivalent_dhw_c_weeks": 12.73, "dhw_severity_band": "severe_equivalent"}
  },
  "context_metrics": {
    "precipitation_mm": {"gpm_mean": 122.7, "chirps_mean": 243.0, "era5_mean": 217.2, "precip_consensus_mean": 194.3, "precip_spread_ratio": 1.98},
    "exposure_response": {"worldpop_population": 46416, "osm_emergency_facilities": 27, "unique_elkhorn_individuals": 150, "unique_staghorn_individuals": 300, "minimum_rescue_fragments": 900, "forecast_persistence_chance_percent": [70, 100]},
    "remote_sensing": {"embedding_change_mean": 0.01, "dnbr_mean": -0.012, "remote_disturbance_norm": 0.16}
  },
  "computed_metrics": {
    "normalizers": {"thermal_dhw_norm": 1.0, "duration_norm": 0.667, "hotspot_norm": 0.99, "mmm_anomaly_norm": 0.993, "precip_norm": 0.777, "population_norm": 0.928, "genetic_rescue_norm": 0.9, "facility_coordination_norm": 0.9},
    "marine_heat_stress_index": 91.35,
    "coral_rescue_priority_score": 89.74
  },
  "scenario_analysis": {
    "storm_mixing_cool_peak": {"peak_sst_c": 32.1, "duration_days": 30, "peak_equivalent_dhw_c_weeks": 6.3, "dhw_severity_band": "significant_not_severe", "marine_heat_stress_index": 67.23, "coral_rescue_priority_score": 80.09, "priority_delta_from_baseline": -9.65},
    "continued_hot_persistence": {"peak_sst_c": 34.1, "duration_days": 44, "peak_equivalent_dhw_c_weeks": 21.81, "dhw_severity_band": "severe_equivalent", "marine_heat_stress_index": 99.44, "coral_rescue_priority_score": 92.98, "priority_delta_from_baseline": 3.24}
  },
  "mechanism_chain": [
    "Satellite SST exceeded the bleaching threshold for 30 inclusive days before the reported peak.",
    "The peak-equivalent heat accumulation exceeded the severe bleaching and mortality threshold.",
    "Low land-surface disturbance metrics make direct heat stress the dominant process signal in the package evidence.",
    "Genetically unique elkhorn and staghorn rescue needs create immediate triage pressure alongside exposed Keys communities."
  ],
  "final_interpretation": "The package supports an extreme, persistent marine heat-stress event requiring immediate coral-rescue prioritization, with storm mixing able to reduce but not remove the operational concern."
}
```

# Computation

The event report gives the thermal anchors: MMM `29.63 C`, bleaching threshold `30.63 C`, and peak SST `33.60 C`. It also states that the threshold was crossed on June 14 and the peak was on July 13, so the inclusive duration is `30` days.

Thermal exceedance:

```text
above_bleaching_c = 33.60 - 30.63 = 2.97
above_mmm_c = 33.60 - 29.63 = 3.97
peak_equivalent_dhw_c_weeks = 2.97 * 30 / 7 = 12.73
```

Because `12.73 >= 8`, the baseline DHW band is `severe_equivalent`.

Context metrics:

```text
precip_consensus_mean = (122.7346 + 243.0468 + 217.1942) / 3 = 194.3 mm
precip_spread_ratio = 243.0468 / 122.7346 = 1.98
minimum_rescue_fragments = 2 * (150 + 300) = 900
osm_emergency_facilities = 12 fire stations + 6 police + 9 shelters = 27
remote_disturbance_norm = ((0.009982 / 0.05) + (abs(-0.011960) / 0.10)) / 2 = 0.160
```

Baseline normalized values:

```text
thermal_dhw_norm = clip(12.73 / 8) = 1.000
duration_norm = 30 / 45 = 0.667
hotspot_norm = 2.97 / 3 = 0.990
mmm_anomaly_norm = 3.97 / 4 = 0.993
precip_norm = 194.3 / 250 = 0.777
population_norm = 46416 / 50000 = 0.928
genetic_rescue_norm = 900 / 1000 = 0.900
facility_coordination_norm = 27 / 30 = 0.900
```

Scores:

```text
marine_heat_stress_index =
100 * (0.40*1.000 + 0.25*0.667 + 0.20*0.990 + 0.15*0.993)
= 91.35

coral_rescue_priority_score =
100 * (0.40*0.9135 + 0.25*0.900 + 0.15*0.928 + 0.10*0.777 + 0.10*0.900)
= 89.74
```

The label rule is met because the DHW band is severe, the heat index is above `85`, and the priority score is above `85`.

Scenario recomputation:

```text
storm_mixing_cool_peak:
peak = 32.10 C
above_bleaching = 1.47 C
DHW = 1.47 * 30 / 7 = 6.30 C-weeks
heat index = 67.23
priority = 80.09
delta = -9.65

continued_hot_persistence:
peak = 34.10 C
above_bleaching = 3.47 C
duration = 44 days
DHW = 3.47 * 44 / 7 = 21.81 C-weeks
heat index = 99.44
priority = 92.98
delta = +3.24
```

# Scoring Rubric

- 3 points: Finds relevant package files independently and cites package-relative paths across narrative, heat-monitoring, precipitation, exposure, remote-sensing, and geospatial evidence.
- 4 points: Reconstructs the thermal process: MMM `29.63 C`, threshold `30.63 C`, peak `33.60 C`, June 14 crossing, July 13 peak, `30` inclusive days, `2.97 C`, `3.97 C`, and `12.73 C-weeks`.
- 4 points: Computes multi-source context: precipitation means `122.7`, `243.0`, `217.2 mm`; consensus `194.3 mm`; spread ratio `1.98`; population `46416`; emergency facilities `27`; rescue fragments `900`; remote disturbance norm `0.160`.
- 4 points: Applies clipping, normalized variables, heat index `91.35`, rescue-priority score `89.74`, severe DHW band, and the final label.
- 3 points: Correctly recomputes both counterfactual scenarios and reports the DHW bands, scores, and deltas.
- 2 points: Gives a concise disaster-process interpretation tying persistent heat accumulation to bleaching/mortality risk, coral rescue pressure, community exposure, and the contextual role of remote-sensing disturbance.
