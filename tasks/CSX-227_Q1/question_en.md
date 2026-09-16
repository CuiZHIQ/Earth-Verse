# Taan Fiord Candidate Score Ledger

A hazard-mechanism analyst is checking the 2015-10-17 Taan Fiord event with a deterministic score ledger. Use the event package to compute the measured indices, threshold flags, and four candidate scores below. The final label is the candidate with the highest score; the score gap is the winning score minus the next-highest score.

Use these formulas and thresholds:

- `rock_mass_million_tons` comes from the institutional event report text.
- `max_runup_m` comes from the same report text.
- `s1_abs_change_db = max(abs(post_minus_pre_db_max), abs(post_minus_pre_db_min))` from Sentinel-1 VV pre/post statistics.
- `precip_median_mm` is the median of the non-null event-day precipitation estimates from Open-Meteo, NASA POWER, ERA5-Land mean, and GPM IMERG mean.
- `population_sum` comes from the 2015 WorldPop population sum.
- `event_window_days` is the inclusive day count between the locked start and end dates.

Score the candidates as:

- `landslide_displacement_tsunami = 3*I(rock_mass_million_tons >= 100) + 3*I(max_runup_m >= 100) + 1*I(s1_abs_change_db >= 30) + 1*I(event_window_days == 1) + 1*I(population_sum < 1)`
- `rain_flood_pulse = 3*I(precip_median_mm >= 50) + 1*I(rock_mass_million_tons < 100) + 1*I(max_runup_m < 100)`
- `radar_change_standalone = 2*I(s1_abs_change_db >= 30) + 2*I(rock_mass_million_tons < 100) + 2*I(max_runup_m < 100)`
- `population_broad_impact = 3*I(population_sum >= 100) + 1*I(max_runup_m >= 100)`

Return only compact JSON with these keys:

```json
{
  "winning_label": "short_label",
  "score_summary": {
    "winning_score": 0,
    "runner_up_label": "short_label",
    "score_gap": 0
  },
  "diagnostic_indices": {
    "rock_mass_million_tons": 0,
    "max_runup_m": 0,
    "s1_abs_change_db": 0,
    "precip_median_mm": 0,
    "population_sum": 0
  },
  "threshold_flags": {
    "mass_ge_100": false,
    "runup_ge_100": false,
    "radar_abs_ge_30": false,
    "precip_median_ge_50": false,
    "population_lt_1": false,
    "event_window_eq_1_day": false
  },
  "candidate_scores": {
    "landslide_displacement_tsunami": 0,
    "rain_flood_pulse": 0,
    "radar_change_standalone": 0,
    "population_broad_impact": 0
  },
  "window_ledger": {
    "event_window_days": 0,
    "sentinel1_pre_count": 0,
    "sentinel1_post_count": 0
  },
  "computed_interpretation": "one sentence tied to the score gap"
}
```
