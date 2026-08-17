# Correct Answer

The correct compact JSON is:

```json
{
  "rainfall": {"mean_mm": 290.112, "range_mm": 14.759, "agreement": 0.9491},
  "climate_gate": {"oni_mean": 0.465, "soi_mean": -1.2, "gate": 1},
  "receptor_score": 0.8691,
  "image_score": 0.5822,
  "event_consistency_score": 90.94,
  "class": "high",
  "window_scope": {
    "rainfall_products": "2019-09-01 to 2019-10-16 early wet-season rainfall-product window",
    "climate_gate": "September-December 2019 ONI/SOI background gate; no IOD term is scored in this task"
  },
  "consistency_proof": "High ECS follows from rainfall load 0.967, agreement 0.9491, climate gate 1, receptor score 0.8691, and image score 0.5822."
}
```

# Key Computations

Regional rainfall means for the 2019-09-01 to 2019-10-16 product window are 294.239, 295.427, and 280.668 mm. Their mean is 290.112 mm, their range is 14.759 mm, and rainfall agreement is `1 - 14.759 / 290.112 = 0.9491`.

The September-December index means are ONI `0.465` and SOI `-1.200`, so the climate gate is `1`; no IOD term is scored. The local population sum is 42161.965 and the bounded-map building count is 537, giving receptor concentration `0.5 * 42161.965 / 50000 + 0.5 * 537 / 600 = 0.8691`. The annual embedding-change mean is 0.008356, so the image-stability score is `1 - 0.008356 / 0.02 = 0.5822`.

The final score is:

```text
100 * (0.30 * 0.9670 + 0.25 * 0.9491 + 0.15 * 1
       + 0.20 * 0.8691 + 0.10 * 0.5822)
= 90.94
```

# Reasoning Path

The score is high because the three regional rainfall estimates are all near 280-295 mm and differ by only about 5.1% of their mean. The ONI/SOI gate keeps the Pacific background from becoming the decisive term, while the population and building counts add a strong local receptor term. The annual image-change mean is small, so it contributes a positive stability score rather than dominating the calculation.

# Numeric Consistency Reading

All major terms are positive: rainfall load `0.9670`, rainfall agreement `0.9491`, climate gate `1`, receptor concentration `0.8691`, and image stability `0.5822`. The weighted ledger therefore supports a high internal-consistency classification for the wet-season flood signal.

# Scoring Rubric

- 4 points: Reports the final numeric score as 90.94 within 0.05 and gives class `high`.
- 4 points: Extracts the three September-October rainfall means and computes the mean, range, and agreement with units.
- 3 points: Computes the September-December ONI and SOI means, applies the climate gate correctly, and does not introduce an unscored IOD term.
- 4 points: Computes receptor concentration from population plus building count and image stability from the annual change mean.
- 3 points: Applies the ECS formula with the stated weights and shows enough arithmetic to audit the result.
- 2 points: Gives a compact consistency proof tied to the threshold ledger and component scores.
