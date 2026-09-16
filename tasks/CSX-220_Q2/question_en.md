# Threshold Ledger Diagnosis

A technical review team is checking whether the 30 December 2020 Gjerdrum landslide at Ask, Norway, is numerically consistent with a sensitive-ground threshold ledger rather than an event-day-rainfall-dominant ledger.

Compute the six ledger tests below from the local event data. Round local precipitation totals and area values to 1 decimal place, gridded precipitation means and gridded temperature means to 2 decimal places, surface magnitudes to 4 decimals, and ratios to 3 decimals.

Required tests:

- `wet_context_consistency`: `min(local_event_mm, gridded_event_mm, independent_event_mm) > 0` and `min/max >= 0.50`.
- `event_day_rainfall_dominance`: `local_event_mm / local_15d_mm >= 0.50` and the event day is the local 15-day precipitation maximum.
- `near_freezing_state`: `-1 <= gridded_tmax_mean_c <= 3` and `local_event_tmin_c <= 0 <= local_event_tmax_c`.
- `reported_extent_geometry`: `flow_ha = reported_length_m * reported_width_m / 10000`; `total_affected_ha = flow_ha + reported_debris_ha`; pass when `flow_ha >= 20` and `total_affected_ha >= 30`.
- `short_window_surface_dominance`: `abs(short_window_SAR_VV_mean) / abs(optical_dNBR_mean) >= 1.5` and `abs(short_window_SAR_VV_mean) / annual_embedding_change >= 5`.
- `local_exposure_context`: compact exposure elements `>= 10`, amenity features `>= 1`, and highway features `>= 1`.

Final label rule: return `sensitive_ground_wet_context_short_window_disturbance` only if `wet_context_consistency`, `near_freezing_state`, `reported_extent_geometry`, `short_window_surface_dominance`, and `local_exposure_context` pass while `event_day_rainfall_dominance` fails. Otherwise return `ledger_inconsistent_or_rainfall_dominant`.

Return compact JSON:

```json
{
  "ledger_rows": [
    {
      "test": "<required test name>",
      "formula": "<formula used>",
      "value": "<computed value or compact object>",
      "threshold": "<pass/fail threshold>",
      "result": "PASS or FAIL"
    }
  ],
  "computed_label": "<final label>",
  "rejected_alternative": "<one sentence based on the rainfall-dominance test>"
}
```
