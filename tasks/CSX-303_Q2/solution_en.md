# Correct Answer

```json
{
  "answer": {
    "brightness_delta": 11.846,
    "contrast_drop": 7.514,
    "rgb_delta_range": 0.652,
    "veil_index": 11.719,
    "wet_ratio": 0.054,
    "surface_change_max": 0.5082,
    "veil_score": 6,
    "classification": "transported_saharan_dust_optical_veil"
  },
  "interpretation": "The scene-level brightening and contrast loss pass the optical-veil thresholds while wet and persistent-surface readings remain below their screens."
}
```

# Computation Path

The pre-event scene has mean brightness 158.504 and mean contrast 72.020. The event-window scene has mean brightness 170.350 and mean contrast 64.506.

Thus `brightness_delta = 170.350 - 158.504 = 11.846`, and `contrast_drop = 72.020 - 64.506 = 7.514`. The event-minus-pre mean RGB deltas are `[11.428, 12.028, 12.080]`, giving `rgb_delta_range = 12.080 - 11.428 = 0.652`.

The normalized index is `(11.846 + 7.514) / (1 + 0.652) = 11.719`. The event-window accumulated precipitation maximum is 0.640 mm, so `wet_ratio = 0.640 / 11.846 = 0.054`; the precipitation mean is 0.026 mm. The annual surface-change screen remains below its limits, with mean 0.0752 and maximum 0.5082.

All six threshold tests pass, so `veil_score = 6` and the deterministic classification is `transported_saharan_dust_optical_veil`.

# Scoring Rubric

- 3 points: Returns the requested compact JSON structure with the eight answer fields and one concise interpretation.
- 4 points: Computes scene brightness, scene contrast, brightness delta, and contrast drop from the RGB scenes with correct units or unit-implied field names.
- 3 points: Computes the RGB delta range and `veil_index` with the stated formulas and acceptable rounding.
- 3 points: Computes `wet_ratio` from accumulated precipitation and applies the precipitation mean screen correctly.
- 3 points: Applies the annual surface-change mean and maximum screens correctly.
- 3 points: Counts all six threshold tests and returns `veil_score = 6` with `transported_saharan_dust_optical_veil`.
- 1 point: Keeps the interpretation to a computed consequence and avoids escalating the numbers into unmeasured damage or regional concentration.

Total: 20 points.
