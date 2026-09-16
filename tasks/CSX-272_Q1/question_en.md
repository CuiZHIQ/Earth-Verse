# Queensland La Nina Rainfall Load Score

For CSX-272, compute a cold-phase rainfall-load score for the 2010-09-01 through 2011-02-28 climate phase period using the local package data.

Use ONI seasons SON 2010, OND 2010, NDJ 2010, and DJF 2011. Use SOI months September-December 2010 and January-February 2011. From package-local gridded precipitation evidence, use each event precipitation mean and maximum.

The ONI/SOI ledger covers the full cold-phase period. The available gridded precipitation summaries in this package cover their declared precipitation evidence window; report that window separately and do not describe those gridded means/maxima as six-month totals.

Compute the ledger values:

- `oni_cold_n`: count of the four ONI anomalies at or below -1.0 C.
- `oni_mean`: arithmetic mean of those four ONI anomalies.
- `soi_pos_n`: count of the six SOI months above zero.
- `soi_mean`: arithmetic mean of those six SOI values.
- `grid_mean_mm`: arithmetic mean of the three gridded precipitation means.
- `grid_max_mm`: maximum of the three gridded precipitation maxima.
- `ratio_mean`: arithmetic mean of each product's `maximum / mean` precipitation ratio.

Then compute:

```text
score =
  20 * (oni_cold_n / 4)
  + 20 * min(abs(oni_mean) / 1.5, 1)
  + 15 * (soi_pos_n / 6)
  + 10 * min(soi_mean / 4, 1)
  + 15 * min(grid_mean_mm / 120, 1)
  + 10 * min(grid_max_mm / 200, 1)
  + 10 * min(ratio_mean / 1.5, 1)
```

Round `score`, `oni_mean`, `soi_mean`, `grid_mean_mm`, `grid_max_mm`, `ratio_mean`, and component terms to two decimals. Return JSON with the numeric ledger, `climate_period`, `precip_evidence_window`, and a one-sentence derivation.
