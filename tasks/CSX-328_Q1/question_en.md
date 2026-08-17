# Great Barrier Reef Bleaching Priority Brief

A marine incident analysis team is preparing a short technical brief on the 2016 Great Barrier Reef marine heatwave and mass coral bleaching episode, covering the February through May 2016 event window along the reef.

The decision needed for the brief is whether the response analysis should prioritize reef bleaching and marine ecosystem heat stress, or whether a competing land-focused pathway such as land heat exposure, rainfall or flooding disruption, wind-driven coastal damage, or generic land-cover change is more defensible.

Using the technical record and quantitative diagnostics, identify the dominant mechanism and support the priority with concrete reef and marine heat-stress anchors: the event duration, surveyed-reef bleaching severity, north-to-south severity gradient, Degree Heating Week interpretation, relevant marine heat-stress indicators, and why those reef-specific anchors dominate the priority decision.

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
    "surveyed_reefs_with_bleaching_percent": "<value>",
    "northern_severely_bleached_percent": "<value>",
    "degree_heating_week_death_possible_threshold": "<value>",
    "marine_index_terms": ["<term>", "..."]
  }
}
```
