# Correct Answer

```json
{
  "evidence_windows": {
    "event_window": {
      "start": "2020-02-06",
      "end": "2020-02-06"
    },
    "precip_wind_window": {
      "start": "2020-02-06",
      "end": "2020-02-06"
    },
    "transport_report_context_date": "2020-03-07"
  },
  "pmax_mm": 0.602,
  "dry_count": 3,
  "wind_m_s": 1.758,
  "transport_km_lb": 120,
  "pm_obs_frac": 0.0,
  "conclusion": "dry_wind_conditions_with_report_context_transport_not_measured_pm"
}
```

# Computation

The event-window precipitation means are 0.602039 mm from ERA5-Land, 0.031947 mm from GPM, and 0.000000 mm from CHIRPS. Therefore `pmax_mm = 0.602` and all three products are below 1.0 mm, so `dry_count = 3`.

The mean wind-vector proxy is:

```text
sqrt(1.0989165526^2 + 1.3726806159^2) = 1.7583713097 m/s
```

Rounded to three decimals, `wind_m_s = 1.758`, which satisfies the 1.5 m/s rule. The event precipitation and wind products are bounded to 2020-02-06. The NASA report gives a March 7 report-context lower-bound transport distance of 120 km, satisfying the transport-context rule but not functioning as same-day measured transport for February 6. The PM10, PM2.5, and dust hourly series contain 0 non-null values across 72 slots, so `pm_obs_frac = 0.000`.

The computed consequence is dry wind-lofting consistency with report-context transport support, not a measured PM burden or same-day transport measurement.

# Scoring Rubric

- 3 points: Returns exactly the six requested JSON fields with numeric rounding and the final label.
- 4 points: Uses the three mean precipitation products, computes `pmax_mm = 0.602`, and counts all three below 1.0 mm.
- 3 points: Applies `sqrt(u_mean^2 + v_mean^2)`, reports `wind_m_s = 1.758` within tolerance, and tests the 1.5 m/s threshold.
- 3 points: Extracts `transport_km_lb = 120` as report-context transport evidence and verifies that it satisfies the transport-context rule without treating it as same-day measured transport.
- 3 points: Counts 0 non-null PM10, PM2.5, and dust values across 72 hourly slots and computes `pm_obs_frac = 0.0`.
- 3 points: Combines all threshold states to produce `dry_wind_conditions_with_report_context_transport_not_measured_pm`.
- 1 point: Avoids adding casualty, closure, asset-loss, or measured concentration claims not implied by the calculations.
