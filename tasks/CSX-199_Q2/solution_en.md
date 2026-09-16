# Final Answer

```json
{
  "final_label": "patchy_moderate_burn_index_distribution",
  "severity_class": "moderate",
  "heterogeneity_class": "patchy",
  "dnbr_mean": 0.329,
  "dnbr_max": 1.003,
  "dnbr_min": -0.379,
  "dnbr_cv": 0.515,
  "patchiness_score": "3/3",
  "computed_interpretation": "The mean dNBR is moderate, while the maximum, negative lower tail, and CV all satisfy the patchiness rule."
}
```

# Key Computations

`compute_gt.py` reads the CSX-199 event metadata, Sentinel-2 dNBR summary, and annual satellite-embedding change summary from the local event data.

Core dNBR statistics:

- `dnbr_mean = 0.32850663068510844`, rounded to `0.329`.
- `dnbr_max = 1.0028549834547134`, rounded to `1.003`.
- `dnbr_min = -0.3792478971336555`, rounded to `-0.379`.
- `dnbr_stddev = 0.16904180069503502`.
- `dnbr_cv = dnbr_stddev / abs(dnbr_mean) = 0.16904180069503502 / 0.32850663068510844 = 0.5145765257233752`, rounded to `0.515`.
- Sentinel-2 comparison counts: `pre_count = 20`, `post_count = 33`.
- Annual embedding-change context: mean `0.020350222884793205`, max `0.09374681781073446`, comparing 2022 to 2023.

Mean dNBR severity bins:

- `< 0.00`: `unburned_or_regrowth`
- `0.00` to `< 0.27`: `low`
- `0.27` to `< 0.44`: `moderate`
- `0.44` to `< 0.66`: `high`
- `>= 0.66`: `very_high`

Patchiness tests:

- `dnbr_cv >= 0.45`: `0.515 >= 0.45`, pass.
- `dnbr_max >= 0.66`: `1.003 >= 0.66`, pass.
- `dnbr_min < 0.00`: `-0.379 < 0.00`, pass.

# Reasoning Path

1. The mean dNBR falls inside the `0.27` to `< 0.44` interval, so the mean-severity class is `moderate`.
2. The maximum dNBR is above the `0.66` high-tail threshold, so the upper tail includes severe burn-index values.
3. The minimum dNBR is negative, showing that the summarized distribution also includes a low or opposite-sign tail.
4. The coefficient of variation is about `0.515`, which exceeds the `0.45` patchiness threshold.
5. All three patchiness tests pass, so the heterogeneity class is `patchy` and the patchiness score is `3/3`.
6. Combining the moderate mean class with the full patchiness score gives the final label `patchy_moderate_burn_index_distribution`.

# Computed Interpretation

The numbers support a moderate-average burn-index distribution with a severe upper tail, so the maximum value should not be used as a summary of the whole distribution.

# Scoring Rubric

Total: 20 points.

- 4 points: Final structured answer. Full credit for the final label `patchy_moderate_burn_index_distribution`, severity class `moderate`, heterogeneity class `patchy`, and patchiness score `3/3`. Partial credit: 2 points for only the correct severity or heterogeneity class; 3 points for both classes without the final label or score.
- 4 points: dNBR numeric extraction and rounding. Full credit for reporting `dnbr_mean` near `0.329`, `dnbr_max` near `1.003`, `dnbr_min` near `-0.379`, and `dnbr_cv` near `0.515`. Partial credit: 1 point for each correct value within tolerance.
- 3 points: CV formula. Full credit for computing `dnbr_stddev / abs(dnbr_mean)` and applying it to the provided statistics. Partial credit: 1 point for naming the correct formula but not computing it; 2 points for computing a nearby CV with a rounding or denominator mistake.
- 3 points: Mean-severity threshold logic. Full credit for using the stated mean dNBR bins and placing `0.329` in the `moderate` interval. Partial credit: 1 point for using the bins but landing one adjacent class away; 2 points for the right class with incomplete interval logic.
- 3 points: Patchiness gate ledger. Full credit for evaluating all three tests and finding `3/3` passes. Partial credit: 1 point for one correct test, 2 points for two correct tests, or 2 points for the right `patchy` class without all test values.
- 2 points: Computed interpretation. Full credit for stating that the distribution is moderate on average with a severe upper tail and that the peak should not summarize the full distribution. Partial credit: 1 point for a correct but vague sentence tied to only one statistic.
- 1 point: Concise JSON format. Full credit for returning the requested compact JSON with rounded numeric fields and no added prose outside the object. Partial credit: 0.5 points for a readable answer with minor field omissions.
