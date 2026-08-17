# Hurricane Ida Northeast Rainfall Concentration Ledger

For the September 1-3, 2021 Northeast phase of Hurricane Ida, compute a compact hydrometeorological ledger that tests whether the event data satisfy a concentrated-rainfall flood signature.

Use these formulas and thresholds:

- `event_total_mm = sum(hourly precipitation)`
- `wettest_6h_mm = max rolling 6-hour precipitation sum`
- `six_hour_share = wettest_6h_mm / event_total_mm`
- `wet_run_hours = longest contiguous run of hourly precipitation > 0`
- `rain_pass_count` is the number of true tests among `regional_peak_floor_mm >= 254`, `central_park_record_hour_mm >= 75`, `wettest_6h_mm >= 75`, `six_hour_share >= 0.60`, `city_report_total >= 400`, and `top3_borough_share >= 0.75`
- `contrast_pass_count` is the number of true tests among `max_point_wind_kmh < 63`, `abs(sentinel1_mean_db) < 1`, and `alphaearth_mean_change < 0.05`

Set `final_state` to `"rainfall_concentration_signature_supported"` when `rain_pass_count >= 5` and `contrast_pass_count >= 2`; otherwise set it to `"rainfall_concentration_signature_not_supported"`.

Return compact JSON with exactly this shape:

```json
{
  "event_total_mm": 0.0,
  "wettest_6h_mm": 0.0,
  "six_hour_share": 0.0,
  "wet_run_hours": 0,
  "threshold_counts": {"rain": 0, "contrast": 0},
  "final_state": ""
}
```
