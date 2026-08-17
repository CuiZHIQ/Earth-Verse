# Saharan Dust Optical-Veil Consistency Check

For the March 2022 Saharan dust episode affecting Spain, Portugal, and France, compute a deterministic optical-veil consistency check from the pre-event RGB scene, the event-window RGB scene, event-window accumulated precipitation, and annual surface-change context.

Use these formulas:

- `scene_brightness = mean((R + G + B) / 3)`
- `scene_contrast = mean(stddev(R), stddev(G), stddev(B))`
- `brightness_delta = event_scene_brightness - pre_scene_brightness`
- `contrast_drop = pre_scene_contrast - event_scene_contrast`
- `rgb_delta_range = max(event_mean_rgb - pre_mean_rgb) - min(event_mean_rgb - pre_mean_rgb)`
- `veil_index = (brightness_delta + contrast_drop) / (1 + rgb_delta_range)`
- `wet_ratio = event_precip_mm_max / max(brightness_delta, 0.001)`
- `veil_score` is the count of passed tests: `brightness_delta >= 10`, `contrast_drop >= 5`, `rgb_delta_range <= 2`, `veil_index >= 10`, `wet_ratio <= 0.10` with `event_precip_mm_mean <= 0.10`, and `annual_surface_change_mean <= 0.10` with `annual_surface_change_max <= 0.60`.

Classify the case as `transported_saharan_dust_optical_veil` when `veil_score == 6`; otherwise use `mixed_or_surface_dominated_signal`.

Return compact JSON:

```json
{
  "answer": {
    "brightness_delta": 0.0,
    "contrast_drop": 0.0,
    "rgb_delta_range": 0.0,
    "veil_index": 0.0,
    "wet_ratio": 0.0,
    "surface_change_max": 0.0,
    "veil_score": 0,
    "classification": "<classification label>"
  },
  "interpretation": "<one short computed consequence>"
}
```
