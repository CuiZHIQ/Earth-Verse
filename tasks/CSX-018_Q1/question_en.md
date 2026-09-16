# West Africa Day-Night Heat Persistence Diagnosis

A heat-health methods team is reconstructing the late-March to early-April 2024 humid heat wave over Mali, Burkina Faso, and the Sahel as a thermal persistence problem. The diagnostic question is whether the package evidence supports continuous day-night heat loading, or whether the event is better described as a short peak-temperature episode.

Use only the local CSX-018 event package. Select package-relative evidence for the daily maximum temperature, daily minimum temperature, and apparent-temperature timing values you use.

For 2024-03-31 through 2024-04-04, compute:

- `event_days`: inclusive event duration.
- `hot_day_count_tmax_ge_40c`: number of days with Tmax >= 40 C.
- `hdd40_c_days`: accumulated dry-bulb heat load `sum(max(Tmax - 40, 0))`.
- `hottest_3day_mean_tmax_c`: maximum rolling three-day mean of daily Tmax.
- `warm_night_count_tmin_ge_27c`: number of nights with Tmin >= 27 C.
- `apparent_peak_lead_days`: dry-bulb Tmax peak date minus apparent-temperature peak date, expressed as a positive number of days when the apparent peak occurs earlier.
- `classification`.

Use one decimal place for temperature-derived values. The classification must be `persistent_day_night_heat_load` when every event day reaches Tmax >= 40 C, every event night reaches Tmin >= 27 C, and `hdd40_c_days` exceeds 10 C-days. Otherwise use `single_peak_or_incomplete_heat_load`.

Return compact JSON only with exactly these fields:

```json
{
  "event_days": 0,
  "hot_day_count_tmax_ge_40c": 0,
  "hdd40_c_days": 0.0,
  "hottest_3day_mean_tmax_c": 0.0,
  "warm_night_count_tmin_ge_27c": 0,
  "apparent_peak_lead_days": 0,
  "classification": ""
}
```

The calculation should make clear whether persistence across days and nights, rather than a single afternoon maximum, is the controlling physical signal.
