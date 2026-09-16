# Post-Fire Debris-Flow Mechanism Diagnosis

For the 2018 Montecito post-fire debris flows, diagnose the full hazard sequence and response priority from the supplied case materials. Do not treat this as a simple label-selection problem: explain how the event progressed from pre-storm landscape conditioning to downstream consequences.

Your diagnosis should distinguish a rainfall-only flood, an active-fire or burn-severity-only event, a generic exposed-assets event, and a post-fire rainfall debris-flow cascade. Combine the antecedent wildfire and burn-scar conditioning, rainfall intensity or threshold support, rapid runoff and debris entrainment, channel and alluvial-fan routing, downstream exposure and service impacts, image-derived or numeric measurements, and the resulting response priority.

Return your response as compact JSON:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority": "<compact_priority_label>",
  "cascade_priority_index": "<numeric index>",
  "impact_chain": ["<condition>", "<trigger>", "<impact pathway>"],
  "key_metrics": {
    "open_meteo_precip_mm": "<value>",
    "max_precip_support_mm": "<value>",
    "dnbr_mean": "<value>",
    "exposed_population": "<value>",
    "critical_facilities": "<value>"
  }
}
```

