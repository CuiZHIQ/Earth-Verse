# Sao Sebastiao Rainfall-Slope Trigger Diagnostic

A technical review team is checking the February 2023 Sao Sebastiao, Brazil floods and landslides. The team needs a compact calculation diagnostic that tests whether the event is best summarized as an extreme local rainfall and slope-failure trigger, rather than as a drainage-only, basin-storage, coarse-grid-rainfall, image-count, seasonal, or delayed-failure explanation.

Compute the trigger diagnostic from the technical record and return only compact JSON with this shape. When the report says the storm produced more than 680 mm in 24 hours, use 680 mm as the conservative lower-bound rainfall input for all reported-rainfall calculations.

```json
{
  "rainfall": {
    "reported_24h_mm": 0,
    "mean_24h_mm_h": 0,
    "ratio_to_250mm_day": 0,
    "threshold_state": ""
  },
  "process_flags": {
    "score": 0,
    "max_score": 7,
    "state": ""
  },
  "grid_ratios": {
    "reported_to_gpm_max": 0,
    "reported_to_era5_max": 0,
    "gpm_peak_to_mean": 0,
    "era5_peak_to_mean": 0,
    "state": ""
  },
  "observation_timing": {
    "post_lag_days": 0,
    "pre_lead_days": 0,
    "sentinel1_mean_db_change": 0,
    "annual_surface_change_mean": 0,
    "state": ""
  },
  "population_exposure": {
    "worldpop_population": 0,
    "state": ""
  },
  "trigger_score": {
    "score": 0,
    "max_score": 6,
    "state": ""
  },
  "final_answer": "",
  "rejected_alternatives": []
}
```

Use these scoring tests: reported rainfall at least 250 mm/day, 24-hour mean intensity at least 20 mm/h, process flags at least 6 of 7, local rainfall report not replaced by coarse gridded maxima, post-event observation timing is compatible with scar or surface-change checking, and exposed population is at least 10,000. Round ratios and rates to three decimals where needed. Keep the final answer to one concise label and the rejected alternatives to compact tokens.
