# Compound Air-Hazard Numeric Ledger

For the 17-25 July 2023 Mediterranean heatwave, Saharan dust, and wildfire-smoke episode, compute a compact compound air-hazard ledger from the local event package. The ledger should test whether the evidence supports a combined heat, dust, smoke/wildfire, gridded stagnation, and surface-fire-change diagnosis.

Rules:
- `compound_component_count`: count the report-confirmed components among heat or extreme heat, Saharan dust, and wildfire smoke or wildfire.
- `pollutant_component_count`: count the dust and wildfire-smoke/wildfire components only.
- `gridded_heat_score`: from ERA5-Land aggregate statistics, add one point each for event maximum Tmax >= 30 C, mean Tmax >= 25 C, and minimum Tmax >= 20 C.
- `gridded_stagnation_proxy_score`: from ERA5-Land aggregate statistics, add one point each for mean 10 m wind-vector speed <= 3 m/s, maximum wind-vector screen <= 5 m/s, mean precipitation <= 20 mm, and minimum precipitation <= 10 mm.
- `surface_fire_signal_score`: add one point each for Sentinel-2 dNBR maximum >= 1.0, Sentinel-2 dNBR mean >= 0.05, AlphaEarth mean annual change >= 0.03, and AlphaEarth maximum annual change >= 0.5.
- `compound_air_load_index`: `2 * pollutant_component_count + gridded_heat_score + gridded_stagnation_proxy_score + surface_fire_signal_score`.

Return JSON:

```json
{
  "compound_component_count": 0,
  "pollutant_component_count": 0,
  "gridded_heat_score": 0,
  "gridded_stagnation_proxy_score": 0,
  "surface_fire_signal_score": 0,
  "compound_air_load_index": 0,
  "diagnosis_label": ""
}
```

Use the diagnosis label `compound_heat_dust_smoke_air_hazard_with_gridded_stagnation_screen` when all three compound components are present, both pollutant components are present, `gridded_heat_score >= 2`, `gridded_stagnation_proxy_score >= 3`, and `surface_fire_signal_score >= 3`. Otherwise use `compound_air_hazard_threshold_not_met`.
