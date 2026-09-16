# Hurricane Ida Short-Window Flood Ledger

New York City analysts are reviewing the September 1-2, 2021 Hurricane Ida rainfall flood signal. Test whether the local data support a short-window urban pluvial-feedback diagnosis, rather than a delayed routing, wind-led, citywide-uniform, or coarse-grid-downweighted explanation.

Build a compact JSON score ledger with exactly these fields:

```json
{
  "component_scores": {
    "hour_anchor": 0,
    "rain_concentration": 0,
    "feedback_overlap": 0,
    "sewer_dominance": 0,
    "local_concentration": 0
  },
  "computed_values": {
    "official_record_hour_mm": 0,
    "official_to_point_ratio": 0,
    "peak_3h_share": 0,
    "peak_6h_share": 0,
    "hours_ge_25mm": 0,
    "feedback_window_share": 0,
    "peak_created_hour_share": 0,
    "peak_window_sewer_share": 0,
    "total_sewer_share": 0,
    "top_borough_share": 0,
    "max_1km_cluster": 0,
    "official_to_gpm_ratio": 0
  },
  "total_score": 0,
  "rejected_substitutes": [],
  "final_label": ""
}
```

Use one point for each component that passes its test:

- `hour_anchor`: `official_to_point_ratio >= 2.0`.
- `rain_concentration`: `peak_3h_share >= 0.50`, `peak_6h_share >= 0.70`, and `hours_ge_25mm >= 2`.
- `feedback_overlap`: the point rainfall peak is inside the `2021-09-01T21:00` to `2021-09-02T03:00` feedback window and `feedback_window_share >= 0.50`.
- `sewer_dominance`: `peak_window_sewer_share >= 0.85` and `total_sewer_share >= 0.85`.
- `local_concentration`: `top_borough_share >= 0.30` and `max_1km_cluster >= 20`.

Include the coarse-grid rain ratio only as a check against downgrading the local cloudburst signal. Return only the JSON and concise calculation notes inside string values if needed.
