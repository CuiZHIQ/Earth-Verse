# Heat-Wave Persistence Decomposition

A climatology analyst is reviewing the June 25-July 1, 2021 Pacific Northwest heat-wave record. The goal is to determine whether the heat signal is mostly a peak-day spike or a distributed persistence-and-recovery pattern in the daily and hourly meteorological series.

For the event window, compute these derived indices:

- `total_heat_load_c_day = sum(max(Tmax - 30 C, 0))`
- `peak_day_heat_share = max(max(Tmax - 30 C, 0)) / total_heat_load_c_day`
- `non_peak_heat_load_c_day = total_heat_load_c_day - max(max(Tmax - 30 C, 0))`
- `hot_run_days = longest consecutive run with Tmax >= 30 C`
- `warm_night_share_in_hot_run = count(Tmin >= 16 C within that longest hot run) / hot_run_days`
- `wet_bulb_margin_to_24c = 24 C - max(hourly wet-bulb temperature)`, using the Stull approximation from hourly air temperature and relative humidity.

Set `diagnosis` to `persistence_recovery_dry_heat_signature` if the non-peak heat load exceeds the peak-day heat load, the hot run lasts at least three days, at least half of the hot-run nights meet the warm-night threshold, and the wet-bulb margin remains positive.

Return JSON:

```json
{
  "total_heat_load_c_day": <number>,
  "peak_day_heat_share": <number>,
  "non_peak_heat_load_c_day": <number>,
  "hot_run_days": <integer>,
  "warm_night_share_in_hot_run": <number>,
  "wet_bulb_margin_to_24c": <number>,
  "diagnosis": "<label>"
}
```

After the JSON, add one sentence explaining what the decomposition shows.
