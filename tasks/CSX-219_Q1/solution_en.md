# Final Answer

```json
{
  "target_family": "oso_rain_relief_runout_threshold_ledger",
  "rainfall_wetness": {
    "event_day_mean_mm": 0.728,
    "antecedent_mean_mm": 200.41,
    "rainfall_load_mm": 201.14,
    "antecedent_share": 0.996,
    "pass": true
  },
  "relief_proxy": {
    "m_per_km": 288.5,
    "slope_proxy_degrees": 16.1,
    "pass": true
  },
  "runout_area_ratio": {
    "mi_per_sq_mi": 2.0,
    "speed_mph": 40,
    "pass": true
  },
  "image_pair_count": {
    "score": 0,
    "pass": false
  },
  "exposure_normalized_index": {
    "impact_units_per_100k": 11.0,
    "pass": true
  },
  "threshold_pass_fail": {
    "passed_groups": 4,
    "total_groups": 5,
    "mandatory_groups_pass": true
  },
  "final_label": "passes_rain_relief_runout_4of5_thresholds",
  "one_sentence_proof": "Four of five threshold groups pass, including the mandatory rainfall/wetness, relief, and runout/area groups; only the pre/post image-pair count group fails."
}
```

# Key Computations

Event-day precipitation mean:

`(0.00 + 1.56 + 0.584331 + 1.493414 + 0.00) / 5 = 0.727549 mm`, rounded to `0.728 mm`.

Antecedent wetness:

`Open-Meteo March 8-21 total = 218.20 mm`; `NASA POWER March 8-21 total = 182.62 mm`; their mean is `200.41 mm`.

Rainfall load and antecedent share:

`rainfall_load_mm = 200.41 + 0.727549 = 201.14 mm`; `antecedent_share = 200.41 / 201.137549 = 0.996`.

Relief proxy:

The lowland point is `85.0 m`; the gridded mountain point is `671.57 m`. Their haversine distance is `2.033 km`, so `586.57 m / 2.033 km = 288.5 m/km`. The arctangent slope proxy is `16.1 degrees`.

Runout/area ratio:

Using `1.0 mile` for the reported "nearly a mile" of State Route 530 and `0.5 square mile` for the overrun area gives `1.0 / 0.5 = 2.0 mi per sq mi`. Reported average speed is `40 mph`.

Image-pair count:

The two analytic image-change products have `pre_count = 0` and `post_count = 0`, so neither contributes a paired product and `image_pair_score = 0`.

Exposure-normalized index:

`(43 fatalities + 40 covered homes_or_structures) / 754664.615108 * 100000 = 10.998`, rounded to `11.0` impact units per 100,000 context population.

# Reasoning Path

The rainfall/wetness group passes because `201.14 >= 150`, `0.728 <= 2`, and `0.996 >= 0.95`.

The relief group passes because `288.5 m/km >= 100 m/km`.

The runout/area group passes because `2.0 mi per sq mi >= 1.5` and `40 mph >= 30 mph`.

The image-pair count group fails because `0 < 1`.

The exposure-normalized group passes because `11.0 >= 5`. That gives `4` passing groups out of `5`, and the three mandatory groups all pass, so the final label is `passes_rain_relief_runout_4of5_thresholds`.

# Computed Interpretation

The computed ledger is internally positive under the stated rule: rainfall/wetness, relief, runout/area, and exposure clear their thresholds, while the image-pair count does not. Because the three mandatory groups pass and the pass count is four of five, the threshold label is assigned.

# Scoring Rubric

- 3 points: Gives the exact final label `passes_rain_relief_runout_4of5_thresholds`, the pass count `4 of 5`, and `mandatory_groups_pass = true`. Partial credit: award 1-2 points for the correct pass count or mandatory-group result with an incomplete label.
- 3 points: Returns the requested JSON ledger with `target_family`, five group objects, `threshold_pass_fail`, `final_label`, and `one_sentence_proof`. Partial credit: award 1-2 points for a mostly correct structure with one missing group or minor field-name drift.
- 5 points: Reports the numeric anchors within tolerance: `0.728 mm`, `200.41 mm`, `201.14 mm`, `0.996`, `288.5 m/km`, `16.1 degrees`, `2.0 mi per sq mi`, `40 mph`, image-pair score `0`, and exposure index `11.0`. Partial credit: award 3-4 points for mostly correct values with one or two small arithmetic errors; award 1-2 points for copied values without the derived ratios.
- 3 points: Applies the rainfall and exposure formulas correctly, including the five-source event-day mean, two-source antecedent mean, load/share calculation, and per-100,000 exposure normalization. Partial credit: award 1-2 points for correct formulas with missing rounding or one omitted input source.
- 3 points: Applies the relief and runout formulas correctly, including haversine distance, arctangent slope proxy, road length divided by overrun area, and speed threshold. Partial credit: award 1-2 points for correct setup with a wrong distance convention or a missing speed comparison.
- 2 points: Marks all five threshold states correctly and derives the final label from the mandatory-groups plus four-of-five rule. Partial credit: award 1 point for the right label with one mistaken group state.
- 1 point: Keeps the proof concise and numeric, without adding unrelated narrative beyond the requested ledger. Partial credit: award 0.5 points for a correct ledger with extra prose that does not change the result.
