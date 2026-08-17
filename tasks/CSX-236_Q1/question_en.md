# Near-Term Earthquake Response Triage: 2023 Morocco Al Haouz

A national emergency operations cell is setting first-48-hour priorities after the 8 September 2023 Al Haouz earthquake in Morocco. The assessment record combines earthquake source parameters, shaking intensity, exposed population, mapped settlement and road context, aftershock advisory text, tsunami screening, and limited radar-change context.

Classify the dominant near-term response priority by combining the shaking severity, the exposed population, mapped built-environment exposure, tsunami relevance, and aftershock safety context. Choose the best compact priority label and report a reproducible priority index on a 0 to 100 scale. The operations chief wants an answer that supports action prioritization without turning exposure indicators into confirmed collapse, casualty, or outage counts.

Use these component definitions:

- `intensity_component = min(maximum_mmi / 10, 1) * 35`
- `population_component = min(exposed_population / 250000, 1) * 25`
- `building_component = min(mapped_building_features / 500, 1) * 15`
- `alert_component = 15` when the earthquake alert is red, otherwise `0`
- `aftershock_component = 10` when the advisory text flags aftershock danger to weakened or poorly constructed structures, otherwise `0`
- `priority_index = min(intensity_component + population_component + building_component + alert_component + aftershock_component, 100)`

Set `answer` to `highest_priority_structural_collapse_aftershock_safety` when `priority_index >= 85`, `tsunami_flag == 0`, and the aftershock-safety flag is present. If `tsunami_flag == 1`, use `coastal_tsunami_evacuation_priority`; otherwise use `moderate_ground_shaking_damage_assessment`.

Return your answer as:

```json
{
  "answer": "<compact_priority_label>",
  "priority_index": "<value>",
  "key_metrics": {
    "maximum_mmi": "<value>",
    "exposed_population": "<value>",
    "mapped_building_features": "<value>",
    "tsunami_flag": "<value>"
  },
  "impact_chain": ["<driver>", "<impact_pathway>", "<response_priority>"]
}
```
