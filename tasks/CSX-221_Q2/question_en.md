# Rainfall-Loaded Debris-Flow Process and Response Priority Model

Use only the local event package for CSX-221. Select package-relative evidence for every value family and qualitative process claim you use.

Develop a process-based response-priority model for the 3 July 2021 Izusan/Atami debris flow. The model must combine rainfall conditioning, localized surface disturbance, exposure/impact pressure, and a wetter final-48-hour scenario. Round physical values to 2-3 decimals, ratios/norms to 4 decimals, and final indices to 2 decimals.

Use `clip(x,0,1)` to mean truncation below 0 and above 1.

## Required Calculations

1. Establish the event name, date, location, hazard family, and reported impact counts available in the package.

2. Rainfall conditioning:
   - For the two point-rainfall time series, compute the 15-day totals for 2021-06-19 through 2021-07-03, the final-three-day totals for 2021-07-01 through 2021-07-03, each final-three-day share, the mean final-three-day total, the mean event-day point rainfall on 2021-07-03, and the mean antecedent 12-day total before 2021-07-01.
   - Compute `final3_to_antecedent12_ratio = mean_final3_total_mm / mean_antecedent12_total_mm`.
   - From the gridded precipitation products, compute each event-day maximum, `grid_peak_max_mm`, and `grid_peak_heterogeneity = (max(product maxima) - min(product maxima)) / mean(product maxima)`.
   - Compute:

```text
rainfall_loading_norm =
0.40 * clip(mean_final3_total_mm / 400, 0, 1)
+ 0.20 * clip(mean_event_day_point_precip_mm / 100, 0, 1)
+ 0.20 * clip(mean_final3_share, 0, 1)
+ 0.20 * clip(grid_peak_max_mm / 100, 0, 1)
```

3. Surface-change localization:
   - Compute the optical dNBR maximum, mean, and max-to-mean ratio.
   - Compute Sentinel-1 VV maximum change, minimum change, mean change, absolute mean change, and range in dB.
   - Compute the annual embedding cosine-change maximum, mean, and max-to-mean ratio.
   - Compute:

```text
surface_localization_norm =
0.30 * clip(dnbr_max / 1.5, 0, 1)
+ 0.20 * clip(dnbr_max_to_mean_ratio / 60, 0, 1)
+ 0.25 * clip(radar_vv_range_db / 45, 0, 1)
+ 0.15 * (1 - clip(abs(radar_vv_mean_db) / 0.15, 0, 1))
+ 0.10 * clip(alphaearth_max_to_mean_ratio / 20, 0, 1)
```

4. Exposure and response pressure:
   - Estimate the AOI area in km2 from the package AOI polygon using `lat_span_degrees * 111.32 * lon_span_degrees * 111.32 * cos(mean_latitude_radians)`.
   - Compute population density from the broad population layer, `population_log_norm = clip(log10(population_sum) / 7, 0, 1)`, the count of mapped features in the smallest local OSM slice, and the count/usability note for the larger OSM slice.
   - Using report-derived impact counts, compute:

```text
human_impact_norm = clip((deaths + missing + 0.1 * injuries) / 30, 0, 1)
housing_loss_norm = clip(destroyed_houses / 60, 0, 1)

exposure_response_norm =
0.30 * clip(population_density_per_km2 / 1000, 0, 1)
+ 0.15 * clip(near_trace_osm_feature_count / 5, 0, 1)
+ 0.25 * human_impact_norm
+ 0.20 * housing_loss_norm
+ 0.10 * population_log_norm
```

5. Combine the components:

```text
debris_flow_process_index =
100 * (0.40 * rainfall_loading_norm
     + 0.30 * surface_localization_norm
     + 0.30 * exposure_response_norm)
```

Classify the priority as:

```text
severe_response_priority: index >= 75
high_response_priority:   60 <= index < 75
moderate_response_priority: 45 <= index < 60
low_response_priority:    index < 45
```

6. Scenario analysis: increase the July 2 and July 3 point rainfall by 20%, and increase the gridded event-day maxima by 20%. Recompute only the rainfall-loading component and the final process index, keeping surface-change and exposure-response components fixed. Report the scenario index, index delta, and priority class.

Return one valid JSON object with this structure:

```json
{
  "process_model": {
    "event": {},
    "rainfall_loading_norm": 0.0,
    "surface_localization_norm": 0.0,
    "exposure_response_norm": 0.0,
    "debris_flow_process_index": 0.0,
    "priority_class": ""
  },
  "computed_metrics": {
    "rainfall_conditioning": {},
    "surface_change": {},
    "exposure_response": {}
  },
  "scenario_analysis": {},
  "mechanism_chain": [],
  "source_paths": [],
  "final_interpretation": ""
}
```

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to make the Atami debris-flow answer integrate rainfall loading, localized disturbance, exposure pressure, and a wetter scenario as a process model.

