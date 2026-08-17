# CSX-248 Q2: Remote-Sensing Change Ratios for the 2018 Europe Compound Event

Using the CSX-248 event package, compute a compact numeric summary for the event-period preview imagery and the annual spatial-change statistics.

Use these formulas:

- `brightness_delta = round(event_mean_brightness - pre_mean_brightness, 2)`, where mean brightness is the average of the RGB channel means.
- `green_share_delta = round(event_green_dominant_share - pre_green_dominant_share, 4)`, where a pixel is green-dominant when `G > R` and `G > B`.
- `spatial_change_ratio = round(annual_change_max / annual_change_mean, 2)`.
- `contrast_index = round(abs(brightness_delta) * spatial_change_ratio / 100, 2)`.

Return only this JSON object, with no extra prose:

```json
{
  "target_family": "remote_sensing_scene_change_numeric",
  "brightness_delta": 0.0,
  "green_share_delta": 0.0,
  "spatial_change_ratio": 0.0,
  "contrast_index": 0.0
}
```
