# Regional Heat Source Arbitration

A benchmark reviewer suspects a model solved the 2015 India-Pakistan heat wave task by using a full-window point weather file as the event's regional heat-severity source. Audit that source choice using only package-local CSX-004 evidence. Do not use web search, hidden answers, or invented values.

Your job is to decide which package file should be the heat-severity basis for a regional/AOI maximum-temperature answer, quantify what changes if the point file is used instead, and reject package files that are wrong-variable context rather than usable heat-severity evidence.

Return only a compact JSON object with this exact schema. Use package-relative source paths.

```json
{
  "answer_type": "expert_source_arbitration",
  "decision": "<select_regional_aoi_heat_not_point_series|other>",
  "selected_source": {
    "path": "<package-relative path>",
    "role": "<short role>",
    "dataset": "<dataset>",
    "coverage_days_inclusive": 0
  },
  "rejected_point_source": {
    "path": "<package-relative path>",
    "role": "<short role>",
    "point_inside_aoi": false,
    "point_elevation_m": 0.0,
    "point_coverage_days_inclusive": 0,
    "rejection_reason": "<short reason>"
  },
  "spatial_check": {
    "aoi_path": "<package-relative path>",
    "point_lat": 0.0,
    "point_lon": 0.0,
    "aoi_bounds": {
      "min_lon": 0.0,
      "min_lat": 0.0,
      "max_lon": 0.0,
      "max_lat": 0.0
    },
    "distance_point_to_aoi_centroid_km": 0.0
  },
  "numeric_consequence": {
    "selected_tmax_max_c": 0.0,
    "selected_tmax_mean_c": 0.0,
    "wrong_point_apparent_max_c": 0.0,
    "wrong_point_air_tmax_max_c": 0.0,
    "selected_minus_point_apparent_c": 0.0,
    "selected_minus_point_air_tmax_c": 0.0
  },
  "event_window_check": {
    "anchor_path": "<package-relative path>",
    "official_window_days_inclusive": 0,
    "selected_hazard_window_days_inclusive": 0,
    "temporal_arbitration_note": "<short note>"
  },
  "wrong_variable_rejections": {
    "<package-relative path>": "<short reason>"
  },
  "minimal_evidence_set": [
    "<package-relative path>"
  ],
  "ruling": "<not_interchangeable|consistent|insufficient_overlap>",
  "reference_trace": [
    "<short reproducible step>"
  ]
}
```
