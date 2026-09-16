# Zhengzhou Rainfall Concentration Calibration

Using the CSX-051 event package, calibrate the July 2021 Zhengzhou flood signal from real data rather than from a broad narrative. Determine whether the 201.9 mm one-hour report is an isolated cloudburst signal or a peak-hour concentration embedded in a wet multi-day event window.

Compute the ratios of the one-hour peak to the three event-window mean precipitation products. Then use population, road/service counts, and pre/post surface-change summaries only as context checks after the rainfall calibration.

Round rainfall means, ratios, spread, and surface-change metrics to three decimals; round the one-hour peak to one decimal and population to the nearest thousand.

Return JSON only:

```json
{
  "diagnosis_label": "",
  "hourly_peak_mm": 0,
  "event_window_mean_mm": {
    "gpm": 0,
    "chirps": 0,
    "era5_land": 0
  },
  "peak_share_of_means": {
    "gpm": 0,
    "chirps": 0,
    "era5_land": 0
  },
  "product_spread_ratio": 0,
  "context_metrics": {
    "population_rounded": 0,
    "road_ways": 0,
    "bridge_tagged": 0,
    "critical_service_nodes": 0,
    "sentinel1_vv_change_mean_db": 0,
    "alphaearth_change_mean": 0
  },
  "interpretation": ""
}
```
