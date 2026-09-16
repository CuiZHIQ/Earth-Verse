# Vertical Smoke Exposure Ledger

During the June 2023 Canadian wildfire-smoke episode across New York City and the U.S. Northeast, a technical team needs a calculation-first check of whether the reported vertical smoke structure supports a near-surface exposure reading rather than treating every visible layer as equivalent.

Using the local CSX-211 package, reconstruct the event-window and smoke-layer ledger:

- Extract the event start date, end date, and inclusive duration in days.
- Extract the three reported smoke-layer heights in kilometers: the low layer top, the middle layer, and the high layer.
- Compute `near_surface_share = low_layer_top_km / high_layer_km`.
- Compute `high_to_low_ratio = high_layer_km / low_layer_top_km`.
- Report the lower-bound PM2.5 value described for Syracuse in micrograms per cubic meter.
- Compute the lag in days from the Alberta source date named for the high layer to the event end date.
- Give one short consistency proof that identifies the surface-coupled layer and the old high-layer context.

Return strict JSON with this shape:

```json
{
  "event_window": {"start_date": "", "end_date": "", "duration_days": 0},
  "layer_km": {"low_top": 0, "mid": 0, "high": 0},
  "near_surface_share": 0,
  "high_to_low_ratio": 0,
  "pm25_floor_ug_m3": 0,
  "high_layer_lag_days": 0,
  "consistency_proof": ""
}
```
