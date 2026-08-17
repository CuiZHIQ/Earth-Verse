# Black Summer Fire-Weather, Pyroconvection, and Receptor-Stress Model

Use only the local event package for CSX-194. Select package-relative evidence for every value, timeline claim, and qualitative process link you use. The answer should make clear when multiple independent evidence streams support the same mechanism.

Build a coupled disaster-process model for the 2019-2020 Australian Black Summer bushfires focused on the early-season quantitative window where the package provides daily fire-weather data, gridded precipitation summaries, burn-scar evidence, and receptor exposure. Your answer must compute both the observed baseline state and a simple hotter/windier/drier sensitivity case.

Use these definitions.

1. Analysis window:
   - Use the event anchor to identify the broader event period.
   - For the quantitative weather calculation, use the shared early-season window covered by the daily weather series and gridded precipitation summaries.

2. Fire-weather and rainfall terms:
   - A dry day has local daily precipitation `<= 1.0 mm`.
   - A hot-windy day has local daily maximum temperature `>= 25.0 C` and local daily maximum 10 m wind speed `>= 20.0 km/h`.
   - `gridded_precip_consensus_mm` is the mean of the available areal mean accumulated-precipitation values from the ERA5-Land, GPM IMERG, and CHIRPS event-window summaries.
   - `point_to_grid_precip_ratio` is the mean of the local daily-weather precipitation total and the NASA POWER daily precipitation total over the same window, divided by `gridded_precip_consensus_mm`.
   - `fire_weather_stress_norm =
     0.35 * dry_day_fraction
     + 0.25 * min(longest_dry_spell_days / 14, 1)
     + 0.20 * min(hot_windy_days / 10, 1)
     + 0.10 * min(max_wind_kmh / 35, 1)
     + 0.10 * min(1 - gridded_precip_consensus_mm / 100, 1)`.

3. Burn, surface-change, smoke, and exposure terms:
   - `burn_severity_norm =
     min(0.55 * min(dnbr_mean / 0.20, 1)
       + 0.35 * min(dnbr_max / 0.85, 1)
       + 0.10 * min((dnbr_max - dnbr_mean) / 0.70, 1), 1)`.
   - `surface_change_norm =
     min(0.65 * min(annual_embedding_change_mean / 0.05, 1)
       + 0.35 * min(annual_embedding_change_max / 0.40, 1), 1)`.
   - `smoke_pyroconvective_norm =
     0.45 * firestorm_norm
     + 0.35 * min(max_smoke_height_km / 20, 1)
     + 0.20 * transport_norm`, where `firestorm_norm = 1` if the report states more than 20 firestorms, otherwise use the reported count divided by 20 and clipped to 1; `transport_norm` is the fraction of the two named downwind receptor regions, New Zealand and South America, explicitly reached by smoke.
   - `exposure_load_norm =
     0.50 * min(population / 350000, 1)
     + 0.25 * min(road_features / 1000, 1)
     + 0.25 * min(amenity_features / 100, 1)`.

4. Coupled process and response scores:
   - `coupled_process_index =
     100 * (0.25 * fire_weather_stress_norm
          + 0.25 * burn_severity_norm
          + 0.20 * surface_change_norm
          + 0.15 * smoke_pyroconvective_norm
          + 0.15 * exposure_load_norm)`.
   - Response priorities:
     - `fireline_containment = 100 * (0.45 * fire_weather_stress_norm + 0.35 * burn_severity_norm + 0.20 * exposure_load_norm)`.
     - `smoke_air_quality = 100 * (0.50 * smoke_pyroconvective_norm + 0.25 * exposure_load_norm + 0.25 * fire_weather_stress_norm)`.
     - `access_evacuation = 100 * (0.40 * exposure_load_norm + 0.30 * fire_weather_stress_norm + 0.20 * burn_severity_norm + 0.10 * surface_change_norm)`.

5. Sensitivity case:
   - Recompute the weather and rainfall parts after increasing every local daily maximum temperature by `+2.0 C`, increasing every local daily maximum wind speed by `15%`, and reducing both local and gridded precipitation by `20%`.
   - Hold the observed burn, surface-change, smoke, and exposure terms fixed.
   - Report `scenario_delta = scenario_coupled_process_index - baseline_coupled_process_index`.

Classify the result as `extreme_coupled_fire_smoke_response_case` if the baseline coupled process index is at least 75, the scenario delta is at least 1.0, `smoke_pyroconvective_norm` is at least 0.90, and `exposure_load_norm` is at least 0.85. Otherwise classify it as `lower_coupled_response_pressure`.

Return structured JSON:

```json
{
  "target_family": "black_summer_coupled_process_model",
  "source_paths": {
    "event_context": ["<package-relative path>", "..."],
    "weather_and_precipitation": ["<package-relative path>", "..."],
    "burn_and_surface_change": ["<package-relative path>", "..."],
    "exposure": ["<package-relative path>", "..."],
    "smoke_and_response_context": ["<package-relative path>", "..."]
  },
  "process_model": {
    "event_period": {"start": "<YYYY-MM-DD>", "end": "<YYYY-MM-DD>"},
    "analysis_window": {"start": "<YYYY-MM-DD>", "end": "<YYYY-MM-DD>", "days": <integer>},
    "baseline_classification": "<classification_label>"
  },
  "computed_metrics": {
    "baseline_weather": {
      "precip_total_mm": <number>,
      "dry_days": <integer>,
      "dry_day_fraction": <number>,
      "longest_dry_spell_days": <integer>,
      "hot_windy_days": <integer>,
      "max_temp_c": <number>,
      "max_wind_kmh": <number>,
      "gridded_precip_consensus_mm": <number>,
      "point_to_grid_precip_ratio": <number>,
      "fire_weather_stress_norm": <number>
    },
    "burn_surface_smoke_exposure": {
      "dnbr_mean": <number>,
      "dnbr_max": <number>,
      "dnbr_spread": <number>,
      "annual_embedding_change_mean": <number>,
      "annual_embedding_change_max": <number>,
      "max_smoke_height_km": <number>,
      "firestorms_minimum": <integer>,
      "population": <integer>,
      "road_features": <integer>,
      "amenity_features": <integer>,
      "burn_severity_norm": <number>,
      "surface_change_norm": <number>,
      "smoke_pyroconvective_norm": <number>,
      "exposure_load_norm": <number>
    },
    "baseline_coupled_process_index": <number>
  },
  "scenario_analysis": {
    "perturbation": {"temperature_c": 2.0, "wind_multiplier": 1.15, "precip_multiplier": 0.80},
    "scenario_fire_weather_stress_norm": <number>,
    "scenario_coupled_process_index": <number>,
    "scenario_delta": <number>
  },
  "response_priorities": [
    {"priority": "<name>", "score": <number>, "rank": <integer>},
    {"priority": "<name>", "score": <number>, "rank": <integer>},
    {"priority": "<name>", "score": <number>, "rank": <integer>}
  ],
  "mechanism_chain": [
    "<concise process link>",
    "<concise process link>",
    "<concise process link>"
  ],
  "final_interpretation": "<one concise disaster-science interpretation>"
}
```
