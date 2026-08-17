# Correct Answer

```json
{
  "answer": "heat_melt_glof_consistent",
  "mean_temp_c": 31.49,
  "point_precip_mm": 0.0,
  "grid_precip_mm": 2.11,
  "component_scores": {
    "temperature": 0.7662,
    "dryness": 1.0,
    "rainfall": 0.0844,
    "surface": 0.3413,
    "exposure": 0.2846
  },
  "indices": {
    "heat_melt_glof": 63.2,
    "rainfall_flood": 12.6,
    "margin": 50.6
  },
  "rejected_alternative": "rainfall_runoff_competitive"
}
```

# Computation

The temperature mean is `(28.04 + 35.20 + 31.2392) / 3 = 31.49 C`. Point precipitation is `(0.00 + 0.00) / 2 = 0.00 mm`, while gridded precipitation is `(2.7265 + 2.9820 + 0.6202) / 3 = 2.11 mm`.

The component scores are:

- `temperature_score = clamp((31.4931 - 20) / 15) = 0.7662`
- `dryness_score = clamp(1 - 0.00 / 10) = 1.0000`
- `rainfall_score = clamp(2.1096 / 25) = 0.0844`
- `surface_score = mean(0.5554 / 2, 0.1587 / 0.3, 0.0109 / 0.05) = 0.3413`
- `exposure_score = clamp(14230.1020 / 50000) = 0.2846`

The weighted indices are:

- `heat_melt_glof_index = 100 * (0.40 * 0.7662 + 0.25 * 1.0000 + 0.15 * 0.0844 + 0.10 * 0.3413 + 0.10 * 0.2846) = 63.2`
- `rainfall_flood_index = 100 * (0.55 * 0.0844 + 0.20 * 0.0000 + 0.15 * 0.3413 + 0.10 * 0.2846) = 12.6`
- `margin = 63.2 - 12.6 = 50.6`

Because the margin is at least 20.0 and point precipitation is at most 1.0 mm, the deterministic answer is `heat_melt_glof_consistent`. The compact consequence is that `rainfall_runoff_competitive` fails the margin and dry-point-precipitation tests.

# Scoring Rubric

- 3 points: Returns the required compact JSON fields with the prescribed rounding.
- 4 points: Extracts the temperature, point precipitation, gridded precipitation, surface, and exposure inputs correctly.
- 4 points: Computes `temperature_score`, `dryness_score`, `rainfall_score`, `surface_score`, and `exposure_score` with the stated clamp formulas.
- 4 points: Applies both weighted index formulas correctly and reports 63.2, 12.6, and a 50.6-point margin within tolerance.
- 2 points: Applies the deterministic rule using both thresholds: `margin >= 20.0` and `point_precip_mm <= 1.0`.
- 1 point: Gives `rainfall_runoff_competitive` as the rejected alternative from the failed numeric tests.
- 1 point: Keeps the final mechanism label concise and tied to the computed consequence.
- 1 point: Does not infer asset-level damage or regional-scale conclusions beyond the calculation.
