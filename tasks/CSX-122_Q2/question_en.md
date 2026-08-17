# Cyclone Freddy Temporal Rainfall-Concentration Test

A hydrometeorology team is preparing a short technical note on Tropical Cyclone Freddy during its February-March 2023 southern Africa phase. The team needs to decide whether the Malawi rainfall signal is better described as a long wet episode with a late concentrated pulse, or as a nearly uniform accumulation with no late concentration.

Using the technical record and quantitative diagnostics, compute a compact ledger with these rows:

1. `duration_alignment`: `wmo_days`, `gdacs_days`, `ratio`, `gap_days`, and `lag_h` from the GDACS tropical-cyclone end to the Malawi flood start.
2. `rainfall_concentration`: `event_mm`, `wet_days`, `wetday_mean_mm`, `late_mm`, `late_share`, `late_day_mean_mm`, and `late_amp`, where `late_amp` compares the late-window daily mean with the event wet-day mean.
3. `peak_window_check`: `max72h_mm`, `max72h_share`, `max168h_mm`, and `max168h_share`.
4. `gridded_contrast`: `gpm_max_mean`, `chirps_max_mean`, and `chirps_gpm_mean`.

For the late rainfall window, use 2023-03-12 through 2023-03-15 inclusive, matching the available hourly and gridded package data.

Return JSON in this shape:

```json
{
  "answer": {
    "duration_alignment": {},
    "rainfall_concentration": {},
    "peak_window_check": {},
    "gridded_contrast": {}
  },
  "classification": "<under 12 words>",
  "not_pattern": "<one short phrase>"
}
```

Round shares and ratios to three decimals unless the diagnostic is naturally reported to two decimals. Round millimetres, days, and hours to one decimal or two decimals as appropriate.
