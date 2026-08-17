# Dust-Storm Response Priority Diagnosis

During the March 2021 East Asia dust storm, a regional emergency desk needs a short response-priority diagnosis for Mongolia, northern China, and Korea. The decision is whether the event should be handled as an acute dust-disruption episode affecting air quality, visibility, transport, and public health, or whether another pathway such as rainfall disruption, long-term land-cover damage, or low-impact observation better fits the evidence.

Base the answer on the event mechanism, short-window meteorology, exposed population and infrastructure, and whether satellite-change context supports acute dust impact versus structural land-cover damage. Treat the weather values as package point-sample meteorology and the population, road, and amenity values as exposure-context anchors, not as confirmed regional maxima or confirmed direct impacts for every exposed person.

Return your answer as:

```json
{
  "answer": "<compact_priority_label>",
  "key_metrics": {
    "peak_wind_kmh": "<value>",
    "event_precip_mm": "<value>",
    "population_millions": "<value>",
    "critical_amenities": "<value>",
    "annual_embedding_change_mean": "<value>"
  },
  "impact_chain": ["<driver>", "<hazard>", "<priority>"]
}
```
