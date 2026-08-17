# Marmolada Glacier Collapse Impact Priority

An Alpine civil-protection analyst is preparing a technical note on the 3 July 2022 Marmolada glacier collapse in northern Italy. The decision team needs to know which interpretation should drive first-priority impact reasoning: a warm-condition cryosphere collapse with direct life-safety consequences, a rainfall-driven flood or glacial-lake outburst concern, a wind or storm infrastructure problem, an urban service-exposure issue, a vegetation or burn-change signal, or a case where the incident record is too weak to prioritize.

Using the incident record and quantitative diagnostics, classify the event with one compact label and support it with the casualty, thermal, precipitation, and wind anchors that make the classification physically stronger than the alternatives.

Return your response as JSON:

```json
{
  "answer": "<compact_label>",
  "priority_index": "<0_to_1_value>",
  "key_metrics": {
    "fatalities": "<value>",
    "injuries": "<value>",
    "high_elevation_tmax_c": "<value>",
    "high_elevation_precip_mm": "<value>",
    "high_elevation_wind_kmh": "<value>"
  },
  "impact_chain": ["<driver>", "<hazard>", "<impact_priority>"]
}
```

Use one of these compact labels: `heat_conditioned_serac_collapse_life_safety_priority`, `rainfall_triggered_flood_or_glof_priority`, `wind_or_storm_infrastructure_priority`, `urban_critical_amenity_exposure_priority`, `vegetation_or_burn_change_priority`, or `insufficient_evidence_for_priority`.
