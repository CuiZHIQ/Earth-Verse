# Guinsaugon Rainfall Window Ledger

A draft rainfall note for the February 17, 2006 Guinsaugon landslide says the local numeric record is dominated by rainfall that accumulated before the event date, not by a same-day rainfall spike.

Using the incident package's daily precipitation records and event-day precipitation summaries, test that note quantitatively. Compute:

1. The Open-Meteo daily precipitation ledger: 14-day, 10-day, and 7-day totals before 2006-02-17; the event-day total; and the wettest pre-event date and amount.
2. The NASA POWER daily precipitation ledger using the same windows and event date.
3. The event-day mean precipitation checks from ERA5-Land, GPM IMERG, and CHIRPS, rounded to two decimals, plus their maximum mean.
4. Four threshold tests: Open-Meteo prior-14-day total at least 100 mm; NASA POWER prior-14-day total at least 250 mm; both daily event-day totals below 10 mm; maximum event-day gridded mean below 5 mm. Score one point for each passing test.

Return a compact JSON object with this shape:

```json
{
  "answer": "<pre_event_window_dominant or event_day_rain_dominant>",
  "openmeteo": {
    "prior14_mm": 0.0,
    "prior10_mm": 0.0,
    "prior7_mm": 0.0,
    "event_day_mm": 0.0,
    "wettest_prior_date": "YYYY-MM-DD",
    "wettest_prior_mm": 0.0
  },
  "nasa_power": {
    "prior14_mm": 0.0,
    "prior10_mm": 0.0,
    "prior7_mm": 0.0,
    "event_day_mm": 0.0,
    "wettest_prior_date": "YYYY-MM-DD",
    "wettest_prior_mm": 0.0
  },
  "event_day_means_mm": {
    "era5": 0.0,
    "gpm": 0.0,
    "chirps": 0.0,
    "max_mean": 0.0
  },
  "threshold_ledger": {
    "openmeteo_prior14_ge_100": true,
    "nasa_power_prior14_ge_250": true,
    "both_daily_event_lt_10": true,
    "gridded_event_max_lt_5": true,
    "score": 0
  },
  "decision_rule": "<one sentence explaining how the score determines the label>"
}
```
