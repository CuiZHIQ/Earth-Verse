# Correct Answer

```json
{
  "target_family": "southeast_asia_2023_2024_coral_bleaching_heatstress_countermetric_gate",
  "metrics": {
    "extent_pct": 84.4,
    "coverage_pct": 95.0,
    "marine_text_score": 5,
    "rainfall_ratio": 1.3052,
    "land_temp_excess_c": 1.5556,
    "image_nodata_delta": 0.0755,
    "surface_mean_sum": 0.0303
  },
  "gates": {
    "marine_heat_gate": true,
    "coverage_gate": true,
    "land_weather_context_gate": true,
    "visual_guardrail": true,
    "surface_guardrail": true
  },
  "answer": "coral_bleaching_heatstress_countermetric_gate_pass",
  "computed_consequence": "marine_heatstress_primary_land_visual_surface_counters_contextual"
}
```

# Computation Path

The marine text score is 5: the package text includes bleaching-level heat stress, an SST monitoring basis, accumulated heat stress, Alert Level language, and all five named CRW product terms. The status text gives `extent_pct = 84.4`, and the product description gives `coverage_pct = 95.0`.

For land-weather countermetrics, `rainfall_ratio = max(428.0731, 332.8795, 434.4847) / min(428.0731, 332.8795, 434.4847) = 1.3052`, and `land_temp_excess_c = 36.5556 - 35 = 1.5556`. For image and surface countermetrics, `image_nodata_delta = 0.1642 - 0.0887 = 0.0755`, and `surface_mean_sum = 0.0276366 + abs(0.0026708) = 0.0303`.

All gates pass: `marine_text_score >= 5`, `extent_pct >= 80`, `coverage_pct >= 90`, `rainfall_ratio <= 1.5`, `land_temp_excess_c >= 1`, `image_nodata_delta >= 0.05`, and `surface_mean_sum <= 0.05`. The short computed consequence is that marine heat stress remains primary while land-weather, visible-image, and broad surface-change counters stay contextual.

# Scoring Rubric

- 4 points: Returns compact JSON with `target_family`, `metrics`, `gates`, `answer`, and `computed_consequence`.
- 5 points: Correctly computes the marine heat-stress anchors: `marine_text_score = 5`, `extent_pct = 84.4`, and `coverage_pct = 95.0`.
- 4 points: Correctly computes countermetrics within tolerance: `rainfall_ratio = 1.3052`, `land_temp_excess_c = 1.5556`, `image_nodata_delta = 0.0755`, and `surface_mean_sum = 0.0303`.
- 3 points: Applies all five threshold gates and returns `coral_bleaching_heatstress_countermetric_gate_pass` only because every gate is true.
- 2 points: Rejects land-weather, visible-image, and broad surface-change dominance as a direct consequence of the computed gates.
- 1 point: Keeps the computed consequence short and tied to the gate results.
- 1 point: Avoids inferred realized reef loss, human burden, or local coral mortality from these package-level calculations.
