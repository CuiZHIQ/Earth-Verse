# Final Answer

```json
{
  "gate_metrics": {
    "shallow_shaking_gate": {
      "values": {
        "mainshock_magnitude": 7.8,
        "mainshock_depth_km": 8.22,
        "kathmandu_ems98_midpoint": 6.5,
        "kathmandu_ems98_upper": 7
      },
      "threshold_result": "pass"
    },
    "strong_sequence_gate": {
      "values": {
        "usgs_nepal_m6plus_count": 4,
        "usgs_later_nepal_m6plus_count": 3,
        "catalog_count_scope": "Package ComCat query count; the report-cited May 12 M7.3 aftershock is recorded separately below.",
        "later_m6plus_ratio": 0.75,
        "reported_aftershock_magnitude": 7.3,
        "reported_aftershock_lag_days": 17,
        "reported_aftershock_source": "data/event_reports/event_reports_001_Locked_anchor_USGS.html"
      },
      "threshold_result": "pass"
    },
    "collapse_exposure_gate": {
      "values": {
        "houses_destroyed": 500717,
        "houses_damaged": 269190,
        "destroyed_to_damaged_house_ratio": 1.86,
        "destroyed_share": 0.65,
        "population_sum_2015": 3193357.78,
        "people_per_destroyed_house": 6.38,
        "low_quality_building_pct": 98.0
      },
      "threshold_result": "pass"
    },
    "secondary_ground_failure_gate": {
      "values": {
        "secondary_ground_failure_signal_count": 4,
        "landslides_second_to_structural_collapses": true,
        "signals": ["landslides", "dammed_river_lake", "liquefaction", "progressive_slope_failure"]
      },
      "threshold_result": "pass"
    },
    "surface_change_not_primary_gate": {
      "values": {
        "radar_pre_count": 2,
        "radar_post_count": 0,
        "radar_post_pre_ratio": 0.0,
        "radar_pair_available": false,
        "surface_change_inference": "Sentinel-1 has no usable post-event pair here, so it does not prove absence of change; the non-primary gate relies on the report's no-surface-rupture statement and lack of image-led support.",
        "no_surface_rupture_reported": true
      },
      "threshold_result": "pass"
    },
    "rainfall_not_primary_gate": {
      "values": {
        "gpm_precip_max_mm": 28.34,
        "chirps_precip_max_mm": 26.02,
        "larger_precip_max_mm": 28.34,
        "gpm_to_chirps_mean_precip_ratio": 4.16
      },
      "threshold_result": "pass"
    }
  },
  "final_label": "collapse_led_shallow_earthquake_sequence",
  "rejected_leads": [
    "landslide_led_primary",
    "surface_change_or_image_led_primary",
    "rainfall_led_primary"
  ],
  "interpretation": "The numbers prove a shallow, strong-shaking earthquake sequence whose dominant severity is collapse and exposure, with ground failures retained as secondary coupled hazards."
}
```

# Computation Path

The shallow-shaking gate passes because the mainshock is M7.8 at 8.22 km depth and the Kathmandu Valley EMS-98 range is 6-7, giving midpoint `(6 + 7) / 2 = 6.5`. Those values meet `M >= 7.5`, `depth <= 15 km`, and `EMS midpoint >= 6.0`.

The sequence gate passes because the package ComCat query has 4 Nepal M6+ events and 3 occur after the mainshock, so `3 / 4 = 0.75`. The report separately supplies the May 12 largest aftershock as M7.3 at 17 days after the mainshock, meeting the `>=7.0` and `<=20 days` thresholds; the catalog count is not treated as a complete aftershock inventory.

The collapse/exposure gate passes from the housing and exposure arithmetic: `500717 / 269190 = 1.86`, and `500717 / (500717 + 269190) = 0.65`. The population-normalized check is `3193357.78 / 500717 = 6.38 people per destroyed house`, and the low-quality-building percentage is 98.0, above the 95 percent threshold.

The secondary ground-failure gate passes, but only as secondary context: all four counted signals are present, while landslides are ranked second to structural collapses. The surface-change gate supports the same ordering because Sentinel-1 has 2 pre-event scenes and 0 post-event scenes, so no usable paired radar-change test is available; this does not prove absence of surface change. The non-primary decision instead rests on the report's no-surface-rupture statement plus lack of image-led support. The rainfall gate rejects a rainfall-led result because the larger local event-window precipitation maximum is only 28.34 mm, below the 50 mm threshold; the GPM/CHIRPS mean ratio is `13.143 / 3.158 = 4.16`.

Because all six gates pass, the computed label is `collapse_led_shallow_earthquake_sequence`. The rejected leads follow directly: a landslide-led result fails the reported rank ordering, an image-led or surface-rupture result lacks paired Sentinel-1 support and conflicts with the no-surface-rupture report, and a rainfall-led result fails the precipitation threshold.

# Scoring Rubric (20 points)

- 4 points: Returns the requested JSON structure with all six named gates, per-gate values, pass/fail results, final label, rejected leads, and one concise interpretation.
- 5 points: Computes the key numeric values correctly within tolerance: M7.8, 8.22 km, EMS midpoint 6.5, package-catalog later M6+ ratio 0.75, separately reported M7.3 aftershock, 17-day lag, destroyed/damaged ratio 1.86, destroyed share 0.65, people per destroyed house 6.38, surface post/pre ratio 0.0 as an availability indicator, larger precipitation maximum 28.34 mm, and GPM/CHIRPS mean ratio 4.16.
- 4 points: Applies all threshold gates correctly and derives `collapse_led_shallow_earthquake_sequence` only after all six gates pass.
- 3 points: Explains the candidate-by-candidate proof logic, especially why ground failures pass as coupled secondary hazards rather than the lead result, and avoids treating missing Sentinel-1 post scenes as proof of no surface change.
- 2 points: Rejects at least two tempting lead interpretations using computed gates rather than broad prose: landslide-led, image/surface-change-led, or rainfall-led. Image-led rejection must be based on no surface rupture plus absent paired image support, not on a claim of observed no-change.
- 1 point: Gives a concise mechanism label that is consistent with the calculations.
- 1 point: Keeps the answer bounded to the numeric proof and requested computed fields, including the catalog/report sequence distinction and Sentinel-1 availability limit.

Accept small rounding differences: +/-0.1 for magnitudes, +/-0.1 km for depth, +/-0.02 for ratios and shares, +/-0.1 mm for precipitation maxima, and +/-0.01 for the GPM/CHIRPS mean ratio.
