# CSX-226 Locked-Date Precipitation Score Ledger

Use the local CSX-226 event package.
Reconstruct the locked event date from the package anchor. Then build a
precipitation ledger from the resource-registry physical-hazard JSON records in
the package manifest.

Use these source rules:

- `sample_a_precip_mm` comes from the first lexicographic relative path that
  contains `daily_point_sample`.
- `sample_b_precip_mm` comes from the second lexicographic relative path that
  contains `daily_point_sample`.
- For a point record with `daily.time`, use the matching
  `daily.precipitation_sum`.
- For a point record with `properties.parameter`, use `PRECTOTCORR` for the
  matching `YYYYMMDD` date key.
- The three grid-summary precipitation inputs are the physical-hazard JSON
  records whose `stats` object contains one of these keys:
  `chirps_event_precip_mm_mean`, `precipitation_sum_mm_mean`, or
  `gpm_event_precip_mm_mean`.

Use these formulas:

- `point_abs_gap_mm = abs(sample_a_precip_mm - sample_b_precip_mm)`, rounded to
  2 decimals.
- `grid_mean_precip_mm` is the mean of the three grid-summary precipitation
  inputs, rounded to 2 decimals.
- A source is wet when its precipitation value is at least `1.0` mm.
- `wet_count_5` is the wet-source count across the two point values and three
  grid-summary values.
- The `diagnosis` is `point_split_grid_dry_consensus` only when exactly one
  point value is wet, all three grid-summary values are dry, and
  `point_abs_gap_mm <= 1.0`; otherwise use `mixed_precipitation_ledger`.
- The `answer` token is `point_split_grid_dry_gap_{point_abs_gap_mm:.2f}mm`
  when the diagnosis is `point_split_grid_dry_consensus`; otherwise use
  `mixed_precipitation_ledger`.

Return only JSON in this form:

```json
{
  "answer": "string",
  "event_date": "YYYY-MM-DD",
  "sample_a_precip_mm": 0.0,
  "sample_b_precip_mm": 0.0,
  "point_abs_gap_mm": 0.0,
  "grid_mean_precip_mm": 0.0,
  "wet_count_5": 0,
  "diagnosis": "point_split_grid_dry_consensus|mixed_precipitation_ledger"
}
```
