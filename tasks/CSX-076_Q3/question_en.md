# Indus Monsoon Memory and Floodplain-Response Stress Model

You are supporting a flood coordination desk after the 2022 Pakistan monsoon floods. The package contains event reports, point daily rainfall, gridded precipitation summaries, SAR/embedding change, population, and local exposure context.

Build a deep hydrometeorological stress model. The question is not asking for a one-day rainfall total. It asks whether the floodplain response is better explained by rainfall memory, spatially coherent wetness, surface-water change, and exposure pressure.

Use only files inside the package. Discover the relevant files yourself and cite package-relative paths. Return JSON with exactly these top-level fields:

```json
{
  "answer": "<short snake_case label>",
  "event_window": {},
  "source_files_used": ["<package-relative path>", "..."],
  "monsoon_accumulation": {},
  "runoff_memory_pulse": {},
  "multi_sensor_hydrology": {},
  "exposure_and_response_pressure": {},
  "stress_scenario_plus_rain": {},
  "recommended_reasoning_path": ["..."]
}
```

Use the daily point rainfall series to compute the late-August pulse and antecedent memory:

`runoff_pressure_index_mm = fresh_7day_mm * (1 + antecedent_14day_mm / 200)`

For the stress scenario, increase pulse rainfall by 15 percent and antecedent rainfall by 10 percent, then recompute the same runoff-pressure formula.

Your reasoning should connect antecedent wetness, a late-August pulse, gridded precipitation agreement, SAR/embedding surface change, population/critical-amenity pressure, and the consequences of the rainfall-amplification scenario. When using gridded precipitation summaries, report their declared coverage window and use them for spatial wetness context over that declared window rather than as the source of the late-August point-rainfall pulse.
