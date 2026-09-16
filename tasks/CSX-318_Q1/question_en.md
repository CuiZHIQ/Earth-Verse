# Tasman Glacier Lake-Impact Diagnosis

An emergency-planning team in Aoraki/Mount Cook National Park is preparing a brief on the late-February 2011 Tasman Glacier and Tasman Lake incident in New Zealand. The team needs to decide which disaster pathway should drive response planning: earthquake-triggered glacier calving with lake-iceberg operations, rainfall or snowmelt flooding, heat or fire stress, or a broad population-exposure emergency.

Prepare a compact disaster-analysis diagnosis that names the dominant pathway, explains the physical trigger-to-impact chain, and states the response priority for lake users, visitors, and nearby operations. Use a few quantitative anchors only where they help distinguish the glacier-lake hazard from the competing explanations.

Return a JSON object with these keys:

```json
{
  "diagnosis": "short_label",
  "response_priority": "one sentence",
  "mechanism_summary": "one sentence",
  "impact_chain": ["trigger", "physical process", "operational concern"],
  "key_numeric_anchors": [
    {"name": "anchor name", "value": "rounded value"}
  ],
  "context_role": "one sentence"
}
```

Keep the answer concise and focused on the disaster mechanism and operational consequence, not on cataloging measurements.
