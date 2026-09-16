# Correct Answer

```json
{
  "answer": "all_5_thresholds_met",
  "dry_ratio_mean": 0.263,
  "dry_deficit_mean": 0.737,
  "agreement_delta": 0.003,
  "oni_peak_c": 2.75,
  "soi_neg_frac": 1.0,
  "tmax_spread_c": 4.1,
  "ledger_score": 93.91
}
```

# Calculation Notes

The GPM and CHIRPS precipitation minima are both close to 26% of their respective slice means, giving a mean dry-pocket ratio of 0.263 and a mean deficit of 0.737. The cross-product ratio gap is 0.003. The selected ONI seasons peak at 2.75 C, all seven SOI months are negative, and the ERA5-Land maximum-temperature spread is 4.10 C. All five threshold tests pass, so the ledger label is `all_5_thresholds_met`.

# Scoring Rubric

Total: 20 points

- 4 points: Correctly parses the two precipitation JSON files and computes both min/mean ratios before averaging them.
- 4 points: Correctly derives `dry_deficit_mean` and `agreement_delta`, with rounding consistent to three decimals.
- 4 points: Correctly parses the ONI ASCII seasons SON 2015 through MAM 2016 and reports the 2.75 C peak.
- 3 points: Correctly parses the SOI monthly row values from October 2015 through April 2016 and reports `soi_neg_frac = 1.0`.
- 3 points: Correctly derives the ERA5-Land temperature spread and applies the five threshold tests.
- 2 points: Correctly evaluates the weighted ledger-score formula and returns the compact JSON schema requested in the prompt.
