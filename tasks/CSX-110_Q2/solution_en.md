# Correct Answer

```json
{
  "answer": "rainfall_duration_shortened",
  "target_family": "freddy_duration_wind_rain_lag_sensitivity_ranking",
  "computed_values": {
    "wmo_days": 36,
    "cat_days": 33.75,
    "rain_mm": 393.6,
    "wet_hours": "420/912",
    "wet_days": 36,
    "grid_min_ratio": 2.719,
    "lag_h": 34.0,
    "pressure_range_hpa": 11.4,
    "gust_ratio": 0.264
  },
  "scenario_scores": {
    "rainfall_duration_shortened": 95.0,
    "rainfall_load_reduced": 76.22,
    "peak_wind_reinterpreted_as_primary": 10.319,
    "pressure_signal_weakened": 43.86,
    "flood_lag_removed": 47.222,
    "gridded_rainfall_context_weakened": 73.555
  },
  "ranked_scenarios": [
    "rainfall_duration_shortened",
    "rainfall_load_reduced",
    "gridded_rainfall_context_weakened",
    "flood_lag_removed",
    "pressure_signal_weakened",
    "peak_wind_reinterpreted_as_primary"
  ],
  "top_sensitivity": {
    "scenario": "rainfall_duration_shortened",
    "why": "21/420 wet hours can be removed before wet hours drop below 400"
  },
  "rejected_sensitivity": {
    "scenario": "peak_wind_reinterpreted_as_primary",
    "why": "0.264 gust/catalog ratio needs +89.7% to reach 0.50"
  },
  "reasoning_path": [
    "compute baseline margins",
    "score threshold-crossing changes",
    "rank high scores as small changes"
  ]
}
```

# Key Computations

The WMO report gives a `36 d` record-duration anchor. The catalog tropical-cyclone window runs from `2023-02-06T06:00:00` to `2023-03-12T00:00:00`, so `catalog_duration = 33.75 d`, `duration_gap = 36 - 33.75 = 2.25 d`, and `catalog/WMO = 0.938`. The catalog is `Red` with peak wind `250.0 km/h`. The Malawi flood starts `34.0 h` after the catalog cyclone end.

Hourly point weather gives `393.6 mm` rainfall across `912 h`, with `420` wet hours, `420/912 = 0.461`, `36` wet days, and a `62 h` longest wet run. The wettest windows are `112.4 mm` in 72 h and `146.7 mm` in 168 h, giving shares `0.286` and `0.373`. Daily point rainfall totals `482.85 mm`, with `7` days at or above `25 mm` and `2` days at or above `50 mm`.

The local gust is `65.9 km/h`, so `65.9 / 250.0 = 0.264`. The pressure range is `1016.7 - 1005.3 = 11.4 hPa`. Gridded rainfall ratios are `389.398 / 115.284 = 3.378` for GPM and `328.847 / 120.942 = 2.719` for CHIRPS; the CHIRPS/GPM mean ratio is `120.942 / 115.284 = 1.049`.

# Ranking Logic

The rule is `score = max(0, 100 * (1 - fractional_change_needed))`.

- `rainfall_duration_shortened`: smaller of `21/420 = 0.050` wet-hour removal and `7/36 = 0.194` wet-day removal, score `95.000`.
- `rainfall_load_reduced`: smaller of `(393.6 - 300) / 393.6 = 0.237805` and `(482.85 - 300) / 482.85 = 0.379`, score `76.220`.
- `gridded_rainfall_context_weakened`: smaller of `(3.378 - 2) / 3.378 = 0.408` and `(2.719 - 2) / 2.719 = 0.264451`, score `73.555`.
- `flood_lag_removed`: `(72 - 34) / 72 = 0.527778`, score `47.222`.
- `pressure_signal_weakened`: `(11.4 - 5) / 11.4 = 0.561404`, score `43.860`.
- `peak_wind_reinterpreted_as_primary`: `0.50 / (65.9 / 250.0) - 1 = 0.896813`, score `10.319`.

# Reasoning Path

The most sensitive perturbation is shortening rainfall duration, because only `21` of `420` wet hours need to be removed before the wet-hour persistence test drops below `400`. Rainfall load and gridded rainfall context are next: both still have meaningful margins, but not huge ones. Removing the flood lag or pressure signal requires larger changes. A peak-wind reinterpretation is the rejected alternative because the local gust-to-catalog ratio is only `0.264`, far below the `0.50` competing-diagnosis threshold.

# Scoring Rubric

- 3 points: Final ranking JSON. Full credit requires all requested compact JSON fields, `rainfall_duration_shortened` as the top sensitivity, and all six ranked scenarios. Partial credit: 1-2 points if the structure is mostly present but the top scenario or one required ranking field is missing.
- 3 points: Duration, catalog, and lag evidence. Full credit requires the `36 d` WMO anchor, `33.75 d` catalog duration, `2.25 d` duration gap, `Red` catalog level, `250.0 km/h` catalog wind, and `34.0 h` Malawi flood lag. Partial credit: 1-2 points for mostly correct timing evidence with one missing catalog, report, or lag value.
- 4 points: Hourly and daily rainfall calculations. Full credit requires `393.6 mm`, `420/912`, `36` wet days, `62 h`, `112.4/393.6 = 0.286`, `146.7/393.6 = 0.373`, `482.85 mm`, and daily exceedance counts of `7` and `2`. Partial credit: 2-3 points for correct rainfall totals with minor rounding errors; 1 point if only one rainfall timescale is used.
- 3 points: Wind, pressure, and gridded context. Full credit requires `65.9 km/h`, `0.264`, `1005.3` to `1016.7 hPa`, `11.4 hPa`, GPM ratio `3.378`, CHIRPS ratio `2.719`, and CHIRPS/GPM mean ratio `1.049`. Partial credit: 1-2 points if either the wind-pressure or gridded-rainfall calculations are correct but the other family is missing.
- 5 points: Scenario sensitivity scoring. Full credit requires the threshold-crossing formula and scores `95.000`, `76.220`, `73.555`, `47.222`, `43.860`, and `10.319` in the ranked order. Partial credit: 3-4 points if the formula is right but one or two scores are rounded or ordered incorrectly; 1-2 points for a qualitative ranking without reproducible margins.
- 2 points: Interpretation and rejected alternative. Full credit explains that rainfall-duration shortening is most sensitive, while peak-wind reinterpretation is rejected because the local gust/catalog ratio would need an about `89.7%` increase to reach `0.50`. Partial credit: 1 point if the interpretation is broadly consistent but omits either the top-sensitivity margin or the rejected wind margin.
