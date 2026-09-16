# Calbuco Eruption Observation Ledger

For the April 2015 Calbuco eruption in southern Chile, compute a compact ledger that tests whether the event-window true-color view should be treated as an obstructed observation window rather than as a surface-change map.

Use these definitions:

- `white_neutral_share`: share of RGB pixels where all three channels are greater than 180 and `max(R,G,B) - min(R,G,B) < 60`.
- `white_ratio`: event-window `white_neutral_share` divided by pre-event `white_neutral_share`.
- `event_rgb_spread`: `max(mean_R, mean_G, mean_B) - min(mean_R, mean_G, mean_B)` for the event-window RGB image.
- `s1_mean_change_db`: the package Sentinel-1 VV `post_minus_pre` mean-change statistic, used only as a side metric for image-context consistency.
- `rain_max_mean_ratio`: event-window maximum accumulated precipitation divided by mean accumulated precipitation.

Apply this threshold rule: the final label is `obstructed_window_not_surface_map` when `event_white_share >= 0.60`, `white_ratio >= 20`, `event_rgb_spread <= 5`, and the Sentinel-2 dNBR status is `no_sufficient_scenes`.

Compute the RGB metrics first. Round `event_white_share` and `pre_white_share` to `3` decimals, then compute and round `white_ratio` to `1` decimal. Round `event_rgb_spread`, `s1_mean_change_db`, and `rain_max_mean_ratio` to `1` decimal. Keep Sentinel-1, Sentinel-2, and rainfall values as side metrics; do not turn them into measured surface damage.

Return compact JSON:

```json
{
  "event_white_share": 0.0,
  "pre_white_share": 0.0,
  "white_ratio": 0.0,
  "event_rgb_spread": 0.0,
  "s1_mean_change_db": 0.0,
  "rain_max_mean_ratio": 0.0,
  "s2_status": "<status>",
  "thresholds": {
    "event_white_ge_0_60": true,
    "white_ratio_ge_20": true,
    "event_rgb_spread_le_5": true,
    "s2_scene_gap": true
  },
  "conclusion": "<final label>",
  "interpretation": "<one sentence tied to the numbers>"
}
```
