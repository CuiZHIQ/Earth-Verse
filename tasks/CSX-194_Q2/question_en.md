# Black Summer Fire-Weather Phase Ledger

A fire-weather review team is checking the early escalation of the 2019-2020 Australian Black Summer bushfires in southeastern Australia from late August through mid-October 2019. The key diagnostic question is whether the record supports an early-September spread peak with continued later renewed-spread concern, or whether the later period was effectively rain-suppressed.

Compute a score ledger for three phase windows:

- `baseline_watch`: 2019-08-18 to 2019-08-31
- `initial_spread`: 2019-09-01 to 2019-09-16
- `later_renewed_spread`: 2019-09-17 to 2019-10-16

For each window, use the package point-weather daily diagnostic as a phase-comparison input, not as a complete regional weather field:

`score = 0.35 * dry_day_fraction + 0.25 * zero_rain_fraction + 0.20 * (max_daily_high_temperature_c / 30) + 0.20 * (max_daily_wind_speed_kmh / 35)`

Also compute the strongest post-2019-09-16 single-day warning score:

`single_day_score = 0.45 * (temperature_c / 30) + 0.35 * (wind_kmh / 35) + 0.20 if precipitation is 0 mm`

Return compact JSON with:

- `period_scores`: each period's total precipitation, dry-day count, zero-rain-day count, maximum temperature, maximum wind, and score rounded to 3 decimals;
- `score_comparison`: dominant, secondary, and baseline period labels plus the top-minus-second score gap;
- `strongest_later_day`: date, temperature, precipitation, wind, and score;
- `burn_signal`: mean dNBR, maximum dNBR, and whether positive mean dNBR supports burn disturbance; and
- `final_label`: one concise stage diagnosis.

Keep the interpretation to one sentence and do not expand into operational advice or a broad disaster explanation.
