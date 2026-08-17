# El Nino Winter Impact Priority

A national emergency-planning desk is preparing a short technical note on the 1997-1998 El Nino and its U.S. winter flood and storm impacts. The desk needs to decide how to frame the event for seasonal readiness: as a strong warm-ENSO teleconnection with regional winter flood and storm preparedness implications, as a mostly localized precipitation episode, as a vegetation or burn-scar problem, or as a weak anomaly that should remain low priority.

Use the event evidence to identify the best planning frame. Anchor the decision with quantitative indicators of warm-ENSO strength, atmospheric coupling, and planning context, and explain why the selected mechanism is more appropriate than the alternative framings. Treat `planning_context_count` as the number of emergency-relevant features in the package's planning-context slice, not as a national exposure or loss total.

Return a concise JSON object:

```json
{
  "answer": "<compact_priority_label>",
  "priority_chain": ["<climate_driver>", "<circulation_mechanism>", "<planning_priority>"],
  "key_metrics": {
    "peak_warm_anomaly_c": "<number>",
    "strong_warm_seasons": "<integer>",
    "lowest_coupling_index": "<number>",
    "planning_context_count": "<integer>"
  },
  "context_scope": "<what the planning-context count represents>",
  "brief_rationale": "<one or two sentences>"
}
```
