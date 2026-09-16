# Final Answer

The correct answer is `all_five_tests_pass`.

```json
{
  "target_family": "ian_landfall_threshold_window_ledger",
  "ledger_rows": [
    {
      "row": "wind_pressure_window",
      "formula_or_test": "peak_gust_time == min_pressure_time and pressure_fall_24h_hpa >= 40",
      "values": {
        "local_peak_gust_kmh": 185.4,
        "local_peak_gust_time": "2022-09-28T19:00",
        "local_peak_wind_kmh": 105.7,
        "local_peak_wind_time": "2022-09-28T18:00",
        "gust_to_wind_ratio": 1.754,
        "local_min_pressure_hpa": 966.9,
        "local_min_pressure_time": "2022-09-28T19:00",
        "pressure_fall_6h_hpa": 29.5,
        "pressure_fall_12h_hpa": 35.9,
        "pressure_fall_24h_hpa": 42.5,
        "hours_gust_ge_100_kmh": 13,
        "hours_gust_ge_119_kmh": 10,
        "hours_wind_ge_63_kmh": 9,
        "hours_wind_ge_100_kmh": 2
      },
      "pass": true,
      "reason": "The peak gust and pressure minimum coincide at 2022-09-28T19:00, and the 24-hour pressure fall is 42.5 hPa."
    },
    {
      "row": "rainfall_concentration_window",
      "formula_or_test": "event_precip_mm > 200 and wettest_24h_mm / event_precip_mm > 0.65",
      "values": {
        "event_precip_mm": 211.5,
        "wettest_hour_mm": 14.4,
        "wettest_hour_time": "2022-09-28T22:00",
        "wettest_6h_mm": 67.0,
        "wettest_24h_mm": 149.9,
        "wettest_48h_mm": 188.0,
        "wettest_24h_share": 0.709,
        "wettest_48h_share": 0.889
      },
      "pass": true,
      "reason": "The event total exceeds 200 mm and 70.9% falls within the wettest 24 hours."
    },
    {
      "row": "peak_timing_window",
      "formula_or_test": "wind_pressure_window_pass and rain_pressure_lag_hours <= 6",
      "values": {
        "gust_pressure_lag_hours": 0.0,
        "peak_wind_pressure_lag_hours": 1.0,
        "rain_pressure_lag_hours": 3.0
      },
      "pass": true,
      "reason": "The wettest hour is 3 hours after the pressure minimum while gust and pressure extrema are simultaneous."
    },
    {
      "row": "catalog_station_wind_check",
      "formula_or_test": "catalog_alertlevel == 'Red' and local_gust_to_catalog_wind_ratio >= 0.70 and local_gust_squared_proxy_kmh2 >= 30000",
      "values": {
        "catalog_peak_wind_kmh": 250.0,
        "catalog_alertlevel": "Red",
        "local_gust_to_catalog_wind_ratio": 0.742,
        "local_gust_squared_proxy_kmh2": 34373.2
      },
      "pass": true,
      "reason": "The Red catalog entry and 0.742 local gust ratio pass the wind consistency thresholds."
    },
    {
      "row": "precipitation_product_check",
      "formula_or_test": "daily_total_precip_mm >= 150 and daily_peak_precip_mm >= 50 and min(grid_max_mean_ratios) >= 4",
      "values": {
        "daily_total_precip_mm": 157.7,
        "daily_peak_precip_day": "20220927",
        "daily_peak_precip_mm": 70.9,
        "daily_peak_wind_day": "20220928",
        "era5_precip_max_mm": 46.63,
        "era5_precip_mean_mm": 9.55,
        "era5_precip_max_mean_ratio": 4.882,
        "gpm_precip_max_mm": 53.22,
        "gpm_precip_mean_mm": 10.08,
        "gpm_precip_max_mean_ratio": 5.281,
        "chirps_precip_max_mm": 73.14,
        "chirps_precip_mean_mm": 14.72,
        "chirps_precip_max_mean_ratio": 4.968
      },
      "pass": true,
      "reason": "The daily point total, peak daily rain, and all three gridded maximum-to-mean ratios pass their thresholds."
    }
  ],
  "final_classification": "all five Ian landfall threshold windows pass",
  "numeric_summary": {
    "event_window": {
      "start_date": "2022-09-23",
      "end_date": "2022-09-30"
    },
    "passed_rows": 5,
    "pressure_fall_24h_hpa": 42.5,
    "event_precip_mm": 211.5,
    "wettest_24h_share": 0.709,
    "rain_pressure_lag_hours": 3.0
  }
}
```

