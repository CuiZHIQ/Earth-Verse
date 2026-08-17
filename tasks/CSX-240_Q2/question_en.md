# Day-of-Event Shelter Stress Chain

An emergency coordination cell is preparing the first-night support brief for survivors of the 26 December 2003 Bam earthquake in southeastern Iran. The earthquake struck a dry-region city with widespread structural collapse and many households unable to safely remain indoors. The team needs to decide which same-day environmental stressor should most shape immediate survivor support: cold and dry shelter exposure, rain or flood response, heat-stress response, high-wind response, or remote damage-triage as the primary driver.

Diagnose the strongest compound shelter-stress chain for that day. Anchor the answer with concise quantitative or categorical values for nighttime cold, precipitation, wind, and the building-loss context, then state the operational priority implied by those anchors.

Compute the benchmark `shelter_stress_index` as the sum of these components:

```text
cold_score = clamp((5 - mean_min_temp_c) / 5, 0, 1) * 35
dryness_score = 25 if mean_precip_mm < 0.1, else 12.5 if mean_precip_mm < 5.0, else 0
wind_score = 15 if max_wind_kmh < 25, else 7.5 if max_wind_kmh < 50, else 0
displacement_score = clamp(building_destroyed_percent / 60, 0, 1) * 20
vulnerability_score = 5 if mud-brick vulnerability is present, else 0
shelter_stress_index = cold_score + dryness_score + wind_score + displacement_score + vulnerability_score
```

Treat this as a benchmark-derived index, not an official emergency-management metric. Return a compact JSON answer:

```json
{
  "answer": "<compact_diagnosis_label>",
  "shelter_stress_index": "<number_or_band>",
  "key_anchors": {
    "nighttime_cold_level": "<value_or_short_phrase>",
    "precipitation_level": "<value_or_short_phrase>",
    "wind_level": "<value_or_short_phrase>",
    "building_loss_context": "<value_or_short_phrase>"
  },
  "impact_chain": ["<earthquake_damage_context>", "<day_of_event_environment>", "<response_priority>"]
}
```
