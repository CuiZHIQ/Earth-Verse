# Boreal Fire Source, Smoke Transport, and Health-Response Model

You are designing a smoke-risk briefing for the 2023 Canadian wildfire-smoke episode. The local package has fire/smoke reporting, aerosol clues, local burn/surface-change context, precipitation summaries, population, and OSM exposure context.

Build a source-to-receptor model: quantify fire-source instability, aerosol-column transport, downwind smoke severity, supporting surface/weather context, and public-health response pressure. Do not collapse the answer into a single satellite burn metric.

Use only package-local files and cite package-relative paths. Return JSON with exactly these top-level fields:

```json
{
  "answer": "<short snake_case label>",
  "source_files_used": ["<package-relative path>", "..."],
  "source_fire_intensity": {},
  "smoke_column_transport": {},
  "surface_and_weather_context": {},
  "exposure_and_decision_logic": {},
  "stress_scenario_hotter_drier_source": {},
  "recommended_reasoning_path": ["..."]
}
```

Use these definitions where the package supports the inputs:

- `aod_excess_load = (Grand Forks average AOD - Goddard average AOD) + (Grand Forks peak AOD - Goddard average AOD)`.
- In `stress_scenario_hotter_drier_source`, increase the out-of-control fire count by 25 percent and keep burned area per out-of-control fire unchanged when computing the source-area proxy.

Your reasoning should make the physical chain explicit: burning area and out-of-control fires create a source, aerosol optical depth captures atmospheric loading, and exposure context determines health and visibility response priorities.
