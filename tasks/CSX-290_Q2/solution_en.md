# Final Answer

Correct answer: `82.6`.

```json
{
  "score_label": "antecedent_runoff_persistence_dominant",
  "local_total_mm": 486.5,
  "heavy_days_ge_50mm": 5,
  "pre_peak_mm": 404.1,
  "peak_day_mm": 82.4,
  "antecedent_share": 0.8306,
  "peak_share": 0.1694,
  "pre_peak_to_peak_ratio": 4.9,
  "regional_mean_mm": 210.4,
  "bright_change_to_annual_change_ratio": 2.77,
  "arps": 82.6
}
```

# Computation Path

The local daily precipitation series sums to `486.5 mm`. The peak local day is `82.4 mm`, and the precipitation before that day sums to `404.1 mm`.

The antecedent and peak shares are:

```text
antecedent_share = 404.1 / 486.5 = 0.8306
peak_share = 82.4 / 486.5 = 0.1694
pre_peak_to_peak_ratio = 404.1 / 82.4 = 4.90
```

The three regional precipitation means average to `210.4 mm`. The paired-image bright-fraction increase divided by the annual surface-change mean is `2.77` when computed from unrounded bright fractions and the unrounded annual mean, then rounded at the final step.

The final score is:

```text
arps = 100 * (0.35 * min(486.5 / 600, 1)
            + 0.25 * min(5 / 6, 1)
            + 0.25 * 0.8306
            + 0.15 * min(210.4 / 250, 1))
     = 82.6
```

The label follows the numeric threshold ledger: `arps >= 80`, `antecedent_share >= 0.75`, and `peak_share < 0.25`.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "Decisive weight goes to the local precipitation split, heavy-day count, antecedent share, and regional precipitation mean; the image brightness ratio is a contextual surface-response check.",
    "counterfactual_rejection": "A peak-day-only reading fails because the peak day is only 16.94 percent of the local total while pre-peak rainfall is 4.90 times larger than the peak day.",
    "uncertainty_or_scale_caveat": "The RGB and annual-change ratio should not be interpreted as a direct flood-depth or runoff-volume measurement."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

Total: 20 points.

- 3 points for computing `local_total_mm = 486.5` and `heavy_days_ge_50mm = 5`.
- 4 points for computing `pre_peak_mm = 404.1`, `peak_day_mm = 82.4`, `antecedent_share = 0.8306`, and `peak_share = 0.1694`.
- 2 points for computing `pre_peak_to_peak_ratio = 4.90`.
- 3 points for computing the regional mean as `210.4 mm` from the three regional precipitation means.
- 3 points for computing `bright_change_to_annual_change_ratio = 2.77` from unrounded paired-image bright fractions and the unrounded annual change mean, with rounding only at the final ratio step.
- 4 points for applying the ARPS formula and reporting `arps = 82.6`.
- 1 point for returning concise JSON with the requested fields and numeric rounding.
