# Final Answer

```json
{
  "target_family": "candidate_score_ledger",
  "metrics": {
    "point_precip_mm": 233.39,
    "areal_precip_mm": 112.67,
    "path_length_km": 6.0,
    "damaged_structures": 349,
    "damaged_roads_km": 1.3,
    "deaths_lower_bound": 1141,
    "people_lost_homes": 3000,
    "forest_decline_percent": 52,
    "local_population": 1099869
  },
  "components": {
    "precip_pair": 1.0,
    "path": 1.0,
    "damage": 1.0,
    "loss": 1.0,
    "context": 0.933
  },
  "candidate_scores": {
    "rain_runout_loss": 99.33,
    "rain_only": 75.0,
    "loss_only": 75.0,
    "context_only": 60.67
  },
  "best_label": "rain_runout_loss",
  "margin_to_second": 24.33,
  "interpretation": "The score ledger favors rain_runout_loss because rainfall, path, damage, and loss components all reach their caps while the context component is lower."
}
```

# Key Computations

`compute_gt.py` reads these local package files:

- `metadata/event.json`
- `data/other/other_001_NASA_Earth_Observatory_Freetown_landslide.html`
- `data/exposure_impact/exposure_impact_001_HDX_CKAN_package_search.json`
- `data/exposure_impact/exposure_impact_005_salvaged_existing_stage8_file.json`
- `data/physical_hazard/physical_hazard_002_NASA_POWER_daily_point_sample.json`
- `data/physical_hazard/physical_hazard_006_salvaged_existing_stage8_file.json`

Extracted values:

- NASA POWER point precipitation on 2017-08-14: 233.39 mm.
- ERA5-Land areal mean precipitation on 2017-08-14: 112.67 mm.
- Regent path length: 6.0 km.
- Damaged structures and roads: 349 structures and 1.3 km of roads.
- Reported loss values: more than 1,141 deaths and 3,000 people losing homes.
- Forest decline and local population: 52 percent and 1,099,869 people.

Component arithmetic:

- `precip_pair = 0.6 * 1 + 0.4 * 1 = 1.000`.
- `path = min(6.0 / 5, 1) = 1.000`.
- `damage = 0.7 * 1 + 0.3 * 1 = 1.000`.
- `loss = 0.55 * 1 + 0.45 * 1 = 1.000`.
- `context = 0.5 * (52 / 60) + 0.5 * 1 = 0.933`.

Candidate score arithmetic uses the unrounded component values and rounds only the final scores:

- `rain_runout_loss = 100 * (0.30 + 0.25 + 0.20 + 0.15 + 0.0933) = 99.33`.
- `rain_only = 100 * 0.75 = 75.00`.
- `loss_only = 100 * 0.75 = 75.00`.
- `context_only = 100 * (0.65 * 0.933333...) = 60.67`.
- The second-best score is 75.00, so the margin is 24.33.

# Reasoning Path

The ledger first converts extracted quantities into five capped components. The precipitation pair, path, damage, and loss components all saturate because their package values meet or exceed the formula caps. The context component is high but not saturated because the forest term is 52/60 while the population term is capped at 1.

The `rain_runout_loss` formula is the only candidate that receives positive weight from all five components. The `rain_only` and `loss_only` formulas each receive 75.00 because they use one saturated main component and receive no benefit from the complement terms. The `context_only` formula is lower at 60.67 because its main component is 0.933 and its complement terms are zero.

# Computed Interpretation

The computed result is a deterministic candidate score ledger: `rain_runout_loss` wins with 99.33 points and a 24.33 point margin over the next score.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns compact JSON with the requested fields and `best_label` equal to `rain_runout_loss`. Partial credit: 1-2 points for the right label with one missing field or minor naming drift.
- 4 points: Extracts the package values for precipitation, path length, damage, loss, forest decline, and local population. Partial credit: award value by value; small rounding differences are acceptable for continuous quantities.
- 4 points: Computes `precip_pair`, `path`, `damage`, `loss`, and `context` using the stated caps and weights. Partial credit: 1 point for each mostly correct component; reduce credit for missing caps or swapped weights.
- 4 points: Applies all four candidate score formulas using unrounded component values, then rounds final scores to two decimals. Partial credit: give credit for correct formulas with arithmetic or rounding errors in one or two candidates.
- 3 points: Identifies the second-best score as 75.00 and computes a 24.33 point margin. Partial credit: 1-2 points for the correct best label with an incorrect or missing margin.
- 2 points: Keeps the interpretation tied to the numeric ledger rather than a broad event narrative. Partial credit: 1 point for a concise statement that names the best label but omits the component reason.
