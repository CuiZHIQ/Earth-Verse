# Arba'at Rainfall-Exposure Diagnostic

A hydrometeorology team is checking the August-September 2024 Sudan flood signal around the Arba'at Dam corridor near Port Sudan. The question is whether the technical record supports a compact threshold diagnosis: concentrated event-window rainfall coinciding with a majority signal among assessed health facilities.

Compute the diagnostic using the event-window rainfall products and the Arba'at health-facility exposure record. Apply these decision tests:

- `rainfall_concentration`: true only if the rainfall product with the largest accumulated maximum has `max_to_mean_ratio >= 3.0` and `peak_excess_mm >= 150`.
- `product_spread_guard`: true only if `largest_product_max_mm / smallest_product_max_mm <= 1.6`.
- `facility_majority`: true only if `likely_affected_share >= 0.50` and `likely_to_unaffected_ratio > 1.0`.
- `composite_load`: true only if `rainfall_exposure_index_mm = largest_product_max_mm * likely_affected_share >= 150`.

Return JSON only, using this shape:

```json
{
  "event_window_days": "<integer>",
  "largest_product": "<name>",
  "rainfall": {
    "largest_product_max_mm": "<number>",
    "largest_product_mean_mm": "<number>",
    "max_to_mean_ratio": "<number>",
    "peak_excess_mm": "<number>",
    "peak_excess_pct": "<number>",
    "product_peak_spread_ratio": "<number>",
    "largest_vs_ensemble_peak_ratio": "<number>"
  },
  "facility_exposure": {
    "likely_affected_facilities": "<integer>",
    "unaffected_facilities": "<integer>",
    "assessed_facilities": "<integer>",
    "likely_affected_share": "<number>",
    "likely_affected_pct": "<number>",
    "likely_to_unaffected_ratio": "<number>"
  },
  "rainfall_exposure_index_mm": "<number>",
  "threshold_flags": {
    "rainfall_concentration": "<boolean>",
    "product_spread_guard": "<boolean>",
    "facility_majority": "<boolean>",
    "composite_load": "<boolean>"
  },
  "final_label": "<compact label>",
  "computed_interpretation": "<one sentence>"
}
```

Use the exact `final_label` value `concentrated_rainfall_majority_facility_exposure` when all four threshold flags are true. Use `rainfall_facility_thresholds_not_all_met` otherwise. Keep all reasoning inside the requested JSON fields.
