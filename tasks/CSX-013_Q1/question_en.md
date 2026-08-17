# Heat-Stress Persistence and Emergency Cooling Priority Model

Use only the local event package for CSX-013. Select package-relative evidence for every value and process claim used.

Build a disaster-science model for the June 2021 Pacific Northwest heat wave that links the physical heat-dome process, persistent physiological exposure, built-environment vulnerability, and near-term emergency response priorities.

Your answer must be valid JSON with exactly these top-level keys:

`answer_type`, `event_scope`, `source_paths`, `computed_metrics`, `process_model`, `future_heat_scenario`, `response_priorities`, `mechanism_chain`, `final_interpretation`.

Use this fixed answer type:

`heat_stress_persistence_response_model`

Required analysis:

1. Establish the event name, official package event window, region, and hazard family from package-local metadata and event-report evidence.
2. Extract the report-supported physical mechanism and built-environment vulnerability values, including the high-pressure/sinking-air/downslope mechanism and the Seattle/Portland primary-air-conditioning percentages.
3. From the package-local point meteorology, compute baseline thermal exposure over the official event window:
   - daily Tmax and Tmin series;
   - heat-load above 30 C: `sum(max(Tmax - 30, 0))`;
   - apparent-heat-load above 30 C using daily apparent-temperature maxima;
   - hourly degree-hours above 30 C for air temperature and apparent temperature;
   - hours with air temperature >= 30 C and apparent temperature >= 30 C;
   - longest consecutive run of days with Tmax >= 30 C;
   - hottest 3-day mean Tmax window;
   - warm-night count using Tmin >= 18 C;
   - peak-hour air temperature, apparent temperature, and relative humidity.
4. Compute a baseline heat-stress persistence score:

```text
heat_stress_persistence_score =
100 * (0.40 * min(heat_load_c_day / 30, 1)
     + 0.25 * min(longest_hot_run_days / 6, 1)
     + 0.20 * min(warm_night_count / 5, 1)
     + 0.15 * min(apparent_degree_hours_above_30c / 220, 1))
```

5. Use package-local AOI population and OSM exposure data to compute:
   - AOI centroid and approximate spherical-rectangle area;
   - population density;
   - counts of hospitals, schools, police, fire stations, shelters, major roads, and small-slice fire/road assets.
6. Compute response-priority scores for these four missions: `medical_cooling_operations`, `public_safety_welfare_checks`, `school_family_outreach`, and `road_access_continuity`.

Use:

```text
response_priority_score =
100 * (0.35 * (heat_stress_persistence_score / 100)
     + 0.20 * built_environment_uncooled_norm
     + 0.20 * asset_norm
     + 0.15 * population_density_norm
     + 0.10 * mission_urgency_norm)
```

Where:

```text
built_environment_uncooled_norm = mean(100 - Seattle_AC_percent, 100 - Portland_AC_percent) / 100
population_density_norm = min(population_density_people_per_km2 / 5, 1)
```

Use these mission constants and data-derived asset norms:

```text
medical_cooling_operations: mission_urgency_norm=1.00, asset_norm=min((hospitals + shelters) / 5, 1)
public_safety_welfare_checks: mission_urgency_norm=0.75, asset_norm=min((police + fire_stations) / 4, 1)
school_family_outreach: mission_urgency_norm=0.80, asset_norm=min(schools / 20, 1)
road_access_continuity: mission_urgency_norm=0.60, asset_norm=min(major_roads / 30, 1)
```

7. Compute a future heat perturbation in which all daily and hourly thermal fields are increased by +2 C and the peak-day thermal profile is repeated once immediately before cooldown. Recompute the daily heat-load, hot-run length, warm-night count, hourly apparent degree-hours, and heat-stress persistence score. Report the scenario delta from baseline.
8. Use broad-area meteorology, precipitation, and remote-sensing products only as environmental context for the mechanism chain, not as substitutes for the point thermal-exposure computation.

Rounding rules: temperatures to 1 decimal C; heat-load and degree-hours to 1 decimal; scores and score components to 1 decimal unless they are normalized fractions, which should use 3 decimals; distances and AOI area to 1 decimal; population to 3 decimals; density to 3 decimals; precipitation and remote-sensing statistics to 3 decimals.

Return only the JSON object.
