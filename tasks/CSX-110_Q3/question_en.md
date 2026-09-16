# Cyclone Freddy Rainfall Lag and Humanitarian Access Model

You are preparing a high-level scientific operations note for Cyclone Freddy. The package includes storm/event catalog data, hourly wind-rain-pressure observations, gridded rainfall summaries, SAR context, a WMO-style report, and exposure files.

Construct a long-duration cyclone impact model. The model must distinguish storm lifetime, persistent rainfall, flood lag, wind/pressure stress, spatial rainfall context, and humanitarian access pressure. It must use calculations, not only prose.

Use only package-local files and cite package-relative paths. Return JSON with exactly these top-level fields:

```json
{
  "answer": "<short snake_case label>",
  "source_files_used": ["<package-relative path>", "..."],
  "storm_lifecycle": {},
  "rain_wind_pressure_diagnosis": {},
  "grid_and_surface_context": {},
  "reported_impact_and_exposure": {},
  "stress_scenario_plus_20pct_rain": {},
  "recommended_reasoning_path": ["..."]
}
```

Use these metric definitions inside the nested sections:

- `storm_lifecycle`: compare the WMO-style reported lifetime with GDACS tropical-cyclone timing, then compute the hour lag from GDACS TC end to the Malawi flood start.
- `rain_wind_pressure_diagnosis`: compute event-total point rain, 1-15 March point rain, wet-hour fraction, wettest 72 h total and window, longest continuous wet run, maximum hourly rain, maximum wind/gust, and minimum pressure.
- `grid_and_surface_context`: compute GPM and CHIRPS event peak precipitation, their peak ratio, and Sentinel-1 VV absolute extreme as `max(abs(s1_vv_post_minus_pre_db_max), abs(s1_vv_post_minus_pre_db_min))`.
- `reported_impact_and_exposure`: combine report-stated impacts with package-derived population, school, hospital, and major-road counts as access-pressure context.
- `stress_scenario_plus_20pct_rain`: recompute the wettest 72 h and 1-15 March rainfall totals after multiplying rainfall by 1.20.

The final explanation should show why the disaster process is a delayed rain-flood and access-stress problem, not just a cyclone-track label.
