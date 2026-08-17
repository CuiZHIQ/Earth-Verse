# Tropical Cyclone Freddy Response-Priority Diagnosis

A regional humanitarian coordination desk is preparing its first technical handover on Tropical Cyclone Freddy after its February-March 2023 traverse across the Indian Ocean and severe impacts in Madagascar, Malawi, Mozambique, and surrounding southern Africa.

Decide which response-priority posture should guide the analysis: a prolonged compound tropical-cyclone disaster, a short isolated flood episode, an image-led monitoring case, or a weak-cyclone watch. Your answer should connect Freddy's persistence, wind-rainfall-flood mechanism, humanitarian impact chain, and settlement or infrastructure context, while avoiding unsupported claims about exact national exposure or damage totals.

Return your answer as JSON:

```json
{
  "answer": "<compact_priority_label>",
  "priority_level": "<low|moderate|high>",
  "priority_chain": ["<hazard_driver>", "<compound_mechanism>", "<response_focus>"],
  "numeric_anchors": [
    {"name": "<anchor>", "value": "<value>"}
  ],
  "brief_rationale": "<two or three sentences>"
}
```
