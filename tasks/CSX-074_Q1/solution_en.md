# Final Answer

```json
{
  "target_family": "regional_multiday_rainfall_timing_diagnosis",
  "computed_values": {
    "event_days": 5,
    "catalog_union_days": 4,
    "catalog_overlap_days": 2,
    "union_event_share": 0.8,
    "overlap_event_share": 0.4,
    "gpm_max_mean_ratio": 2.279,
    "era5_max_mean_ratio": 2.343,
    "gridded_max_agreement_pct": 99.97,
    "point_peak_hour_total_ratio": 0.077,
    "point_peak_hour_gpm_max_ratio": 0.14,
    "point_total_power_total_ratio": 1.056
  },
  "test_results": {
    "catalog_timing": "pass",
    "gridded_rainfall": "pass",
    "point_burst_rejection": "pass",
    "daily_point_crosscheck": "pass"
  },
  "score": 4,
  "max_score": 4,
  "final_label": "regional_multiday_rainfall_timing_diagnosis",
  "one_sentence_interpretation": "The timing and rainfall ratios support a regional multi-day rainfall-to-flood diagnosis rather than an isolated one-hour point-burst explanation."
}
```

# Key Computations

The event window is July 12-16, 2021 inclusive, so `event_days = 5`.

Germany spans July 13-15 inclusive, `3` days. Belgium spans July 14-16 inclusive, `3` days. The country-span intersection is July 14-15 inclusive, `2` days, and the union is July 13-16 inclusive, `4` days. Therefore `union_event_share = 4 / 5 = 0.800` and `overlap_event_share = 2 / 5 = 0.400`.

The gridded rainfall maxima are `53.5049987 mm` and `53.4888834 mm`; their absolute difference is `0.016115 mm`, giving `gridded_max_agreement_pct = 99.970`. The max-to-mean ratios are `53.5049987 / 23.4759267 = 2.279` and `53.4888834 / 22.8291021 = 2.343`.

The point rainfall total is `97.1 mm`, the point peak hour is `7.5 mm`, and the independent daily point total is `91.96 mm`. Thus `point_peak_hour_total_ratio = 7.5 / 97.1 = 0.077`, `point_peak_hour_gpm_max_ratio = 7.5 / 53.5049987 = 0.140`, and `point_total_power_total_ratio = 97.1 / 91.96 = 1.056`.

# Reasoning Path

The catalog timing test passes because the country-event union covers `0.800` of the five-day event window, above the `0.750` rule, and the Germany-Belgium overlap lasts `2` days.

The gridded rainfall test passes because the maximum rainfall estimates agree at `99.970%`, above the `99.5%` rule, and both max-to-mean ratios are greater than `2.0`.

The point-burst test rejects a one-hour point-burst explanation because the peak hour is only `0.077` of the point total and `0.140` of the gridded maximum, both below the 0.15 rejection ceilings.

The daily point crosscheck passes because the point total divided by the independent daily total is `1.056`, which is within 10% of unity. With four passing tests, the score is `4/4` and the final label is `regional_multiday_rainfall_timing_diagnosis`.

# Computed Interpretation

The computed pattern is a multi-day regional rainfall-timing signal with a local point series that supports the event window but does not dominate it as a single-hour burst.

# Scoring Rubric

- 4 points: Returns the requested compact JSON with target family, computed values, four test results, score, final label, and one concise interpretation. Partial credit: 2-3 points if one block is missing or several field names are malformed but the answer is still gradable.
- 4 points: Computes the event and country timing values correctly: `5` event days, `4` union days, `2` overlap days, `0.800` union share, and `0.400` overlap share. Partial credit: 2-3 points for correct day counts with one share or inclusive-date mistake.
- 3 points: Computes gridded rainfall agreement and concentration: `99.970%` maximum agreement, `2.279` GPM max-to-mean ratio, and `2.343` ERA5 max-to-mean ratio. Partial credit: 1-2 points for using the right rainfall values but missing one derived metric.
- 3 points: Computes the point rainfall burst ratios: `0.077` peak-hour share of point total and `0.140` peak-hour share of gridded maximum. Partial credit: 1-2 points for correct point total and peak hour without both ratios.
- 2 points: Computes the daily point crosscheck ratio `1.056` and applies the within-10% rule. Partial credit: 1 point for reporting the two daily totals but not the ratio or rule.
- 2 points: Applies all four pass rules correctly and reports score `4/4`. Partial credit: 1 point if one pass rule is misapplied while the final direction remains consistent.
- 1 point: Gives the exact final label `regional_multiday_rainfall_timing_diagnosis`. Partial credit: 0.5 points for a close label that preserves the same meaning.
- 1 point: Keeps the interpretation concise and avoids turning point rainfall, exposure, or broad context into a direct whole-event cause or loss estimate. Partial credit: 0.5 points for a mostly concise interpretation with one weak extra inference.
