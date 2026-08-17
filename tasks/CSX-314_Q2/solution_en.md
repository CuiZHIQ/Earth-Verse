# Correct Answer

```json
{
  "answer": "mass_movement_source_supported",
  "max_precip_mm": 0.0013,
  "dry_source_count": 5,
  "prepost_obs": 213,
  "radar_abs_db": 15.7049,
  "optical_abs": 0.9206,
  "annual_span_yr": 1,
  "point_in_bbox": false
}
```

# Computation

The event-day precipitation summaries are `0.0`, `0.0`, `0.0012934458`, `0`, and `0` mm. Their maximum is `0.0013 mm` after rounding, and all five are `<= 0.01 mm`.

The paired terrain-change observation total is `(27 + 24) + (87 + 75) = 213`. The radar absolute extreme is `max(abs(-15.7049332376), abs(14.9806619001)) = 15.7049 dB`. The optical absolute extreme is `max(abs(-0.7018519859), abs(0.9205501171)) = 0.9206`.

The annual embedding span is `2021 - 2020 = 1` year. The point-weather coordinate `(78.668, 22.351)` is outside the compact polygon bounding box with longitude range `77.4739..78.4739` and latitude range `29.7837..30.7837`, so `point_in_bbox` is `false`.

The rainfall threshold is not met, while the dry-weather, terrain-change, annual-scale, and coordinate tests all satisfy the ledger rule. The resulting label is `mass_movement_source_supported`.

# Scoring Rubric

- 3 points: Returns the required eight-field JSON object with the correct field names and value types.
- 4 points: Computes the precipitation ledger correctly, including `max_precip_mm = 0.0013` within `0.0001 mm` and `dry_source_count = 5`.
- 4 points: Computes the terrain-change ledger correctly, including `prepost_obs = 213`, `radar_abs_db = 15.7049` within `0.001 dB`, and `optical_abs = 0.9206` within `0.0001`.
- 3 points: Computes the annual-span and coordinate tests correctly, including `annual_span_yr = 1` and `point_in_bbox = false`.
- 4 points: Applies the stated thresholds correctly and returns `mass_movement_source_supported`.
- 2 points: Shows enough formula work or intermediate values for the numeric result to be reproducible, without converting annual, optical, or point-sample values into stronger conclusions than the ledger supports.
