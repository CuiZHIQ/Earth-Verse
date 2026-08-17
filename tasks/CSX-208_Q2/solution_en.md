# Final Answer

```json
{
  "fire_smoke_load": {"fire_count": 17, "smoke_score": 1.0, "load": 17.0, "pass": true},
  "burn_contrast": {"dnbr_max": 0.6516, "dnbr_mean": 0.0442, "ratio": 14.75, "pass": true},
  "weather_load": {"heat_c_days": 30.04, "dry_days": 46, "days": 46, "max_wind_mps": 6.81, "load": 50.5, "pass": true},
  "precipitation_clearing": {"point_total_max_mm": 0.02, "gridded_mean_max_mm": 3.2, "absent_score": 1, "pass": true},
  "exposure_normalized_index": {"population": 4365.74, "index": 12658.29, "per_1000_people": 2899.46, "pass": true},
  "classification": "compound_fire_smoke_hazard_supported"
}
```

# Key Computations

The wildfire catalog contributes `17` Australian point events inside 112 to 154 E and 44 to 10 S during the event window. The three smoke-report terms are all present, so `smoke_score = 3 / 3 = 1.0` and `fire_smoke_load = 17 * 1.0 = 17.0`.

The Sentinel-2 burn contrast is `0.6515902721 / 0.0441892126 = 14.7454601328`, rounded to `14.75`. The available NASA POWER daily fire-weather slice covers 2019-09-01 through 2019-10-16 and has `heat_c_days = sum(max(Tmax - 35, 0)) = 30.04`, `dry_days = 46`, `days = 46`, and `max_wind_mps = 6.81`; no missing daily values are inferred outside that slice. Thus `weather_load = 30.04 * (46 / 46) * (1 + 6.81 / 10) = 50.49724`, rounded to `50.50`.

The larger point-source precipitation total is `0.02 mm`, and the larger gridded precipitation mean is `3.1971901481 mm`, rounded to `3.20 mm`; therefore `absent_score = 1`. The compound index is `17.0 * 14.7454601328 * 50.49724 * 1 = 12658.285667`. With population `4365.744481`, the normalized value is `12658.285667 / (4365.744481 / 1000) = 2899.456375` per 1000 people.

# Reasoning Path

The fire-smoke row passes because the fire count is at least `10` and the smoke score is exactly `1.0`.

The burn row passes because `dnbr_max = 0.6516` is at least `0.6`, `dnbr_mean = 0.0442` is below `0.1`, and the max-to-mean ratio is above `10`.

The weather row passes because `weather_load = 50.50` is at least `40` and the dry fraction is `46 / 46 = 1.0`, above `0.9`.

The precipitation-clearing row passes because the point total is no more than `1 mm` and the gridded mean is below `5 mm`. The exposure-normalized row passes because `2899.46` per 1000 people is above the `1000` threshold. Since all five rows pass, the final classification is `compound_fire_smoke_hazard_supported`.

# Computed Interpretation

The local data satisfy the numeric fire-smoke threshold ledger: the event has enough cataloged fire points, complete smoke-term support, strong max-to-mean burn contrast, dry-hot weather loading, weak precipitation clearing, and a large exposure-normalized compound index.

# Scoring Rubric

- 4 points: Returns the requested six-key JSON structure with nested numeric values and pass/fail states for all ledger components. partial_credit: Award 1-3 points for a mostly complete structure with missing or misplaced fields.
- 5 points: Computes the main numeric anchors correctly within tolerance: 17 fire events, smoke score 1.0, dNBR ratio about 14.75, heat load about 30.04 C-days, 46/46 dry days, max wind about 6.81 m/s, weather load about 50.50, precipitation values about 0.02 mm and 3.20 mm, population about 4365.74, and normalized index about 2899.46. partial_credit: Award 1-4 points for correct subsets or minor rounding differences.
- 4 points: Applies the threshold logic correctly for fire-smoke, burn contrast, weather load, precipitation clearing, and exposure-normalized index. partial_credit: Award 1-3 points for mostly correct decisions with one or two threshold errors.
- 3 points: Shows or implies the formulas for `fire_smoke_load`, `dnbr_max / dnbr_mean`, `sum(max(Tmax - 35, 0))`, weather load, compound index, and population normalization. partial_credit: Award 1-2 points when formulas are partly correct but incomplete.
- 2 points: Encodes the low dNBR mean, high max-to-mean dNBR ratio, and weak precipitation-clearing values in the JSON pass/fail states so broad-burn or rainfall-clearing alternatives are not selected. partial_credit: Award 1 point when one alternative is correctly ruled out by the JSON states.
- 1 point: Keeps the final answer JSON-only with the concise compound fire-smoke support classification. partial_credit: Award 0.5 point if the classification is correct but accompanied by minor extra prose outside the JSON.
- 1 point: Avoids converting nearby population, roads, or report wording into measured casualties, infrastructure damage, or response actions. partial_credit: No credit if the answer makes a direct-loss claim not present in the ledger.
