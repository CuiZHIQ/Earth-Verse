# Correct Answer

The computed `rainfall_scale_score` is **0.874**, so the class label is **`localized_persistent_rainfall_dominant`**.

# Key Computations

- Event span: 2023-08-19 through 2023-08-22, inclusive, gives `event_span_days = 4`.
- Local point totals: NASA POWER totals 66.9 mm and Open-Meteo totals 174.5 mm, so `local_total_mean_mm = 120.7`.
- Daily peak: the maximum daily point rainfall is `local_max_daily_mm = 54.5`.
- Heavy-day persistence: both point series have four days at or above 10 mm, so `heavy_day_fraction = 4 / 4 = 1.000`.
- Regional mean maximum: the regional mean accumulated precipitation values are 0.570 mm, 0.019 mm, and 8.871 mm, so `regional_mean_max_mm = 8.871` and `point_to_regional_ratio = 120.7 / 8.871 = 13.606`.
- Image shift: all RGB pixels in the package JPEG images are used as delivered, with no separate no-data mask. Bright-fraction delta is -0.035300 and blue-fraction delta is -0.011915, giving `image_shift_index = 0.651`.
- Annual change: the mean annual 1-minus-cosine value is `annual_change_mean = 0.0611`.

The capped components are:

```json
{
  "total_c": 1.000,
  "peak_c": 1.000,
  "persistence_c": 1.000,
  "scale_c": 1.000,
  "image_c": 0.349,
  "annual_c": 0.389
}
```

Final score:

```text
0.25*1.000 + 0.20*1.000 + 0.15*1.000 + 0.20*1.000 + 0.10*0.349 + 0.10*0.389 = 0.874
```

# Reasoning Path

The ledger gives full credit to the local rainfall total, the daily peak, the four-day persistence fraction, and the point-to-regional contrast. The image and annual-change terms contribute smaller positive values because the true-color shift and annual mean surface-change value are moderate rather than dominant in the formula. Since the score exceeds 0.80 and the heavy-day fraction equals 1.000, the final class follows directly from the stated threshold rule.

# Scoring Rubric

- 4 points: Computes the inclusive four-day span and extracts both local daily rainfall series with correct totals and daily maximum.
- 4 points: Computes the heavy-day fraction from both local series and reports `heavy_day_fraction = 1.000`.
- 3 points: Extracts the three regional mean precipitation values, identifies 8.871 mm as the maximum, and computes `point_to_regional_ratio = 13.606`.
- 3 points: Computes the bright-fraction and blue-fraction image deltas over all RGB pixels in the package JPEG images as delivered, converts them into `image_shift_index = 0.651`, and extracts `annual_change_mean = 0.0611`.
- 4 points: Applies all six capped component formulas and combines them with the stated weights to obtain `rainfall_scale_score = 0.874` within 0.005.
- 2 points: Returns compact JSON with anchors, components, score, and `localized_persistent_rainfall_dominant` as the final class.
