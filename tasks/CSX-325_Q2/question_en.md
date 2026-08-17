# Southeast Asia Coral Bleaching Heat-Stress Gate Test

A technical review is checking whether the 2023-2024 global coral bleaching event, for the Southeast Asia package slice, satisfies a marine heat-stress primary rule after land-weather, visible-image, and surface-change countermetrics are calculated.

Compute these quantities:

- `marine_text_score`: count 1 point for each condition found in the package text or product description: bleaching-level heat stress, sea-surface-temperature monitoring basis, accumulated heat stress, Alert Level language, and all five CRW product terms (`SST`, `SST Anomaly`, `HotSpot`, `Degree Heating Week`, `Bleaching Alert Area`).
- `extent_pct`: the reported percent of the world's coral reef area impacted by bleaching-level heat stress.
- `coverage_pct`: the reported percent of global coral reefs directly monitored by the 5 km CRW product suite.
- `rainfall_ratio = max(GPM_mean_mm, CHIRPS_mean_mm, ERA5_Land_precip_mean_mm) / min(GPM_mean_mm, CHIRPS_mean_mm, ERA5_Land_precip_mean_mm)`.
- `land_temp_excess_c = ERA5_Land_max_2m_temperature_c - 35`.
- `image_nodata_delta = event_black_or_nodata_fraction - pre_black_or_nodata_fraction`, using RGB pixels with all channels below 8 as black/nodata.
- `surface_mean_sum = AlphaEarth_1_minus_cosine_mean + abs(Sentinel2_dNBR_mean)`.

Apply these gates:

- `marine_heat_gate`: `marine_text_score >= 5` and `extent_pct >= 80`.
- `coverage_gate`: `coverage_pct >= 90`.
- `land_weather_context_gate`: `rainfall_ratio <= 1.5` and `land_temp_excess_c >= 1`.
- `visual_guardrail`: `image_nodata_delta >= 0.05`.
- `surface_guardrail`: `surface_mean_sum <= 0.05`.

Set `answer` to `coral_bleaching_heatstress_countermetric_gate_pass` when all five gates are true; otherwise use `coral_bleaching_heatstress_countermetric_gate_fail`.

Return compact JSON:

```json
{
  "target_family": "southeast_asia_2023_2024_coral_bleaching_heatstress_countermetric_gate",
  "metrics": {
    "extent_pct": 0.0,
    "coverage_pct": 0.0,
    "marine_text_score": 0,
    "rainfall_ratio": 0.0,
    "land_temp_excess_c": 0.0,
    "image_nodata_delta": 0.0,
    "surface_mean_sum": 0.0
  },
  "gates": {
    "marine_heat_gate": false,
    "coverage_gate": false,
    "land_weather_context_gate": false,
    "visual_guardrail": false,
    "surface_guardrail": false
  },
  "answer": "<label>",
  "computed_consequence": "<short consequence derived from the gates>"
}
```
