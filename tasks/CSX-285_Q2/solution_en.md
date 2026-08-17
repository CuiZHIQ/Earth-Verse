# Correct Answer

```json
{
  "anchors": {
    "gpm_mean_mm": 142.2,
    "gpm_max_mm": 637.7,
    "chirps_mean_mm": 105.5,
    "chirps_max_mm": 492.3,
    "brightness_delta": 10.11,
    "dark_fraction_delta": 0.0593,
    "annual_change_mean": 0.0202
  },
  "components": {
    "gpm_c": 0.948,
    "chirps_c": 0.879,
    "brightness_c": 0.842,
    "dark_c": 0.847,
    "annual_c": 0.596
  },
  "storm_surface_score": 0.861,
  "classification": "storm_window_transient_signal_dominant"
}
```

# Calculation

The precipitation anchors are `142.2 mm` mean and `637.7 mm` maximum from GPM, plus `105.5 mm` mean and `492.3 mm` maximum from CHIRPS. The bilinear-resized image metrics are `119.14` pre-event brightness, `109.03` event brightness, `0.2546` pre-event dark fraction, and `0.3139` event dark fraction, giving `brightness_delta = 10.11` for pre-event minus event brightness and `dark_fraction_delta = 0.0593`. The annual `1-cosine` mean is `0.0202`.

The capped components are:

- `gpm_c = min(142.2 / 150, 1) = 0.948`
- `chirps_c = min(105.5 / 120, 1) = 0.879`
- `brightness_c = min((119.14 - 109.03) / 12, 1) = 0.842`
- `dark_c = min(0.0593 / 0.07, 1) = 0.847`
- `annual_c = 1 - min(0.0202 / 0.05, 1) = 0.596`

So `storm_surface_score = 0.30*0.948 + 0.30*0.879 + 0.20*0.842 + 0.10*0.847 + 0.10*0.596 = 0.861`. Since `0.861 >= 0.75` and `0.0202 < 0.05`, the class label is `storm_window_transient_signal_dominant`.

# Scoring Rubric

- 4 points: Correctly extracts GPM and CHIRPS means and maxima in millimeters.
- 4 points: Correctly computes bilinear-resized image brightness and dark-fraction deltas, with brightness_delta as pre-event minus event brightness.
- 5 points: Correctly applies all five capped component formulas.
- 4 points: Correctly computes the weighted score within `0.01`.
- 3 points: Returns compact JSON with anchors, components, score, and class label.
