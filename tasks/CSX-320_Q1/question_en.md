# Glacier Outburst Flood Response Priority

Juneau emergency managers are preparing a same-day technical note after the August 2024 Mendenhall Glacier flooding. The briefing has to distinguish whether the response should be led as a cryosphere-driven outburst flood from Suicide Basin into the Mendenhall River corridor, a conventional rainfall flood, a wildfire or heat-stress episode, or a broad regional exposure emergency.

Give a concise disaster-analysis judgment that identifies the leading mechanism, the operational priority for responders, the numeric anchors that justify that stance, and the source-to-impact chain connecting the glacier-basin release to community concerns.

Return your answer as JSON:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority": "<compact_priority_label>",
  "key_numeric_anchors": {
    "water_release_billion_gallons": "<value>",
    "river_crest_ft": "<value>",
    "streamflow_cfs_lower_bound": "<value>",
    "crest_above_previous_record_ft": "<value>"
  },
  "impact_chain": ["<source_zone>", "<release_and_routing>", "<community_concern>"],
  "rationale": "<brief explanation>"
}
```
