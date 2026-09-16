# Sao Sebastiao Rain-Slope Evidence Ledger

Using the local data, compute a 0-6 numeric evidence ledger for the February 18-21, 2023 Sao Sebastiao rain-flood-landslide event. Use calculation, threshold checks, and compact JSON. Use these deterministic rules:

1. In the storm-date and pre-date true-color scenes, count a pixel as bright when mean RGB is at least 220, and count it as cloud-like when all three RGB channels are at least 200 and the channel spread is at most 35. Compute `cloud_ratio = storm_cloud_share / pre_cloud_share` and `bright_ratio = storm_bright_share / pre_bright_share`.
2. From the event-window gridded precipitation summaries, compute `max_grid_precip_mm`, `min_grid_precip_mm`, and `grid_product_max_spread_mm = max_grid_precip_mm - min_grid_precip_mm`. This spread is a cross-product maximum-value spread, not a within-grid spatial spread. From the event report text, extract the stated 24-hour rainfall floor in millimeters and compute `report_to_grid_ratio = reported_24h_rain_floor_mm / max_grid_precip_mm`.
3. Count five report markers: saturated soils, flooding, widespread landslides, steep or hilly terrain, and building-or-highway damage.
4. Score the ledger as `obscuration_component + rainfall_component + report_component + low_change_component - wind_penalty`, clamped to 0-6, where:
   - `obscuration_component = int(cloud_ratio >= 4) + int(bright_ratio >= 10)`
   - `rainfall_component = int(max_grid_precip_mm >= 50) + int(report_to_grid_ratio >= 10)`
   - `report_component = int(report_marker_count == 5)`
   - `low_change_component = int(annual_cosine_change_mean < 0.10 and abs(dNBR_mean) < 0.10)`
   - `wind_penalty = int(max_event_window_daily_wind_kmh >= 70)`

Return compact JSON:

```json
{
  "answer": "score_<score>_of_6",
  "ledger": {
    "score_0_to_6": 0,
    "cloud_ratio": 0.0,
    "bright_ratio": 0.0,
    "reported_24h_rain_floor_mm": 0,
    "max_grid_precip_mm": 0.0,
    "grid_product_max_spread_mm": 0.0,
    "report_to_grid_ratio": 0.0,
    "report_marker_count": 0,
    "low_change_component": 0,
    "wind_penalty": 0
  },
  "label": "<short ledger label>"
}
```
