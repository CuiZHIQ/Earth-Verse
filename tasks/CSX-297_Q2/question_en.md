# Haze Rainfall-Contrast Consistency Test

A technical reviewer is testing whether broad regional rain is enough to treat the September 2019 Indonesian haze episode as rain-washed at the fire-source point. Compute a compact rainfall-contrast ledger for the event.

Use these definitions:

- `point_total_mm`: sum of daily point precipitation over the point-sample window.
- `zero_run_days`: longest consecutive run with daily point precipitation equal to 0 mm.
- `dry_day_fraction`: count of point-sample days with precipitation equal to 0 mm divided by the point-sample day count.
- `regional_mean_mm`: arithmetic mean of the three event-window regional precipitation means.
- `min_regional_ratio`: lowest of the three regional precipitation means divided by `point_total_mm`.

Decision rule: a rain-washout downgrade fails if `point_total_mm <= 1.0`, `zero_run_days >= 7`, and `min_regional_ratio >= 50`.

Return compact JSON:

```json
{
  "point_total_mm": 0.0,
  "zero_run_days": 0,
  "dry_day_fraction": 0.0,
  "regional_mean_mm": 0.0,
  "min_regional_ratio": 0.0,
  "answer": "<washout_downgrade_fails or washout_downgrade_passes>"
}
```
