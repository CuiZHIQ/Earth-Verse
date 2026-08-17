# Central Chile Rainfall-Scale Consistency Ledger

For the August 19-22, 2023 atmospheric-river period in central Chile, build a calculation ledger that tests whether the event record is numerically dominated by persistent local rainfall rather than regional precipitation averages or durable surface change.

Compute these values from the technical record:

- `event_span_days = end_date - start_date + 1`
- `local_total_mean_mm = mean(total rainfall from the two local daily point series)`
- `local_max_daily_mm = maximum daily rainfall across those two point series`
- `heavy_day_fraction = minimum count of days with at least 10 mm in the two local series / event_span_days`
- `regional_mean_max_mm = maximum mean accumulated precipitation among the regional summaries`
- `point_to_regional_ratio = local_total_mean_mm / regional_mean_max_mm`
- `image_shift_index = mean(abs(bright_fraction_delta) / 0.05, abs(blue_fraction_delta) / 0.02)`, where deltas are event minus pre-event values, `bright_fraction` is the share of RGB pixels with mean brightness greater than 180, and `blue_fraction` is the share with `B > R + 20` and `B > G + 10`. Compute these fractions over all RGB pixels in the package JPEG images as delivered; no separate no-data mask is applied.
- `annual_change_mean = mean annual 1-minus-cosine surface-change statistic`

Then apply this capped component ledger:

```text
total_c = min(local_total_mean_mm / 100, 1)
peak_c = min(local_max_daily_mm / 50, 1)
persistence_c = heavy_day_fraction
scale_c = min(point_to_regional_ratio / 10, 1)
image_c = 1 - min(image_shift_index, 1)
annual_c = 1 - min(annual_change_mean / 0.10, 1)
rainfall_scale_score = 0.25*total_c + 0.20*peak_c + 0.15*persistence_c + 0.20*scale_c + 0.10*image_c + 0.10*annual_c
```

Round millimeter anchors to one decimal except `regional_mean_max_mm` to three decimals, ratios and components to three decimals, `annual_change_mean` to four decimals, and `rainfall_scale_score` to three decimals.

Set `class_label` to `localized_persistent_rainfall_dominant` when `rainfall_scale_score >= 0.80` and `heavy_day_fraction == 1.0`; otherwise use `mixed_or_surface_change_dominant`.

Return only compact JSON:

```json
{
  "anchors": {
    "event_span_days": 0,
    "local_total_mean_mm": 0,
    "local_max_daily_mm": 0,
    "heavy_day_fraction": 0,
    "regional_mean_max_mm": 0,
    "point_to_regional_ratio": 0,
    "image_shift_index": 0,
    "annual_change_mean": 0
  },
  "components": {
    "total_c": 0,
    "peak_c": 0,
    "persistence_c": 0,
    "scale_c": 0,
    "image_c": 0,
    "annual_c": 0
  },
  "rainfall_scale_score": 0,
  "class_label": ""
}
```
