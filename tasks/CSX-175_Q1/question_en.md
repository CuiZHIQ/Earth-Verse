# Smoke-Burden Calculation Ledger

A technical reviewer is checking a numeric smoke-burden ledger for the May 2023 Canadian wildfire smoke episode. Build the ledger from the incident record's reported AOD observations, burned-area anomaly statement, and local satellite-context summaries.

Use these rules:

- Treat the quoted upper bound for a perfectly clear blue sky as the clear-sky AOD threshold.
- Use the two reported AERONET daily-average AOD station observations as the station-days.
- Use the Grand Forks peak AOD statement only for the peak-to-mean ratio.
- A station-day is an exceedance when its daily-average AOD is greater than the clear-sky threshold.
- `aod_excess_load = sum(max(mean_AOD - clear_sky_AOD, 0))` over the two station-days.
- `burned_area_baseline_ha = reported_burned_hectares / reported_seasonal_anomaly_factor`.

Return a concise JSON object with exactly these keys:

```json
{
  "aod_excess_load": 0.0,
  "station_exceedance_count": 0,
  "station_exceedance_fraction": 0.0,
  "grand_forks_clear_sky_multiplier": 0.0,
  "grand_forks_vs_goddard_mean_ratio": 0.0,
  "grand_forks_peak_to_mean_ratio": 0.0,
  "burned_area_baseline_ha": 0,
  "diagnosis": "short_label"
}
```

Round ratios and AOD load to two decimals, and round the burned-area baseline to the nearest hectare. After the JSON, add one sentence stating whether the AOD ledger is consistent with a severe regional smoke-burden episode and whether the local satellite-change metrics can be converted into PM2.5 exposure hours.
