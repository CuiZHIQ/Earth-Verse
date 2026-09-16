# Storm Alexa Snow-Phase and Depth-Scale Ledger

A hydrometeorology team is checking a proposed summary of the December 2013 Middle East winter storm Alexa: that a single point snowfall total can stand in for the reported highland snow depths around Jerusalem and Amman.

Reconstruct the event ledger for 10-13 December 2013 using the technical record. Test the point snow phase, the reported-depth scale gap, and whether the gridded precipitation summaries have a large magnitude spread.

Use these decision rules:

- `wet_snow_point` is true when `snow_hours > 0`, `freeze_hours == 0`, and `min_temp_c > 0`.
- `highland_depth_gap` is true when the smallest reported-depth-to-point-snow ratio is at least `10`.
- `point_total_as_highland_depth` is true only when the smallest reported-depth-to-point-snow ratio is at most `1.25`.
- `sustained_subfreezing_point` is true when `freeze_hours >= 12`.
- `strong_precip_spread` is true when the largest-to-smallest gridded mean precipitation ratio is at least `5`, or the largest-to-middle ratio is at least `3`.

Return one compact JSON object:

```json
{
  "target_family": "snow_phase_depth_precip_ledger",
  "answer_label": "<concise conclusion>",
  "point_phase": {
    "snow_cm": 0.0,
    "snow_hours": 0,
    "freeze_hours": 0,
    "min_temp_c": 0.0,
    "hours_le_5c": 0,
    "max_gust_kmh": 0.0,
    "min_wind_chill_c": 0.0
  },
  "reported_depth_ratios": {
    "jerusalem_min_to_point": 0.0,
    "jerusalem_max_to_point": 0.0,
    "amman_to_point": 0.0
  },
  "gridded_precip": {
    "largest_mean_mm": 0.0,
    "middle_mean_mm": 0.0,
    "smallest_mean_mm": 0.0,
    "largest_to_smallest_ratio": 0.0,
    "largest_to_middle_ratio": 0.0
  },
  "logic_flags": {
    "wet_snow_point": "<boolean>",
    "highland_depth_gap": "<boolean>",
    "point_total_as_highland_depth": "<boolean>",
    "sustained_subfreezing_point": "<boolean>",
    "strong_precip_spread": "<boolean>"
  },
  "computed_interpretation": "<one sentence tying the numeric tests together>"
}
```
