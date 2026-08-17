# Dust Transport Consistency Check

For the 22-23 September 2009 eastern Australia dust storm, compute a deterministic Dust Wind Index that tests whether the event-window numbers fit a dry, wind-driven dust-transport state.

Use these definitions:

- `max_wind_ms`: the larger available 10 m daily maximum wind value, converting km/h to m/s when needed.
- `point_precip_total_mm`: the sum of available point daily precipitation totals across the two-day window.
- `regional_mean_precip_mm`: the mean of the available gridded event-window mean precipitation values.
- `regional_max_precip_mm`: the maximum of the available gridded event-window maximum precipitation values.
- `major_roads`, `critical_amenities`, and `local_population`: receptor-context metrics from the package exposure summaries.

Let `clip(x) = min(1, max(0, x))`.

Compute:

- `wind_score = clip((max_wind_ms - 8.0) / 4.0)`
- `dryness_score = clip(1.0 - regional_mean_precip_mm / 0.1)`
- `transport_score = clip(major_roads / 150.0)`
- `facility_score = clip(critical_amenities / 50.0)`
- `population_score = clip(local_population / 10000.0)`
- `dust_wind_index = 100 * (0.35 * wind_score + 0.30 * dryness_score + 0.20 * transport_score + 0.10 * facility_score + 0.05 * population_score)`

The threshold result is `dust_transport_consistent` only when all gates pass: `max_wind_ms >= 8.0`, `point_precip_total_mm == 0.0`, `regional_mean_precip_mm <= 0.1`, `regional_max_precip_mm < 3.0`, and `dust_wind_index >= 70.0`. Keep point-weather gates and receptor-context components as separate evidence roles.

Return compact JSON with these keys: `max_wind_ms`, `point_precip_total_mm`, `regional_precip_mm`, `receptors`, `component_scores`, `dust_wind_index`, and `threshold_result`.

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

For this task, use that object to turn the dust index into a mechanism check that separates wind transport and dryness from receptor context.

