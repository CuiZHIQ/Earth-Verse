# Compound Typhoon Consistency Ledger

Super Typhoon Yagi affected Hainan, southern China, northern Viet Nam, and nearby rainfall-affected areas during 1-7 September 2024. A technical reviewer is testing whether the event diagnosis can be reduced to one compact weather-layer signal.

Build a calculation ledger that proves or rejects that reduction. Use the inclusive event window and compute the requested quantities from the event evidence. Round derived ratios to two decimals.

Use these rules:

- `wind_kmh_from_133_mph = 133 * 1.609344`.
- `wind_difference_kmh = abs(wind_kmh_from_133_mph - reported_landfall_wind_kmh)`.
- `rain_mm_from_25_cm = 25 * 10`.
- `rain_difference_mm_between_25cm_and_10in = abs(rain_mm_from_25_cm - 10 * 25.4)`.
- `reported_wind_unit_pair_ratio = wind_kmh_from_133_mph / reported_landfall_wind_kmh`.
- `rain_unit_pair_ratio = rain_mm_from_25_cm / (10 * 25.4)`.
- `regional_to_gridded_peak_rainfall_ratio = reported_regional_rainfall_mm / larger_event_accumulated_gridded_precipitation_max_mm`.
- `gridded_rain_max_ratio = larger_event_accumulated_gridded_precipitation_max_mm / smaller_event_accumulated_gridded_precipitation_max_mm` across the two event-accumulated precipitation products.
- `evacuees_per_death_report_threshold = evacuated_people_threshold / deaths_threshold`.
- `houses_per_death_report_threshold = damaged_or_destroyed_houses_threshold / deaths_threshold`.

Set `unit_pairs_consistent` to `true` only if `wind_difference_kmh <= 2` and `rain_difference_mm_between_25cm_and_10in <= 5`. Set `compact_weather_layer_passes` to `true` only if `regional_to_gridded_peak_rainfall_ratio <= 3` and both impact threshold ratios are below 50. Set `single_layer_diagnosis_passes` to `true` only if the unit pairs are consistent and the compact weather-layer test passes.

Return only JSON in this shape:

```json
{
  "answer": "<compact diagnosis label>",
  "event_window_days": 0,
  "unit_checks": {
    "wind_kmh_from_133_mph": 0,
    "wind_difference_kmh": 0,
    "rain_mm_from_25_cm": 0,
    "rain_difference_mm_between_25cm_and_10in": 0
  },
  "hazard_contrasts": {
    "reported_wind_unit_pair_ratio": 0,
    "rain_unit_pair_ratio": 0,
    "regional_to_gridded_peak_rainfall_ratio": 0,
    "gridded_rain_max_ratio": 0
  },
  "impact_ratios": {
    "evacuees_per_death_report_threshold": 0,
    "houses_per_death_report_threshold": 0
  },
  "consistency_tests": {
    "unit_pairs_consistent": true,
    "compact_weather_layer_passes": false,
    "single_layer_diagnosis_passes": false
  },
  "conclusion": "<one sentence>"
}
```
