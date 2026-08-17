# Operational Priority Brief: 2022 China Heat Wave and Yangtze Drought

During the 2022 prolonged heat wave and Yangtze River drought in China, a regional emergency coordination team needs a concise technical basis for the dominant response priority. The key question is whether the incident should be framed primarily as compound heat-drought water-supply stress, a heat-only health-alert problem, a flood-response problem, or a land-change monitoring problem.

Diagnose the best response priority from the incident record. Support the conclusion with quantitative anchors, a short mechanism-to-impact chain, and a brief explanation of why the weaker response framings should not drive the main operational posture. Keep the analysis to the documented incident record and avoid adding later or unverified loss claims.

Use component scores on a 0-1 scale and compute:

`priority_index = round(100 * (0.25*heat_extremity + 0.30*drought_water_stress + 0.20*reported_human_impact + 0.15*official_response + 0.10*local_exposure), 1)`

Return JSON only:

```json
{
  "answer": "<compact_priority_label>",
  "priority_index": "<0-100 value>",
  "component_scores": {
    "heat_extremity": "<value>",
    "drought_water_stress": "<value>",
    "reported_human_impact": "<value>",
    "official_response": "<value>",
    "local_exposure": "<value>"
  },
  "impact_chain": ["<driver>", "<compound_hazard>", "<priority_impact>"],
  "brief_reasoning": "<2-4 sentence expert explanation>"
}
```
