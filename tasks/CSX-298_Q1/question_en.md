# June 2020 Saharan Dust Response Priority

A Caribbean public-health and emergency-management team is preparing a short technical note on the June 2020 Saharan dust "Godzilla" outbreak. The team needs to decide which response priority should lead the disaster analysis: respiratory exposure from a long-range fine-dust plume, rainfall and flood disruption, heat-stress response, or direct land-surface damage.

Diagnose the dominant hazard mechanism and explain the impact pathway that should drive the response posture. Support the conclusion with a small set of bounded package-derived quantitative anchors, including timing, transport-relevant meteorology, precipitation context, and exposed-population context where useful. The answer should make clear why the alternative rainfall, heat, and land-damage framings are weaker for this event.

Return your answer as:

```json
{
  "answer": "<compact_mechanism_label>",
  "response_priority": "<compact_priority_label>",
  "mechanism_summary": "<one or two sentences>",
  "key_numeric_anchors": [
    {"name": "<anchor_name>", "value": "<value>", "unit": "<unit_or_null>"}
  ],
  "impact_chain": ["<source_or_driver>", "<hazard_process>", "<impact_receptor>"]
}
```
