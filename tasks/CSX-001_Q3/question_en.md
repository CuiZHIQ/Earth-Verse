# Heat-Dome Physiology and Cooling-Response Stress Model

You are the duty scientist for a regional heat emergency cell preparing the June 2021 Pacific Northwest heat-wave briefing. The package contains local hourly/daily weather, regional reanalysis summaries, event reports, exposure context, and remote-sensing context.

Your task is to build a mechanism-first heat-stress model from the local package. Do not search the web. The model must discover which files matter, compute the key heat physiology quantities, compare local heat stress with broader regional context, and reason through a modest future-warming stress test.

Return JSON with exactly these top-level fields:

```json
{
  "answer": "<short snake_case label>",
  "event_window": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "daily_rows": 0,
    "hourly_rows": 0
  },
  "source_files_used": ["<package-relative path>", "..."],
  "heat_stress_physiology": {
    "peak_daily_tmax_c": 0,
    "peak_tmax_date": "YYYY-MM-DD",
    "peak_apparent_temperature_c": 0,
    "heat_load_c_days_above_30c": 0,
    "hot_hours_t_ge_30c": 0,
    "warm_nights_tmin_ge_16c": 0,
    "wet_bulb_hours_ge_20c": 0
  },
  "regional_and_future_stress": {
    "era5_aoi_peak_c": 0,
    "local_minus_era5_c": 0,
    "future_plus_1c_peak_tmax_c": 0,
    "future_plus_1c_heat_load_c_days_above_30c": 0
  },
  "attribution_and_vulnerability_clues": {},
  "exposure_context": {},
  "recommended_reasoning_path": ["..."]
}
```

The final reasoning must explain the chain from persistent heat to daytime load, nighttime recovery, humid-hour physiology, vulnerable cooling access, and response prioritization.
