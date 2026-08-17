# Hassanabad/Shishper GLOF Heat-Rainfall Index Check

A technical review team is checking a proposed calculation for the 7 May 2022 Hassanabad/Shishper Glacier flood. Recompute the heat-melt GLOF priority index and the rainfall-flood priority index from the available quantitative diagnostics, then test whether the heat-melt diagnosis clears the deterministic margin rule.

Use `clamp(x) = min(1, max(0, x))` and these formulas:

- `mean_temp_c`: average of the event-day point mean temperature, event-day point maximum temperature, and reanalysis maximum temperature.
- `point_precip_mm`: average of the two event-day point precipitation totals.
- `grid_precip_mm`: average of the three event-day gridded precipitation means.
- `temperature_score = clamp((mean_temp_c - 20) / 15)`.
- `dryness_score = clamp(1 - point_precip_mm / 10)`.
- `rainfall_score = clamp(grid_precip_mm / 25)`.
- `surface_score`: mean of `clamp(abs(radar VV post-pre mean) / 2)`, `clamp(abs(optical dNBR mean) / 0.3)`, and `clamp(annual embedding cosine-change mean / 0.05)`.
- `exposure_score = clamp(population_sum / 50000)`.
- `heat_melt_glof_index = 100 * (0.40 * temperature_score + 0.25 * dryness_score + 0.15 * rainfall_score + 0.10 * surface_score + 0.10 * exposure_score)`.
- `rainfall_flood_index = 100 * (0.55 * rainfall_score + 0.20 * (1 - dryness_score) + 0.15 * surface_score + 0.10 * exposure_score)`.
- `margin = heat_melt_glof_index - rainfall_flood_index`.

Return `heat_melt_glof_consistent` when `margin >= 20.0` and `point_precip_mm <= 1.0`; otherwise return `rainfall_runoff_competitive`.

Return compact JSON:

```json
{
  "answer": "...",
  "mean_temp_c": 0.0,
  "point_precip_mm": 0.0,
  "grid_precip_mm": 0.0,
  "component_scores": {
    "temperature": 0.0,
    "dryness": 0.0,
    "rainfall": 0.0,
    "surface": 0.0,
    "exposure": 0.0
  },
  "indices": {
    "heat_melt_glof": 0.0,
    "rainfall_flood": 0.0,
    "margin": 0.0
  },
  "rejected_alternative": "..."
}
```

Round temperatures and precipitation to 2 decimals, component scores to 4 decimals, and index values to 1 decimal.
