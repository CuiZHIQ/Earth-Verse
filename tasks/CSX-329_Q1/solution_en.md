# Expected Answer

```json
{
  "answer": {
    "region_fraction": 1.0,
    "term_fraction": 1.0,
    "scores": {
      "heat": 10,
      "rain": 2,
      "land": 1,
      "later": 2,
      "ceiling": 2
    },
    "margin": 8,
    "precip_ratio": 1.223,
    "land_values": {
      "alpha_mean": 0.02831,
      "dnbr_mean": -0.108468,
      "dnbr_max": 0.682589
    },
    "passes": true,
    "label": "alert_level2_bleaching_heat_stress_dominant"
  },
  "interpretation": "The named-region and product-term fractions are both 1.0, and the heat score exceeds the strongest context score by 8, so the dominance rule passes."
}
```

# Calculation Path

The three named regions are present, so `region_fraction = 3 / 3 = 1.0`. The four heat-stress product terms are present, so `term_fraction = 4 / 4 = 1.0`.

The heat score is `hazard_match + Alert_Level_2 + severity_definition + region_count + term_count = 1 + 1 + 1 + 3 + 4 = 10`. The rainfall score is `I(451.939 >= 100) + I(369.486 >= 100) = 2`. The land score is `I(0.02831 >= 0.1) + I(-0.108468 >= 0.2) + I(0.682589 >= 0.5) = 1`. The later-context score is `1 + 1 = 2`.

The context ceiling is `max(2, 1, 2) = 2`, so `margin = 10 - 2 = 8`. Since the two fractions equal `1.0` and `8 >= 5`, the rule passes. The precipitation ratio is `451.939 / 369.486 = 1.223`.

# Scoring Rubric

- 4 points: Returns the requested JSON answer object with fractions, scores, margin, precipitation ratio, land values, pass state, label, and one calculation-tied sentence.
- 4 points: Computes 3/3 named-region coverage and 4/4 heat-stress product-term coverage, both reported as `1.0`.
- 4 points: Computes the score ledger as heat `10`, rain `2`, land `1`, later `2`, and ceiling `2`.
- 3 points: Computes margin `8` and applies the `margin >= 5` plus two full-coverage gates correctly.
- 2 points: Reports GPM/CHIRPS ratio `1.223` and land values `0.02831`, `-0.108468`, and `0.682589` within tolerance.
- 2 points: Treats rainfall, land-change, and later eastward context as non-dominant because their scores do not exceed `2`.
- 1 point: Uses the compact label `alert_level2_bleaching_heat_stress_dominant` without adding unscored impact estimates.
