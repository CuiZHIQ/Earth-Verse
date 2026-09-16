# ENSO Mature-Core Coupling and Teleconnection-Risk Model

You are preparing a climate diagnostics item for the 2023-2024 El Nino episode. The package contains oceanic index data, pressure-index data, precipitation summaries, remote-sensing context, population context, and the event anchor.

Build a coupled ocean-atmosphere reasoning model. The task is not simply to name El Nino. Reconstruct the mature ONI core, pair it with SOI central months, diagnose ramp/decay behavior, and then use regional hydro/exposure files only as lag-aware teleconnection stress context.

Use only local package files and cite package-relative paths. Return JSON with exactly these top-level fields:

```json
{
  "answer": "<short snake_case label>",
  "source_files_used": ["<package-relative path>", "..."],
  "mature_core_window": {},
  "ocean_atmosphere_coupling": {},
  "event_evolution": {},
  "regional_hydro_exposure_context": {},
  "stress_scenario_core_extension": {},
  "recommended_reasoning_path": ["..."]
}
```

Inside `regional_hydro_exposure_context`, include the precipitation-product window and a short scope note explaining that hydro, exposure, and embedding values are regional stress context rather than direct local-impact attribution. Inside `stress_scenario_core_extension`, label the scenario as a sensitivity test rather than a forecast. The final explanation should show the difference between an index-defined global climate driver and local impacts that are lagged, regionally variable, and only partly constrained by this package.
