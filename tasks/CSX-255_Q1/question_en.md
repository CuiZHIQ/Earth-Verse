# Cyclone Freddy Compound Response Priority

You are preparing a March 2023 regional emergency-analysis brief after Cyclone Freddy's repeated impacts across Madagascar, Mozambique, and Malawi. The response team needs a compact diagnosis of which operational priority should dominate: a wind-core cyclone response, a rainfall-driven flood and slope-failure cascade with public-health monitoring, a drought/heat response, or a wildfire/burn-scar response.

Determine the priority that best explains Freddy's long-lived disaster phase. Include the main physical driver, the leading impact pathway, a secondary monitoring need, and the priority modes that should be downgraded because they do not match the event mechanism.

Return a compact JSON answer:

```json
{
  "answer": "<compact_priority_label>",
  "key_metrics": {
    "event_period": "<start_to_end>",
    "rainfall_signature": "<concise amount_or_range>",
    "exposed_population_context": "<concise amount_or_scale>"
  },
  "priority_chain": ["<driver>", "<main_impact>", "<secondary_monitoring_need>"],
  "rejected_priorities": ["<brief reason for rejected priority>", "<brief reason for rejected priority>"]
}
```
