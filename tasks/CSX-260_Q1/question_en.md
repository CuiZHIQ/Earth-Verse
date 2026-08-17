# Western Europe Flood Response Diagnosis

In mid-July 2021, extreme rainfall across western Germany, Belgium, and nearby river corridors escalated into one of Western Europe's most damaging flood disasters in recent decades. An emergency coordination team needs a concise expert diagnosis for prioritizing response and explaining the dominant disaster mechanism.

Assess whether the episode is best treated as a high-priority cascading flash-and-river flood, a more limited rainfall anomaly, a non-flood heat or drought stress event, or a surface-change signal that should not drive urgent flood operations. Support the decision with quantitative anchors, the physical mechanism, a clear impact pathway, and a brief explanation of how surface-change evidence should be weighed against rainfall and flood indicators.

Return only a compact JSON object in this form:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority_level": "<high|moderate|review>",
  "key_findings": [
    {"name": "<finding>", "value": "<concise value>", "role": "<why it matters>"}
  ],
  "impact_chain": ["<driver>", "<hazard>", "<impact pathway>"]
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

For this task, use that object to rank flood mechanism evidence against point rainfall and surface-change context, rather than merely assigning a high-priority flood label.

