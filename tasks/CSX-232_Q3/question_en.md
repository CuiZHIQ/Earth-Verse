# Earthquake Rupture, Access Fragility, and Cold-Rescue Window Model

You are preparing the hardest earthquake-response reasoning item in this benchmark. The package contains earthquake catalog entries, disaster activation text, SAR/embedding change, road/bridge exposure, population, and daily weather.

Build a cascading-rescue model for the 2023 Turkiye-Syria earthquake sequence. The model must integrate rupture timing, shaking intensity, surface-change signals, road/bridge access fragility, cold-weather survival pressure, and humanitarian complexity.

Use only files inside the package and cite package-relative paths. Return JSON with exactly these top-level fields:

```json
{
  "answer": "<short snake_case label>",
  "source_files_used": ["<package-relative path>", "..."],
  "rupture_sequence": {},
  "surface_damage_and_access": {},
  "cold_weather_rescue_modifier": {},
  "reported_humanitarian_complexity": {},
  "priority_model": {},
  "stress_scenario_aftershock_plus_cold": {},
  "recommended_reasoning_path": ["..."]
}
```

The final reasoning must explain why the response problem is controlled by the interaction of two shallow high-intensity shocks, route/bridge exposure indicators, broad SAR/embedding surface-change context, subfreezing nights, and cross-border humanitarian constraints.
