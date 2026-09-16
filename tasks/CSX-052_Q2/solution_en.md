# Final Answer

```json
{
  "event_window": "2023-12-03 to 2023-12-06",
  "runoff_equivalent_mm": 110.0,
  "report_to_max_gridded_ratio": 19.0,
  "highway_per_waterway": 5.44,
  "critical_per_million": 78.1,
  "wet_surface_flag": true,
  "score": 5,
  "final_label": "rainfall_runoff_exposure_consistent"
}
```

The ledger rejects a wind-only or image-only explanation because the rainfall lower bound, runoff-equivalent depth, transport-drainage coupling, receptor density, and wet-surface signal all pass their thresholds.

# Key Computations

- Event window: 2023-12-03 to 2023-12-06.
- Reported rainfall lower bound: 200 mm.
- Runoff equivalent: `200 mm * 0.55 = 110.0 mm`.
- Largest gridded event-precipitation maximum: `max(10.5489, 4.4850, 9.7155) = 10.5489 mm`.
- Report-to-gridded maximum ratio: `200 / 10.5489 = 18.96`, rounded to `19.0`.
- Highway-per-waterway ratio: `598 / 110 = 5.436`, rounded to `5.44`.
- Critical amenities per million people: `263 / (3,368,009.160 / 1,000,000) = 78.087`, rounded to `78.1`.
- Wet-surface flag: `true` because mean radar backscatter change is `-0.809 dB <= -0.5 dB` and annual embedding mean change is `0.022 <= 0.05`.
- Score: all five tests pass: rainfall threshold, runoff threshold, highway-waterway ratio, critical-amenity density, and wet-surface flag.

The population and mapped receptor values are spatially masked package-derived statistics. Their internal absolute coordinates, place names, and georeferencing metadata are not used to judge event-location validity in this task.

# Reasoning Path

1. The event passes the rainfall trigger because the report-level lower bound is 200 mm.
2. Applying the specified runoff coefficient gives 110.0 mm, which exceeds the 100 mm runoff-equivalent threshold.
3. The report-to-gridded maximum ratio is about 19.0, so the rainfall trigger should be carried forward in the ledger rather than replaced by a much smaller gridded maximum.
4. The mapped highway-to-waterway ratio of 5.44 exceeds the 5.0 threshold, indicating that transport corridors and drainage routes are tightly coupled in the receptor ledger.
5. The critical-amenity density of 78.1 per million people exceeds the 50 per million threshold, so the receptor side of the ledger is not sparse.
6. The radar and embedding changes satisfy the wet-surface rule, adding the fifth point.
7. With `score = 5`, the deterministic label is `rainfall_runoff_exposure_consistent`.

# Computed Interpretation

The computed ledger supports a rainfall-runoff exposure diagnosis for Cyclone Michaung: a 200 mm rainfall lower bound yields a 110 mm runoff-equivalent depth, and the exposure ratios show why floodwater interacting with roads, waterways, and key amenities is the stronger event-specific interpretation.

# Scoring Rubric

- 4 points: Final ledger and label. Full credit gives the required compact JSON fields with `score = 5` and `final_label = "rainfall_runoff_exposure_consistent"`. Partial credit: 2-3 points for the correct label with one or two missing fields; 1 point for a plausible label without the ledger.
- 4 points: Rainfall and runoff arithmetic. Full credit uses 200 mm as the rainfall lower bound and computes `200 * 0.55 = 110.0 mm`. Partial credit: 2-3 points for the right formula with rounding or unit mistakes; 1 point for using rainfall qualitatively without the runoff calculation.
- 3 points: Gridded-maximum ratio. Full credit identifies 10.5489 mm as the largest gridded event-precipitation maximum and computes a report-to-maximum ratio of about 19.0. Partial credit: 2 points for using the right ratio idea with the wrong gridded maximum; 1 point for listing gridded rainfall numbers without the ratio.
- 4 points: Exposure ratios. Full credit computes `598 / 110 = 5.44` and `263 / 3.368009 = 78.1 per million people`, with correct units or field names, treating masked OSM/WorldPop derived statistics as package-authoritative rather than judging them by internal coordinates or place names. Partial credit: 2-3 points for one correct ratio; 1 point for listing receptor counts without derived ratios.
- 3 points: Wet-surface flag and score arithmetic. Full credit applies both thresholds, `-0.809 <= -0.5` and `0.022 <= 0.05`, sets `wet_surface_flag` to true, and counts all five passing tests. Partial credit: 2 points for the right flag but incomplete score logic; 1 point for using only one remote-sensing condition.
- 2 points: Rejected competing explanation and concise interpretation. Full credit explicitly rejects wind-only or image-only explanation as weaker than the computed rainfall-runoff exposure ledger. Partial credit: 1 point for a correct but generic interpretation that does not name the rejected explanation.
