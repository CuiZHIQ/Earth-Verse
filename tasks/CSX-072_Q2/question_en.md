# Kathmandu Valley Access-Corridor Rainfall Diagnostic

A hydrometeorology review team is checking the September 27-29, 2024 Nepal flood and landslide episode around Kathmandu Valley and the mountain access corridors. The team needs a compact calculation diagnostic that tests whether the event is best represented as persistent valley/corridor rainfall reinforced by clustered station records and river-gauge exceedances, rather than as a single peak-hour event, a coarse-grid precipitation cap, or a river-only signal.

Return a JSON object with this shape:

```json
{
  "answer": "<final_label>",
  "ledger_rows": [
    {
      "row_id": "<required row id>",
      "formula": "<calculation used>",
      "computed": {"<metric_name>": "<numeric value>"},
      "pass_fail": "<conclusion state>"
    }
  ],
  "rejected_substitutions": ["<short rejected substitute>", "..."]
}
```

Use exactly these five `row_id` values:

- `point_intensity_signature`
- `persistence_signature`
- `valley_record_cluster_signature`
- `river_reinforcement_signature`
- `access_corridor_context_signature`

Compute the peak-to-event-mean hourly rainfall ratio, wet-hour and multiday persistence shares, Kathmandu Valley and compact record-cluster shares and density, station-to-GPM normalization ratios, river-gauge exceedance share and maximum observed/historic gauge ratio, and OSM corridor-context ratios. End with one compact label indicating whether the calculations support a persistent valley/access-corridor rainfall signature while keeping mapped roads, facilities, population, and bridges as context rather than observed loss counts.

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

For this task, use that object to make the Kathmandu diagnosis synthesize point rainfall, station clustering, river gauges, and access-corridor context instead of one row.

