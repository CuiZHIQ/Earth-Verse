# 2004 Indian Ocean Tsunami Mechanism Briefing

On 26 December 2004, catastrophic tsunami impacts spread from the Sumatra-Andaman source region across the Indian Ocean basin. A coastal emergency-management coordination team is preparing a technical note that must decide which hazard mechanism should dominate response prioritization and which index best captures immediate life-safety risk.

Prepare a concise expert-analysis answer that attributes the dominant mechanism, links the physical trigger to basin-scale coastal impacts, and explains why plausible meteorological or generic change-detection interpretations should not drive the primary response priority.

Return your answer as JSON only:

```json
{
  "answer": "<compact_mechanism_priority_label>",
  "priority": "<compact_response_priority_label>",
  "primary_index": "<compact_index_label>",
  "quantitative_anchors": {
    "earthquake": "<magnitude/depth/source-region anchor>",
    "runup": "<runup or coastal hazard anchor>",
    "impact": "<life-safety or displacement anchor>",
    "context_rejection": "<short anchor for why competing hazard signals are secondary>"
  },
  "impact_chain": ["<trigger>", "<mechanism>", "<hazard_expression>", "<impact_priority>"],
  "not_primary": ["<non_primary_interpretation_1>", "<non_primary_interpretation_2>", "<non_primary_interpretation_3>"],
  "briefing": "<2-4 sentences connecting the trigger, propagation pathway, quantitative severity, and operational decision>"
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

For this task, use that object to make the tsunami briefing explicitly connect source mechanics, runup, life-safety impact, and rejected meteorological/change-detection alternatives.

