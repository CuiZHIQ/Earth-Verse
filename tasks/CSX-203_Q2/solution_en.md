# Final Answer

```json
{
  "metrics": {
    "haze_term_count": 3,
    "dry_fraction": 1.0,
    "mean_vector_wind_mps": 0.44,
    "regional_precip_mean_mm": 0.713,
    "diffuse_veil_index": 37.061,
    "burn_evidence_count": 0
  },
  "tests": {
    "haze_text": "pass",
    "dry_window": "pass",
    "weak_wind": "pass",
    "low_precipitation": "pass",
    "diffuse_brightening": "pass",
    "no_package_burn_evidence": "pass"
  },
  "consistency_score": "6/6",
  "final_label": "persistent_winter_aerosol_haze",
  "rejected_alternative": "wet_removal_or_package_burn_control_not_supported"
}
```

# Key Computations

The event narrative contains all three tracked air-quality terms: `haze`, `smog`, and `air quality`, so `haze_term_count = 3`.

For 2013-01-06 through 2013-01-16, the daily precipitation series has 11 dry days across 11 event-window days:

`dry_fraction = 11 / 11 = 1.0`, passing the `>= 0.80` threshold.

The regional mean wind components are `u10_mean = 0.332 m/s` and `v10_mean = -0.289 m/s`:

`mean_vector_wind_mps = sqrt(0.332^2 + (-0.289)^2) = 0.44 m/s`, passing the `< 1.0 m/s` weak-wind threshold.

The two regional accumulated-precipitation means are `1.030 mm` and `0.397 mm`:

`regional_precip_mean_mm = (1.030 + 0.397) / 2 = 0.713 mm`, passing the `<= 2.0 mm` low-precipitation threshold.

The pre-event and event true-color image summaries give mean brightness `153.197` and `190.601`, and mean chroma `6.392` and `6.735`:

`diffuse_veil_index = (190.601 - 153.197) - abs(6.735 - 6.392) = 37.061`, passing the `>= 20.0` diffuse-brightening threshold.

The available package burn-source count is:

`burn_evidence_count = wildfire_event_count + burn_pre_count + burn_post_count = 0 + 0 + 0 = 0`, passing the package-burn-evidence threshold.

All six tests pass, so the consistency score is `6/6` and the derived label is `persistent_winter_aerosol_haze`.

# Reasoning Path

The proof starts with report text and local weather. All three haze terms are present, and the event-window weather is completely dry, so both the text and dry-window tests pass. The regional wind-vector speed is only `0.44 m/s`, and the two-product precipitation mean is `0.713 mm`, so the weak-wind and low-precipitation tests also pass.

The image check then evaluates the diffuse-brightening formula rather than making a broad visibility claim, using the selected pre-event and event MODIS true-color images recorded in provenance. The event image is much brighter than the pre-event image with little chroma change, producing a diffuse veil index of `37.061`, above the threshold. Finally, the wildfire-event and available burn-scene counts sum to zero, so package-supported active-burn-source control is not supported by the package values.

With six passing tests out of six, the consistency proof yields `persistent_winter_aerosol_haze` and rejects wet-removal or package-supported active-burn-source control.

# Computed Interpretation

The computed ledger supports persistent winter aerosol haze: haze terms, dry conditions, weak winds, low precipitation, diffuse image brightening, and zero available package burn-source evidence all pass their thresholds.

# Scoring Rubric

Total: 20 points.

- 4 points: Returns the requested compact JSON with metrics, tests, `consistency_score`, `final_label`, and `rejected_alternative`. Partial credit: 2-3 points for a mostly complete JSON object with one missing or renamed field.
- 5 points: Computes the six numeric metrics correctly: `haze_term_count = 3`, `dry_fraction = 1.0`, `mean_vector_wind_mps = 0.44`, `regional_precip_mean_mm = 0.713`, `diffuse_veil_index = 37.061`, and `burn_evidence_count = 0`, with reasonable rounding. Partial credit: proportional credit for correct metric values and formulas.
- 4 points: Applies all thresholds correctly and reports every test as `pass`, yielding `consistency_score = 6/6`. Partial credit: 1 point for each cluster of correctly evaluated tests.
- 3 points: Uses the dry-window, weak-wind, and low-precipitation calculations together as the meteorological consistency proof for pollutant persistence. Partial credit: 1-2 points for using only one or two of those calculations correctly.
- 2 points: Rejects wet-removal control and package-supported active-burn-source control using the precipitation and available burn-count calculations. Partial credit: 1 point for one correctly rejected alternative.
- 1 point: Gives only the compact derived label `persistent_winter_aerosol_haze` after the calculations. Partial credit: 0.5 points for a correct but overly verbose label.
- 1 point: Avoids extra-data PM concentration, AOD, casualty, economic-loss, or response-advice assertions. Partial credit: 0.5 points for one minor extra inference that does not change the proof.
