# Final Answer

```json
{
  "answer_type": "fire_smoke_reported_process_index",
  "window_days": 21,
  "reported_rain_fraction_of_normal": 0.25,
  "fire_weather_index": 86.05,
  "smoke_disruption_index": 100.0,
  "burn_activity_index": 89.2,
  "direct_damage_reported": false,
  "formula_check": "pass"
}
```

The formula check is `pass`: the three indices reproduce from the report-supported formulas, and the incident narrative does not state property, building, or critical-facility damage.

# Key Computations

The event window runs from 2021-03-26 through 2021-04-15, which is 21 inclusive days.

The report says Nepal received just a quarter of its normal January-April rainfall:

`reported_rain_fraction_of_normal = 0.25`

`rainfall_deficit_norm = 1 - 0.25 = 0.75`

The report gives roughly 41,000 VIIRS hotspots:

`hotspot_norm = 41000 / 50000 = 0.82`

Fire-weather terms:

- `hot_windy_norm = 1`
- `terrain_norm = 1`
- `fire_weather_index = 100 * (0.45 * 0.75 + 0.25 * 1 + 0.15 * 1 + 0.15 * 0.82) = 86.05`

Smoke-disruption terms:

- four smoke signals are present: countrywide smoke, smoke in valleys near Pokhara, unhealthy or hazardous air, and eastward smoke transport
- four disruption signals are present: school closure, evacuation, fatality signal, and flight cancellation
- `transport_path_norm = 1`
- `smoke_disruption_index = 100 * (0.50 * 1 + 0.40 * 1 + 0.10 * 1) = 100.00`

Burn-activity terms:

- `hotspot_norm = 0.82`
- `second_rank_norm = 1`
- `uncontrolled_forest_burn_norm = 1`
- `burn_activity_index = 100 * (0.60 * 0.82 + 0.25 * 1 + 0.15 * 1) = 89.20`

# Reasoning Path

The coupled process index uses only report-supported quantities. The rainfall deficit, hot/windy text, rugged terrain, and hotspot burden support a high fire-weather index. The smoke and disruption signals are all present, so the smoke-disruption index reaches the top of its scale. The hotspot count, second-rank status, and uncontrolled forest-burn text support a high burn-activity index.

`direct_damage_reported` remains `false` because the report describes smoke exposure, school closures, evacuations, deaths, and flight cancellations, but not explicit property, building, or critical-facility damage.

# Scoring Rubric

Total: 20 points.

- 3 points: Reports 21 inclusive days and the report-supported rainfall fraction `0.250`.
- 4 points: Recomputes `fire_weather_index = 86.05` from rainfall deficit, hot/windy text, rugged terrain, and hotspot normalization.
- 4 points: Recomputes `smoke_disruption_index = 100.00` from four smoke signals, four disruption signals, and the eastward transport path.
- 3 points: Recomputes `burn_activity_index = 89.20` from `hotspot_norm = 0.82`, second-rank hotspot status, and uncontrolled forest-burn text.
- 2 points: Keeps `direct_damage_reported = false` because smoke disruption and fatalities are not direct property/building/facility damage statements.
- 2 points: Uses the requested fields, correct rounding, and `formula_check = "pass"`.
- 2 points: Bases the indices on report-supported values and does not use off-event weather, dNBR, embedding, or receptor counts as physical-process substitutes.
