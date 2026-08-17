# Bam Earthquake Response-Priority Diagnosis

A rapid analysis cell supporting emergency managers in Kerman Province is preparing its first operational brief after the 26 December 2003 Bam earthquake. The team needs a response-priority diagnosis, not a general event summary: should the first analytical emphasis be urban collapse search-and-rescue, coastal inundation response, weather-driven disruption, or satellite-change reconnaissance?

Decide which priority should lead the brief for Bam and explain the mechanism-to-impact chain that makes it urgent. Ground the diagnosis in a few quantitative anchors, such as earthquake severity, affected population context, service-disruption exposure, and reported building damage. Also explain why the other candidate priorities should be lower for this specific inland city earthquake.

Return your answer as:

```json
{
  "answer": "<compact_priority_label>",
  "priority_band": "<band>",
  "key_numeric_anchors": {
    "<anchor_name>": "<value>"
  },
  "impact_chain": ["<driver>", "<damage_mechanism>", "<response_priority>"],
  "why_other_priorities_are_lower": ["<short reason>", "<short reason>"]
}
```
