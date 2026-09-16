# Flood Response Priority Diagnosis

In late April and early May 2024, emergency managers in East Africa were tracking an exceptional wet-season flood episode after weeks of climate-mode-enhanced rainfall. A regional coordination team needs a compact technical diagnosis that separates the dominant disaster mechanism from weaker explanations such as unrelated heat, drought, wind, or gradual landscape change.

Classify the dominant disaster mechanism and assign the response-priority tier for the incident. Support the decision with quantitative rainfall and persistence anchors, a brief explanation of the physical driver chain, and the exposed-population or critical-asset context that makes the response priority operationally important.

Return your answer as:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority_tier": "<tier>",
  "priority_index": "<integer_0_to_100>",
  "key_metrics": {
    "regional_precip_mean_mm": "<value>",
    "point_precip_total_mm": "<value>",
    "heavy_rain_days": "<value>",
    "critical_amenities": "<value>",
    "population_exposed": "<value>"
  },
  "impact_chain": ["<driver>", "<hazard>", "<impact_priority>"]
}
```
