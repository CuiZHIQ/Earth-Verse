# Noto Peninsula Earthquake Impact-Priority Diagnosis

On January 1, 2024, a major earthquake struck Japan's Noto Peninsula and affected communities along the Sea of Japan coast. An emergency coordination team needs a concise technical briefing that separates the dominant operational priority from secondary or weaker signals during the first impact assessment.

Decide what the incident record most strongly supports: a response centered on severe earthquake shaking and earthquake-induced ground failure, a primarily coastal tsunami posture, a weather-driven disruption, or a broad land-surface-change interpretation. Support the conclusion with quantitative anchors and a short mechanism-to-impact chain, not just a label.

Return your answer as JSON:

```json
{
  "answer": "<compact_priority_label>",
  "key_metrics": {
    "magnitude": "<value>",
    "depth_km": "<value>",
    "max_mmi": "<value>",
    "alert": "<value>",
    "tsunami_flag": "<value>",
    "liquefaction_exposed_population": "<value>",
    "landslide_exposed_population": "<value>",
    "liquefaction_to_landslide_population_ratio": "<value>"
  },
  "priority_chain": ["<driver>", "<main_impact>", "<secondary_or_rejected_context>"]
}
```

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to deepen the Noto answer by forcing a priority comparison between severe shaking, liquefaction, tsunami, weather, and remote-sensing signals.

