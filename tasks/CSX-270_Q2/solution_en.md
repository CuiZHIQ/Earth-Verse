# Correct Answer

```json
{
  "target_family": "east_africa_multisource_rainfall_structure_ledger",
  "score": 7,
  "cv_order": ["GPM_IMERG", "ERA5_Land", "CHIRPS"],
  "strongest_peak_to_mean_product": "GPM_IMERG",
  "product_metrics": {
    "GPM_IMERG": {"mean_mm": 295.427, "cv": 0.138616, "peak_to_mean": 1.366667, "normalized_range": 0.599535},
    "ERA5_Land": {"mean_mm": 294.239, "cv": 0.116756, "peak_to_mean": 1.334116, "normalized_range": 0.531741},
    "CHIRPS": {"mean_mm": 280.668, "cv": 0.051422, "peak_to_mean": 1.187026, "normalized_range": 0.357059}
  },
  "ledger": {
    "mean_ge_280_count": 3,
    "cv_ge_0_10_count": 2,
    "cv_order_pass": 1,
    "chirps_smoother_pass": 1,
    "inside_point_samples": 0
  },
  "inside_point_samples": 0,
  "sampling_scope": "Point-sample/AOI overlap is reported as a package diagnostic only; it is not part of the score and is not used to judge event-location validity.",
  "final_label": "localized_gridded_rainfall_structure_score_7"
}
```

# Core Reasoning

The rainfall-window products all have means at or above `280 mm`: `295.427`, `294.239`, and `280.668 mm`. Their CV values are `0.138616`, `0.116756`, and `0.051422`, giving the required high-to-low order `GPM_IMERG > ERA5_Land > CHIRPS`. The peak-to-mean ratios are `1.366667`, `1.334116`, and `1.187026`; GPM_IMERG is therefore the strongest peak-to-mean signal.

The score ledger is `3 + 2 + 1 + 1 = 7`. The point-sample/AOI overlap diagnostic is `inside_point_samples = 0`; it is reported for package transparency but is not part of the rainfall-structure score.

# Scoring Rubric

- 4 points: Extract all three gridded rainfall products and the four base fields for each product.
- 4 points: Compute CV, peak-to-mean, and normalized range for each product within tolerance.
- 4 points: Compute the score ledger components and final score `7`.
- 3 points: Report the point-sample/AOI overlap diagnostic and keep it out of the rainfall-structure score.
- 3 points: Report the CV order and strongest peak-to-mean product correctly.
- 2 points: Return compact numeric JSON with the requested fields and one-line final label.
