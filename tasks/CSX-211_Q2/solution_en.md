# Final Answer

```json
{
  "event_window": {"start_date": "2023-06-06", "end_date": "2023-06-08", "duration_days": 3},
  "layer_km": {"low_top": 3, "mid": 6, "high": 12},
  "near_surface_share": 0.25,
  "high_to_low_ratio": 4.0,
  "pm25_floor_ug_m3": 400,
  "high_layer_lag_days": 34,
  "consistency_proof": "The low smoke layer reaches from near the surface to about 3 km, so it is the surface-coupled exposure layer; the 12 km layer is four times that height and traces back 34 days to Alberta, so it is old high-layer transport context."
}
```

# Key Computations

The locked event window is 2023-06-06 through 2023-06-08.

```text
duration_days = (2023-06-08 - 2023-06-06) + 1 = 3
layer_km = {low_top: 3, mid: 6, high: 12}
near_surface_share = low_top / high = 3 / 12 = 0.25
high_to_low_ratio = high / low_top = 12 / 3 = 4.0
pm25_floor_ug_m3 = 400
high_layer_lag_days = 2023-06-08 - 2023-05-05 = 34
```

# Reasoning Path

First, use the locked local event anchor to fix the date window and inclusive duration. Next, read the NASA report's vertical smoke description as three numeric layer heights: the low layer top, the middle layer, and the high layer. Then compute the two vertical ratios from those extracted heights, keeping the near-surface share as the primary numeric answer. Finally, add the Syracuse PM2.5 lower-bound value and the Alberta source-date lag to support the consistency proof.

# Computed Interpretation

The computed ledger is internally consistent: the low smoke layer is the only reported layer extending from near the surface up to 3 km, while the 12 km layer is four times higher and 34 days removed from the named Alberta source date. The PM2.5 lower bound anchors the near-surface exposure reading, and the high layer is retained as vertical context rather than treated as equivalent to the surface-coupled layer.

# Scoring Rubric

- 3 points: Reconstructs the 2023-06-06 to 2023-06-08 event window and the 3-day inclusive duration. partial_credit: Award 1-2 points for correct dates with an arithmetic slip or correct duration with incomplete dates.
- 4 points: Extracts the three smoke-layer heights as 3, 6, and 12 km. partial_credit: Award partial credit for each correctly reported height with km units.
- 4 points: Computes `near_surface_share = 0.25` and `high_to_low_ratio = 4.0` from the extracted heights. partial_credit: Award 1-3 points for a correct setup with one missing or rounded derived value.
- 3 points: Reports the PM2.5 lower bound as above 400 micrograms per cubic meter. partial_credit: Award 1-2 points for recognizing the surface-air anchor without the numeric lower bound.
- 3 points: Computes the Alberta May 5 to 2023-06-08 high-layer lag as 34 days. partial_credit: Award 1-2 points for correct source date or approximate month-old reading without exact lag.
- 3 points: Gives a compact consistency proof that distinguishes the near-surface exposure layer from the older high-layer transport context using computed fields. partial_credit: Award 1-2 points for a concise proof missing one of the two contrasts.

Total: 20 points.
