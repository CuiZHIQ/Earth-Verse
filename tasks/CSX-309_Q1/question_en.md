# Calbuco Eruption Response Priority

You are supporting a first-cycle emergency briefing for the April 2015 Calbuco volcanic crisis in Chile's Los Lagos Region. The briefing team needs a compact operational posture that distinguishes the physical driver of the crisis from supporting context in the package evidence.

Evaluate four possible postures: ashfall, evacuation, and air-quality management; wet-ash and lahar-access monitoring; lava or burn-scar image triage; and ordinary weather response. Give the highest-priority posture, rank all four from most to least urgent, include the main quantitative anchors that support the decision, and explain the mechanism-to-impact chain in practical emergency-management terms. Use mapped exposure, precipitation, and image statistics as operational context rather than as independent event-location proof.

Return your answer as JSON:

```json
{
  "answer": "<compact_priority_label>",
  "priority_rank": ["<highest>", "<next>", "<next>", "<lowest>"],
  "key_numeric_anchors": [
    {"name": "<anchor>", "value": "<value>"}
  ],
  "impact_chain": ["<driver>", "<hazard>", "<response_relevance>"],
  "rationale": "<brief explanation>"
}
```
