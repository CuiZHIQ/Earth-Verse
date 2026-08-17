# Compound Fire-Haze Response Priority

A regional emergency-analysis team is preparing a response-priority note for the 2015 Indonesian drought, peat-fire, and transboundary haze crisis. The decision problem is whether this episode should be prioritized mainly as a drought-conditioned peat-fire haze disaster with downwind air-quality exposure, or instead as a rainfall/flood disruption, direct burn-scar damage event, or weakly diagnosed catalog entry.

Assess the event-specific mechanism chain and response priority. Your answer should connect the physical driver, the fire-smoke process, and exposed people or infrastructure into one disaster-priority judgment.

Return a compact JSON answer:

```json
{
  "answer": "<compact_priority_label>",
  "priority_class": "<low|moderate|high|very_high>",
  "mechanism_chain": ["<driver>", "<hazard_process>", "<impact_pathway>"],
  "response_priority": "<one sentence>",
  "key_numeric_anchors": {
    "<anchor_name>": "<value>",
    "<anchor_name>": "<value>"
  }
}
```

Use 2-5 numeric anchors at most. Keep the response concise, but make the causal logic specific enough to distinguish peat-fire haze exposure from flood response, burn-scar mapping, or an uncertain event label.
