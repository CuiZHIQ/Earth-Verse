# Rainfall-Structure Score

The local package contains structured data for an East Africa wet-season flood context. Use the package rainfall window and compute the rainfall-structure ledger from the available local JSON summaries.

Build a calculation ledger from the package JSON data. For the three accumulated-precipitation products covering the package rainfall window, extract `mean_mm`, `stddev_mm`, `min_mm`, and `max_mm`, then derive:

- `cv = stddev_mm / mean_mm`
- `peak_to_mean = max_mm / mean_mm`
- `normalized_range = (max_mm - min_mm) / mean_mm`

Compute these ledger fields:

- `mean_ge_280_count`: number of products with `mean_mm >= 280`.
- `cv_ge_0_10_count`: number of products with `cv >= 0.10`.
- `cv_order_pass`: `1` when the CV order is `GPM_IMERG > ERA5_Land > CHIRPS`, otherwise `0`.
- `chirps_smoother_pass`: `1` when `CHIRPS cv < 0.06` and both `GPM_IMERG` and `ERA5_Land` have `cv >= 0.10`, otherwise `0`.
- `inside_point_samples`: number of daily point-sample coordinates inside the compact AOI polygon.

Use this formula:

`score = mean_ge_280_count + cv_ge_0_10_count + cv_order_pass + chirps_smoother_pass`

Return a compact JSON object:

```json
{
  "target_family": "east_africa_multisource_rainfall_structure_ledger",
  "score": 0,
  "cv_order": [],
  "strongest_peak_to_mean_product": "",
  "product_metrics": {},
  "ledger": {},
  "inside_point_samples": 0,
  "sampling_scope": "<brief note on how point-sample/AOI overlap is used>",
  "final_label": ""
}
```

Include formulas and numeric values; keep the final label to one line. The point-sample/AOI overlap is a diagnostic field only and is not part of the rainfall-structure score.
