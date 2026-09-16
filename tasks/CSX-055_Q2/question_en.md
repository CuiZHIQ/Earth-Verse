# Basin Rainfall Routing and Flood-Response Stress Model

Use only the local CSX-055 event package. Cite package-relative evidence for every reported value or text claim you use, and keep the analysis driven by the disaster process rather than by file inventory.

Reconstruct the late April-May 2024 Rio Grande do Sul flood as a coupled rainfall-loading, river-routing, surface-inundation, and response-pressure problem. Use event reports, the locked event window, gridded precipitation summaries, remote-sensing products or images, and mapped exposure data where relevant.

Compute the following model components:

1. `event_duration_days`: inclusive days from the package's event start date through event end date.
2. `burst_min_daily_rate_mm_day`: use 300 mm as the conservative lower bound for the reported rainfall burst of more than 300 mm in less than one week, divided by 7 days.
3. `duration_to_burst_reference_ratio`: `event_duration_days / 7`.
4. `gpm_localization_ratio`: event-accumulated GPM maximum divided by GPM mean.
5. `product_peak_spread_ratio`: largest event-accumulated precipitation maximum across the available ERA5-Land, GPM, and CHIRPS summaries divided by the smallest of those three maxima.
6. `rainfall_loading_index`: `(300 / event_duration_days) * gpm_localization_ratio * product_peak_spread_ratio`.
7. `visual_inundation_score`: compare the package's pre-event and during-event true-color images after converting each image to RGB and resizing both to a 256 x 192 grid with bicubic resampling. Use `dark_pixel_share = share of pixels with RGB mean < 60` and `brown_water_proxy_share = share of pixels with r > g > b, r > 70, and r - b > 25`. Compute event-minus-pre gains, then calculate `0.5 * min(dark_gain / 0.15, 1) + 0.5 * min(brown_gain / 0.07, 1)`.
8. `sar_water_change_score`: `min(abs(mean Sentinel-1 VV post-minus-pre dB change) / 2, 1)`.
9. `annual_land_change_score`: `min(mean annual 1-minus-cosine embedding change / 0.06, 1)`.
10. `surface_inundation_norm`: `0.45 * visual_inundation_score + 0.35 * sar_water_change_score + 0.20 * annual_land_change_score`.
11. From mapped exposure data, count population, road elements carrying a `highway` tag, and critical amenities with `amenity` in `{hospital, clinic, fire_station, police, school, shelter}`. Compute `critical_amenities_per_10000_people` and `road_elements_per_10000_people`.
12. `exposure_access_norm`: `0.40 * min(population / 60000, 1) + 0.35 * min(critical_amenities_per_10000_people / 3, 1) + 0.25 * min(road_elements_per_10000_people / 15, 1)`.
13. `compound_basin_flood_stress`:  
   `100 * (0.30 * min(burst_min_daily_rate_mm_day / 50, 1) + 0.20 * min(event_duration_days / 35, 1) + 0.20 * ((min(gpm_localization_ratio / 4, 1) + min(product_peak_spread_ratio / 2, 1)) / 2) + 0.15 * surface_inundation_norm + 0.15 * exposure_access_norm)`.
14. `routing_amplifier`: start at `1.0`; add `0.10` if the reports describe overtopping of the Jacui, Cai, and Sinos rivers; add `0.05` if the reports describe brown sediment-laden runoff into Patos Lagoon; add `0.05` if they describe transport disruption such as airport closure or impassable highways.
15. `routed_response_stress`: `compound_basin_flood_stress * routing_amplifier`.
16. A sensitivity case: increase the reported burst lower bound by 15 percent, keep the duration, precipitation ratios, remote-sensing terms, exposure terms, and routing amplifier fixed, and recompute `rainfall_loading_index`, `compound_basin_flood_stress`, and `routed_response_stress`.

Return compact JSON with this structure:

```json
{
  "source_paths": {
    "event_window": [],
    "event_process_report": [],
    "precipitation": [],
    "remote_sensing": [],
    "exposure": []
  },
  "process_model": {
    "event_duration_days": 0,
    "burst_min_daily_rate_mm_day": 0.0,
    "duration_to_burst_reference_ratio": 0.0,
    "gpm_localization_ratio": 0.0,
    "product_peak_spread_ratio": 0.0,
    "rainfall_loading_index": 0.0,
    "surface_inundation_norm": 0.0,
    "exposure_access_norm": 0.0,
    "routing_amplifier": 0.0,
    "compound_basin_flood_stress": 0.0,
    "routed_response_stress": 0.0
  },
  "remote_sensing_metrics": {
    "dark_pixel_share_gain": 0.0,
    "brown_water_proxy_gain": 0.0,
    "visual_inundation_score": 0.0,
    "sar_water_change_score": 0.0,
    "annual_land_change_score": 0.0
  },
  "exposure_metrics": {
    "population": 0.0,
    "road_elements": 0,
    "critical_amenities": 0,
    "road_elements_per_10000_people": 0.0,
    "critical_amenities_per_10000_people": 0.0
  },
  "scenario_analysis": {
    "burst_increase_percent": 15,
    "scenario_rainfall_loading_index": 0.0,
    "scenario_compound_basin_flood_stress": 0.0,
    "scenario_routed_response_stress": 0.0,
    "routed_response_stress_delta": 0.0
  },
  "mechanism_chain": [
    "",
    "",
    ""
  ],
  "final_interpretation": ""
}
```
