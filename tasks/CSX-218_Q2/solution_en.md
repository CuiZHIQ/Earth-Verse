# Final Answer

The computed label is `source_plus_transport_smoke_persistence`.

```json
{
  "answer": "source_plus_transport_smoke_persistence",
  "window_days": 1,
  "source_smoke": {
    "fire_hits": 2,
    "source_flags": 3,
    "transport_flags": 3,
    "transport_source_ratio": 1.0,
    "smoke_family_hits": 4,
    "aod_pm_hits": 0
  },
  "clearing": {
    "local_precip_mm": 1.04,
    "low_precip_days_le2mm": 5,
    "regional_mean_mm": 5.34,
    "regional_max_mean_ratio": 15.24,
    "era5_wind_ms": 0.74,
    "local_wind_kmh": 8.2,
    "pass_count": 4
  },
  "satellite": {
    "mean_abs_rgb_delta": 82.66,
    "normalized_rgb_delta": 0.324,
    "smoke_delta_pct_points": 0.53
  },
  "persistence_score": 11
}
```

# Key Computations

The locked event window runs from 2004-08-28 to 2004-08-28, so the inclusive duration is 1 day.

The article-title-plus-body text gives 2 exact `fire` or `fires` hits. The source ledger has 3 present indicators: seasonal burning, charcoal production, and satellite-detected fires. The transport ledger also has 3 present indicators: high-pressure persistence, counterclockwise recirculation, and Atlantic haze. Therefore `transport_source_ratio = 3 / 3 = 1.0`. Smoke-family terms sum to `smoke + smog + haze = 2 + 1 + 1 = 4`, while AOD/PM-family terms sum to 0.

For the clearing ledger, event-day local precipitation is `(1.10 + 0.97) / 2 = 1.04 mm`, below the 2 mm threshold. Five of the 15 local-context days have mean precipitation at or below 2 mm. The regional mean precipitation is `(3.14 + 5.64 + 7.25) / 3 = 5.34 mm`. The largest regional precipitation max/mean ratio is `85.95 / 5.64 = 15.24`. The mean 10 m vector wind is `sqrt(0.411^2 + -0.619^2) = 0.74 m/s`, and the local maximum wind is 8.2 km/h. All four clearing and weak-wind tests pass, so `pass_count = 4`.

The pre-event and event true-color image comparison gives a mean absolute RGB change of 82.66. Thus `normalized_rgb_delta = 82.66 / 255 = 0.324`. Smoke-like pixels change from 0.5429 to 0.5482, a +0.53 percentage-point difference. The satellite-change flag passes because 0.324 is at least 0.05.

# Reasoning Path

The persistence score combines the source flags, transport flags, clearing-ledger pass count, and satellite-change pass:

`persistence_score = 3 + 3 + 4 + 1 = 11`.

The final label rule requires a score of at least 9, at least 4 smoke-family hits, and a transport/source ratio of at least 1. The computed values are 11, 4, and 1.0, so the label is `source_plus_transport_smoke_persistence`.

# Computed Interpretation

The ledger favors the source-plus-transport persistence label because source indicators and transport indicators are both complete, while the clearing and weak-wind tests do not point to rapid removal. A source-only label fails the ratio check because transport indicators are as numerous as source indicators. A broad rainfall-clearing label fails because local precipitation is 1.04 mm and the regional mean is 5.34 mm. A point-wind-only label fails because local wind is weak and the transport ledger is complete.

# Scoring Rubric

Total: 20 points.

- 3 points: Requested JSON schema. partial_credit: Award 1 point for the six requested top-level keys, 1 point for preserving the nested numeric fields, and 1 point for using the computed label field without extra keys.
- 4 points: Source and smoke counts. partial_credit: Award 1 point for `window_days = 1`, 1 point for `fire_hits = 2` and `source_flags = 3`, 1 point for `transport_flags = 3` and `transport_source_ratio = 1.0`, and 1 point for `smoke_family_hits = 4` plus `aod_pm_hits = 0`.
- 5 points: Clearing and weak-wind tests. partial_credit: Award 1 point each for local precipitation 1.04 mm, low-precipitation days = 5, regional mean precipitation 5.34 mm with max/mean ratio 15.24, wind values 0.74 m/s and 8.2 km/h, and `pass_count = 4`.
- 3 points: Satellite metrics. partial_credit: Award 1 point each for mean absolute RGB delta 82.66, normalized RGB delta 0.324, and smoke-like delta +0.53 percentage points.
- 3 points: Score and threshold. partial_credit: Award 1 point for the correct score formula, 1 point for `persistence_score = 11`, and 1 point for the final label `source_plus_transport_smoke_persistence`.
- 1 point: Alternative-label checks. partial_credit: Award the point when at least two rejected alternatives are tied to the numeric ledger; otherwise award 0.
- 1 point: Concise interpretation. partial_credit: Award the point when the final text stays within the requested data-driven diagnosis and does not add external impact or action statements.
