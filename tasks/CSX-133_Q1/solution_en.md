# Final Answer

The correct answer is `same_day_wind_rain_peak`.

```json
{
  "answer": "same_day_wind_rain_peak",
  "peak_day": "2024-09-07",
  "metrics": {
    "peak_gust_kmh": 116.6,
    "peak_hourly_rain_mm": 17.8,
    "event_rain_mm": 165.3,
    "wettest_day_rain_mm": 119.0,
    "wettest_day_share": 0.72,
    "gust_to_rain_lag_h": 1.0
  },
  "rule_flags": {
    "same_day": true,
    "lag_le_2h": true,
    "share_ge_0_60": true,
    "daily_cross_check": true
  },
  "computed_sentence": "The 7 September peak gust and rainfall maximum satisfy the same-day, 2-hour lag, 60% rainfall-share, and daily cross-check tests."
}
```

# Key Computations

- Hourly gust maximum: 116.6 km/h at 2024-09-07T12:00.
- Hourly precipitation maximum: 17.8 mm at 2024-09-07T13:00.
- Signed lag from gust peak to hourly rain peak: +1.0 hour, so the absolute lag is within the 2-hour rule.
- Event-window rainfall from the hourly series: 165.3 mm.
- Wettest package-timestamp day: 2024-09-07 with 119.0 mm.
- Wettest-day rainfall share: 119.0 / 165.3 = 0.720, or 72.0%.
- Separate daily check: daily precipitation peaks on 2024-09-07 at 118.6 mm/day and daily 10 m wind speed peaks on 2024-09-07 at 11.81 m/s.

# Reasoning Path

The label is determined by four Boolean tests. First, the package timestamp date of the peak gust is 2024-09-07, which is the same date as the wettest package-timestamp day. Second, the hourly rainfall maximum occurs one hour after the gust maximum, satisfying the 2-hour lag condition. Third, the wettest day contributes 72.0% of the full 1-7 September rainfall total, exceeding the 60% concentration threshold. Fourth, the daily cross-check has both wind and precipitation maxima on 2024-09-07.

Because all four tests are true, the rule returns `same_day_wind_rain_peak`. A separated-episode answer fails the lag and concentration checks: the strongest wind and the largest rainfall load are tightly aligned in time, and most of the event rainfall falls on the peak day.

# Computed Interpretation

For this task's numeric test, 2024-09-07 is the single wind-rain peak window. The result should be reported as a compact timing and threshold ledger, not as a broad damage narrative.

# Scoring Rubric

Total: 20 points.

- Final peak-window label, 4 points: Full credit for returning `same_day_wind_rain_peak` with peak day 2024-09-07. Partial credit: 2 points for identifying 2024-09-07 as the key day but using an imprecise label; 1 point for noting strong wind and rain without applying the rule.
- Hourly peak extraction, 4 points: Full credit for 116.6 km/h peak gust at 2024-09-07T12:00 and 17.8 mm peak hourly rain at 2024-09-07T13:00. Partial credit: 2-3 points for one exact peak plus the correct date; 1 point for approximate peak values without times.
- Rainfall aggregation and share, 4 points: Full credit for event rainfall 165.3 mm, wettest-day rainfall 119.0 mm, and wettest-day share 0.72 or 72.0%. Partial credit: 2-3 points for correct accumulation values with a missing or slightly rounded share; 1 point for only naming the wettest day.
- Lag and rule flags, 3 points: Full credit for computing a +1.0 hour gust-to-rain lag and marking same_day, lag_le_2h, and share_ge_0_60 as true. Partial credit: 1-2 points for correct flags with a missing signed lag or minor threshold wording error.
- Daily cross-check, 2 points: Full credit for using the daily precipitation maximum of 118.6 mm/day and daily 10 m wind maximum of 11.81 m/s, both on 2024-09-07. Partial credit: 1 point for recognizing daily agreement but omitting one value.
- Structured answer discipline, 3 points: Full credit for concise JSON with the requested fields and no unrequested casualty, housing, mapped-damage, or broad narrative additions. Partial credit: 1-2 points for correct computations with minor JSON or verbosity problems.
