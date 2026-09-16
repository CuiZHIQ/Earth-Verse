# Marine Heatwave Impact Priority

Marine ecosystem analysts are reviewing the 2013-2016 Northeast Pacific marine heatwave known as "The Blob." They need a compact first-pass priority label that distinguishes persistent basin-scale ocean heat stress from short-duration rainfall, wind, urban-exposure, or terrestrial vegetation-disturbance framings.

The purpose is not to estimate final fishery losses or perform formal climate attribution. Instead, the analysts want a reproducible screening answer that captures the dominant driver, its unusually persistent oceanic scale, and the most defensible ecological impact priority while showing that common land-weather or population-response alternatives are weaker.

Classify the event as one of these compact labels:

- `basin_scale_marine_heatwave_ecosystem_heat_stress_priority`
- `rainfall_flood_or_landslide_response_priority`
- `wind_storm_or_wave_damage_infrastructure_priority`
- `urban_population_and_critical_amenity_response_priority`
- `terrestrial_burn_or_vegetation_loss_priority`
- `insufficient_evidence_for_priority`

Return your response as:

```json
{
  "answer": "<compact_label>",
  "priority_index": "<0_to_1_value>",
  "key_metrics": {
    "event_window_days": "<value>",
    "event_window_years": "<value>",
    "source_result_count": "<value>",
    "marine_heatwave_term_count": "<value>",
    "ecosystem_impact_term_count": "<value>",
    "northeast_pacific_reference_count": "<value>"
  },
  "impact_chain": ["<driver>", "<hazard>", "<impact_priority>"]
}
```
