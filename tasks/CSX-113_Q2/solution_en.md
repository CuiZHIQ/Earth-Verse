# Final Answer

```json
{
  "answer": {
    "local_precip_mm": 111.7,
    "wettest_72h_mm": 111.7,
    "wettest_24_to_72_ratio": 0.504,
    "wet_run_hours": 62,
    "flood_lag_days": 1.42,
    "max_gust_kmh": 65.9,
    "gust_to_peak_wind_ratio": 0.264,
    "consequence_label": "linked_multi_day_runoff_pulse"
  },
  "proof": "The March 12-14 total equals the rolling 72-hour maximum, the 24h/72h ratio is 0.504, the wet run lasts 62 hours, the flood lag is 1.42 days, and the gust ratio is 0.264, so all thresholds pass."
}
```

# Key Computations

- The hourly precipitation series gives `local_precip_mm = 111.7` for 2023-03-12 00:00 through 2023-03-14 23:00.
- The maximum rolling 72-hour precipitation total is `wettest_72h_mm = 111.7`, matching the tested window within the 0.05 mm tolerance.
- The maximum rolling 24-hour total is `56.3` mm, so `wettest_24_to_72_ratio = 56.3 / 111.7 = 0.504`.
- The longest continuous hourly run with precipitation greater than 0 is `wet_run_hours = 62`.
- The Malawi flood catalog start follows Freddy's tropical-cyclone catalog end by `flood_lag_days = 1.42`.
- The maximum local gust is `65.9` km/h, and the cataloged Freddy peak wind is `250.0` km/h, so `gust_to_peak_wind_ratio = 65.9 / 250.0 = 0.264`.

# Reasoning Path

The rainfall-total test passes because the March 12-14 local accumulation is at least 100 mm and is also the rolling 72-hour maximum. The concentration test passes because the 24-hour share is below 0.60, meaning the event window is not dominated by one 24-hour burst. The duration test passes because the wet run lasts 62 hours, exceeding the 48-hour threshold. The timing test passes because the Malawi flood start is 1.42 days after Freddy's tropical-cyclone end, within the 2.0-day limit. The wind-ratio test passes because the local gust ratio is 0.264, below 0.35. Since every threshold passes, the deterministic label is `linked_multi_day_runoff_pulse`.

# Computed Interpretation

The threshold ledger supports a compact rain-lag result: the tested Malawi window is the wettest 72-hour span, rainfall is spread across a 62-hour wet run, flood onset follows within 1.42 days, and the local gust ratio remains below the wind-dominance cutoff.

# Scoring Rubric

- 4 points: Computes `local_precip_mm = 111.7` and `wettest_72h_mm = 111.7` from the hourly precipitation series. Partial credit: award 2 points for one correct total, or 3 points for both totals with only minor rounding or window-edge error.
- 4 points: Computes `wettest_24_to_72_ratio = 0.504` using the maximum rolling 24-hour total divided by the maximum rolling 72-hour total. Partial credit: award 2 points for the correct formula with a wrong rolling numerator, or 3 points for a correct ratio rounded less precisely.
- 3 points: Computes `wet_run_hours = 62` using precipitation greater than 0 as the hourly condition. Partial credit: award 1-2 points for a continuous wet-run calculation with a minor threshold or endpoint mistake.
- 3 points: Computes `flood_lag_days = 1.42` from Freddy's tropical-cyclone end timestamp and the Malawi flood start timestamp. Partial credit: award 1-2 points for using the right timestamps but rounding or time-unit conversion incorrectly.
- 3 points: Computes `max_gust_kmh = 65.9` and `gust_to_peak_wind_ratio = 0.264` using the 250.0 km/h cataloged peak wind. Partial credit: award 1-2 points for one correct gust value or for a correct division with imprecise rounding.
- 3 points: Returns the compact JSON with `consequence_label = linked_multi_day_runoff_pulse` and a one-sentence proof that all thresholds pass. Partial credit: award 1-2 points for the right label with missing proof details or for a correct proof but incomplete JSON.
