# Final Answer

```json
{
  "event_window_days": 24,
  "largest_product": "GPM IMERG V07",
  "rainfall": {
    "largest_product_max_mm": 258.84,
    "largest_product_mean_mm": 83.362,
    "max_to_mean_ratio": 3.105,
    "peak_excess_mm": 175.478,
    "peak_excess_pct": 210.5,
    "product_peak_spread_ratio": 1.513,
    "largest_vs_ensemble_peak_ratio": 1.291
  },
  "facility_exposure": {
    "likely_affected_facilities": 7,
    "unaffected_facilities": 5,
    "assessed_facilities": 12,
    "likely_affected_share": 0.583,
    "likely_affected_pct": 58.333,
    "likely_to_unaffected_ratio": 1.4
  },
  "rainfall_exposure_index_mm": 150.99,
  "threshold_flags": {
    "rainfall_concentration": true,
    "product_spread_guard": true,
    "facility_majority": true,
    "composite_load": true
  },
  "final_label": "concentrated_rainfall_majority_facility_exposure",
  "computed_interpretation": "The event-window rainfall maximum is highly concentrated, remains within the product-spread guard, and combines with a majority health-facility exposure signal."
}
```

# Key Computations

Event window length:

`2024-08-13` through `2024-09-05`, inclusive, gives `24` days.

Rainfall product summaries:

- ERA5-Land: max `171.630` mm, mean `102.470` mm.
- GPM IMERG V07: max `258.840` mm, mean `83.362` mm.
- CHIRPS daily: max `171.054` mm, mean `96.895` mm.

Rainfall formulas:

- `max_to_mean_ratio = 258.840 / 83.362 = 3.105`.
- `peak_excess_mm = 258.840 - 83.362 = 175.478` mm.
- `peak_excess_pct = (3.105 - 1) * 100 = 210.5%`.
- `product_peak_spread_ratio = 258.840 / 171.054 = 1.513`.
- `largest_vs_ensemble_peak_ratio = 258.840 / mean(171.630, 258.840, 171.054) = 1.291`.

Facility formulas:

- `assessed_facilities = 7 + 5 = 12`.
- `likely_affected_share = 7 / 12 = 0.583`.
- `likely_affected_pct = 0.583333 * 100 = 58.333%`.
- `likely_to_unaffected_ratio = 7 / 5 = 1.4`.
- `rainfall_exposure_index_mm = 258.840 * 0.583333 = 150.990` mm.

Threshold tests:

- `rainfall_concentration`: pass, because `3.105 >= 3.0` and `175.478 >= 150`.
- `product_spread_guard`: pass, because `1.513 <= 1.6`.
- `facility_majority`: pass, because `0.583 >= 0.50` and `1.4 > 1.0`.
- `composite_load`: pass, because `150.990 >= 150`.

# Reasoning Path

The largest accumulated rainfall maximum comes from GPM IMERG V07, so its maximum and mean values control the concentration test. The GPM maximum is more than three times its product mean and exceeds that mean by more than 150 mm, satisfying the rainfall concentration rule. The largest product maximum is only 1.513 times the smallest product maximum, so the result does not depend on an extreme product split under the stated guard.

The health-facility record gives 7 likely affected and 5 unaffected facilities, for 12 assessed facilities. The likely affected share is therefore 58.333%, and the affected-to-unaffected ratio is 1.4, satisfying the majority exposure rule. Multiplying the largest rainfall maximum by the affected share gives a composite rainfall-exposure index of 150.990 mm, just above the 150 mm threshold.

Because all four flags pass, the correct compact answer is `concentrated_rainfall_majority_facility_exposure`.

# Computed Interpretation

The computed result supports a concentrated rainfall forcing diagnosis coupled to a majority health-facility exposure signal for the Arba'at corridor.

# Scoring Rubric

- 4 points: Final JSON and label. Full credit for returning the requested JSON shape, all required fields, all four threshold flags, and the exact final label `concentrated_rainfall_majority_facility_exposure` when all flags are true. Partial credit for a mostly complete JSON response with one missing nested field or a synonymous but less exact label.
- 4 points: Rainfall extraction and arithmetic. Full credit for identifying GPM IMERG V07 as the largest product and computing max, mean, max-to-mean ratio, peak excess, peak excess percent, product spread ratio, and largest-versus-ensemble ratio within tolerance. Partial credit for correct product identification with one or two arithmetic mistakes.
- 3 points: Facility exposure arithmetic. Full credit for using 7 likely affected, 5 unaffected, 12 assessed, share 0.583, percent 58.333, and ratio 1.4. Partial credit for correct counts with one derived ratio missing or rounded too coarsely.
- 3 points: Threshold logic. Full credit for correctly applying all four pass/fail tests with the stated inequalities. Partial credit for correct flags but incomplete comparison values, or for one incorrect flag.
- 3 points: Composite rainfall-exposure index. Full credit for computing `258.840 * 7/12 = 150.990` mm and recognizing that it passes the 150 mm threshold. Partial credit for using the right formula with a minor rounding error, or for computing the value but missing the threshold comparison.
- 2 points: Computed interpretation inside JSON. Full credit for using the requested `computed_interpretation` field to tie the four true flags to concentrated rainfall and majority facility exposure, without adding response planning or realized-loss claims. Partial credit for a mostly correct interpretation that omits one link or adds minor extra narrative.
- 1 point: Concision and scope control. Full credit for a compact computed interpretation without response planning or extra realized-loss assertions. Partial credit for a mostly concise interpretation with minor extra narrative.
