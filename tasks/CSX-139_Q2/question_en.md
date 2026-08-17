# Storm Ciaran Pressure-Wind Consistency Ledger

A technical reviewer is checking this proposed diagnosis for Storm Ciaran at the package point-weather reference site during 1-2 November 2023:

> At the reference site, rapid pressure deepening is quantitatively consistent with a multi-hour wind-led hazard signal; rainfall is present but does not dominate the local hourly ledger.

Compute the ledger below from the event data and return only JSON in this shape:

```json
{
  "answer": "<diagnosis label>",
  "rapid_deepening": {
    "fall_24h_hpa": 0,
    "threshold_hpa": 0,
    "ratio": 0,
    "pass": true
  },
  "wind_persistence": {
    "min_pressure_hpa": 0,
    "max_gust_kmh": 0,
    "gust_lag_hr": 0,
    "hours_gust_ge_70": 0,
    "hours_gust_ge_80": 0,
    "impulse_score": 0,
    "pass": true
  },
  "rainfall_contrast": {
    "point_total_mm": 0,
    "nov2_share": 0,
    "gpm_max_mean_ratio": 0,
    "local_rain_dominant": false
  },
  "conclusion": "<one sentence>",
  "rejected_alternative": "<one sentence>"
}
```

Use these definitions:

- `fall_24h_hpa` is the largest value of `pressure(t - 24 h) - pressure(t)` in the hourly pressure series.
- `threshold_hpa = 24 * sin(abs(latitude)) / sin(60 degrees)`. The rapid-deepening test passes when `fall_24h_hpa >= threshold_hpa`; `ratio = fall_24h_hpa / threshold_hpa`.
- `gust_lag_hr` is the time of maximum gust minus the time of minimum pressure. The wind-persistence test passes when `0 <= gust_lag_hr <= 6` and `impulse_score >= 15`, where `impulse_score = hours_gust_ge_70 + 2 * hours_gust_ge_80`.
- `point_total_mm` is the event-total hourly precipitation at the point, `nov2_share` is the 2 November share of that total, and `gpm_max_mean_ratio` is event accumulated GPM precipitation maximum divided by its mean. Set `local_rain_dominant` to true only if `point_total_mm >= 50` or `nov2_share >= 0.50`.

Round pressures, wind speeds, rainfall totals, and the threshold to 0.1; round ratios and shares to three decimals except `gpm_max_mean_ratio`, which should be rounded to two decimals.
