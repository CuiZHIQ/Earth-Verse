# East Africa Rainfall Concentration Ledger

Use the local CSX-286 package data for the late-April to early-May 2024 East Africa rainfall and floods. Build a numeric ledger from the event-period precipitation records.

Construct the local daily precipitation series by date-matching the two point daily precipitation records and averaging the two values for each date. For the regional pair, use the two gridded records whose summaries are event-accumulated precipitation means; hourly aggregate summaries are not part of this regional-pair calculation.

Derive the following quantities:

1. `event_days`, `regional_mean_mm`, and `regional_spread_pct`.
2. `local_total_mm`, `local_daily_mean_mm`, `peak_day`, and `peak_day_mm`.
3. `peak_to_mean_ratio = peak_day_mm / local_daily_mean_mm`.
4. `peak_share_pct = 100 * peak_day_mm / local_total_mm`.
5. `max_3day_total_mm`, `max_5day_total_mm`, and their start/end dates from the averaged local daily series.
6. `wet_days_ge_5mm` and `wet_days_ge_10mm`.
7. `persistence_weighted_regional_mm = regional_mean_mm * (wet_days_ge_5mm / event_days) * (1 - peak_share_pct / 100) * (1 - regional_spread_pct / 100)`.

Return compact JSON with those keys. Round millimeter values and percentages to one decimal place, ratios to two decimals, and dates as `YYYY-MM-DD`.
