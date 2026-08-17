## Final Answer

The correct answer is `marine_heat_stress_coral_rescue_priority`.

```json
{
  "answer": "marine_heat_stress_coral_rescue_priority",
  "key_metrics": {
    "peak_sst_c": 33.6,
    "bleaching_threshold_c": 30.63,
    "sst_above_bleaching_threshold_c": 2.97,
    "priority_sst_exceedance_cutoff_c": 2.0,
    "significant_bleaching_dhw_threshold_c_weeks": 4.0,
    "severe_bleaching_dhw_threshold_c_weeks": 8.0,
    "minimum_target_rescue_fragments": 900,
    "primary_nonpriority_checks": [
      "rainfall_or_terrestrial_disruption_not_reported_priority",
      "population_displacement_not_supported_by_report",
      "vegetation_or_burn_surface_change_not_the_severity_index"
    ]
  },
  "impact_chain": [
    "persistent_ocean_heat_above_bleaching_threshold",
    "degree_heating_week_bleaching_and_mortality_index",
    "coral_rescue_and_reef_protection_triage"
  ]
}
```

## Key Computations

- The event report defines the Florida Keys Maximum Monthly Mean as 29.63 C and the bleaching threshold as 30.63 C.
- Satellite-measured water temperatures crossed the bleaching threshold on June 14 and reached 33.60 C on July 13.
- `sst_above_bleaching_threshold_c = 33.60 - 30.63 = 2.97`.
- The priority cutoff used by the reference diagnosis is `2.0 C` above the bleaching threshold, so the SST exceedance clears the cutoff by `0.97 C`.
- The report states that 4 Degree Heating Weeks indicates significant coral bleaching is expected, while 8 Degree Heating Weeks indicates severe bleaching and significant mortality are expected.
- Rescue context includes relocating nursery coral colonies and targeting two live fragments from each genetically unique remaining staghorn and elkhorn coral: `(150 + 300) * 2 = 900` minimum target rescue fragments.

## Reasoning Path

1. The package is anchored as a Florida Keys marine heatwave and coral bleaching event.
2. The core mechanism is persistent ocean heat above the bleaching threshold.
3. The DHW thresholds supply the accumulated heat-stress severity frame.
4. Coral rescue and reef-protection triage are supported by the report's rescue actions.
5. Rainfall/terrestrial disruption, population displacement, and vegetation or burn-style surface change are not the reported priority mechanism.

## Scoring Rubric

20 points total:

- Priority label (4 pts): selects `marine_heat_stress_coral_rescue_priority` or an equivalent compact label.
- SST threshold computation (5 pts): reports peak SST, bleaching threshold, 2.97 C exceedance, and the explicit 2.0 C priority exceedance cutoff.
- DHW severity interpretation (3 pts): correctly uses 4 C-weeks for significant bleaching and 8 C-weeks for severe bleaching and significant mortality.
- Impact chain (3 pts): links persistent ocean heat to bleaching and mortality risk, then to coral rescue and reef-protection triage.
- Coral rescue context (2 pts): uses nursery-colony relocation and staghorn/elkhorn fragment rescue actions as priority evidence.
- Nonpriority checks (1 pt): keeps rainfall/terrestrial disruption, population displacement, and vegetation or burn-style surface change out of the primary mechanism.
- Overclaim control (2 pts): avoids unsupported exact mortality, evacuation, per-reef DHW, or outside-source claims.
