# Coupled El Nino Score Ledger

For CSX-267, compute a numeric coupled-persistence score for the 2023-06-01 through 2024-05-31 event window using the local package data.

Use these ONI seasons in order: MJJ 2023, JJA 2023, JAS 2023, ASO 2023, SON 2023, OND 2023, NDJ 2023, DJF 2024, JFM 2024, FMA 2024, MAM 2024, AMJ 2024. Use SOI months June-December 2023 and January-May 2024.

Compute the ledger values:

- `warm_run`: longest consecutive ONI anomaly run at or above +0.5 C.
- `strong_run`: longest consecutive ONI anomaly run at or above +1.5 C.
- `peak_oni`: maximum ONI anomaly in the event seasons.
- `final_oni`: AMJ 2024 ONI anomaly.
- `soi_mean`: arithmetic mean of the event SOI months.
- `soi_negative_months`: count of event SOI months below zero.

Then compute:

```text
score =
  40 * (warm_run / 12)
  + 25 * (strong_run / 12)
  + 15 * (peak_oni / 2.5)
  + 15 * (soi_negative_months / 12)
  + 5 * min(abs(soi_mean), 1)
  - 10 * max(0, 0.5 - final_oni)
```

Round `score`, `peak_oni`, `final_oni`, and `soi_mean` to two decimals. Return JSON with the numeric ledger and a one-sentence derivation.
