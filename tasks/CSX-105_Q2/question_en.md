# Hurricane Ian Threshold-Window Ledger

A meteorology team is preparing a calculation note for Hurricane Ian's September 2022 Florida landfall. The open question is whether the local wind, pressure, and rainfall time series jointly satisfy a compact threshold-window diagnosis, and whether those station-level results remain numerically consistent with the catalog wind and independent precipitation summaries.

Use the package's locked event window as the calculation window for hourly, daily, and gridded precipitation products. Compute gridded maximum-to-mean ratios from the source max and mean values before rounding the displayed ratios.

Return only compact JSON in the shape below. Use exactly the five rows listed here. Each row must include the formula or test used, the relevant numeric values with units in the keys, a boolean pass/fail result, and a one-sentence reason.

```json
{
  "target_family": "ian_landfall_threshold_window_ledger",
  "ledger_rows": [
    {
      "row": "wind_pressure_window",
      "formula_or_test": "",
      "values": {},
      "pass": true,
      "reason": ""
    }
  ],
  "final_classification": "",
  "numeric_summary": {}
}
```

Rows and tests:

1. `wind_pressure_window`: test whether the peak gust and minimum pressure occur at the same hour and whether the maximum 24-hour pressure fall is at least 40 hPa. Include peak gust, peak sustained wind, gust-to-wind ratio, pressure minimum, 6-hour/12-hour/24-hour pressure falls, and counts of hours with gusts at or above 100 and 119 km/h and sustained wind at or above 63 and 100 km/h.
2. `rainfall_concentration_window`: test whether event precipitation exceeds 200 mm and the wettest 24-hour share exceeds 0.65. Include event precipitation, wettest hour, wettest 6-hour/24-hour/48-hour totals, and the 24-hour and 48-hour event shares.
3. `peak_timing_window`: test whether the wind-pressure row passes and whether the wettest hour is within 6 hours of the pressure minimum. Include gust-pressure, peak-wind-pressure, and rain-pressure lags in hours.
4. `catalog_station_wind_check`: test whether the catalog alert is Red, the local gust is at least 70% of the catalog peak wind, and the squared local gust proxy is at least 30000 kmh2. Include the catalog peak wind, alert level, local gust-to-catalog-wind ratio, and squared local gust proxy.
5. `precipitation_product_check`: test whether the daily point precipitation total is at least 150 mm, its peak day is at least 50 mm, and each gridded accumulation maximum-to-mean ratio is at least 4. Include the daily total and peak day/value plus the three maximum, mean, and maximum-to-mean ratio pairs.
