# Final Answer

Correct answer: `persistent_remnant_cyclone_rainfall_supported`.

```json
{
  "target_family": "doksuri_rainfall_phase_segmentation",
  "phases": [
    {
      "phase": "sustained_wet_hour_rainfall",
      "time_window": "120-hour event window",
      "dominant_process": "persistent remnant-cyclone rainfall",
      "computed_value": {"window_hours": 120, "wet_hour_fraction": 0.7, "longest_wet_run_share": 0.929, "peak_hour_share": 0.0889, "wet_hour_mean_mm": 2.344, "window_mean_mm_per_hour": 1.641},
      "transition_basis": "A long wet run and low peak-hour share show persistence rather than a single-hour burst."
    },
    {
      "phase": "three_day_concentration",
      "time_window": "wettest three daily totals",
      "dominant_process": "multi-day rainfall concentration",
      "computed_value": {"max_3day_share": 0.926, "peak_day_share": 0.441, "daily_to_hourly_total_ratio": 1.12},
      "transition_basis": "Most daily rainfall sits in a three-day block while the peak day remains below half of the total."
    },
    {
      "phase": "report_calibrated_extreme_rainfall",
      "time_window": "83-hour reported extreme-rainfall anchor",
      "dominant_process": "report-scale rainfall alignment",
      "computed_value": {"report_avg_intensity_mm_per_hour": 3.988, "report_avg_to_hourly_total_ratio": 1.681, "reservoir_to_report_avg_ratio": 2.25, "single_point_to_report_avg_ratio": 3.097},
      "transition_basis": "Report-average intensity and reported maxima align with extreme rainfall rather than weak background rain."
    },
    {
      "phase": "wind_dominance_rejection",
      "time_window": "event wind background",
      "dominant_process": "rainfall-dominant remnant timeline",
      "computed_value": {"peak_wind_ms": 10.69, "peak_wind_kmh": 38.5, "wind_energy_proxy": 114.3},
      "transition_basis": "Peak wind is below the wind-dominance cutoff, so wind cannot replace rainfall as the timeline control."
    }
  ],
  "phase_checks": [
    {"row_id": "rainfall_persistence", "computed_value": {"window_hours": 120, "wet_hour_fraction": 0.7, "longest_wet_run_share": 0.929, "peak_hour_share": 0.0889, "wet_hour_mean_mm": 2.344, "window_mean_mm_per_hour": 1.641}, "result": "pass_persistent_multiday_rainfall"},
    {"row_id": "three_day_concentration", "computed_value": {"max_3day_share": 0.926, "peak_day_share": 0.441, "daily_to_hourly_total_ratio": 1.12}, "result": "pass_multiday_concentrated_rainfall"},
    {"row_id": "report_intensity_alignment", "computed_value": {"report_avg_intensity_mm_per_hour": 3.988, "report_avg_to_hourly_total_ratio": 1.681, "reservoir_to_report_avg_ratio": 2.25, "single_point_to_report_avg_ratio": 3.097}, "result": "pass_report_extreme_rainfall_alignment"},
    {"row_id": "wind_rejection", "computed_value": {"peak_wind_ms": 10.69, "peak_wind_kmh": 38.5, "wind_energy_proxy": 114.3}, "result": "reject_wind_dominant_calibration"}
  ],
  "final_label": "persistent_remnant_cyclone_rainfall_supported"
}
```

# Key Computations

The hourly rainfall series has `window_hours = 120`, `hourly_total_mm = 196.9`, `wet_hours = 84`, `longest_wet_run_hours = 78`, and `peak_hour_mm = 17.5`. Thus `wet_hour_fraction = 84 / 120 = 0.700`, `longest_wet_run_share = 78 / 84 = 0.929`, `peak_hour_share = 17.5 / 196.9 = 0.0889`, `wet_hour_mean = 196.9 / 84 = 2.344`, and `window_mean = 196.9 / 120 = 1.641`.

Daily precipitation gives `max_3day_share = 204.32 / 220.61 = 0.926`, `peak_day_share = 97.29 / 220.61 = 0.441`, and `daily_to_hourly_total_ratio = 220.61 / 196.9 = 1.120`. Report anchors give `331.0 / 83 = 3.988 mm/hour`, `331.0 / 196.9 = 1.681`, `744.8 / 331.0 = 2.250`, and `1025.0 / 331.0 = 3.097`. Peak wind is `38.5 km/h = 10.69 m/s`; the wind-energy proxy is `10.69^2 = 114.3`.

# Reasoning Path

The segmentation is rainfall-first. The sustained wet-hour phase establishes persistence, the three-day phase shows concentration within a multi-day block, the report-calibrated phase connects the point series to reported extreme rainfall anchors, and the wind phase rejects wind as the dominant calibration. All four checks support the final label.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the required phase-segmentation JSON with four phases, four checks, and final label. Partial credit for the correct label with one missing phase.
- 4 points: Computes rainfall-persistence values correctly: 120 hours, 0.700, 0.929, 0.0889, 2.344, and 1.641. Partial credit for four or five correct values.
- 3 points: Computes three-day concentration values correctly: 0.926, 0.441, and 1.120. Partial credit for two correct ratios.
- 4 points: Computes report-intensity alignment correctly: 3.988, 1.681, 2.250, and 3.097. Partial credit for three correct report ratios.
- 3 points: Converts wind and rejects wind dominance correctly: 38.5 km/h, 10.69 m/s, 114.3, and wind-dominance rejection. Partial credit for correct rejection with incomplete conversion.
- 2 points: Explains the phase transitions as a rainfall-dominant timeline rather than isolated metrics. Partial credit for correct checks without transition logic.
- 1 point: Avoids realized-loss, emergency-response, or broad event-history claims beyond the computed timeline.
