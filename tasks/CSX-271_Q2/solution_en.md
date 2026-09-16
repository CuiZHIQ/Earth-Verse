# Correct Answer

```json
{
  "component_scores": {"oni_ge15": 20.0, "oni_ge20": 4.17, "oni_peak": 9.6, "oni_mean": 4.38, "soi_count": 13.75, "soi_mean": 7.81, "chirps": 10.0, "era5": 5.0, "ratio": 4.66, "late_penalty": 0.25},
  "total_score": 79.12,
  "class_label": "strong_enso_rainfall_coupling",
  "derived_values": {"oni_ge15": 8, "oni_ge20": 5, "oni_peak": 2.4, "oni_mean": 1.75, "final_oni": 0.45, "soi_mean": -2.34, "soi_le_neg1": 11, "chirps_mean": 84.93, "era5_mean": 164.13, "rain_ratio": 1.93, "chirps_mm_per_day": 1.85, "era5_mm_per_day": 3.57},
  "density_checks": {"aoi_area_square_degrees": 0.2, "population_per_square_degree": 45948.08, "mapped_feature_density_per_square_degree": 4938.27},
  "arithmetic_trace": "Score = 20.00 + 4.17 + 9.60 + 4.38 + 13.75 + 7.81 + 10.00 + 5.00 + 4.66 - 0.25 = 79.12."
}
```

The ONI ledger uses 12 centered seasons, with 8 at or above +1.5 C, 5 at or above +2.0 C, a 2.40 C peak, a 1.75 C mean, and a 0.45 C final season. The SOI ledger uses 12 monthly values, yielding mean -2.34 and 11 months at or below -1.0. The rainfall ledger uses CHIRPS mean 84.93 mm, ERA5-Land mean 164.13 mm, a 1.93 cross-source ratio, and 46 inclusive days for rates of 1.85 and 3.57 mm/day.

# Scoring Rubric

- 4 points: Parses the 12 ONI seasons and computes `oni_ge15`, `oni_ge20`, `oni_peak`, `oni_mean`, and `final_oni`.
- 4 points: Parses the 12 SOI months and computes `soi_mean` plus `soi_le_neg1`.
- 4 points: Extracts the CHIRPS and ERA5-Land rainfall means, computes the inclusive day count, two rates, and `rain_ratio`.
- 4 points: Applies the score formula with all caps and the late-season deduction, yielding `79.12` within `0.02`.
- 2 points: Computes AOI area, population density, and mapped feature density from structured package data.
- 2 points: Returns the class label and compact JSON fields with enough arithmetic to audit the result.

Total: 20 points.
