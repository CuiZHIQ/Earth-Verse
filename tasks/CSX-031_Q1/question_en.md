# East Asia Cold Wave: Cold-Persistence Dominance Test

A draft technical summary for the January 20-26, 2016 East Asia cold wave says the sampled local signal is cold-persistence dominated, with snow and wind stress co-timed with the cold peak rather than a precipitation-dominated winter-storm signal.

Using the incident's quantitative cold-wave record, test that summary quantitatively. Compute and return:

1. Freezing degree-days from daily minimum temperature relative to 0 C:
   `sum(max(0, 0 - daily_Tmin_C))`
2. The persistence signature: event-window days, daily-minimum days below 0 C, longest consecutive daily-minimum run below 0 C, and hourly temperature observations below 0 C.
3. The peak cold/wind timing: coldest daily minimum with date, maximum hourly wind gust with time, and the temperature at that gust hour.
4. The snow overlap signature: event snowfall total, maximum daily snowfall and date, snowfall-hour count, below-zero snowfall-hour count, and the fraction of event snowfall occurring on days whose daily minimum was below 0 C.
5. The mean precipitation checks from the three gridded precipitation summaries, rounded to two decimals.

Return a compact JSON object with this shape:

```json
{
  "answer": "<concise dominance label>",
  "cold_load": {
    "window_days": 0,
    "fdd_c_day": 0.0,
    "below0_daily_min_days": 0,
    "longest_below0_run_days": 0,
    "below0_hours": 0
  },
  "peak_cold_wind": {
    "date": "YYYY-MM-DD",
    "tmin_c": 0.0,
    "max_gust_kmh": 0.0,
    "gust_time": "YYYY-MM-DDTHH:MM",
    "gust_temp_c": 0.0
  },
  "snow_overlap": {
    "total_cm": 0.0,
    "max_day_cm": 0.0,
    "max_day": "YYYY-MM-DD",
    "snow_hours": 0,
    "below0_snow_hours": 0,
    "snow_share_on_below0_tmin_days": 0.0
  },
  "precip_means_mm": {
    "era5": 0.0,
    "gpm": 0.0,
    "chirps": 0.0
  },
  "decision_rule": "<one-sentence numerical rule used>"
}
```
