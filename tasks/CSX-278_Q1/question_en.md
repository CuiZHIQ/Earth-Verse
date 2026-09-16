# Teleconnection-to-Drought Response Priority

A regional food-security coordination cell is preparing a short technical note on
the 2020-2023 triple-dip La Nina and the Horn of Africa drought. The immediate
decision is which disaster pathway should guide planning across Kenya, Somalia,
and Ethiopia: a persistent ENSO teleconnection that helped suppress rainy
seasons and deepen food insecurity, or a competing priority such as direct local
heat stress, flood response, or land-cover-change triage.

Return a compact JSON answer. Use quantitative anchors for cold-phase
persistence, atmospheric-coupling persistence, reported food-security scale, and
population context. Keep the reasoning focused on the mechanism-to-impact chain
and do not treat contextual land-surface change or partial rainfall summaries as
the dominant explanation.

```json
{
  "answer": "<compact_pathway_label>",
  "mechanism": "<compact_mechanism_label>",
  "priority": "<compact_priority_label>",
  "key_numeric_anchors": {
    "cold_phase_persistence": "<value>",
    "atmospheric_coupling_persistence": "<value>",
    "reported_food_security_scale": "<value>",
    "population_context": "<value>"
  },
  "impact_chain": ["<driver>", "<hazard_translation>", "<impact>", "<response_focus>"]
}
```
