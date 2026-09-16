# Fire-Smoke Threshold Ledger

A technical review team is checking whether the 2019-2020 Australian bushfire smoke and hazardous air-quality episode satisfies a compound fire-smoke threshold ledger using only deterministic counts, ratios, loads, and pass/fail tests.

Use the available NASA POWER daily weather slice in the package for the weather-load calculation; this slice covers 2019-09-01 through 2019-10-16 and should not be expanded by inferring missing daily weather values for the rest of the broader 2019-2020 event window.

Compute the following quantities from the event data and return a compact JSON object with exactly these six top-level keys:

```json
{
  "fire_smoke_load": {"fire_count": 0, "smoke_score": 0.0, "load": 0.0, "pass": false},
  "burn_contrast": {"dnbr_max": 0.0, "dnbr_mean": 0.0, "ratio": 0.0, "pass": false},
  "weather_load": {"heat_c_days": 0.0, "dry_days": 0, "days": 0, "max_wind_mps": 0.0, "load": 0.0, "pass": false},
  "precipitation_clearing": {"point_total_max_mm": 0.0, "gridded_mean_max_mm": 0.0, "absent_score": 0, "pass": false},
  "exposure_normalized_index": {"population": 0.0, "index": 0.0, "per_1000_people": 0.0, "pass": false},
  "classification": ""
}
```

Use these rules:

- `fire_count` is the number of wildfire catalog point events inside Australia bounds (112 to 154 E, 44 to 10 S) during the event window. `smoke_score` is the fraction of three smoke-report terms present: `smoke`, `hazardous air quality`, and `transported across the Pacific`. `fire_smoke_load = fire_count * smoke_score`; pass if `fire_count >= 10` and `smoke_score = 1`.
- `ratio = dnbr_max / dnbr_mean`; pass if `dnbr_max >= 0.6`, `dnbr_mean < 0.1`, and `ratio >= 10`.
- `heat_c_days = sum(max(Tmax - 35 C, 0))` over the available NASA POWER daily fire-weather slice, `dry_days` counts precipitation `<= 0.1 mm/day`, and `weather_load = heat_c_days * (dry_days / days) * (1 + max_wind_mps / 10)`. Pass if `weather_load >= 40` and `dry_days / days >= 0.9`.
- `precipitation_clearing.absent_score = 1` if the larger point-source event precipitation total is `<= 1 mm` and the larger gridded precipitation mean is `< 5 mm`; otherwise it is `0`. Pass when the score is `1`.
- `index = fire_smoke_load.load * burn_contrast.ratio * weather_load.load * precipitation_clearing.absent_score`. `per_1000_people = index / (population / 1000)`. Pass if `per_1000_people >= 1000`.

Round continuous values to two decimals except `dnbr_max` and `dnbr_mean`, which may use four decimals. Use classification `compound_fire_smoke_hazard_supported` only if all five ledger components pass; otherwise use `compound_fire_smoke_hazard_not_supported`.
