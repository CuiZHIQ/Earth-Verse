# Final Answer

```json
{
  "component_ledger": [
    {"term": "S", "value": 1.0, "threshold_result": "pass"},
    {"term": "L", "value": 1.0, "threshold_result": "pass"},
    {"term": "W", "value": 1.0, "threshold_result": "pass"},
    {"term": "P", "value": 0.815, "threshold_result": "pass"},
    {"term": "F", "value": 0.925, "threshold_result": "pass"},
    {"term": "H", "value": 1.0, "threshold_result": "pass"},
    {"term": "C", "value": 0.531, "threshold_result": "pass"},
    {"term": "R", "value": 0.162, "threshold_result": "pass"}
  ],
  "score": 92.4,
  "positive_terms_passing": 7,
  "final_label": "coupled_geophysical_high_consistency",
  "rejected_readings": [
    "rainfall_led",
    "image_only",
    "loss_total_only",
    "single_driver_score"
  ]
}
```

# Key Computations

Raw anchors: M7.5, MMI 8.367, PGA 0.903 g, liquefaction alert population 140000, wave height 7 m, mapped population 407654, facility total 37, killed 2077, displaced 206524, mean embedding change 0.0531, GPM mean precipitation 4.43 mm, and CHIRPS mean precipitation 3.67 mm.

Normalized terms: `S=1.000`, `L=1.000`, `W=1.000`, `P=0.815`, `F=0.925`, `H=1.000`, `C=0.531`, and `R=0.162`.

Weighted score:

```text
100*(0.20*1.000 + 0.18*1.000 + 0.14*1.000 + 0.14*0.815 + 0.12*0.925 + 0.15*1.000 + 0.07*0.531 - 0.05*0.162) = 92.4
```

All seven positive terms pass their thresholds, and the rainfall deduction term remains low (`R=0.162 < 0.25`), so the final label is `coupled_geophysical_high_consistency`.

# Scoring Rubric

- 3 points: JSON ledger completeness. Returns eight named ledger rows plus score, positive-term count, final label, and rejected readings. Partial credit: award 1-2 points for a mostly complete structure with missing rows or missing summary fields.
- 4 points: Raw value extraction. Extracts M7.5, MMI 8.367, PGA 0.903 g, liquefaction alert population 140000, wave height 7 m, population 407654, facility total 37, killed 2077, displaced 206524, embedding mean 0.0531, and precipitation means 4.43 and 3.67 mm. Partial credit: award 2-3 points for most values with minor rounding mistakes, and 1 point for only a few correct anchors.
- 4 points: Normalized terms. Computes `S=1.000`, `L=1.000`, `W=1.000`, `P=0.815`, `F=0.925`, `H=1.000`, `C=0.531`, and `R=0.162` within tolerance. Partial credit: award 2-3 points for mostly correct terms with one or two formula errors.
- 4 points: Weighted score. Applies the stated coefficients and reports 92.4 points out of 100 within 0.1. Partial credit: award 2-3 points for the right formula with arithmetic or rounding errors.
- 2 points: Threshold logic. Marks all seven positive terms as passing, marks the rainfall term as low, and assigns `coupled_geophysical_high_consistency`. Partial credit: award 1 point if the final label is right but one threshold result is missing or wrong.
- 2 points: Rejected readings. Rejects rainfall-led, image-only, loss-total-only, and single-driver readings using computed terms. Partial credit: award 1 point for rejecting at least two readings with numeric support.
- 1 point: Concise numeric framing. Keeps every statement tied to the weighted score or component ledger. Partial credit: award 0.5 point for minor extra prose that does not change the result.

Total: 20 points.
