# Gorkha Earthquake Numeric Consistency Proof

A technical review team is checking whether the 2015 Gorkha earthquake sequence is numerically consistent with a collapse-led shallow earthquake sequence. Build a calculation-first proof using local event data for shaking, later strong shocks, collapse/exposure, secondary ground failure, surface-change constraints, and rainfall rejection.

Compute these gates:

- `shallow_shaking_gate`: report mainshock magnitude, mainshock depth, Kathmandu EMS-98 midpoint, and Kathmandu EMS-98 upper value. It passes when `magnitude >= 7.5`, `depth_km <= 15`, and `ems_midpoint >= 6.0`.
- `strong_sequence_gate`: report the package-catalog Nepal M6+ count, later package-catalog Nepal M6+ count, `later_m6plus_ratio = later_count / total_count`, the separately reported largest aftershock magnitude, and the reported aftershock lag in days. It passes when `later_m6plus_ratio >= 0.50`, `reported_aftershock_magnitude >= 7.0`, and `reported_aftershock_lag_days <= 20`.
- `collapse_exposure_gate`: compute `destroyed_to_damaged_house_ratio`, `destroyed_share = destroyed / (destroyed + damaged)`, people per destroyed house, and low-quality-building percentage. It passes when `destroyed_to_damaged_house_ratio >= 1.0`, `destroyed_share >= 0.60`, and `low_quality_building_pct >= 95`.
- `secondary_ground_failure_gate`: count the secondary ground-failure signals among landslides, dammed-river lake, liquefaction, and progressive slope failure. It passes as a secondary-hazard gate when the count is at least 3 and landslides are ranked second to structural collapses.
- `surface_change_not_primary_gate`: compute `radar_post_pre_ratio = post_count / pre_count`, report whether a paired Sentinel-1 pre/post change test is available, and report whether surface rupture is absent in the text record. It passes when the text record reports no surface rupture and the Sentinel-1 file does not establish an image-led primary explanation; do not interpret zero post-event scenes as proof of no surface change.
- `rainfall_not_primary_gate`: compute the larger of the GPM and CHIRPS event precipitation maxima and the GPM/CHIRPS mean precipitation ratio. It passes when the larger maximum is below 50 mm.

Final label rule: return `collapse_led_shallow_earthquake_sequence` only if all six gates pass; otherwise return `not_proven_by_these_gates`.

Return JSON:

```json
{
  "gate_metrics": {
    "shallow_shaking_gate": {
      "values": {},
      "threshold_result": "pass|fail"
    },
    "strong_sequence_gate": {
      "values": {},
      "threshold_result": "pass|fail"
    },
    "collapse_exposure_gate": {
      "values": {},
      "threshold_result": "pass|fail"
    },
    "secondary_ground_failure_gate": {
      "values": {},
      "threshold_result": "pass|fail"
    },
    "surface_change_not_primary_gate": {
      "values": {},
      "threshold_result": "pass|fail"
    },
    "rainfall_not_primary_gate": {
      "values": {},
      "threshold_result": "pass|fail"
    }
  },
  "final_label": "",
  "rejected_leads": [],
  "interpretation": ""
}
```
