# Nyiragongo Impact-Chain Priority

An emergency operations cell in Goma is preparing the first technical handover after the 22-23 May 2021 Mount Nyiragongo eruption in the Democratic Republic of the Congo. The team needs a concise disaster-analysis judgment on which mechanism should drive immediate operations: direct urban lava-flow damage and displacement, ash-centered disruption, rainfall- or lahar-centered flooding, or a satellite-change interpretation that does not by itself identify the response priority.

Decide the dominant mechanism and response priority. Support the decision with quantitative anchors, a short impact chain, and brief reasons why the other mechanism framings are weaker. Use population and surface-change values as package-derived context for exposure and disturbance, not as direct affected-population counts, exact lava-flow footprint, or complete damage estimates.

Return a concise JSON object:

```json
{
  "answer": "<mechanism_label>",
  "response_priority": "<priority_label>",
  "key_numeric_anchors": {
    "<anchor_name>": "<value>"
  },
  "impact_chain": ["<trigger>", "<exposed_or_affected_element>", "<operational_priority>"],
  "why_alternatives_are_weaker": ["<brief reason>", "<brief reason>"]
}
```
