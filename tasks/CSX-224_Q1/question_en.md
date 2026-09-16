# Freetown Rain-Runout Candidate Ledger

Using only the local CSX-224 package, compute a compact candidate score ledger for the August 2017 Freetown record. Extract the package values for point daily precipitation on 2017-08-14, ERA5-Land areal mean precipitation for the same date, Regent path length, damaged structures, damaged roads, deaths lower bound, people losing homes, forest decline percentage, and local WorldPop population.

Compute these components, rounded to three decimals:

- `precip_pair = 0.6 * min(point_precip_mm / 200, 1) + 0.4 * min(areal_precip_mm / 100, 1)`
- `path = min(path_length_km / 5, 1)`
- `damage = 0.7 * min(damaged_structures / 300, 1) + 0.3 * min(damaged_roads_km / 1, 1)`
- `loss = 0.55 * min(deaths_lower_bound / 1000, 1) + 0.45 * min(people_lost_homes / 3000, 1)`
- `context = 0.5 * min(forest_decline_percent / 60, 1) + 0.5 * min(local_population / 1000000, 1)`

Then compute these candidate scores from the unrounded component values, and round only the final candidate scores to two decimals:

- `rain_runout_loss = 100 * (0.30 * precip_pair + 0.25 * path + 0.20 * damage + 0.15 * loss + 0.10 * context)`
- `rain_only = 100 * (0.75 * precip_pair + 0.10 * (1 - path) + 0.10 * (1 - damage) + 0.05 * (1 - loss))`
- `loss_only = 100 * (0.75 * loss + 0.15 * (1 - precip_pair) + 0.10 * (1 - path))`
- `context_only = 100 * (0.65 * context + 0.15 * (1 - precip_pair) + 0.10 * (1 - path) + 0.10 * (1 - loss))`

Return only compact JSON:

```json
{
  "target_family": "candidate_score_ledger",
  "metrics": {},
  "components": {},
  "candidate_scores": {},
  "best_label": "label",
  "margin_to_second": 0.0,
  "interpretation": "one sentence"
}
```
