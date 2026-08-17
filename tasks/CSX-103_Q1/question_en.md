# Hurricane Sandy Coastal-Forcing Causal Graph

You are a coastal-hazards analyst building a causal graph for the late-October 2012 Hurricane Sandy flooding along the New York-New Jersey Atlantic coast. The graph must compare coastal water level and wave evidence against rainfall-only, wind-only, exposure-only, and image-led simplifications.

Use only the local CSX-103 event package. Select package-relative evidence for every value, mechanism node, and rejected simplification.

Construct a directed graph in which true physical triggers, supporting context, receptors, and weak substitutes are separated. The graph should include:

- coastal water-level, wave, altered-shoreline, submerged-debris, navigation-hazard, and coastal recovery/mapping signals;
- event precipitation and peak local wind as context checks;
- exposed population as receptor context rather than a physical trigger;
- SAR pre/post availability as an observation constraint, not direct proof of inundation when scenes are absent.

Return only a compact JSON object:

```json
{
  "final_label": "<winning mechanism label>",
  "causal_graph": {
    "nodes": [
      {"id": "<node_id>", "role": "<trigger|context|receptor|observation_constraint|rejected_simplification>", "evidence": "<short evidence label>"}
    ],
    "edges": [
      {"from": "<node_id>", "to": "<node_id>", "relationship": "<directional process link>"}
    ]
  },
  "mechanism_scores": {
    "coastal_water_level_wave": 0,
    "rainfall_only": 0,
    "wind_only": 0,
    "exposure_only": 0,
    "image_led": 0
  },
  "key_values": {
    "event_days": 0,
    "event_precip_mm": 0.0,
    "peak_10m_wind_kmh": 0.0,
    "exposed_population_million": 0.0,
    "sar_pre_post_counts": "0/0"
  },
  "failed_simplification": "<rainfall/wind/exposure/image simplification that fails and why>"
}
```

The final label should identify the dominant coastal-forcing mechanism and the graph should show why rain, local wind, exposure, and imagery cannot replace the coastal water-level and wave pathway.
