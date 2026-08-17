# Correct Answer

The rainfall score is **84.06**, with final label `rainfall_dominant_peak_surface_check`.

```json
{
  "event_window_days": 39,
  "precipitation_products": {
    "era5_land": {
      "mean_total_mm": 50.37,
      "max_total_mm": 200.145,
      "mean_daily_mm": 1.29,
      "mean_ge_75mm": false,
      "max_ge_150mm": true
    },
    "gpm_imerg": {
      "mean_total_mm": 95.927,
      "max_total_mm": 114.558,
      "mean_daily_mm": 2.46,
      "mean_ge_75mm": true,
      "max_ge_150mm": false
    },
    "chirps": {
      "mean_total_mm": 105.624,
      "max_total_mm": 158.826,
      "mean_daily_mm": 2.71,
      "mean_ge_75mm": true,
      "max_ge_150mm": true
    }
  },
  "rainfall_ledger": {
    "ensemble_mean_total_mm": 83.974,
    "ensemble_max_total_mm": 200.145,
    "mean_score": 0.82099,
    "max_score": 0.92124,
    "pass_share": 0.66667,
    "rainfall_score": 84.06
  },
  "surface_check": {
    "area_mean_passes": 0,
    "peak_passes": 2,
    "surface_role": "peak_only_check"
  },
  "mapped_feature_ledger": {
    "facility_count": 163,
    "facility_rate_per_100k": 14.95
  },
  "final_label": "rainfall_dominant_peak_surface_check"
}
```

Core arithmetic: the inclusive period is 39 days. Product mean totals are 50.370, 95.927, and 105.624 mm; product maximum totals are 200.145, 114.558, and 158.826 mm. The mean-total tests pass for GPM and CHIRPS; the maximum-total tests pass for ERA5-Land and CHIRPS, giving `pass_share = 4/6 = 0.66667`. The weighted formula gives `100 * (0.55 * 0.82099 + 0.35 * 0.92124 + 0.10 * 0.66667) = 84.06`.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "counterfactual_rejection": "A surface-change-dominant reading fails because both area-mean surface checks fail even though peak surface checks pass.",
    "evidence_weighting": "The three precipitation products and rainfall score are decisive; surface metrics are peak-only checks and mapped features provide exposure context.",
    "uncertainty_or_scale_caveat": "Mapped facility rates are exposure indicators and should not be interpreted as direct damage or service-disruption counts."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the requested compact JSON ledger with the final scalar score.
- 5 points: Computes the precipitation product means, maxima, daily means, ensemble mean, and ensemble maximum within tolerance.
- 5 points: Applies the 75 mm and 150 mm threshold tests and derives `mean_score`, `max_score`, `pass_share`, and `rainfall_score` correctly.
- 3 points: Computes the surface-check counts from AlphaEarth and Sentinel-2 values and assigns `peak_only_check`.
- 2 points: Computes the mapped-feature count and facility rate per 100,000 people.
- 2 points: Provides the final label and a concise calculation-based synthesis.
