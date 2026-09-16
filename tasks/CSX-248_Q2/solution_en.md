# Correct Answer

```json
{
  "target_family": "remote_sensing_scene_change_numeric",
  "brightness_delta": -64.52,
  "green_share_delta": 0.3863,
  "spatial_change_ratio": 12.89,
  "contrast_index": 8.32
}
```

# Key Computations

The computation uses the CSX-248 package metadata, the pre-event and event-period preview images, and the annual spatial-change summary.

- Pre-event mean brightness: `160.40`.
- Event-period mean brightness: `95.88`.
- Brightness delta: `round(95.88 - 160.40, 2) = -64.52`.
- Pre-event green-dominant share: `0.0852`.
- Event-period green-dominant share: `0.4715`.
- Green-share delta: `round(0.4715 - 0.0852, 4) = 0.3863`.
- Annual spatial-change mean: `0.0529`.
- Annual spatial-change maximum: `0.6819`.
- Spatial-change ratio: `round(0.6819 / 0.0529, 2) = 12.89`.
- Contrast index: `round(abs(-64.52) * 12.89 / 100, 2) = 8.32`.

# Scoring Rubric

Total: 20 points.

- **Target family and JSON shape (3 points):** Returns exactly the requested JSON fields and uses `remote_sensing_scene_change_numeric` as the target family. Partial credit: 1-2 points for a valid JSON object with minor field-name or ordering issues.
- **Brightness delta (4 points):** Computes event-period minus pre-event mean brightness as `-64.52` within `0.05`. Partial credit: up to 2 points for the correct direction with an out-of-tolerance value.
- **Green-share delta (4 points):** Computes event-period minus pre-event green-dominant pixel share as `0.3863` within `0.0005`. Partial credit: up to 2 points for the correct direction with an out-of-tolerance value.
- **Spatial-change ratio (4 points):** Computes annual maximum divided by annual mean as `12.89` within `0.05`. Partial credit: up to 2 points for using the correct numerator and denominator with an arithmetic or rounding error.
- **Contrast index (3 points):** Applies `round(abs(brightness_delta) * spatial_change_ratio / 100, 2)` and returns `8.32` within `0.05`. Partial credit: up to 2 points for using the right formula with one upstream value slightly outside tolerance.
- **Concision and numeric discipline (2 points):** Provides only the requested numeric JSON and limits interpretation to measured image and change-stat fields. Partial credit: 1 point for extra prose that does not alter the numeric result.
