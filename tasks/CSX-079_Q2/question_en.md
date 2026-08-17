# Central Chile Flood Uncertainty Propagation

You are a hydrologic uncertainty analyst testing whether the August 20-26, 2023 central Chile flood interpretation is robust to multi-source differences. The central hypothesis is a sustained moisture-transport rainfall load amplified by terrain, with official impact counts documenting burden and image/exposure layers providing context rather than direct loss measurements.

Use only the local CSX-079 event package. Select package-relative evidence for every rainfall, terrain, official-impact, remote-sensing, and exposure value.

Propagate uncertainty across six evidence streams:

- rainfall duration/load;
- terrain amplification;
- official people burden;
- official housing/alert burden;
- surface-change context;
- exposure context.

For each stream, compute the package-derived values, state whether the stream supports the central hypothesis, identify the main uncertainty or data-source limitation, and reject one tempting overinterpretation.

Return compact JSON:

```json
{
  "target_family": "central_chile_flood_uncertainty_propagation",
  "uncertainty_propagation": [
    {
      "evidence_stream": "<stream id>",
      "computed_values": {},
      "robust_conclusion": "",
      "uncertainty_limit": "",
      "rejected_alternative": ""
    }
  ],
  "evidence_stream_checks": [
    {"row_id": "rainfall_duration_load", "computed_values": {}, "pass_fail": "", "rejected_alternative": ""},
    {"row_id": "terrain_amplification", "computed_values": {}, "pass_fail": "", "rejected_alternative": ""},
    {"row_id": "official_people_burden", "computed_values": {}, "pass_fail": "", "rejected_alternative": ""},
    {"row_id": "official_housing_alert_burden", "computed_values": {}, "pass_fail": "", "rejected_alternative": ""},
    {"row_id": "surface_change_context", "computed_values": {}, "pass_fail": "", "rejected_alternative": ""},
    {"row_id": "exposure_context", "computed_values": {}, "pass_fail": "", "rejected_alternative": ""}
  ],
  "fragile_links": [],
  "final_consistency_label": ""
}
```

The final label should state whether the rainfall-duration, terrain-amplification, and official-burden chain remains internally consistent after accounting for source differences. Do not infer flood depth, housing loss, road failure, or observed population losses from image or exposure context alone.
