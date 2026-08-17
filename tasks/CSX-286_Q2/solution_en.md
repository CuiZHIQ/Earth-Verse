# Correct Answer

```json
{
  "event_days": 13,
  "regional_mean_mm": 83.5,
  "regional_spread_pct": 6.4,
  "local_total_mm": 116.7,
  "local_daily_mean_mm": 9.0,
  "peak_day": "2024-04-26",
  "peak_day_mm": 20.9,
  "peak_to_mean_ratio": 2.32,
  "peak_share_pct": 17.9,
  "max_3day_total_mm": 49.7,
  "max_3day_start": "2024-04-24",
  "max_3day_end": "2024-04-26",
  "max_5day_total_mm": 70.8,
  "max_5day_start": "2024-04-24",
  "max_5day_end": "2024-04-28",
  "wet_days_ge_5mm": 10,
  "wet_days_ge_10mm": 5,
  "persistence_weighted_regional_mm": 49.3
}
```

# Computation Notes

The regional pair uses the two event-accumulated gridded precipitation means, 86.149968 mm and 80.784195 mm, so `regional_mean_mm = (86.149968 + 80.784195) / 2 = 83.5` and `regional_spread_pct = |86.149968 - 80.784195| / 83.467082 * 100 = 6.4`.

The date-matched local daily series sums to 116.675 mm across 13 days. The largest averaged daily value is 20.855 mm on 2024-04-26, giving `local_daily_mean_mm = 116.675 / 13 = 9.0`, `peak_to_mean_ratio = 20.855 / 8.975 = 2.32`, and `peak_share_pct = 20.855 / 116.675 * 100 = 17.9`.

Rolling sums from the averaged local daily series give 49.695 mm for 2024-04-24 through 2024-04-26 and 70.780 mm for 2024-04-24 through 2024-04-28. The wet-day counts are 10 days at or above 5 mm and 5 days at or above 10 mm. The final score is `83.467082 * (10 / 13) * (1 - 0.178744) * (1 - 0.064286) = 49.3 mm`.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns compact JSON with the requested numeric fields and date fields.
- 4 points: Extracts the two regional accumulated-precipitation means and computes the regional mean and spread correctly.
- 4 points: Builds the date-matched local daily series from the two point records and computes total, daily mean, peak day, peak amount, peak-to-mean ratio, and peak share.
- 4 points: Computes rolling 3-day and 5-day maxima with correct start/end dates plus both wet-day counts.
- 3 points: Applies the persistence-weighted regional formula with correct order of operations and rounding.
- 2 points: Uses units, percentages, ratios, and dates consistently while keeping the explanation calculation-centered.
