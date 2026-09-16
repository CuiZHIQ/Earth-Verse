# Final Answer

```json
{
  "threshold_mm": 1000,
  "max_sample_mm": 491.133,
  "threshold_ratio": 0.491,
  "shortfall_mm": 508.867,
  "poyang_excess_m": 3.4,
  "classification": "sampled_rain_below_1000mm_with_poyang_high_water_excess"
}
```

Canonical answer label: `sampled_rain_below_1000mm_with_poyang_high_water_excess`.

# Key Computations

- Convert the regional rainfall threshold: `100 cm * 10 = 1000 mm`.
- Compare the sampled precipitation maxima:
  - ERA5-Land maximum precipitation sum: `491.133 mm`.
  - GPM event maximum precipitation: `466.113 mm`.
  - CHIRPS event maximum precipitation: `382.717 mm`.
- Use the largest sampled precipitation value: `max(491.133, 466.113, 382.717) = 491.133 mm`.
- Threshold ratio: `491.133 / 1000 = 0.491133`, rounded to `0.491`.
- Threshold shortfall: `1000 - 491.133 = 508.867 mm`.
- Poyang Lake high-water excess: `22.6 m - 19.2 m = 3.4 m`.

# Reasoning Path

The threshold test fails for the sampled rainfall diagnostics. Even the largest sampled precipitation maximum, `491.133 mm`, is only about `49.1%` of the `1000 mm` report threshold, leaving a `508.867 mm` shortfall. The sampled area should therefore be described as heavy-rainfall but below the `>100 cm` rainfall class, not as a sampled `>100 cm` maximum.

The lake-level calculation is a separate hydrologic anchor. Poyang Lake reached `22.6 m` against an average annual maximum of `19.2 m`, so the computed excess is `3.4 m`. That supports a high-water floodplain interpretation without changing the rainfall threshold result for the sampled precipitation diagnostics.

# Computed Interpretation

For this July 2020 monsoon event, the deterministic ledger separates two facts: sampled local precipitation was intense but below the `1000 mm` threshold, while the documented Poyang Lake level sat `3.4 m` above its average annual maximum. The compact interpretation is therefore `sampled_rain_below_1000mm_with_poyang_high_water_excess`.

# Scoring Rubric

Award 20 points:

- Final JSON and label, 4 points: returns the six requested fields and gives `sampled_rain_below_1000mm_with_poyang_high_water_excess` or an equivalent snake_case classification. Partial credit: 2-3 points if the conclusion is correct but one field is missing or the label is not compact; 1 point if the answer is mostly prose but the threshold failure is clear.
- Threshold conversion and sampled maximum, 4 points: converts `100 cm` to `1000 mm` and uses `491.133 mm` as the maximum across the sampled precipitation diagnostics. Partial credit: 2-3 points for using the correct threshold with a non-maximum sampled value such as `466.113 mm`; 1 point for correct units but weak comparison logic.
- Ratio and shortfall arithmetic, 4 points: computes `threshold_ratio = 0.491` and `shortfall_mm = 508.867` with acceptable rounding. Partial credit: 2-3 points if one derived value is correct; 1 point if the arithmetic setup is right but the rounded numbers are off.
- Poyang high-water calculation, 3 points: computes `22.6 - 19.2 = 3.4 m` and treats it as a separate high-water anchor. Partial credit: 1-2 points for naming the two lake levels but omitting or misrounding the excess.
- Consistency proof, 3 points: explains that the sampled rainfall diagnostics fail the `>100 cm` threshold while the lake level still supports floodplain high-water conditions. Partial credit: 1-2 points if only one side of this distinction is explained.
- Precision and bounded interpretation, 2 points: keeps the answer concise, uses the requested rounding, and avoids adding loss totals or action advice beyond the computed ledger. Partial credit: 1 point if the values are mostly correct but the output is cluttered or over-interpreted.
