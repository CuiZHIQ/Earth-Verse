# Smoke Window Threshold Ledger

Using only the local CSX-211 package, compute a smoke-window threshold ledger for the June 6-8, 2023 Canadian wildfire-smoke episode over New York City and the U.S. Northeast.

Build a compact JSON result that determines whether the event satisfies the `surface_smoke_pm25_window` label. Use the event dates, source/transport/surface-air text gates, PM2.5 and PM2.5 AQI anchors, vertical smoke-layer heights, and context countermetrics from precipitation, temperature, Sentinel-2 dNBR, and annual embedding change.

Use this scoring rule:

- 1 point: inclusive event window is at least 3 days.
- 1 point: Quebec fire-source text gate is present.
- 1 point: coastal-low southward transport text gate is present.
- 1 point: surface-level air degradation text gate is present.
- 2 points: highest reported PM2.5 is at least 400 ug/m3.
- 2 points: NYC PM2.5 AQI is at least 175 and above the previous record.
- 1 point: near-surface smoke depth is at least 3 km.
- 1 point: aerosol optical depth context is present.

Label as `surface_smoke_pm25_window` when the smoke score is at least 8 and the context countermetric gates stay below threshold.

Use these context countermetric thresholds:

- Surface-change countermetric passes if `sentinel2_dnbr_mean >= 0.1` or `annual_embedding_change_mean >= 0.1`.
- Rainfall countermetric passes if `GPM_mean_precipitation >= 25 mm` or `CHIRPS_mean_precipitation >= 25 mm`.
- Heat countermetric passes if `ERA5_mean_max_temperature >= 35 C` or `ERA5_max_temperature >= 38 C`.

Return compact JSON with: `target_family`, `answer`, `event_window_days`, `smoke_score`, `threshold_ledger`, `gates`, and `computed_consequence`.
