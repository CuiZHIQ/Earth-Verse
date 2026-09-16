# Post-Fire Debris-Flow Coupling and Response Priority Model

For the 9 January 2018 Montecito and Carpinteria, California post-fire debris-flow event, use only the local event package to reconstruct how rainfall triggering, burn-scar conditioning, runout behavior, and exposed settlement combined into a response-priority problem.

Select package-relative evidence for every evidence family used in your final JSON.

Compute these values:

- `event_window_days`: inclusive event duration in days.
- Rainfall trigger metrics:
  - `grid_peak_mm`: highest maximum event precipitation among gridded precipitation summaries.
  - `grid_peak_mean_mm` and `grid_peak_to_mean_ratio`: the mean and max/mean ratio from the same gridded product as `grid_peak_mm`.
  - `spatial_concentration_ratio`: the largest max/mean ratio among the gridded precipitation summaries.
  - `point_precip_floor_mm`, `point_precip_ceiling_mm`, and `grid_peak_to_point_floor_ratio`: use the two available daily point precipitation samples.
- Burn-scar conditioning metrics:
  - `fire_lag_days`: convert the reported burn-to-flow lag to days.
  - `fire_area_km2`, `dnbr_mean`, `dnbr_max`, annual surface-change mean and max, and the dNBR-to-annual-change ratios.
- Runout, exposure, and impact metrics:
  - conservative lower-bound `runout_km_min`, reported `runout_paths`, fatalities, and minimum damaged homes.
  - exposed population, count of critical facilities tagged as `school`, `fire_station`, `hospital`, `police`, or `shelter`, and count of mapped road ways carrying a `highway` tag.
  - fatalities per 100,000 exposed population, critical facilities per 100,000 exposed population, and minimum damaged homes per runout path.

Use `clip(x) = max(0, min(1, x))`. Compute:

```text
rainfall_trigger_norm =
0.70 * clip(grid_peak_mm / 75)
+ 0.30 * clip(spatial_concentration_ratio / 5)

burn_conditioning_norm =
0.55 * clip(dnbr_mean / 0.30)
+ 0.30 * clip((dnbr_mean / annual_change_mean) / 3)
+ 0.15 * clip(1 - fire_lag_days / 90)

runout_exposure_norm =
0.50 * clip(runout_km_min / 3)
+ 0.25 * clip(runout_paths / 5)
+ 0.25 * clip(critical_facilities / 75)

impact_norm =
0.55 * clip(fatalities / 25)
+ 0.45 * clip(homes_damaged_min / 500)

post_fire_debris_flow_process_index =
100 * (0.40 * rainfall_trigger_norm
     + 0.35 * burn_conditioning_norm
     + 0.25 * runout_exposure_norm)

response_priority_score =
100 * (0.35 * post_fire_debris_flow_process_index / 100
     + 0.25 * clip(population_exposed / 150000)
     + 0.20 * clip(critical_facilities / 75)
     + 0.20 * impact_norm)
```

Then run a stress scenario with daily rainfall intensified by 15%, exposed population increased by 20%, and critical facilities increased by 25%. Hold the spatial rainfall pattern, burn metrics, runout distance/path count, and reported impact anchors constant. Recompute the process index and response-priority score, and report both deltas from baseline.

Use these labels:

- Process index: `very_high_post_fire_debris_flow_coupling` for scores >= 85, `high_post_fire_debris_flow_coupling` for scores >= 70, `moderate_post_fire_debris_flow_coupling` for scores >= 50, otherwise `limited_post_fire_debris_flow_coupling`.
- Response priority: `extreme_escalation_priority` for scores >= 85, `high_response_priority` for scores >= 70, `elevated_response_priority` for scores >= 50, otherwise `watch_response_priority`.

Return one valid JSON object with this structure. Round millimeter values to 0.1, counts to whole numbers unless a scenario creates fractional facilities, ratios/norms/scores to 2 decimals, and dNBR or annual-change values to 3 decimals.

```json
{
  "process_model": {
    "event_window_days": 0,
    "mechanism_chain": []
  },
  "computed_metrics": {
    "rainfall_trigger": {},
    "burn_scar_conditioning": {},
    "runout_and_exposure": {},
    "process_scores": {}
  },
  "scenario_analysis": {},
  "source_paths": [],
  "final_interpretation": ""
}
```
