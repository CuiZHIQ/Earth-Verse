# Final Answer

Correct answer: `washout_downgrade_fails`

```json
{
  "point_total_mm": 0.8,
  "zero_run_days": 7,
  "dry_day_fraction": 0.867,
  "regional_mean_mm": 74.2,
  "min_regional_ratio": 56.7,
  "answer": "washout_downgrade_fails"
}
```

# Computation

The point precipitation series has 15 daily values. Its total is `0.8 mm`, with 13 zero-rain days, so `dry_day_fraction = 13 / 15 = 0.867`. The longest zero-rain run is 7 days, from 2019-09-09 through 2019-09-15.

The three regional event-window precipitation means are `45.3`, `68.2`, and `109.0 mm`. Their arithmetic mean is `(45.329 + 68.195 + 109.029) / 3 = 74.2 mm`. The lowest regional/source contrast is `45.329 / 0.8 = 56.7`.

All rule tests are satisfied: `0.8 <= 1.0`, `7 >= 7`, and `56.7 >= 50`. The computed consequence is a source-dry, region-wet contrast, so the rain-washout downgrade fails.

# Scoring Rubric

Award up to 20 points:

- 4 points for returning the requested compact JSON fields with numeric values.
- 5 points for the point rainfall metrics: `0.8 mm` total, `7` zero-run days, and `0.867` dry-day fraction.
- 4 points for the regional contrast metrics: regional means `45.3`, `68.2`, `109.0 mm`, `74.2 mm` regional mean, and `56.7` minimum regional/source ratio.
- 4 points for applying the three threshold tests exactly.
- 2 points for the conclusion `washout_downgrade_fails` as a direct consequence of the thresholds.
- 1 point for keeping the interpretation bounded to the computed rainfall contrast and avoiding unsupported impact claims.
