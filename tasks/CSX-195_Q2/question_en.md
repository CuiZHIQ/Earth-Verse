# Pyroconvective Smoke Injection and Response-Load Model

Use only the local event package for CSX-195. Select package-relative evidence for every evidence stream you use and make each stream's role clear in `source_paths`.

Build a compact disaster-science diagnosis for the late-December 2019 to early-January 2020 Australian wildfire smoke episode over the South Pacific. Treat the event as a coupled source-weather, burn-severity, pyroconvective plume-injection, and local response-load problem.

Use these definitions and round reported numeric outputs to three decimals unless a field states otherwise.

1. Event window:
   - Use the package event window.
   - `window_days` is inclusive.

2. Report-derived plume context:
   - Extract the lower-bound count of firestorm/pyrocumulonimbus outbreaks from the narrative.
   - Extract the reported CALIPSO smoke-altitude range in kilometers.
   - Mark `stratospheric_link` true only if the narrative explicitly links the plume height to the stratosphere.
   - `firestorm_rate_per_day = firestorm_minimum / window_days`.

3. Source-weather stress:
   - Use the event-window maximum 2 m temperature from the hourly aggregate weather record.
   - Build a precipitation consensus as the arithmetic mean of the mean accumulated precipitation values from the hourly aggregate, satellite precipitation, and daily precipitation products.
   - Build a gridded wind summary from the ERA5-Land mean 10 m u and v wind components.
   - `heat_norm = clip((temperature_2m_max_c - 30) / 10, 0, 1)`.
   - `dryness_norm = clip(1 - precipitation_consensus_mean_mm / 1.0, 0, 1)`.
   - `wind_norm = clip(era5_mean_wind_speed_mps / 6.0, 0, 1)`.
   - `fire_weather_norm = 0.45 * heat_norm + 0.35 * dryness_norm + 0.20 * wind_norm`.

4. Burn and land-surface disturbance:
   - Use the Sentinel-2 dNBR mean and maximum.
   - Use the annual satellite-embedding cosine-change mean and maximum.
   - `burn_severity_norm = 0.55 * clip(dnbr_mean / 0.30, 0, 1) + 0.45 * clip(dnbr_max / 0.80, 0, 1)`.
   - `remote_change_norm = 0.60 * clip(alphaearth_change_mean / 0.05, 0, 1) + 0.40 * clip(alphaearth_change_max / 0.60, 0, 1)`.

5. Pyroconvective plume-injection:
   - `altitude_mid_km = mean(smoke_altitude_km)`.
   - `altitude_norm = clip((altitude_mid_km - 10) / 10, 0, 1)`.
   - `firestorm_norm = clip(firestorm_minimum / 20, 0, 1)`.
   - `plume_injection_norm = 0.45 * altitude_norm + 0.35 * firestorm_norm + 0.20 * int(stratospheric_link)`.
   - `pyroconvective_smoke_potential = 100 * (0.35 * fire_weather_norm + 0.25 * burn_severity_norm + 0.25 * plume_injection_norm + 0.15 * remote_change_norm)`.

6. Local response-load proxy:
   - Use the compact AOI polygon to estimate approximate area in square kilometers with 111.32 km per degree latitude and longitude distance scaled by cos(mid-latitude).
   - Use the WorldPop population sum for the AOI.
   - Count OSM amenities in the bounded AOI slice by amenity tag.
   - `population_density_per_km2 = population / aoi_area_km2`.
   - `population_density_norm = clip(population_density_per_km2 / 100, 0, 1)`.
   - `critical_facility_count = hospitals + police + fire_stations + shelters`.
   - `critical_facility_norm = clip(critical_facility_count / 200, 0, 1)`.
   - `sensitive_site_norm = clip((hospitals + schools + shelters) / 900, 0, 1)`.
   - `shelters_per_million_people = shelters / (population / 1,000,000)`.
   - `shelter_gap_norm = clip(1 - shelters_per_million_people / 5, 0, 1)`.
   - `local_response_load_index = 100 * (0.35 * pyroconvective_smoke_potential / 100 + 0.20 * population_density_norm + 0.20 * sensitive_site_norm + 0.15 * critical_facility_norm + 0.10 * shelter_gap_norm)`.

7. Severe recurrence scenario:
   - Increase maximum 2 m temperature by 2 C.
   - Halve the precipitation consensus.
   - Increase ERA5 mean wind speed by 20 percent.
   - Increase dNBR mean and maximum by 10 percent before applying the same clipping rules.
   - Increase the firestorm lower bound by 25 percent.
   - Increase the upper end of the smoke-altitude range by 1 km and recompute the altitude midpoint.
   - Hold remote-change and exposure terms fixed.
   - Recompute `pyroconvective_smoke_potential`, `local_response_load_index`, and both deltas from baseline.

Return one JSON object:

```json
{
  "process_model": "pyroconvective_smoke_injection_and_response_load",
  "source_paths": {
    "reports": [],
    "weather": [],
    "burn_and_remote_sensing": [],
    "exposure_and_geospatial": []
  },
  "event_window": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "window_days": 0
  },
  "computed_metrics": {
    "report_context": {},
    "source_weather": {},
    "burn_and_change": {},
    "response_exposure": {},
    "normalizations": {},
    "baseline_indices": {}
  },
  "scenario_analysis": {
    "scenario_name": "hotter_windier_drier_recurrence",
    "scenario_indices": {},
    "delta_from_baseline": {}
  },
  "response_priorities": [],
  "mechanism_chain": [],
  "final_interpretation": ""
}
```

In `response_priorities`, provide exactly three ranked actions with a short rationale and a numeric `priority_score` from 0 to 100. Base the ranking on the computed indices and the source evidence, not on generic wildfire advice.
