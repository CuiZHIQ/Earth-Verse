# Rio Grande do Sul Persistent Flood-Signal Diagnostic

A hydrometeorology review team is testing whether the 2024 Rio Grande do Sul flood package supports a persistent heavy-rainfall flood signal with concurrent displacement pressure and surface-change evidence. Use the local package to extract the event window, the report rainfall and displacement anchors, gridded accumulated-precipitation maxima, and available surface-change indicators. Your answer should show the computed diagnostic state, not a broad narrative summary.

Return one JSON object only, with this exact shape:

```json
{
  "answer": "...",
  "event_window_days": 0,
  "rain_rate_mm_day": 0,
  "precip_spread_ratio": 0,
  "displacement_per_100mm": 0,
  "surface_signal_count": 0,
  "threshold_score": 0,
  "threshold_state": "..."
}
```

Use these five checks:

- `event_window_days`: inclusive days in the flood event window; pass if it is at least 30.
- `rain_rate_mm_day`: rainfall lower bound divided by 7 days; pass if it is at least 40 mm/day.
- `precip_spread_ratio`: maximum divided by minimum across the recorded gridded accumulated-precipitation maxima; pass if it is at least 2.0.
- `displacement_per_100mm`: displaced-people lower bound divided by `(rainfall lower bound in mm / 100)`; pass if it is at least 50000 people per 100 mm.
- `surface_signal_count`: count the following indicator tests that pass: mean radar VV change <= -1.0 dB, embedding mean change >= 0.05, and true-color luminance delta <= -5.0. The surface check passes if at least 2 indicators pass.

Set `threshold_score` to the number of the five checks that pass. Use three decimals for rates and ratios, one decimal for `displacement_per_100mm`, and an integer for `surface_signal_count`.

Set `threshold_state` to `"pass"` only when all five checks pass; otherwise use `"partial"`. If all five checks pass, set `answer` to `"persistent_rainfall_displacement_surface_signal_supported"`.
