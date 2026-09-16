# Pacific Drought Deficit Ledger

A technical review team is checking whether the 2015-2016 tropical Pacific drought record satisfies an extreme water-deficit threshold, using the reported Koror/Palau rainfall amounts, the stated local drinking-water conditions, and the gridded precipitation summaries for the local June 1-July 16 analysis window.

Compute a compact numeric ledger. Use these formulas:

- `normal_rain_in = observed_rain_in + below_average_in`
- `observed_fraction = observed_rain_in / normal_rain_in`
- `deficit_fraction = below_average_in / normal_rain_in`
- `deficit_mm = below_average_in * 25.4`
- the deficit threshold passes only if `observed_fraction <= 1/3` and `deficit_fraction >= 2/3`
- `water_source_stress_score = stressed_drinking_water_source_flags / 2`, where the two flags are the main dam being dry and the other drinking-water source being very low
- `coverage_fraction = inclusive_local_window_days / inclusive_event_window_days`
- for the three accumulated-precipitation mean products, compute their ensemble mean, range, and range as a percent of the ensemble mean

Return a compact JSON object with:

```json
{
  "answer": "<short numeric diagnosis label>",
  "palau_deficit": {
    "observed_fraction": 0.0,
    "deficit_fraction": 0.0,
    "deficit_mm": 0.0,
    "threshold_pass": true
  },
  "water_source_stress_score": 0.0,
  "local_window": {
    "event_days": 0,
    "local_days": 0,
    "coverage_fraction": 0.0
  },
  "precipitation_spread": {
    "ensemble_mean_mm": 0.0,
    "range_mm": 0.0,
    "range_pct_of_mean": 0.0
  },
  "interpretation": "<one sentence tying the numeric ledger to drought-stress consistency>"
}
```
