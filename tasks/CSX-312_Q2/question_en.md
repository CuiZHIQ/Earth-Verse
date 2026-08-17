# Kilauea 2018 Coupled-System Diagnosis

For the 2018 Kilauea eruption, an incident scientist is preparing a mechanism note for downstream hazard interpretation. The central question is whether the crisis should be treated mainly as an isolated lower-rift lava outbreak, an isolated summit-collapse crisis, a rainfall-triggered secondary hazard, or a coupled summit-drainage and lower-rift effusion system.

Choose the diagnosis that best explains the linked summit and lower-rift behavior. Support it with a physical index, the numerical value of that index, and three concise clues: one mechanism clue, one volume or rate clue, and one operational implication.

Return your response as compact JSON:

```json
{
  "diagnosis": "<compact_label>",
  "physical_index": {
    "name": "<index_name>",
    "value": <number>
  },
  "why": ["<mechanism clue>", "<volume clue>", "<operational implication>"]
}
```
