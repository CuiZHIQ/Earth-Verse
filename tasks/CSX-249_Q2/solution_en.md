# Correct Answer

```json
{
  "component_scores": {"heat_core": 6, "persistence": 4, "dry_stress": 5, "context_checks": 4},
  "total_score": 19,
  "class_label": "sustained_heat_yangtze_dry_stress_confirmed",
  "derived_values": {
    "event_window_days": 92,
    "heat_streak_days": 64,
    "record_excess_days": 2,
    "heat_peak_mean_delta_c": 3.039,
    "gpm_chirps_mean_diff_mm": 0.15,
    "dnbr_max_mean_ratio": 24.438,
    "embedding_max_mean_ratio": 25.072,
    "population_million": 8.454
  },
  "report_anchors": {"red_heat_warning_count": 30, "deficit_pct": 80.0, "affected_million": 5.527, "loss_billion_cny": 2.73}
}
```

The heat component earns all 6 points: ERA5-Land Tmax mean is 36.421 C, Tmax max is 39.460 C, their peak-mean delta is 3.039 C, and the report gives 30 red heat warnings. The persistence component earns 4 points from a 92-day locked window, a 64-day June 13 through August 15 streak marker, and a 2-day excess over the prior 62-day record.

The dry-stress component earns 5 points from an 80.0 percent lower-than-normal precipitation anchor, 5.527 million affected people, 2.73 billion CNY direct loss, and a present water-supply flag. The context-check component earns 4 points because the GPM and CHIRPS means differ by only 0.150 mm, the dNBR and embedding max-mean ratios are 24.438 and 25.072 with low means, and the masked WorldPop total is 8.454 million. These context checks support consistency but are not treated as standalone proof of the regional drought mechanism.

# Scoring Rubric

- 4 points: Extract the required package JSON values and report-text numeric anchors.
- 4 points: Compute the heat peak-mean delta, inclusive date spans, and record-excess days.
- 4 points: Apply the dry-stress score rules from the report anchors exactly.
- 4 points: Apply bounded context-check calculations for precipitation agreement, surface ratios, and masked population summary.
- 4 points: Return the total score 19 and confirmed class label with compact formula traces or derived values that make the arithmetic auditable.

Total: 20 points.
