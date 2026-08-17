# Pakistan Monsoon Flood Threshold Ledger

A hydrologic analytics team is checking whether the 2022 Pakistan monsoon-flood record forms a long-span, rain-dominant, spatially concentrated flood case.

Compute the six ledger values below from the event record. Keep the full flood-event span separate from the precipitation-product evidence window used by the three precipitation summaries.

- `event_span_days = end_date - start_date + 1`
- `mean_precip_peak_ratio = mean(max_precip / mean_precip)` across the three event precipitation summaries
- `precip_ratio_spread = max(precip_peak_ratio) - min(precip_peak_ratio)`
- `surface_change_concentration_ratio = annual_change_max / annual_change_mean`
- `people_per_counted_facility = population_sum / counted_facilities`
- `rain_anomaly_midpoint_x = midpoint of the report's "five to six times" rainfall statement`

Then compute:

`flood_consistency_score_0to6 = I(event_span_days >= 90) + I(mean_precip_peak_ratio >= 1.50) + I(precip_ratio_spread <= 0.60) + I(surface_change_concentration_ratio >= 10) + I(people_per_counted_facility >= 10000) + I(rain_anomaly_midpoint_x >= 5)`

Use `high_consistency_long_span_monsoon_flood_concentration` when all six tests pass, and `partial_consistency_monsoon_flood_ledger` otherwise.

Return only compact JSON:

```json
{
  "answer": {
    "event_span_days": 0,
    "mean_precip_peak_ratio": 0.0,
    "precip_ratio_spread": 0.0,
    "surface_change_concentration_ratio": 0.0,
    "people_per_counted_facility": 0.0,
    "rain_anomaly_midpoint_x": 0.0
  },
  "evidence_windows": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "precipitation_evidence_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}
  },
  "score": 0,
  "class_label": "<ledger-derived label>"
}
```
