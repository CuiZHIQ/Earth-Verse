# Correct Answer

```json
{
  "answer": {
    "score": 98.58,
    "climate_period": "2010-09-01_to_2011-02-28",
    "precip_evidence_window": "2010-09-01_to_2010-10-16",
    "oni_cold_n": 4,
    "oni_mean": -1.53,
    "soi_pos_n": 6,
    "soi_mean": 3.63,
    "grid_mean_mm": 118.11,
    "grid_max_mm": 202.71,
    "ratio_mean": 1.46
  },
  "derivation": "The score is 20.00 + 20.00 + 15.00 + 9.08 + 14.76 + 10.00 + 9.74 = 98.58."
}
```

The ONI/SOI ledger covers the full 2010-09-01 to 2011-02-28 cold-phase period. The gridded precipitation values are the package's declared precipitation evidence window, 2010-09-01 to 2010-10-16, and should not be described as six-month precipitation totals.

# Scoring Rubric

- 4 points: Extracts the four ONI seasons in order and computes `oni_cold_n = 4` and `oni_mean = -1.53`.
- 4 points: Extracts the six SOI months and computes `soi_pos_n = 6` and `soi_mean = 3.63`.
- 4 points: Computes `grid_mean_mm = 118.11`, `grid_max_mm = 202.71`, and `ratio_mean = 1.46` from the three gridded precipitation summaries, while reporting their declared 2010-09-01 to 2010-10-16 evidence window.
- 5 points: Applies every score term, denominator, and cap to obtain `98.58` within `0.02`.
- 3 points: Provides a compact derivation with enough intermediate arithmetic to reproduce the result.

Total: 20 points.
