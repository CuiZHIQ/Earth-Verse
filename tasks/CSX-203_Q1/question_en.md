# Air-Quality Exposure Consistency Ledger

A technical reviewer is checking whether the January 6-16, 2013 northern and eastern China severe haze episode is internally consistent with an air-quality exposure classification. Compute the threshold ledger below and return JSON only.

Use these formulas and thresholds:

- `aqi_peak_ratio = peak_AQI / 300`.
- `pm25_peak_ratio = peak_PM25_ug_m3 / 25`.
- `air_quality_label = "hazardous_air_quality_exceedance"` when both ratios are greater than 1.
- `max_tmax_c = max(event-window maximum temperature across the available weather summaries)`.
- `dry_day_fraction = dry event-window days / event_days` from the local daily weather series.
- `precip_fraction_max = max(each event-window precipitation total or mean / 5 mm across the available precipitation summaries)`.
- `meteo_label = "cool_dry_low_precip"` when `max_tmax_c < 10`, `dry_day_fraction >= 0.8`, and `precip_fraction_max <= 1`.
- `sensitive_amenity_count = hospital_count + school_count + police_count + fire_station_count`.
- `exposure_index = population_millions * (1 + sensitive_amenity_count / 1000)`.
- `exposure_label = "high_receptor_exposure"` when `population_millions >= 1` and `sensitive_amenity_count >= 50`.
- `counter_signal_count = wildfire_event_count + burn_pre_count + burn_post_count`.
- `counter_label = "no_wildfire_burn_counter_signal"` when `counter_signal_count == 0`.
- `final_label = "air_quality_exposure_consistent"` only when all four labels above satisfy their thresholds; otherwise use `"mixed_or_insufficient"`.

Return this JSON shape:

```json
{
  "aqi_peak_ratio": 0.0,
  "pm25_peak_ratio": 0.0,
  "meteo_context": {
    "max_tmax_c": 0.0,
    "dry_day_fraction": 0.0,
    "precip_fraction_max": 0.0,
    "label": ""
  },
  "exposure_index": 0.0,
  "counter_signal_count": 0,
  "final_label": ""
}
```
