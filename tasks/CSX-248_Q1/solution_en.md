# Correct Answer

```json
{
  "answer": "compound_onset_gate_met",
  "heat_load_cday": 35.7,
  "hot_spell_days": 9,
  "warm_night_run_days": 7,
  "dry_run_days": 12,
  "hot_dry_overlap_days": 5,
  "local_regional_precip_ratio": 0.657,
  "onset_score": 96.71
}
```

# Calculation Notes

The 2018-05-01 through 2018-06-15 daily weather slice has 35.7 C-days above 25 C. The longest Tmax >= 25 C run lasts 9 days, the longest Tmin >= 16 C run lasts 7 days, the longest precipitation <= 1 mm run lasts 12 days, and the longest hot-dry overlap run lasts 5 days. Local precipitation totals 47.5 mm, while the ERA5-Land regional precipitation mean is 72.25560489748231 mm, giving a local/regional ratio of 0.657 after rounding. The weighted index is 96.71, so the gate label is `compound_onset_gate_met`.

# Scoring Rubric

Total: 20 points

- 4 points: Correctly filters the Open-Meteo daily series to 2018-05-01 through 2018-06-15.
- 4 points: Computes `heat_load_cday` from daily Tmax exceedance above 25 C and rounds to 35.7.
- 3 points: Computes the 9-day Tmax >= 25 C run and the 7-day Tmin >= 16 C run.
- 3 points: Computes the 12-day precipitation <= 1 mm run and the 5-day hot-dry overlap run.
- 3 points: Computes the local precipitation sum, divides by the ERA5-Land regional mean, and rounds the ratio to 0.657.
- 3 points: Applies the weighted formula, rounds `onset_score` to 96.71, and returns the requested compact JSON fields.
