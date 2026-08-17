# August 2023 Central Chile Flood Response Classification

In late August 2023, central Chile was affected by a multi-day atmospheric-river storm sequence that struck river valleys and foothill communities in regions including Maule and Biobio. A hydrometeorology response cell is preparing a concise situation classification for planners who must decide whether the acute priority is flood and access response or a different hazard pathway.

Determine the dominant disaster mechanism and response-priority tier for the event. Your assessment should weigh the physical driver, the persistence and peak of rainfall, the reported impact pathway, and the population or critical-asset context. For the numeric anchors, define `point_precip_total_mm` as the mean of the two point-sample event totals, `max_daily_point_precip_mm` as the largest single-day value across those point samples, `heavy_rain_days` as the conservative count of dates with at least 10 mm/day in both point samples, and `critical_amenities` as hospital, clinic, school, or shelter features in the package context slice. Treat antecedent drought, wind, heat, and annual land-surface change as competing explanations only if they better account for the acute impacts.

Return your answer as JSON:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority_tier": "<tier>",
  "priority_index": "<integer_0_to_100>",
  "key_metrics": {
    "point_precip_total_mm": "<value>",
    "max_daily_point_precip_mm": "<value>",
    "heavy_rain_days": "<value>",
    "critical_amenities": "<value>",
    "population_exposed": "<value>"
  },
  "impact_chain": ["<driver>", "<hazard>", "<impact_priority>"]
}
```

Use the incident record and quantitative diagnostics for the values, and keep the justification focused on the mechanism, impact chain, and response priority.
