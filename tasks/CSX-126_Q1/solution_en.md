# Final Answer

```json
{
  "answer": "compound_oman_landfall_rain_gust_pressure_window",
  "rows": [
    {
      "row_id": "landfall_peak_day_concentration",
      "calculation": "148.6/170.2 and 15.7/170.2",
      "value": "170.2 mm total; 0.873 peak-day fraction; 0.092 peak-hour fraction",
      "decision": "pass: landfall-day concentration is strong, but one-hour replacement fails"
    },
    {
      "row_id": "wind_pressure_timing_window",
      "calculation": "inclusive span from 2007-06-06T08:00 to 2007-06-06T12:00; 109.1/53.0",
      "value": "5 h span; 109.1 km/h gust; 53.0 km/h wind; 991.8 hPa pressure; ratio 2.058",
      "decision": "pass: gust, wind, and pressure extrema form a tight same-day timing window"
    },
    {
      "row_id": "independent_daily_same_day_support",
      "calculation": "NASA peak precipitation date equals NASA peak wind date equals Open-Meteo peak rain date; 170.2/69.54",
      "value": "same_day_support=true; NASA total 69.54 mm; NASA peak rain 50.68 mm; NASA peak wind 13.07 m/s; ratio 2.448",
      "decision": "pass: independent daily series supports the same timing with lower magnitude"
    },
    {
      "row_id": "regional_precip_max_context",
      "calculation": "Open-Meteo event total divided by ERA5, GPM, and CHIRPS regional maxima",
      "value": "point-to-regional ratios: ERA5 0.977, GPM 0.658, CHIRPS 0.991",
      "decision": "context: regional maxima inform magnitude but do not replace point-window timing"
    },
    {
      "row_id": "map_layer_nonreplacement_check",
      "calculation": "WorldPop/OSM derived context plus Sentinel pre/post availability",
      "value": "WorldPop 528023.174; OSM elements 1000; Sentinel pre/post 0/0; direct replacement=false",
      "decision": "context: map, exposure, and image layers do not replace the Oman point-window proof"
    }
  ],
  "final_consistency": "Use the co-timed landfall-day rain, gust, wind, and pressure window for the Oman phase; regional precipitation and map/image layers are secondary context."
}
```

# Key Computations

The 168-hour Oman point rainfall total is 170.2 mm. The peak daily total is 148.6 mm on 2007-06-06, so the peak-day concentration is `148.6 / 170.2 = 0.873`. The peak hourly rain is 15.7 mm, so the peak-hour fraction is `15.7 / 170.2 = 0.092`.

The maximum gust is 109.1 km/h at 2007-06-06T08:00, the maximum sustained 10 m wind is 53.0 km/h at 2007-06-06T12:00, and the minimum mean sea-level pressure is 991.8 hPa at 2007-06-06T12:00. The inclusive span is 5 hours, and `109.1 / 53.0 = 2.058`.

The NASA POWER daily series independently supports the same date: total precipitation is 69.54 mm, maximum daily precipitation is 50.68 mm, and maximum wind is 13.07 m/s on 2007-06-06. The Open-Meteo point total is `170.2 / 69.54 = 2.448` times the NASA daily total.

ERA5, GPM, and CHIRPS event maxima are 174.244 mm, 258.798 mm, and 171.783 mm. The Open-Meteo point-to-regional ratios are `0.977`, `0.658`, and `0.991`. WorldPop, OSM, and Sentinel-1 provide derived context only; Sentinel pre/post counts are 0/0.

# Scoring Rubric

- 4 points: Provides the requested compact JSON ledger with the final answer label and all five row labels.
- 4 points: Computes rainfall concentration correctly: 170.2 mm total, 148.6 mm on 2007-06-06, 0.873 peak-day fraction, 15.7 mm peak hour, and 0.092 peak-hour fraction.
- 4 points: Computes the wind-pressure timing window correctly: 109.1 km/h gust at 08:00, 53.0 km/h wind and 991.8 hPa pressure at 12:00, 5 h inclusive span, and 2.058 gust/wind ratio.
- 3 points: Uses the independent daily point series correctly: 69.54 mm total, 50.68 mm precipitation peak, 13.07 m/s wind peak, both on 2007-06-06, and 2.448 Open-Meteo/daily-total ratio.
- 2 points: Computes all three point-to-regional precipitation ratios and treats them as context for magnitude.
- 2 points: Applies the map/image nonreplacement check without using population, amenity, or image summaries as a local loss denominator.
- 1 point: Keeps the final consistency sentence concise and avoids unverified impact or mapped-inundation overclaims.
