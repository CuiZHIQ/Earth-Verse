# CSX-271 ENSO-Rainfall Score Ledger

Use the local CSX-271 package for the 1997-06-01 through 1998-05-31 El Nino period. Build a calculation-first numeric ledger from the ONI, SOI, CHIRPS, ERA5-Land, AOI, WorldPop, and OpenStreetMap package data.

Use ONI seasons whose center months fall in the period: MJJ 1997, JJA 1997, JAS 1997, ASO 1997, SON 1997, OND 1997, NDJ 1997, DJF 1998, JFM 1998, FMA 1998, MAM 1998, AMJ 1998. Use SOI months June-December 1997 and January-May 1998.

Compute these ledger values:

- `oni_ge15`: count of event ONI anomalies at or above +1.5 C.
- `oni_ge20`: count of event ONI anomalies at or above +2.0 C.
- `oni_peak`, `oni_mean`, and `final_oni`.
- `soi_mean` and `soi_le_neg1`, where `soi_le_neg1` counts SOI months at or below -1.0.
- `chirps_mean`, `era5_mean`, `rain_ratio = era5_mean / chirps_mean`, and the two mm/day rates using the inclusive CHIRPS date span.
- `aoi_area_square_degrees`, `population_per_square_degree`, and `mapped_feature_density_per_square_degree`.

Then compute:

```text
score =
  30 * (oni_ge15 / 12)
  + 10 * (oni_ge20 / 12)
  + 10 * min(oni_peak / 2.5, 1)
  + 5 * min(oni_mean / 2, 1)
  + 15 * (soi_le_neg1 / 12)
  + 10 * min(abs(soi_mean) / 3, 1)
  + 10 * min(chirps_mean / 75, 1)
  + 5 * min(era5_mean / 150, 1)
  + 5 * (1 - min(abs(rain_ratio - 2), 1))
  - 5 * max(0, 0.5 - final_oni)
```

Use `class_label = "strong_enso_rainfall_coupling"` when `score >= 75`, `oni_ge15 >= 6`, `soi_le_neg1 >= 8`, `chirps_mean >= 75`, and `era5_mean >= 150`; otherwise use `"ledger_threshold_not_met"`.

Return only compact JSON with `component_scores`, `total_score`, `class_label`, `derived_values`, `density_checks`, and a one-sentence arithmetic trace. Round returned floats to two decimals.
