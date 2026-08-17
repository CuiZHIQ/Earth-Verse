# Correct Answer

```json
{
  "answer": {
    "score": 74.09,
    "warm_run": 11,
    "strong_run": 6,
    "peak_oni": 2.06,
    "final_oni": 0.49,
    "soi_mean": -0.53,
    "soi_negative_months": 8
  },
  "derivation": "The score is 36.67 + 12.50 + 12.36 + 10.00 + 2.67 - 0.10 = 74.09."
}
```

# Scoring Rubric

- 4 points: Extracts the 12 event ONI seasons in the stated order and reports the correct event-season count.
- 4 points: Computes `warm_run = 11`, `strong_run = 6`, `peak_oni = 2.06`, and `final_oni = 0.49`.
- 4 points: Extracts the 12 SOI months and computes `soi_mean = -0.53` and `soi_negative_months = 8`.
- 5 points: Applies every score term with the stated denominators, cap, and final-row deduction, yielding `74.09` within `0.02`.
- 3 points: Provides a compact derivation that makes the threshold and arithmetic steps auditable.

Total: 20 points.
