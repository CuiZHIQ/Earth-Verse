# Final Answer

```json
{
  "answer": "coral_bleaching_rescue_clock_severe_dhw_escalation",
  "source_files_used": [
    "metadata/event.json",
    "data/event_reports/event_reports_003_Locked_event_anchor_2023_Florida_Keys_marine_heatwave_and_coral_bleaching.json",
    "data/event_reports/event_reports_001_Locked_package_evidence_report.html",
    "data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json",
    "data/exposure_impact/exposure_impact_003_OpenStreetMap_Overpass_bounded_AOI_slice.json",
    "data/remote_sensing/remote_sensing_002_Google_Satellite_Embedding_annual_cosine-change_stats.json",
    "data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json"
  ],
  "thermal_threshold_clock": {
    "maximum_monthly_mean_c": 29.63,
    "bleaching_threshold_c": 30.63,
    "peak_sst_c": 33.6,
    "peak_exceedance_c": 2.97,
    "threshold_cross_date": "2023-06-14",
    "peak_sst_date": "2023-07-13",
    "threshold_to_peak_elapsed_days": 29,
    "constant_peak_dhw_by_peak_date_c_weeks": 12.3
  },
  "dhw_escalation": {
    "days_to_4_c_weeks_at_peak_exceedance": 9.4,
    "days_to_8_c_weeks_at_peak_exceedance": 18.9,
    "severe_threshold_reached_before_peak_under_constant_peak_assumption": true,
    "plus_14_days_at_peak_exceedance_additional_c_weeks": 5.9,
    "scenario_total_dhw_if_14_more_peak_days": 18.2,
    "days_to_8_c_weeks_if_peak_plus_0p5c": 16.1
  },
  "ecological_and_rescue_context": {
    "record_warm_since_1985_mentioned": true,
    "widespread_bleaching_and_death_mentioned": true,
    "mission_iconic_reef_response_mentioned": true,
    "nursery_colonies_relocated_mentioned": true,
    "staghorn_and_elkhorn_genetic_preservation_mentioned": true
  },
  "coastal_logistics_context": {
    "worldpop_population_sum": 46416.0,
    "sampled_roads": 964,
    "sampled_major_roads": 32,
    "sampled_bridges": 3,
    "sampled_schools": 9,
    "embedding_change_max": 0.2862,
    "sentinel2_dnbr_mean": -0.012
  },
  "priority_model": {
    "primary_priority": "protect live nursery corals and genetically unique staghorn/elkhorn fragments before severe DHW accumulation outruns rescue capacity",
    "second_priority": "coordinate Keys road/bridge logistics for tank transport, lab capacity, and staff access",
    "third_priority": "monitor additional heat days because the DHW clock accelerates with anomaly persistence"
  },
  "recommended_reasoning_path": [
    "Convert SST above the bleaching threshold into DHW accumulation time, rather than only describing warm water.",
    "Compare the 4 and 8 C-week clocks with the June 14 to July 13 threshold-to-peak interval.",
    "Use rescue text and local logistics exposure to explain why timing matters for coral triage.",
    "Use remote-sensing summaries only as ecosystem/coastal context, not as direct coral mortality counts."
  ]
}
```

# Source Files Used

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_2023_Florida_Keys_marine_heatwave_and_coral_bleaching.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_003_OpenStreetMap_Overpass_bounded_AOI_slice.json`
- `data/remote_sensing/remote_sensing_002_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json`

# Key Computations

- `thermal_threshold_clock.maximum_monthly_mean_c` = `29.63`
- `thermal_threshold_clock.bleaching_threshold_c` = `30.63`
- `thermal_threshold_clock.peak_sst_c` = `33.6`
- `thermal_threshold_clock.peak_exceedance_c` = `2.97`
- `thermal_threshold_clock.threshold_to_peak_elapsed_days` = `29`
- `thermal_threshold_clock.constant_peak_dhw_by_peak_date_c_weeks` = `12.3`
- `dhw_escalation.days_to_4_c_weeks_at_peak_exceedance` = `9.4`
- `dhw_escalation.days_to_8_c_weeks_at_peak_exceedance` = `18.9`
- `dhw_escalation.plus_14_days_at_peak_exceedance_additional_c_weeks` = `5.9`
- `dhw_escalation.scenario_total_dhw_if_14_more_peak_days` = `18.2`
- `dhw_escalation.days_to_8_c_weeks_if_peak_plus_0p5c` = `16.1`
- `coastal_logistics_context.worldpop_population_sum` = `46416.0`
- `coastal_logistics_context.sampled_roads` = `964`
- `coastal_logistics_context.sampled_major_roads` = `32`
- `coastal_logistics_context.sampled_bridges` = `3`
- `coastal_logistics_context.sampled_schools` = `9`
- `coastal_logistics_context.embedding_change_max` = `0.2862`
- `coastal_logistics_context.sentinel2_dnbr_mean` = `-0.012`

# Reasoning Path

- Convert SST above the bleaching threshold into DHW accumulation time, rather than only describing warm water.
- Compare the 4 and 8 C-week clocks with the June 14 to July 13 threshold-to-peak interval.
- Use rescue text and local logistics exposure to explain why timing matters for coral triage.
- Use remote-sensing summaries only as ecosystem/coastal context, not as direct coral mortality counts.

# Scoring Rubric

Total: 20 points.

- 3 points: json_and_sources. Returns JSON and cites event/report, population, OSM, embedding, and Sentinel-2 context files. Partial credit: Partial credit for valid JSON using report only.
- 5 points: thermal_clock. Extracts MMM 29.63 C, bleaching threshold 30.63 C, peak SST 33.60 C, exceedance 2.97 C, June 14 to July 13 as 29 days, and 12.3 C-weeks by peak date. Partial credit: Value-by-value credit within tolerance.
- 4 points: dhw_escalation. Computes 9.4 days to 4 C-weeks, 18.9 days to 8 C-weeks, 5.9 additional C-weeks for 14 more peak days, total 18.2 C-weeks, and 16.1 days to 8 C-weeks with +0.5 C. Partial credit: Partial credit for correct DHW formula with missing scenario.
- 3 points: ecological_rescue_context. Uses record-warm, widespread bleaching/death, Mission: Iconic Reef, nursery relocation, and staghorn/elkhorn preservation clues. Partial credit: Partial credit for ecological context without rescue timing.
- 3 points: logistics_reasoning. Connects WorldPop, roads, major roads, bridges, and schools to Keys transport and lab-rescue logistics. Partial credit: Partial credit for exposure counts without logistics interpretation.
- 2 points: limits. Does not infer exact reef-by-reef mortality or daily observed DHW from summary text alone. Partial credit: Give 1 point for minor overreach.
