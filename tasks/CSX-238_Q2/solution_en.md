# Correct Answer

```json
{
  "answer": "liquefaction_led_ground_failure",
  "pop_ratio": 50.0,
  "hazard_ratio": 22.353,
  "bound_floor": 13.66,
  "alert_gap": 1,
  "dominance_score": 4.048,
  "shaking_index": 1.493
}
```

# Calculation Path

The structured record gives liquefaction and landslide population alert values of `25000` and `500`, so `pop_ratio = 25000 / 500 = 50.0`. The aggregate hazard values are `38.0` and `1.7`, so `hazard_ratio = 38.0 / 1.7 = 22.353`.

The adverse one-sigma floor is `min(19324.78667705625 / 645.5438274307791, 30.824277047883843 / 2.2565945355142194) = min(29.936, 13.66) = 13.66`. Color ranks give `alert_gap = 2 - 1 = 1`. The composite score is `log10(50.0) + log10(22.3529411765) + 1 = 4.048`, and the shaking-depth index is `max(8.808, 8.5) / 5.9 = 1.493`.

The answer label is `liquefaction_led_ground_failure` because `pop_ratio >= 25`, `hazard_ratio >= 10`, `bound_floor >= 10`, `alert_gap >= 1`, and `dominance_score >= 3.5`.

# Scoring Rubric

- 4 points: Extracts the correct structured anchors: `25000`, `500`, `38.0`, `1.7`, the one-sigma bounds, `8.808`, `8.5`, and `5.9 km`.
- 4 points: Computes `pop_ratio = 50.0` and `hazard_ratio = 22.353` with correct denominators.
- 4 points: Computes both adverse-bound ratios and reports the floor as `13.66`.
- 4 points: Applies the color-rank gap and base-10 logarithms to obtain `dominance_score = 4.048`.
- 2 points: Computes `shaking_index = 1.493`.
- 2 points: Returns compact JSON with the label `liquefaction_led_ground_failure` and the requested rounded fields, using the explicit answer rule.
