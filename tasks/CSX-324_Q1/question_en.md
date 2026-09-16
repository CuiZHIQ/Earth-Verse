# Marine Heat-Stress Priority Reasoning

In the 2023 Northern Indian Ocean and Arabian Sea warm-season context, a regional climate-impact team is screening whether the main disaster-impact priority should be coastal ecosystem heat stress from marine heatwave conditions or a competing land-focused pathway such as land heat exposure, rainfall or flooding disruption, wind-driven coastal damage, or generic land-cover change.

Focus on mechanism and impact reasoning: event identity, seasonal duration, marine heat-stress indicator concepts, and whether the local package evidence supports a marine ecosystem priority without inventing precise SST anomaly, Degree Heating Week, coral mortality, flood-loss, or wind-damage values.

Return your answer as:

```json
{
  "answer": "<compact_priority_label>",
  "priority": "<operational_priority>",
  "dominant_mechanism": "<short_mechanism>",
  "impact_pathway": ["<driver>", "<hazard_or_index>", "<impact_receptor>"],
  "key_metrics": {
    "event_window_days": "<value>",
    "marine_evidence_score": "<value>",
    "marine_evidence_score_max": "<value>",
    "marine_index_term_count": "<value>",
    "marine_index_terms": ["<term>", "..."],
    "source_flags": {
      "wmo_surface_temperature_context": "<true_or_false>",
      "wmo_ecosystem_context": "<true_or_false>",
      "oisst_2023_sst_available": "<true_or_false>",
      "oisst_2023_sst_anomaly_available": "<true_or_false>",
      "coral_bleaching_heat_stress_concept": "<true_or_false>"
    }
  }
}
```
