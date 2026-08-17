# Black Summer Fire-Weather Smoke Threshold Ledger

A fire-weather review team is checking whether the 2019-2020 Australian Black Summer in southeastern Australia satisfies a compact compound-cascade threshold test. The task is to compute the ledger, not to write a broad disaster narrative.

Use the technical record to apply these definitions:

Treat the daily weather series as a package point-weather diagnostic and the Sentinel-2 dNBR summary as an early-season burn-change threshold signal, not as a full-season burned-area inventory or a national representativeness claim.

- `hot_dry_day`: daily maximum temperature `>= 40.0 C` and daily precipitation `< 1.0 mm`.
- `very_hot_dry_windy_day`: daily maximum temperature `>= 45.0 C`, daily precipitation `< 1.0 mm`, and daily maximum 10 m wind speed `>= 30.0 km/h`.
- `burn_change_gate`: the mean Sentinel-2 dNBR is `> 0.10`.
- `pyrocb_or_firestorm_text`: the incident narrative explicitly supports pyrocumulonimbus, fire-triggered cloud, or firestorm behavior.
- `stratospheric_smoke_text`: the incident narrative explicitly supports smoke reaching 15-19 km altitude or the stratosphere.

Return `answer = "compound_fire_weather_smoke_threshold_pass"` only if the longest hot-dry run is at least 10 days, the longest very-hot-dry-windy run is at least 2 days, and all three burn/smoke text gates are true. Otherwise return `answer = "compound_fire_weather_smoke_threshold_fail"`.

Return compact JSON:

```json
{
  "target_family": "threshold_ledger",
  "metrics": {
    "longest_hot_dry_run_days": 0,
    "longest_very_hot_dry_windy_run_days": 0,
    "peak_tmax_c": 0,
    "sentinel2_dnbr_mean": 0
  },
  "gates": {
    "hot_dry_run_ge_10": false,
    "vhdw_run_ge_2": false,
    "burn_change_mean_gt_0_10": false,
    "pyrocb_or_firestorm_text": false,
    "stratospheric_smoke_text": false
  },
  "answer": "short_label",
  "rejected_alternative": "short_label",
  "computed_consequence": "one sentence tied only to the ledger"
}
```
