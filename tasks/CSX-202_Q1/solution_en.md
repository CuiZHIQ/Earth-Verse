# Final Answer

```json
{
  "compound_component_count": 3,
  "pollutant_component_count": 2,
  "gridded_heat_score": 3,
  "gridded_stagnation_proxy_score": 4,
  "surface_fire_signal_score": 4,
  "compound_air_load_index": 15,
  "diagnosis_label": "compound_heat_dust_smoke_air_hazard_with_gridded_stagnation_screen"
}
```

# Key Computations

The 2023-07-17 to 2023-07-25 event window has 9 days. The report text confirms heat or extreme heat, Saharan dust, and wildfire or smoke, so `compound_component_count = 3`; the pollutant subset is dust plus wildfire smoke/wildfire, so `pollutant_component_count = 2`.

ERA5-Land gridded heat screen:

```text
Tmax max = 30.426 C >= 30 C -> 1
Tmax mean = 27.447 C >= 25 C -> 1
Tmax min = 23.759 C >= 20 C -> 1
gridded_heat_score = 3
```

ERA5-Land gridded stagnation proxy:

```text
mean wind speed = sqrt(2.429^2 + 0.321^2) = 2.450 m/s <= 3 m/s -> 1
maximum wind-vector screen = sqrt(3.384^2 + 0.775^2) = 3.471 m/s <= 5 m/s -> 1
precipitation mean = 15.640 mm <= 20 mm -> 1
precipitation minimum = 6.428 mm <= 10 mm -> 1
gridded_stagnation_proxy_score = 4
```

Surface fire signal:

```text
Sentinel-2 dNBR max = 1.0904 >= 1.0 -> 1
Sentinel-2 dNBR mean = 0.0968 >= 0.05 -> 1
AlphaEarth mean change = 0.0351 >= 0.03 -> 1
AlphaEarth max change = 0.5256 >= 0.5 -> 1
surface_fire_signal_score = 4
```

The load index is:

```text
compound_air_load_index = 2 * pollutant_component_count
                        + gridded_heat_score
                        + gridded_stagnation_proxy_score
                        + surface_fire_signal_score
                        = 2 * 2 + 3 + 4 + 4
                        = 15
```

All label thresholds are met, so the computed diagnosis label is `compound_heat_dust_smoke_air_hazard_with_gridded_stagnation_screen`.

# Reasoning Path

The ledger first separates report-confirmed compound components from pollutant components. Heat, Saharan dust, and wildfire/smoke give three compound components, while dust plus wildfire/smoke give two pollutant components.

The gridded weather screen then supports a hot, low-wind, low-precipitation environment using ERA5-Land aggregate statistics from the event window. Sentinel-2 dNBR and AlphaEarth annual change add an independent surface-change signal. The final label is therefore driven by local package report text, gridded physical-hazard statistics, and surface-change products, not by off-event point weather or EONET catalog entries.

# Computed Interpretation

The computed result is a compound air-load ledger: heat, dust, smoke/wildfire text, gridded stagnation, and surface-change evidence all contribute to the final diagnosis.

# Scoring Rubric

Total: 20 points.

- 4 points: Requested JSON schema. Full credit for returning all seven requested ledger fields with no unrelated action or briefing content. Partial credit: 2-3 points for a mostly complete JSON ledger with one missing or renamed field.
- 3 points: Report component extraction. Full credit for finding all three report-confirmed components and the two pollutant components from the Copernicus report text. Partial credit: 1-2 points if one component or pollutant flag is missed.
- 4 points: ERA5 gridded heat and stagnation screen. Full credit for computing `gridded_heat_score = 3`, mean wind speed near 2.45 m/s, maximum wind-vector screen near 3.471 m/s, precipitation mean near 15.640 mm, and `gridded_stagnation_proxy_score = 4`. Partial credit for correct heat score, wind vector calculation, precipitation screen, or stagnation score.
- 3 points: Surface fire signal. Full credit for using dNBR and AlphaEarth metrics to compute `surface_fire_signal_score = 4`. Partial credit: 1-2 points for correct use of only one surface-change family.
- 4 points: Load index and diagnosis. Full credit for computing `compound_air_load_index = 15` and returning `compound_heat_dust_smoke_air_hazard_with_gridded_stagnation_screen`. Partial credit: 2-3 points for the correct direction with one arithmetic or threshold error.
- 2 points: Bounded interpretation. Full credit for tying the explanation to report, gridded weather, and surface-change evidence without using off-event point weather, EONET fire catalogs, or health-outcome overclaims. Partial credit: 1 point if one unsupported evidence family is mentioned but does not alter the final label.
