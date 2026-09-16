# Final Answer

```json
{
  "aqi_peak_ratio": 2.583,
  "pm25_peak_ratio": 35.44,
  "meteo_context": {
    "max_tmax_c": 7.875,
    "dry_day_fraction": 1.0,
    "precip_fraction_max": 0.206,
    "label": "cool_dry_low_precip"
  },
  "exposure_index": 10.972,
  "counter_signal_count": 0,
  "final_label": "air_quality_exposure_consistent"
}
```

# Key Computations

The local report gives AQI values of 341 and 775, so `aqi_peak_ratio = 775 / 300 = 2.583`. It gives PM2.5 values of 291 and 886 ug/m3, so `pm25_peak_ratio = 886 / 25 = 35.44`. Both exceed 1, producing `hazardous_air_quality_exceedance`.

For the event window, the maximum temperature across the weather summaries is 7.875 C. The local daily weather series has 11 dry days over 11 event days, so `dry_day_fraction = 1.0`. The largest normalized precipitation fraction is from the gridded precipitation mean: `1.030 / 5 = 0.206`. These satisfy `max_tmax_c < 10`, `dry_day_fraction >= 0.8`, and `precip_fraction_max <= 1`, producing `cool_dry_low_precip`.

Population is 9.3296 million. Sensitive amenities are 45 hospitals, 50 schools, 70 police facilities, and 11 fire stations, for `sensitive_amenity_count = 176`. Therefore `exposure_index = 9.3296 * (1 + 176 / 1000) = 10.972`, and the exposure label is `high_receptor_exposure`. The competing-signal count is `0 wildfire events + 0 pre burn scenes + 0 post burn scenes = 0`, giving `no_wildfire_burn_counter_signal`.

All four threshold labels pass, so the final label is `air_quality_exposure_consistent`.

# Reasoning Path

The ledger first checks air-quality intensity. The peak AQI and PM2.5 ratios both exceed their reference thresholds, so the air-quality row passes. It then checks the meteorological context: the maximum temperature stays below `10 C`, all 11 local daily records are dry, and the largest normalized precipitation fraction is only `0.206`, so the cool-dry-low-precip row passes.

The exposure row is population-normalized rather than a health-outcome claim. The population and sensitive-amenity count produce an exposure index of `10.972`, which passes the receptor screen. The counter-signal row then sums wildfire events and pre/post burn scenes; all are zero, so no wildfire/burn counter-signal is present.

All four rows pass, giving `air_quality_exposure_consistent`. The computed inequalities reject heat, heavy-precipitation, and wildfire/burn readings as the controlling numeric pattern.

# Computed Interpretation

The ledger supports an air-quality exposure consistency result: pollutant ratios and receptor density pass, while heat, precipitation, and wildfire/burn counter-signals do not control the screen.

# Scoring Rubric

Total: 20 points.

- 4 points: Requested JSON schema. Full credit for returning exactly the requested six top-level fields and the nested `meteo_context` fields. Partial credit: 2-3 points for a mostly complete object with one missing or renamed field.
- 4 points: Air-quality ratios. Full credit for computing AQI ratio 2.583 and PM2.5 ratio 35.44 within stated tolerances. Partial credit: 2 points for one correct ratio or 3 points for both ratios with minor rounding issues.
- 4 points: Meteorology fields. Full credit for computing max_tmax_c 7.875, dry_day_fraction 1.0, precip_fraction_max 0.206, and `meteo_context.label = cool_dry_low_precip`. Partial credit: proportional credit for correct temperature, dry fraction, precipitation fraction, and label.
- 5 points: Exposure and counter fields. Full credit for computing exposure_index 10.972 and counter_signal_count 0 from the package exposure and counter-signal inputs. Partial credit: 2-3 points for one correct field and 4 points for both with minor rounding issues.
- 3 points: Final label rule. Full credit for applying the four threshold rows and returning `final_label = air_quality_exposure_consistent`. Partial credit: 1-2 points if the row values are mostly correct but the final label is omitted or slightly misnamed.
