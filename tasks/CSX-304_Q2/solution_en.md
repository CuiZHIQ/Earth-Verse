# Correct Answer

```json
{
  "answer": "onset_wind_supported_then_wet_moderated",
  "wind_pair_days": 1,
  "wind_peak": {"date": "2022-04-07", "ratio": 1.022},
  "rain_pair_days": 1,
  "rain_peak": {"date": "2022-04-08", "ratio": 1.46},
  "lag_days": 1,
  "late_pair": false,
  "regional_mean_mm": 8.6802
}
```

# Key Computations

Daily wind threshold ratios use `min(point_wind_m_s / 4.5, companion_wind_km_h / 22.0)`.

- 2022-04-07: `min(4.60 / 4.5, 25.0 / 22.0) = 1.022`, so this is a paired wind-support day.
- 2022-04-08: `min(4.10 / 4.5, 23.1 / 22.0) = 0.911`.
- 2022-04-09: `min(2.96 / 4.5, 19.3 / 22.0) = 0.658`.
- 2022-04-10: `min(4.67 / 4.5, 14.6 / 22.0) = 0.664`, so the late-window wind revival test is false.

Daily rain threshold ratios use `min(point_precip_mm / 10.0, companion_precip_mm / 10.0)`.

- 2022-04-07: `min(8.98 / 10.0, 14.4 / 10.0) = 0.898`.
- 2022-04-08: `min(37.60 / 10.0, 14.6 / 10.0) = 1.460`, so this is a paired rain-moderation day.
- 2022-04-09: `min(5.03 / 10.0, 2.7 / 10.0) = 0.270`.
- 2022-04-10: `min(2.28 / 10.0, 8.9 / 10.0) = 0.228`.

The rain peak on 2022-04-08 follows the wind peak on 2022-04-07 by one day. The three regional event-precipitation means average to `(14.4043 + 5.3213 + 6.3151) / 3 = 8.6802 mm`.

# Reasoning Path

The threshold proof is satisfied because there is exactly one paired wind-support day, it occurs at the event onset, there is exactly one paired rain-moderation day, the rain peak follows by one day, and the 2022-04-10 late-pair test fails. These are package-derived threshold diagnostics, not measured loss, closure, admission, asset-damage, or exact-footprint evidence. The compact computed consequence is therefore `onset_wind_supported_then_wet_moderated`.

# Scoring Rubric

- 4 points: Returns compact JSON with the requested fields and numeric types, including the final answer label. Partial credit: 2-3 points for minor naming or rounding issues that do not obscure the computed values.
- 4 points: Uses the wind-ratio formula correctly, finds one paired wind-support day, and identifies 2022-04-07 with ratio 1.022. Partial credit: 1-3 points for correct date or count with an incomplete ratio formula.
- 4 points: Uses the rain-ratio formula correctly, finds one paired rain-moderation day, and identifies 2022-04-08 with ratio 1.460. Partial credit: 1-3 points for correct date or count with an incomplete ratio formula.
- 3 points: Computes the one-day lag and marks the 2022-04-10 late-pair test as false. Partial credit: 1-2 points for either lag or late-pair state alone.
- 2 points: Averages the three regional precipitation means to 8.6802 mm, with acceptable rounding to 8.68 mm. Partial credit: 1 point for using at least two means with a close rounded value.
- 2 points: Derives `onset_wind_supported_then_wet_moderated` from the counts, dates, lag, and failed late-pair test. Partial credit: 1 point for a compatible concise label with one missing threshold detail.
- 1 point: Avoids converting the package-derived numeric thresholds into measured losses, closures, admissions, asset damage, or exact footprint evidence.
