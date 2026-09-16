# Correct Answer

```json
{
  "event_white_share": 0.704,
  "pre_white_share": 0.027,
  "white_ratio": 26.1,
  "event_rgb_spread": 1.2,
  "s1_mean_change_db": 1.4,
  "rain_max_mean_ratio": 2.3,
  "s2_status": "no_sufficient_scenes",
  "thresholds": {
    "event_white_ge_0_60": true,
    "white_ratio_ge_20": true,
    "event_rgb_spread_le_5": true,
    "s2_scene_gap": true
  },
  "conclusion": "obstructed_window_not_surface_map",
  "interpretation": "The event-window image is dominated by bright nearly neutral pixels, so it should not be treated as a surface-change map; radar and rainfall values are supporting numeric context."
}
```

# Computation

The event-window RGB preview has `white_neutral_share = 0.704`, while the pre-event preview has `white_neutral_share = 0.027`. The derived contrast is:

`white_ratio = 0.704 / 0.027 = 26.1`.

The event-window mean RGB spread is `1.2` levels, so the bright signal is nearly neutral. The Sentinel-1 side metric is the package VV post-minus-pre mean change, `1.4 dB`. The precipitation contrast is:

`rain_max_mean_ratio = 20.68 / 9.0875 = 2.3`.

All four threshold tests pass: `0.704 >= 0.60`, `26.1 >= 20`, `1.2 <= 5`, and the Sentinel-2 dNBR status is `no_sufficient_scenes`. Therefore the final label is `obstructed_window_not_surface_map`.

The rounding order is part of the answer path: compute and round the two white shares to three decimals, compute `white_ratio` from those rounded shares, and then round the ratio, RGB spread, Sentinel-1 mean change, and precipitation ratio to one decimal. Sentinel-1, Sentinel-2, and rainfall are side metrics for interpreting observation quality, not measured damage.

# Scoring Rubric

- 3 points: Returns the requested JSON structure with the numeric fields, threshold object, final label, and one-sentence interpretation.
- 5 points: Correctly computes the RGB pixel metrics: event white share, pre-event white share, and event RGB spread using the stated formulas.
- 4 points: Correctly derives the white ratio, Sentinel-1 mean change, and precipitation max/mean ratio with the stated definitions and rounding order.
- 4 points: Applies all four threshold tests and reports the correct Boolean outcomes.
- 3 points: Gives the final label `obstructed_window_not_surface_map` and ties it directly to the threshold results.
- 1 point: Keeps Sentinel-1, Sentinel-2, and rainfall as side metrics and does not turn them into measured surface damage.

Total: 20 points.
