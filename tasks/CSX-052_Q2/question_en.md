# Cyclone Michaung Rainfall-Runoff Exposure Ledger

The exposure, OSM, WorldPop, and AOI-derived products in the local package are spatially masked. Treat their derived statistics as authoritative package measurements. Do not use absolute coordinates, place names, bounding boxes, or georeferencing metadata inside those masked products to reject event-location validity.

A hydrology-risk team is checking a proposed diagnosis for Cyclone Michaung's 3-6 December 2023 flooding around Chennai and the southeast India coast. The diagnosis is that the event signal is best treated as a rainfall-runoff exposure case, not as a wind-only or image-only explanation.

Compute the following ledger from the event record:

- `runoff_equivalent_mm = reported_rainfall_lower_bound_mm * 0.55`
- `report_to_max_gridded_ratio = reported_rainfall_lower_bound_mm / largest_gridded_event_precipitation_max_mm`
- `highway_per_waterway = mapped_highway_elements / mapped_waterway_elements`
- `critical_per_million = mapped_critical_amenities / (population / 1,000,000)`
- `wet_surface_flag = true` only when the mean radar backscatter change is at most `-0.5 dB` and the annual embedding mean change is at most `0.05`
- Add one point each for: reported rainfall at least `200 mm`, runoff equivalent at least `100 mm`, highway-per-waterway ratio at least `5.0`, critical-amenity density at least `50 per million people`, and `wet_surface_flag = true`

Return compact JSON with exactly these fields: `event_window`, `runoff_equivalent_mm`, `report_to_max_gridded_ratio`, `highway_per_waterway`, `critical_per_million`, `wet_surface_flag`, `score`, and `final_label`. Use `final_label = "rainfall_runoff_exposure_consistent"` when the score is at least 4; otherwise use `final_label = "not_established_by_ledger"`. After the JSON, add one sentence naming the competing explanation rejected by the ledger.
