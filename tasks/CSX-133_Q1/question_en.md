# Super Typhoon Yagi Wind-Rain Peak Window Test

A technical review team is checking the 1-7 September 2024 Super Typhoon Yagi record for northern Viet Nam. They need a compact, reproducible test of whether the local wind and rainfall observations form one peak-window pulse on 7 September rather than two separated episodes.

Use the package hourly timestamp day for the hourly peak and wettest-day tests, and use the daily product date for the separate daily cross-check. Apply this rule: return `same_day_wind_rain_peak` only when the peak gust date is also the wettest package-timestamp day, the hourly precipitation peak is within 2 hours of the peak gust, the wettest day supplies at least 60% of event-window rainfall, and a separate daily wind/precipitation check also peaks on that date. Otherwise return `not_same_day_wind_rain_peak`.

Return JSON only:

```json
{
  "answer": "<same_day_wind_rain_peak or not_same_day_wind_rain_peak>",
  "peak_day": "YYYY-MM-DD",
  "metrics": {
    "peak_gust_kmh": 0,
    "peak_hourly_rain_mm": 0,
    "event_rain_mm": 0,
    "wettest_day_rain_mm": 0,
    "wettest_day_share": 0,
    "gust_to_rain_lag_h": 0
  },
  "rule_flags": {
    "same_day": true,
    "lag_le_2h": true,
    "share_ge_0_60": true,
    "daily_cross_check": true
  },
  "computed_sentence": "<one sentence explaining the rule result>"
}
```
