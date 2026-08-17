# Monsoon-Flood Mechanism and Response Priority

During the 2022 Pakistan extreme monsoon floods, a disaster coordination cell needs a compact technical diagnosis for downstream planning. The decision is not merely whether flooding occurred, but which mechanism best explains the event and what response priority follows from the combination of basin-scale rainfall, compound melt context, and reported human and economic impacts.

Compare these mechanism interpretations:

- monsoon rainfall accumulation causing basin-scale flooding, with compound melt context
- short-lived windstorm damage
- heat-health emergency as the dominant impact pathway
- remote-sensing land-cover change without a direct flood-impact interpretation

Focus on mechanism, impact scale, and priority reasoning: precipitation accumulation across independent hazard diagnostics, the event window and affected basin context, reported mortality and damage, and whether any non-flood alternative is more convincing. Keep the full event window separate from the gridded precipitation evidence window and the shorter point-sample rainfall timing window.

Return your response as:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority": "<compact_priority_label>",
  "severity_bin": "<compact_severity_label>",
  "evidence_windows": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "gridded_precipitation_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "point_sample_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}
  },
  "key_metrics": {
    "consensus_precip_mean_mm": "<value>",
    "precip_product_spread_percent": "<value>",
    "reported_deaths": "<value>",
    "reported_damage_usd_billion": "<value>"
  },
  "impact_chain": ["<driver>", "<hazard>", "<priority>"]
}
```
