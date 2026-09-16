# Final Answer

```json
{
  "answer_label": "landfall_day_rain_wind_concentration_pass",
  "ledger": [
    {
      "row": "official_landfall_anchor",
      "formula_or_test": "77 kt * 1.852 = 142.6 km/h; 77 kt >= 64 kt; 970 hPa <= 980 hPa",
      "key_values": {
        "near_oman_landfall_wind_kt": 77,
        "near_oman_landfall_wind_kmh": 142.6,
        "near_oman_landfall_pressure_hpa": 970,
        "official_coastal_rainfall_max_mm": 610,
        "official_muscat_wind_kmh": 100,
        "lifetime_peak_wind_kt_context": 127,
        "lifetime_min_pressure_hpa_context": 920
      },
      "state": "pass"
    },
    {
      "row": "subdaily_rain_concentration",
      "formula_or_test": "rolling_window_share = rolling_window_mm / 170.2 mm",
      "key_values": {
        "event_precip_mm": 170.2,
        "rolling_window_shares_3_6_12_24_48_72h": [0.237, 0.427, 0.669, 0.897, 0.999, 1.0],
        "longest_wet_spell_h": 41
      },
      "state": "pass"
    },
    {
      "row": "wind_pressure_coupling",
      "formula_or_test": "109.1 / 53.0 = 2.06; pressure fall = 14.6 hPa",
      "key_values": {
        "peak_gust_kmh": 109.1,
        "peak_wind_kmh": 53.0,
        "gust_to_wind_ratio": 2.06,
        "min_pressure_hpa": 991.8,
        "pressure_fall_hpa": 14.6,
        "gust_hours_ge_75kmh": 17,
        "gust_hours_ge_100kmh": 4
      },
      "state": "pass"
    },
    {
      "row": "daily_peak_alignment",
      "formula_or_test": "NASA daily precipitation and wind peaks occur on 20070606; Open-Meteo 148.6/170.2 = 0.873",
      "key_values": {
        "nasa_event_precip_mm": 69.54,
        "nasa_peak_daily_precip_date": "20070606",
        "nasa_peak_daily_wind_ms": 13.07,
        "nasa_peak_daily_wind_date": "20070606",
        "openmeteo_landfall_day_precip_share": 0.873
      },
      "state": "pass"
    },
    {
      "row": "area_rain_contrast",
      "formula_or_test": "gridded_event_precip_max_mm / gridded_event_precip_mean_mm",
      "key_values": {
        "era5_max_to_mean_ratio": 4.19,
        "gpm_max_to_mean_ratio": 4.7,
        "chirps_max_to_mean_ratio": 2.81
      },
      "state": "pass"
    }
  ],
  "rejected_alternatives": ["offshore_only", "multi_day_rain_only", "daily_downgrade"],
  "conclusion": "The Muscat-area land record supports a concentrated landfall-day rain-and-wind episode rather than an offshore-only, broad multi-day, or daily-weather-downgrade summary."
}
```

# Key Computations

The official near-Oman-landfall anchor is 77 kt and 970 hPa in the detailed track table. Converting wind gives `77 * 1.852 = 142.6 km/h`; this passes a hurricane-strength landfall check. The 127 kt and 920 hPa values are retained only as lifetime-peak context, not as landfall values.

The local event rainfall total is 170.2 mm. Rolling fractions are `0.237`, `0.427`, `0.669`, `0.897`, `0.999`, and `1.000` for 3 h through 72 h windows, with a 41 h wet spell.

The wind-pressure row gives peak gust 109.1 km/h, peak wind 53.0 km/h, ratio `2.06`, minimum pressure 991.8 hPa, pressure fall 14.6 hPa, and gust-threshold counts of 17 h and 4 h.

NASA POWER has both peak daily precipitation and wind on 20070606, and Open-Meteo assigns 87.3% of event rainfall to that date. Area-rain max/mean ratios are ERA5 4.19, GPM 4.70, and CHIRPS 2.81.

# Scoring Rubric

- 3 points: Gives the exact answer label and a five-row ledger with all required row names, formulas or tests, values, units, and pass/fail states.
- 3 points: Reports near-Oman-landfall 77 kt, 142.6 km/h, 970 hPa, 610 mm, and 100 km/h with threshold tests that all pass; treats 127 kt and 920 hPa only as lifetime-peak context.
- 4 points: Computes the rainfall-window cascade from 170.2 mm, including all six fractions and the 41 h wet spell.
- 3 points: Computes the wind-pressure row: 109.1/53.0 = 2.06, 991.8 hPa, 14.6 hPa fall, 17 h >= 75 km/h, and 4 h >= 100 km/h.
- 3 points: Uses the daily timing cross-check: NASA POWER 69.54 mm, 13.07 m/s, both daily peaks on 20070606, and Open-Meteo 148.6/170.2 = 0.873.
- 2 points: Computes area-rain max/mean contrasts for ERA5 4.19, GPM 4.70, and CHIRPS 2.81.
- 2 points: Rejects offshore-only, multi-day-rain-only, and daily-downgrade alternatives using the row results.
