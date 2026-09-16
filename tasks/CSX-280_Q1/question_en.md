# Ethiopia 2015-2016 El Nino Drought Food-Security Planning Priority

An interagency humanitarian analysis cell is preparing a briefing on Ethiopia during the 2015-2016 El Nino-linked drought and food-security crisis. The team needs a planning stance for senior decision-makers: should this be treated as a high-priority strong warm-ENSO drought and food-security emergency, a mostly localized short-rainfall episode, a wind or flood emergency, or a weak climate anomaly with limited response implications?

Assess the climate driver, the drought pathway, and the reported humanitarian consequence together. Return the answer as JSON:

```json
{
  "answer": "<compact_priority_label>",
  "key_numeric_anchors": {
    "enso_peak_anomaly_c": "<value>",
    "coupled_signal_minimum": "<value>",
    "reported_food_insecure_people": "<value>"
  },
  "priority_chain": ["<driver>", "<drought_pathway>", "<response_priority>"],
  "rationale": "<brief explanation>"
}
```