# Key Computations

The wind-pressure row uses `185.4 / 105.7 = 1.754` for the gust-to-wind ratio. The peak gust occurs at `2022-09-28T19:00`, the pressure minimum is `966.9 hPa` at the same hour, and the pressure falls are `29.5 hPa` over 6 hours, `35.9 hPa` over 12 hours, and `42.5 hPa` over 24 hours.

The rainfall row sums the hourly precipitation to `211.5 mm`. The wettest windows are `67.0 mm` over 6 hours, `149.9 mm` over 24 hours, and `188.0 mm` over 48 hours. The corresponding event shares are `149.9 / 211.5 = 0.709` and `188.0 / 211.5 = 0.889`.

The timing row compares extrema times: gust-pressure lag is `0.0 h`, peak-wind-pressure lag is `1.0 h`, and rain-pressure lag is `3.0 h`.

The catalog-station wind row uses catalog peak wind `250.0 km/h`, alert level `Red`, local gust ratio `185.4 / 250.0 = 0.742`, and squared gust proxy `185.4^2 = 34373.2 kmh2`.

The precipitation-product row uses daily point precipitation total `157.7 mm`, daily peak `70.9 mm` on `20220927`, and peak wind day `20220928`. The gridded ratios are computed from the source max and mean values before display rounding: ERA5 `46.63 / 9.55 / 4.882`, GPM `53.22 / 10.08 / 5.281`, and CHIRPS `73.14 / 14.72 / 4.968`.

# Reasoning Path

All five rows pass their stated numeric tests. The wind-pressure row passes because the gust and pressure extrema share the same hour and the 24-hour pressure fall exceeds `40 hPa`. The rainfall row passes because event rainfall is above `200 mm` and the wettest 24-hour share is above `0.65`. The timing row passes because the rainfall peak is within the 6-hour window after the pressure minimum.

The catalog-station row passes because the catalog alert is `Red`, the local gust is more than 70% of the catalog peak wind, and the squared gust proxy is above `30000 kmh2`. The precipitation-product row passes because the daily point series and all three gridded summaries meet their thresholds.

# Computed Interpretation

The calculation-led result is a compact Ian landfall threshold-window pass: the local wind-pressure extrema, rainfall concentration, peak timing, catalog wind check, and precipitation-product check agree on the same high-intensity landfall interval.

# Scoring Rubric

- 4 points: Returns the required JSON shape with `target_family`, exactly five named `ledger_rows`, `formula_or_test`, `values`, `pass`, `reason`, `final_classification`, and `numeric_summary`. Partial credit: 2-3 points for one missing row or minor schema omissions; 1 point for prose with recognizable row labels.
- 4 points: Computes the wind-pressure anchors accurately, including gust-to-wind ratio, pressure minimum, pressure falls, and threshold-hour counts. Partial credit: 2-3 points for mostly correct wind and pressure values with one missing derived value; 1 point for copying only peak wind or pressure values.
- 4 points: Computes rainfall totals over the locked event window, rolling wettest windows, event shares, and timing lags accurately. Partial credit: 2-3 points for correct totals but one wrong rolling window or lag; 1 point for qualitative rainfall statements without calculations.
- 3 points: Applies the threshold tests correctly for the 40 hPa pressure fall, 200 mm event rainfall, 0.65 wettest-day share, 6-hour timing window, 0.70 catalog gust ratio, 30000 kmh2 gust proxy, and gridded ratio threshold of 4. Partial credit: 1-2 points for correct pass/fail calls with one or two threshold mistakes.
- 2 points: Uses the catalog and precipitation-product checks as numeric consistency tests, including grid ratios computed from source max/mean values before display rounding, without substituting catalog wind for station values or mixing daily and hourly totals. Partial credit: 1 point for including these checks but omitting one required ratio or day.
- 2 points: Provides the final answer `all_five_tests_pass` and the classification "all five Ian landfall threshold windows pass." Partial credit: 1 point for an equivalent final result with incomplete wording.
- 1 point: Keeps the answer concise and calculation-led, without adding casualty totals, damage totals, or other claims not computed in the ledger. Partial credit: 0.5 points for one minor extra claim that does not change the numeric answer.
