# July 2021 Henan Zhengzhou Rainfall Threshold Ledger

A hydrometeorology team is checking whether the July 17-23, 2021 Henan/Zhengzhou flood record supports a compact threshold diagnosis: an exceptional short rainfall burst embedded in a multi-day extreme rainfall episode over a dense urban road and population setting. Compute the ledger from the technical record, including at least two derived ratios rather than copied values.

Return a concise JSON object with these fields:

```json
{
  "event_window": {"start": "", "end": "", "days": 0},
  "reported_rainfall": {
    "three_day_mm": 0,
    "one_hour_mm": 0,
    "hour_share": 0,
    "annual_ratio": 0
  },
  "gridded_accumulation": {
    "mean_order": [],
    "max_mean_dataset": "",
    "max_mean_mm": 0,
    "max_grid_mm": 0
  },
  "exposure_context": {
    "population_million": 0,
    "highway_features": 0,
    "amenity_features": 0,
    "tunnel_features": 0
  },
  "threshold_flags": {
    "hour_share_ge_0_30": false,
    "annual_ratio_ge_0_90": false,
    "population_ge_5m": false,
    "highway_features_ge_200": false
  },
  "final_label": "",
  "interpretation": "one sentence tying the threshold results together"
}
```

Use the label `short_burst_multiday_urban_exposure` only if all four threshold flags are true. Otherwise use `mixed_or_incomplete_threshold_support`.
