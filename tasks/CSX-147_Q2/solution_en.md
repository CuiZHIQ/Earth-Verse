# Correct Answer

```json
{
  "answer": "rainfall_to_flood_timing",
  "target_family": "bangladesh_storm_flood_process_chain_control_ranking",
  "computed_values": {
    "event_days": 14,
    "storm_sequence_days": 11,
    "storm_to_flood_lag_days": 7,
    "anchor_to_flood_lag_days": 4,
    "gpm_max_mm": 119.46,
    "chirps_max_mm": 107.61,
    "era5_max_mm": 63.55,
    "gpm_ratio": 7.86,
    "chirps_ratio": 2.54,
    "grid_spread_frac": 0.856,
    "reported_displaced": 500000,
    "gdacs_bangladesh_flood_records": 0
  },
  "control_point_scores": {
    "rainfall_to_flood_timing": 98.0,
    "multi_day_rainfall_accumulation": 91.0,
    "river_or_storage_response": 85.0,
    "single_peak_rainfall_only": 43.0,
    "reported_damage_only": 40.0,
    "wind_or_storm_label_only": 10.0
  },
  "ranked_control_points": [
    "rainfall_to_flood_timing",
    "multi_day_rainfall_accumulation",
    "river_or_storage_response",
    "single_peak_rainfall_only",
    "reported_damage_only",
    "wind_or_storm_label_only"
  ],
  "top_control_point": "rainfall_to_flood_timing",
  "rejected_control_point": "wind_or_storm_label_only",
  "reasoning_path": [
    "lag_controls_classification",
    "grids_show_multiday_rain",
    "khasi_jamuna_route_runoff",
    "peak_damage_wind_decoys"
  ]
}
```

# Key Computations

Local records read by `compute_gt.py` include the CSX-147 event metadata, locked event anchor, NASA flood follow-up text, local GDACS catalog context, and ERA5-Land, GPM, and CHIRPS gridded precipitation summaries.

- Event anchor: 2004-04-09 through 2004-04-22, so the inclusive event window is 14 days.
- Report timing: the severe-thunderstorm sequence began on 2004-04-09 and lasted through 2004-04-19, giving 11 storm-sequence days.
- Flood timing: the flood observation date is 2004-04-26. The lag is 7 days from 2004-04-19 to 2004-04-26, and 4 days from the anchor end, 2004-04-22, to 2004-04-26.
- Report process flags: extensive flooding is present, runoff from the Khasi Hills is present, Jamuna River language is present, and about 500,000 displaced people in Bangladesh are present.
- Gridded rainfall: GPM max 119.46 mm, mean 15.20 mm, max-to-mean ratio 7.86; CHIRPS max 107.61 mm, mean 42.38 mm, ratio 2.54; ERA5-Land max 63.55 mm, mean 37.69 mm, ratio 1.69.
- Gridded spread: the three gridded means have a consensus mean of 31.76 mm and a spread fraction of 0.856, consistent with uneven convective rainfall.
- Local catalog context: the checked GDACS context has two features and no Bangladesh flood record, so it does not override the report and gridded hazard chain.

# Ranking Logic

The score is a diagnostic control score. It measures how strongly each candidate governs the classification from severe-storm rainfall to later floodplain flooding.

`rainfall_to_flood_timing` ranks first because the report gives a dated storm sequence followed by a later flood observation. The 7-day storm-end to flood lag and 4-day anchor-end to flood lag are exactly the evidence needed to separate a lagged rainfall-runoff flood from a same-day wind-only storm label.

`multi_day_rainfall_accumulation` ranks second because the gridded products show locally heavy event rainfall above 100 mm in GPM and CHIRPS, with high max-to-mean ratios. The spread across gridded products also shows why a single peak or single product is a weak representation of an uneven convective rainfall field.

`river_or_storage_response` ranks third because the report links flooding to Khasi Hills runoff and the Jamuna River, but the package does not include river-gauge or storage time series. `single_peak_rainfall_only` is a weak physical decoy because the flood observation is lagged and the gridded field is spatially uneven. `reported_damage_only` confirms inundation but is a downstream consequence, not a process control. `wind_or_storm_label_only` is rejected because a storm label alone does not explain the later floodplain classification.

# Reasoning Path

The process chain is: storm sequence timing -> lagged flood observation -> locally heavy and spatially uneven gridded rainfall -> runoff or river language -> flood impacts. The top control point is the timing bridge from rainfall to flood. Multi-day rainfall accumulation supplies the water input, and river/runoff response supplies the routing interpretation. Single peak rainfall, damage-only reasoning, and wind/storm-label-only reasoning are decoys.

# 20-Point Rubric

- 2 points: Required compact JSON and task family. Full credit returns JSON with answer, target_family, computed_values, control_point_scores, ranked_control_points, top_control_point, rejected_control_point, and reasoning_path. Partial credit: 1 point for mostly valid JSON with one missing top-level field.
- 3 points: Package evidence discovery. Full credit uses only local CSX-147 event anchor, flood-timing report text, gridded precipitation summaries, report process flags, and catalog context, without point weather, OSM, AOI, population, exposure, or web search evidence. Partial credit: 1-2 points if several required local evidence families are used but one major family is missing.
- 4 points: Timing and lag calculations. Full credit computes the 14-day anchor window, 11-day severe-thunderstorm sequence, 7-day storm-end to flood-observation lag, and 4-day anchor-end to flood-observation lag. Partial credit: 2-3 points for correct dates with one missing lag; at most 1 point for date mentions without arithmetic.
- 4 points: Rainfall diagnostics. Full credit computes the gridded precipitation maxima and ratios, including GPM 119.46 mm and 7.86, CHIRPS 107.61 mm and 2.54, ERA5-Land 63.55 mm, plus gridded spread and consensus ratios. Partial credit: 2-3 points for correct gridded rainfall with incomplete spread diagnostics; at most 1 point for uncomputed qualitative rainfall claims.
- 3 points: Process-chain interpretation. Full credit uses report flags for extensive flooding, Khasi Hills runoff, Jamuna River language, and Bangladesh displacement to distinguish a lagged rainfall-runoff chain from wind-only, single-peak, or impact-only readings. Partial credit: 1-2 points if report flags are mentioned but not tied to process-chain control.
- 3 points: Control-point ranking. Full credit returns the ranking shown above. Partial credit: 1-2 points if the top control point is right but middle or low-ranking decoys are misplaced.
- 1 point: Rejection and non-response discipline. Full credit identifies `wind_or_storm_label_only` as the rejected control candidate and keeps the answer diagnostic rather than response-priority advice. No partial credit.
