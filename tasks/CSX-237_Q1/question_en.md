# Maule Event-Data Consistency Score

Compute a numeric score from the local CSX-237 package for the 27 February 2010 Maule, Chile earthquake and tsunami. Use structured package records for the catalog, precipitation, radar-count, population, and mapped-amenity values.

Let `clamp(x)=max(0,min(x,1))`.

Compute these terms:

- `S`: catalog severity term, `mean(clamp((M-5)/(9-5)), clamp(alertscore/3), clamp(1-depth_km/100))`, using the Chile earthquake record.
- `K`: catalog separation term, `clamp((M_chile - max_M_non_chile)/3.5)`, using the same GDACS alert slice.
- `Z`: dry-source agreement term, `(count of precipitation values < 1 mm)/5`, using the two point precipitation values and the three gridded mean precipitation values.
- `V`: paired-radar deficit term, `1 - clamp(min(pre_count, post_count))`.
- `X`: population-scale term, `clamp(log10(population_sum)/7)`.
- `F`: mapped-amenity saturation term, `clamp(amenity_count/1200)`.
- `R`: rainfall magnitude deduction term, `clamp(mean(the five precipitation values)/5)`.

Use:

`score = 100 * (0.26*S + 0.16*K + 0.16*Z + 0.12*V + 0.18*X + 0.12*F - 0.04*R)`

Threshold rules:

- The six positive terms pass at `S>=0.80`, `K>=0.80`, `Z>=0.80`, `V>=0.95`, `X>=0.90`, and `F>=0.80`.
- The rainfall term passes when `R<0.05`.
- Set `final_label` to `high_consistency_catalog_led_record` when `score>=90`, all six positive terms pass, and `R<0.05`; otherwise use `lower_consistency_by_this_score`.

Return JSON only:

```json
{
  "component_ledger": [
    {"term": "S", "value": 0, "threshold_result": ""},
    {"term": "K", "value": 0, "threshold_result": ""},
    {"term": "Z", "value": 0, "threshold_result": ""},
    {"term": "V", "value": 0, "threshold_result": ""},
    {"term": "X", "value": 0, "threshold_result": ""},
    {"term": "F", "value": 0, "threshold_result": ""},
    {"term": "R", "value": 0, "threshold_result": ""}
  ],
  "score": 0,
  "positive_terms_passing": 0,
  "rainfall_term_pass": false,
  "final_label": ""
}
```
