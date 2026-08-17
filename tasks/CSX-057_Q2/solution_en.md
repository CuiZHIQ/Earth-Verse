# Final Answer

```json
{
  "event_duration_days": 7,
  "peak_gauge_mm": 1224.3,
  "hobby_4day_mm": 904.2,
  "two_day_mm": 609.6,
  "four_day_to_two_day_ratio": 1.483,
  "two_day_peak_share": 0.498,
  "min_20in_volume_km3": 38.16,
  "per_person_min_volume_m3": 5694.9,
  "threshold_state": "pass_multiday_volume; fail_two_day_only",
  "diagnosis_label": "multi_day_broad_area_record_rainfall"
}
```

# Key Computations

- Event window: August 25 through August 31, 2017 gives `7` inclusive days.
- Highest reported gauge total: `48.20 in * 25.4 = 1224.3 mm`.
- Houston Hobby four-day total: `35.6 in * 25.4 = 904.2 mm`.
- Two-day Houston amount: `24.0 in * 25.4 = 609.6 mm`.
- Duration ratio: `904.2 / 609.6 = 1.483`.
- Two-day share of the highest gauge total: `609.6 / 1224.3 = 0.498`.
- Minimum 20-inch broad-area volume: `0.508 m * 29000 * 1609.344^2 m2 = 3.81557e10 m3 = 38.16 km3`.
- Per-person minimum volume over 6.7 million people: `3.81557e10 / 6700000 = 5694.9 m3/person`.

# Reasoning Path

The diagnostic satisfies the multi-day volume test because the event lasted seven days, the maximum gauge total exceeded 1000 mm, the four-day Hobby total was 1.483 times the two-day amount, and the broad-area 20-inch minimum volume exceeded 35 km3 and 5000 m3 per exposed person. The two-day-only explanation fails because the two-day amount is only 0.498 of the highest reported gauge total while the four-day total remains substantially larger than the two-day amount. The correct compact diagnosis is therefore a multi-day broad-area record-rainfall regime.

# Computed Interpretation

Harvey's Houston flooding is best anchored by sustained, very large rainfall accumulation and broad-area water volume, not by a short two-day burst alone.

# Scoring Rubric

Total: 20 points.

- 3 points: Final JSON diagnostic is complete, uses the requested field names, and gives the correct threshold state and diagnosis label. Partial credit: 1-2 points for a mostly correct diagnostic with one or two missing fields.
- 4 points: Inch-to-millimeter conversions and inclusive duration are correct: 7 days, 1224.3 mm, 904.2 mm, and 609.6 mm. Partial credit: proportional credit for each correct value, with formula mistakes capped at 2 points.
- 3 points: Duration ratios are correct: four-day to two-day ratio 1.483 and two-day peak share 0.498. Partial credit: 1-2 points for using the right formulas with rounding or one arithmetic error.
- 4 points: Minimum volume and per-person volume are correct: 38.16 km3 and 5694.9 m3/person. Partial credit: 2 points for the correct volume method with a unit-conversion error, or 1 point for identifying the needed area-depth multiplication only.
- 3 points: Applies both threshold tests correctly and states `pass_multiday_volume; fail_two_day_only`. Partial credit: 1-2 points for one correct threshold state or correct logic with one missed inequality.
- 2 points: Explains why the two-day-only interpretation fails using the computed ratios rather than generic flood wording. Partial credit: 1 point if the rejection is present but tied to only one computed value.
- 1 point: Keeps the interpretation concise and does not add loss estimates beyond the computed rainfall-volume diagnostic. Partial credit: no credit if the answer turns into a broad disaster essay.
