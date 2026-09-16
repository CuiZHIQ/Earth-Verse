# Hurricane Harvey Rainfall-Flood Causal Graph

You are an urban flood-process analyst reconstructing why Hurricane Harvey produced extreme rainfall flooding around Houston in late August 2017. The task is to build an evidence-traceable causal graph that links rainfall accumulation, spatial water volume, and exposed receptors.

Use only the local CSX-057 event package. Select package-relative evidence for every value and claim you use.

Compute the required rainfall, exposure, and water-volume quantities:

- `peak_to_20in_ratio = peak storm rainfall inches / 20`
- `hobby_4day_mean_in_per_day = Houston Hobby August 26-29 rainfall inches / 4`
- `hobby_total_to_20in_ratio = Houston Hobby August 26-29 rainfall inches / 20`
- `houston_month_record_ratio = Houston August rainfall inches / previous wettest-month rainfall inches`
- `exposed_density_per_sq_mi = people receiving at least 20 inches / area receiving at least 20 inches`
- `min_20in_area_volume_trillion_gal = 20 * area_sq_mi * 17,378,742.857 / 1,000,000,000,000`

Then organize the result as a directed causal graph that distinguishes:

- persistent multi-day rainfall accumulation;
- spatially extensive 20-inch rainfall volume;
- exposed population density inside the heavy-rain footprint;
- the rejected interpretation that the event was only a short isolated downpour.

Return one compact JSON object:

```json
{
  "label": "<persistent_extreme_rainfall_accumulation or threshold_not_met>",
  "causal_graph": {
    "nodes": [
      {"id": "<node_id>", "role": "<trigger|amplifier|receptor|rejected_alternative>", "evidence": "<short evidence label>"}
    ],
    "edges": [
      {"from": "<node_id>", "to": "<node_id>", "relationship": "<directional process link>"}
    ]
  },
  "key_values": {
    "peak_to_20in_ratio": 0.0,
    "hobby_4day_mean_in_per_day": 0.0,
    "hobby_total_to_20in_ratio": 0.0,
    "houston_month_record_ratio": 0.0,
    "exposed_density_per_sq_mi": 0.0,
    "min_20in_area_volume_trillion_gal": 0.0
  },
  "causal_discriminators": {
    "persistent_accumulation": true,
    "large_area_water_volume": true,
    "exposure_density_context": true,
    "short_isolated_downpour_rejected": true
  },
  "interpretation": "<one sentence>"
}
```

Use `persistent_extreme_rainfall_accumulation` only when the computed graph supports accumulation, record-scale rainfall, large-area water volume, and exposure-density context together. Round numeric fields to two decimals.
