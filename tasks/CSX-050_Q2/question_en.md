# Rainfall-Runoff Reconciliation Ledger

A hydrology analyst is reconciling fixed event-summary values for the July 12-16, 2021 Western Europe flood episode in the Ahr-Meuse region. The goal is to produce a compact numeric ledger for concentrated rainfall and direct runoff, not a general flood narrative.

Use these extracted event values:

- report-box 48-hour rainfall: 104.0 mm
- Jalhay station 48-hour rainfall: 271.0 mm
- Spa station 48-hour rainfall: 217.0 mm
- direct-runoff fraction from the event rainfall: 20-25%
- local ERA5-Land event-precipitation maximum: 53.489 mm
- local GPM IMERG event-precipitation maximum: 53.505 mm
- terrain setting for the label: steep valleys, thin soils, and small to medium rivers

Return a compact JSON object with exactly these fields: `target_family`, `runoff_mm`, `station_to_box`, `station_mean_to_gridded_max`, `gridded_pair_gap_percent`, `gates`, `final_label`, and `computed_consequence`.

Round ratios and percentages to three decimals. In `gates`, report four booleans: `runoff_ge20mm`, `both_stations_ge2x_box`, `gridded_pair_gap_le0_1pct`, and `station_mean_ge4_5x_gridded_max`. Use `concentrated_station_rainfall_runoff_reconciled` only when all four gates are true; otherwise use a shorter label that names the failed gate family.
