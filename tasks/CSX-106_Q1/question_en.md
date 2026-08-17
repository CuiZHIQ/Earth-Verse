# Ophelia Peak-Timing Ledger

In mid-October 2017, Hurricane Ophelia crossed into the Ireland and UK weather window while losing tropical structure. A hydrometeorology analyst needs a compact timing ledger from the hourly point-weather record near the Dublin coast: do the wind, gust, pressure, and rainfall extrema form one synchronized peak, or do they split into a late wind-pressure pulse and offset rainfall peaks?

Build the ledger from the event-window weather series. Report the peak gust, peak 10 m wind speed, minimum sea-level pressure, point rainfall total, and the tied hourly rainfall maxima. Then compute the hour offsets between the gust peak, pressure minimum, and the nearest and earliest rainfall maxima, plus the rainfall accumulated within 3 hours on either side of the gust peak.

Return a short proof followed by compact JSON:

```json
{
  "target_family": "temporal_peak_consistency_ledger",
  "answer": "...",
  "peak_values": {
    "peak_gust_kmh": null,
    "peak_wind_speed_kmh": null,
    "minimum_pressure_hpa": null,
    "point_rainfall_total_mm": null,
    "hourly_rainfall_peak_mm": null
  },
  "peak_times": {
    "gust": "...",
    "wind": "...",
    "pressure": "...",
    "rain_peak_times": []
  },
  "timing_tests": {
    "wind_gust_same_hour": null,
    "pressure_lag_hours_after_gust": null,
    "nearest_rain_peak_lag_hours_before_gust": null,
    "earliest_rain_peak_lag_hours_before_gust": null,
    "rain_mm_within_3h_of_gust": null
  },
  "computed_interpretation": "..."
}
```
