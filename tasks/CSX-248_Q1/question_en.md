# CSX-248 Q1: Heat-Dry Onset Index

Use the local CSX-248 event package to compute a deterministic onset index for the 2018 Northern and Central Europe heatwave, drought, wildfire, and low-river-flow compound event.

Select package-local daily weather evidence for Tmax, Tmin, and precipitation from 2018-05-01 through 2018-06-15, and select package-local regional precipitation evidence over the same slice. Keep the calculation reproducible from package-relative sources.

Derive these quantities from the package data:

1. `heat_load_cday = sum(max(temperature_2m_max - 25.0, 0))`.
2. `hot_spell_days = longest consecutive run with temperature_2m_max >= 25.0`.
3. `warm_night_run_days = longest consecutive run with temperature_2m_min >= 16.0`.
4. `dry_run_days = longest consecutive run with precipitation_sum <= 1.0`.
5. `hot_dry_overlap_days = longest consecutive run with temperature_2m_max >= 25.0 and precipitation_sum <= 1.0`.
6. `local_regional_precip_ratio = local precipitation sum / ERA5-Land precipitation_sum_mm_mean`.
7. `onset_score = 100 * (0.25 * min(heat_load_cday / 35.0, 1) + 0.15 * min(hot_spell_days / 9.0, 1) + 0.15 * min(warm_night_run_days / 7.0, 1) + 0.20 * min(dry_run_days / 12.0, 1) + 0.20 * min(hot_dry_overlap_days / 5.0, 1) + 0.05 * max(0, min(1, 1 - local_regional_precip_ratio)))`.

Set `answer` to `compound_onset_gate_met` when `onset_score >= 90`; otherwise set it to `compound_onset_gate_not_met`.

Return only a compact JSON object with:

```json
{
  "answer": "",
  "heat_load_cday": 0.0,
  "hot_spell_days": 0,
  "warm_night_run_days": 0,
  "dry_run_days": 0,
  "hot_dry_overlap_days": 0,
  "local_regional_precip_ratio": 0.0,
  "onset_score": 0.0
}
```
