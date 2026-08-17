# Nepal Fire-Weather, Smoke Transport, and Burn-Activity Coupled Index

Model the late March to mid-April 2021 Nepal forest-fire episode as a coupled process problem rather than a narrative event summary. Use the local event package to extract the event timing and report-supported signals for rainfall deficit, hot/windy fire weather, rugged terrain, fire-hotspot burden, smoke transport, and reported disruption.

The goal is to compute three coupled report-grounded indices:

1. a `fire_weather_index` describing dry-season stress and spread difficulty;
2. a `smoke_disruption_index` describing whether smoke transport intersects populated valleys and social/transport disruption;
3. a `burn_activity_index` describing whether the report indicates an unusually intense fire season rather than isolated small fires.

Use these formulas:

```text
rainfall_deficit_norm = 1 - reported_rain_fraction_of_normal
hot_windy_norm = 1 if the report states hot, windy weather exacerbated fires, else 0
terrain_norm = 1 if the report ties rugged terrain to difficult fire control, else 0
hotspot_norm = clip(reported_fire_hotspots / 50000, 0, 1)

fire_weather_index =
100 * (0.45 * rainfall_deficit_norm
     + 0.25 * hot_windy_norm
     + 0.15 * terrain_norm
     + 0.15 * hotspot_norm)
```

```text
smoke_signal_fraction = present_smoke_signals / 4
disruption_fraction = present_disruption_signals / 4
transport_path_norm = 1 if the report describes eastward or regional smoke transport, else 0

smoke_disruption_index =
100 * (0.50 * smoke_signal_fraction
     + 0.40 * disruption_fraction
     + 0.10 * transport_path_norm)
```

Use four smoke signals: countrywide smoke, smoke in valleys near Pokhara, unhealthy or hazardous air, and eastward or regional smoke transport. Use four disruption signals: school closure, evacuation, fatality or casualty signal, and flight cancellation or transport disruption.

```text
second_rank_norm = 1 if the report states the 2021 hotspot count was second-highest for the period, else 0
uncontrolled_forest_burn_norm = 1 if the report says fires burned uncontrolled through forests, else 0

burn_activity_index =
100 * (0.60 * hotspot_norm
     + 0.25 * second_rank_norm
     + 0.15 * uncontrolled_forest_burn_norm)
```

Set `direct_damage_reported` to `true` only if the local incident narrative explicitly states property, building, or critical-facility damage. Smoke exposure, school closure, transport disruption, fatalities, population, roads, bridges, hospitals, and other receptor counts are not by themselves direct property/building/facility damage statements.

Return a compact JSON object with exactly these keys:

```json
{
  "answer_type": "fire_smoke_reported_process_index",
  "window_days": 0,
  "reported_rain_fraction_of_normal": 0.0,
  "fire_weather_index": 0.0,
  "smoke_disruption_index": 0.0,
  "burn_activity_index": 0.0,
  "direct_damage_reported": false,
  "formula_check": "pass_or_fail"
}
```

Round `reported_rain_fraction_of_normal` to three decimals and all index values to two decimals. Keep the response to the JSON object plus one short formula-check sentence.
