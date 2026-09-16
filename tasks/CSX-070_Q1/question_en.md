# UAE Rainfall Runoff Diagnostic

During the April 15-17, 2024 record rainfall flood in the United Arab Emirates, a hydrometeorology team is checking whether the event metrics support a rapid-runoff threshold diagnosis rather than relying on a single lower gridded accumulation value.

Using the technical record, compute a compact JSON diagnostic with exactly these fields:

- `airport_runoff_mm`: 0.15 times the Dubai International Airport April 16 rainfall, rounded to 0.1 mm.
- `eastern_runoff_mm`: 0.15 times the eastern UAE less-than-24-hour rainfall maximum, rounded to 0.1 mm.
- `airport_annual_share`: airport rainfall divided by the midpoint of the stated typical annual UAE rainfall range, rounded to 0.01.
- `eastern_annual_share`: eastern rainfall divided by the same annual midpoint, rounded to 0.01.
- `grid_max_to_report_threshold`: highest gridded event accumulation divided by the 100 mm single-day report threshold, rounded to 0.001.
- `threshold_result`: use exactly `reported_runoff_threshold_crossed_grid_peak_lower` when the report rainfall crosses the rapid-runoff threshold and the gridded maximum remains below the 100 mm threshold.

Use round-half-up for the requested one-decimal runoff values, so 17.85 rounds to 17.9. After the JSON, add one sentence explaining the threshold result from the computed values.
