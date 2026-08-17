# Final Answer

```json
{
  "target_family": "candidate_explanation_score_ledger",
  "metrics": {
    "event_duration_days": 182,
    "weather_overlap_days": 46,
    "dry_windy_days": 9,
    "dry_windy_share": 0.195652,
    "dnbr_mean": 0.155941,
    "dnbr_min": -1.074075,
    "dnbr_max": 0.9738,
    "dnbr_stddev": 0.109541,
    "annual_change_mean": 0.028207,
    "population_rounded": 362810,
    "smoke_transport_flag": true,
    "air_quality_flag": true
  },
  "gates": {
    "burn_mean_gate": 1,
    "burn_peak_gate": 1,
    "heterogeneous_gate": 1,
    "dry_windy_gate": 1,
    "smoke_transport_gate": 1,
    "air_quality_gate": 1,
    "population_gate": 1,
    "uniform_burn_gate": 0,
    "annual_change_high_gate": 0
  },
  "scores": {
    "compound_smoke_burn_exposure": 7,
    "burn_only_surface_change": 2,
    "population_only_context": 1
  },
  "score_margin": 5,
  "answer": "compound_smoke_burn_exposure",
  "computed_interpretation": "The compound label wins by 5 points because the ledger has two burn gates, one heterogeneity gate, one dry-windy gate, two smoke-text gates, and one population gate; the burn-only label lacks the uniform-burn and high-annual-change gates."
}
```

# Key Computations

- Inclusive event window: 2019-09-01 through 2020-02-29 gives `(2020-02-29 - 2019-09-01) + 1 = 182` days.
- Weather overlap inside that event window is the package daily-weather coverage from 2019-09-01 through 2019-10-16, giving 46 daily records rather than complete 182-day weather coverage. Of those, 9 have zero precipitation and maximum 10 m wind speed at least 20 km/h, so `dry_windy_share = 9 / 46 = 0.195652`.
- Sentinel-2 dNBR statistics are `mean = 0.155941`, `min = -1.074075`, `max = 0.9738`, and `stddev = 0.109541`.
- Annual embedding-change mean is `0.028207`.
- Rounded population is `362810`.
- Report text contains stratospheric smoke transport language and hazardous or severe air-quality wording, so both text flags are `true`.

# Reasoning Path

The burn gates pass because `dnbr_mean >= 0.10` and `dnbr_max >= 0.66`. The heterogeneity gate also passes because `dnbr_min < 0` and `annual_change_mean < 0.05`, while the uniform-burn gate fails because the dNBR minimum is negative and the dNBR standard deviation is above 0.05. The high annual-change gate fails because `0.028207 < 0.10`.

The dry-windy gate passes because `dry_windy_days = 9` and `dry_windy_share = 0.195652`, meeting the `8` day and `0.15` share thresholds. The smoke-transport and air-quality text gates pass, and the population gate passes because `362810 >= 300000`.

The score arithmetic is therefore:

- `compound_smoke_burn_exposure = 1 + 1 + 1 + 1 + 1 + 1 + 1 = 7`
- `burn_only_surface_change = 1 + 1 + 0 + 0 = 2`
- `population_only_context = 1`
- `score_margin = 7 - max(2, 1) = 5`

# Computed Interpretation

The computed fingerprint is compound rather than burn-only: the highest label has a 5-point margin because the ledger combines positive local burn signal, mixed landscape-change evidence, dry-windy weather overlap, smoke-text evidence, air-quality wording, and population scale.

# Scoring Rubric

Total: 20 points.

- Final label and margin, 4 points: Returns `answer = compound_smoke_burn_exposure`, `score_margin = 5`, and the three scores `7`, `2`, and `1`. Partial credit: 2-3 points for the correct label with an incomplete or slightly wrong margin; 1 point for recognizing the compound label without a valid score comparison.
- Event-window and weather metrics, 3 points: Computes 182 event days, 46 weather-overlap days, 9 dry/windy days, and dry/windy share about 0.195652. Partial credit: 1-2 points for two or three correct values, or for correct counts with a rounded share that remains within 0.01.
- Burn and landscape-change metrics, 4 points: Reports dNBR mean about 0.155941, minimum about -1.074075, maximum about 0.9738, standard deviation about 0.109541, and annual embedding-change mean about 0.028207. Partial credit: 2-3 points if most values are correct but one statistic is omitted; 1 point if only the mean or maximum is correct.
- Text and population flags, 3 points: Reports rounded population about 362810 and sets both smoke-transport and air-quality flags to true. Partial credit: 1-2 points for correct population with one missing text flag, or correct text flags with a population value within 1000.
- Gate and formula arithmetic, 4 points: Applies all nine gates with values `1,1,1,1,1,1,1,0,0` and uses the stated formulas to obtain scores `7,2,1`. Partial credit: 2-3 points for one or two gate errors that do not change the final label; 1 point for using the formulas but omitting several gates.
- Compact JSON and computed interpretation, 2 points: Returns exactly the requested fields and gives a concise interpretation tied to the score ledger. Partial credit: 1 point for valid JSON with extra or missing fields, or for an interpretation that is present but not tied to the computed scores.
