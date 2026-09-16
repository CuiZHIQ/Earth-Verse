# Final Answer

```json
{
  "answer": {
    "exposure_margin_people": 1074.963,
    "radar_margin_db": 14.495,
    "optical_margin": 0.024,
    "same_day_precip_max_mm": 12.245,
    "precip_margin_mm": 12.755,
    "ledger_score": 4,
    "classification": "exposed_strong_surface_limited_rain_ledger"
  },
  "interpretation": "All four gates pass: population is above the ledger threshold, radar and optical surface-change margins are positive, and the same-day rainfall maximum remains below 25 mm."
}
```

# Key Computations

The computation reads the event anchor, population layer, radar pre/post change,
optical dNBR, and five same-day precipitation candidates from the CSX-226 event
package.

Core inputs:

```json
{
  "exposed_population": 6074.962951,
  "minimum_vv_post_minus_pre_db": -34.494922,
  "maximum_dnbr": 0.474423,
  "same_day_precipitation_candidates_mm": {
    "chirps_max": 12.244905,
    "gpm_max": 1.295,
    "era5_max": 0.148493,
    "open_meteo_sum": 0.5,
    "nasa_power_sum": 1.24
  }
}
```

Ledger arithmetic:

```text
exposure_margin_people = 6074.962951 - 5000 = 1074.963
radar_margin_db = abs(-34.494922) - 20.0 = 14.495
optical_margin = 0.474423 - 0.45 = 0.024
same_day_precip_max_mm = max(12.244905, 1.295, 0.148493, 0.5, 1.24) = 12.245
precip_margin_mm = 25.0 - 12.244905 = 12.755
ledger_score = 1 + 1 + 1 + 1 = 4
```

# Reasoning Path

The event anchor fixes the date as 2024-05-24 in Enga Province, Papua New
Guinea, and the hazard family as landslide mass movement. The population value
is above the 5000-person threshold, so the exposure gate contributes one point.

The radar ledger uses the magnitude of the most negative VV post-minus-pre
change, giving a positive 14.495 dB margin beyond the 20 dB threshold. The
optical ledger also passes because maximum dNBR exceeds 0.45 by 0.024.

For the weather window, the maximum same-day precipitation candidate is the
CHIRPS value of 12.245 mm. Since that remains 12.755 mm below the 25 mm cutoff,
the rain gate also contributes one point. Four passing gates produce the score
4 classification.

# Computed Interpretation

This is a threshold-ledger diagnosis, not a free-form impact narrative. The
computed result says the event has exposed population and strong surface-change
signals while same-day rainfall stays below the ledger cutoff. Therefore the
deterministic classification is
`exposed_strong_surface_limited_rain_ledger`.

# Scoring Rubric

Total: 20 points.

- 3 points: Answer schema. Returns compact JSON with all requested numeric
  fields, ledger score, classification, and one-sentence interpretation.
  Partial credit: 1-2 points for parseable JSON that omits one field or has
  minor nesting problems.
- 4 points: Input extraction. Uses 6074.963 people, -34.495 dB minimum VV
  change, 0.474423 maximum dNBR, and the five same-day precipitation
  candidates. Partial credit: 1 point for each correct data family up to 4
  points.
- 4 points: Surface margins. Computes `radar_margin_db = 14.495` and
  `optical_margin = 0.024` within tolerance. Partial credit: 2 points for each
  correct surface margin; 1 point for a correct formula with an arithmetic
  error.
- 4 points: Exposure and rain margins. Computes `exposure_margin_people =
  1074.963`, `same_day_precip_max_mm = 12.245`, and `precip_margin_mm =
  12.755`. Partial credit: up to 1.5 points for exposure, 1 point for
  precipitation maximum, and 1.5 points for precipitation margin.
- 3 points: Gate ledger. Marks all four gates true and totals `ledger_score =
  4`. Partial credit: 1 point for each correct pair of gate state and score
  contribution, up to 3 points.
- 1 point: Final classification. Maps score 4 to
  `exposed_strong_surface_limited_rain_ledger`. Partial credit: 0.5 point for
  a near-equivalent label tied to score 4.
- 1 point: Interpretation discipline. Keeps the interpretation tied to computed
  thresholds and avoids exact loss or cause statements not derived from the
  ledger. Partial credit: 0.5 point for a mostly ledger-tied sentence with one
  extra uncomputed detail.
