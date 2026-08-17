# Hurricane Harvey Rainfall Volume Diagnostic

A hydrometeorology team is checking whether Hurricane Harvey's Houston-area flood severity during August 25-31, 2017 is better represented as a sustained multi-day rainfall event than as a two-day peak burst.

Using the technical record, extract the event window, the highest reported storm-total gauge rainfall, Houston Hobby's four-day rainfall, the two-day Houston rainfall amount, the 20-inch broad-area rainfall threshold, the broad-area size, and the exposed population count. Then compute a compact rainfall-volume diagnostic with unit conversions, duration ratios, and a minimum water-volume estimate.

Use these formulas:

- `event_duration_days` = inclusive days from the event start date through the event end date.
- `peak_gauge_mm` = highest reported gauge rainfall in inches times 25.4.
- `hobby_4day_mm` = Houston Hobby four-day rainfall in inches times 25.4.
- `two_day_mm` = two-day Houston rainfall in inches times 25.4.
- `four_day_to_two_day_ratio` = `hobby_4day_mm / two_day_mm`.
- `two_day_peak_share` = `two_day_mm / peak_gauge_mm`.
- `min_20in_volume_km3` = 20 inches converted to meters times 29,000 square miles converted to square meters, divided by 1e9.
- `per_person_min_volume_m3` = the same minimum volume in cubic meters divided by 6.7 million people.

Apply this threshold state:

- `pass_multiday_volume` if `event_duration_days >= 7`, `peak_gauge_mm >= 1000`, `four_day_to_two_day_ratio >= 1.25`, `min_20in_volume_km3 >= 35`, and `per_person_min_volume_m3 >= 5000`.
- `fail_two_day_only` if `two_day_peak_share <= 0.60` and `four_day_to_two_day_ratio >= 1.25`.

Return only compact JSON in this shape, with numeric values rounded as shown by the field names where applicable:

```json
{
  "event_duration_days": 0,
  "peak_gauge_mm": 0.0,
  "hobby_4day_mm": 0.0,
  "two_day_mm": 0.0,
  "four_day_to_two_day_ratio": 0.0,
  "two_day_peak_share": 0.0,
  "min_20in_volume_km3": 0.0,
  "per_person_min_volume_m3": 0.0,
  "threshold_state": "",
  "diagnosis_label": ""
}
```
