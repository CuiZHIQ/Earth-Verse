# Final Answer

Canonical answer: `smoke_load_5_fire_source_4_surface_change_3_composite_12`

```json
{
  "smoke_load_score": 5,
  "fire_source_score": 4,
  "surface_change_score": 3,
  "composite_score": 12,
  "top_score_family": "smoke_load",
  "context_population_people": 58882
}
```

# Key Computations

Smoke-load score:

- Goddard average AOD on 2023-05-10 = 1.0. Since `1.0 >= 1.0`, award 2 points.
- Grand Forks average AOD on 2023-05-16 = 2.3. Since `2.3 >= 2.0`, award 2 points.
- Grand Forks peak AOD on 2023-05-16 is close to 3.0. Since `3.0 >= 3.0`, award 1 point.
- `smoke_load_score = 2 + 2 + 1 = 5`.

Fire-source score:

- Burned area by 2023-05-16 = 478,000 hectares. Since `478000 >= 400000`, award 2 points.
- Burned area by 2023-05-16 = 1,800 square miles. Since `1800 >= 1500`, award 1 point.
- Alberta active-fire count = 87. Since `87 >= 80`, award 1 point.
- `fire_source_score = 2 + 1 + 1 = 4`.

Surface-change score:

- Mean dNBR = 0.355. Since `0.355 >= 0.30`, award 1 point.
- Maximum dNBR = 1.417. Since `1.417 >= 1.00`, award 1 point.
- Annual embedding mean change = 0.045 and maximum change = 0.792. Since `0.045 < 0.10` and `0.792 >= 0.75`, award 1 point.
- `surface_change_score = 1 + 1 + 1 = 3`.

Other computed values:

- `composite_score = 5 + 4 + 3 = 12`.
- The highest family score is `smoke_load`.
- Rounded compact population sum = 58,882 people.

# Reasoning Path

The ledger gives the transported-aerosol family three tests worth five total points. All three pass, so the smoke-load family earns the full 5 points.

The fire-source family also passes all of its tests, but its maximum is only 4 points because the hectare test carries 2 points and the square-mile and active-fire tests carry 1 point each.

The surface-change family passes all three of its tests, earning 3 points. Its lower total reflects the scoring design, not a failed metric.

With scores of 5, 4, and 3, no tie rule is needed. The top family is `smoke_load`, and the composite ledger total is 12.

# Computed Interpretation

The numerical ledger is strongest for transported aerosol loading, while the large burned area and surface-change metrics remain supporting context for the same May 2023 fire-smoke episode.

# Scoring Rubric

Total: 20 points.

- Output schema and canonical answer (3 points): returns the requested compact JSON fields and includes the canonical ledger values. Partial credit: 1-2 points for a mostly complete object with one missing or mislabeled field.
- Smoke-load extraction and scoring (5 points): reports AOD values of 1.0, 2.3, and about 3.0, applies the three thresholds correctly, and computes `smoke_load_score = 5`. Partial credit: 2-4 points for correct values with one threshold or arithmetic error.
- Fire-source extraction and scoring (4 points): reports 478,000 hectares, 1,800 square miles, and 87 active fires, applies the thresholds, and computes `fire_source_score = 4`. Partial credit: 2-3 points for using two correct anchors or for a minor unit/rounding error.
- Surface-change extraction and scoring (3 points): reports mean dNBR about 0.355, maximum dNBR about 1.417, annual embedding mean about 0.045, and annual embedding maximum about 0.792, then computes `surface_change_score = 3`. Partial credit: 1-2 points for correct dNBR scoring but incomplete annual embedding scoring.
- Composite arithmetic and top family (3 points): computes `composite_score = 12` and identifies `top_score_family = "smoke_load"` without invoking the tie rule. Partial credit: 1-2 points for the right top family with an arithmetic error, or the right composite with a wrong family label.
- Population context and concise interpretation (2 points): rounds the compact population sum to 58,882 people and gives only a short interpretation tied to the ledger. Partial credit: 1 point for a nearby population value or for an interpretation that is longer than needed but still tied to the scores.
