# Final Answer

```json
{
  "diagnosis_label": "peak_hour_burst_embedded_in_wet_event_window",
  "hourly_peak_mm": 201.9,
  "event_window_mean_mm": {
    "gpm": 426.1,
    "chirps": 256.635,
    "era5_land": 214.341
  },
  "peak_share_of_means": {
    "gpm": 0.474,
    "chirps": 0.787,
    "era5_land": 0.942
  },
  "product_spread_ratio": 1.988,
  "context_metrics": {
    "population_rounded": 11097000,
    "road_ways": 252,
    "bridge_tagged": 108,
    "critical_service_nodes": 48,
    "sentinel1_vv_change_mean_db": 0.854,
    "alphaearth_change_mean": 0.045
  },
  "interpretation": "The 201.9 mm Zhengzhou hour is a peak-hour burst inside a wet 2021-07-17 to 2021-07-23 window: all three mean precipitation products exceed 200 mm, and the hourly peak is 47.4%, 78.7%, and 94.2% of those event-window means."
}
```

# Key Computations

The answer is `peak_hour_burst_embedded_in_wet_event_window`.

- GPM mean precipitation: `426.100 mm`; hourly share: `201.9 / 426.100 = 0.474`.
- CHIRPS mean precipitation: `256.635 mm`; hourly share: `201.9 / 256.635 = 0.787`.
- ERA5-Land mean precipitation: `214.341 mm`; hourly share: `201.9 / 214.341 = 0.942`.
- Product spread ratio: `426.100 / 214.341 = 1.988`.
- Context checks: WorldPop rounds to `11,097,000`; the compact Overpass layer has `252` road ways, `108` bridge-tagged ways, and `48` critical service nodes; Sentinel-1 VV mean change is `0.854 dB`; AlphaEarth mean change is `0.045`.

# Reasoning Path

The gridded rainfall summaries all describe a wet multi-day event window, not a dry background with one isolated hour. The reported Zhengzhou hourly peak is still large relative to each accumulated mean, especially against CHIRPS and ERA5-Land, so the correct calibration keeps both facts together: a concentrated peak-hour burst within a high-accumulation event.

The GPM-to-ERA5-Land spread is almost two-to-one, so the lowest mean should not be used as a severity cap. The three products agree on the wet-window conclusion despite their different magnitudes.

The population, road, bridge, service-node, Sentinel-1, and AlphaEarth values are useful cross-checks for urban context and surface change. They do not replace the rainfall timing calculation and should not be converted into exact loss, outage, or flood-depth values.

# Computed Interpretation

The calibrated short answer is that Zhengzhou's July 20 signal is a peak-hour rainfall burst embedded in a wet event window. The decisive calculation is not the largest product alone; it is the joint pattern of all three event means above 200 mm plus a one-hour total that equals about one-half to nearly all of those event-window means.

# Scoring Rubric

- 3 points: Returns the requested JSON shape and gives the diagnosis label `peak_hour_burst_embedded_in_wet_event_window` or a clear equivalent.
- 5 points: Reports the 201.9 mm hourly peak, the three event-window means near 426.100, 256.635, and 214.341 mm, and the three peak-share ratios near 0.474, 0.787, and 0.942.
- 3 points: Uses the all-products-above-200 mm check and the 1.988 spread ratio to show why the case is not isolated-hour-only and not capped by the lowest product.
- 3 points: Treats rainfall timing and accumulation as the primary calibration, while using Sentinel-1 or AlphaEarth values only as surface-change context.
- 3 points: Gives at least three correct context metrics among population 11,097,000, road ways 252, bridge-tagged ways 108, and critical service nodes 48.
- 3 points: Keeps the interpretation concise and avoids invented casualty, outage, facility-failure, or flood-depth values.
