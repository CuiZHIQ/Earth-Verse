# July 2021 Western Europe Flood Timing Diagnosis

A hydrometeorology review team is checking a proposed diagnosis for the July 12-16, 2021 Western Europe floods in Germany and Belgium. The diagnosis says the event record is most consistent with a regional, multi-day rainfall-to-flood timing pattern rather than an isolated one-hour point rainfall burst.

Compute the timing and rainfall checks needed to test that diagnosis. Use inclusive day counts for date intervals and round ratios or percentages to three decimals unless a value naturally has fewer decimals.

Return compact JSON with this shape:

```json
{
  "target_family": "regional_multiday_rainfall_timing_diagnosis",
  "computed_values": {
    "event_days": 0,
    "catalog_union_days": 0,
    "catalog_overlap_days": 0,
    "union_event_share": 0.0,
    "overlap_event_share": 0.0,
    "gpm_max_mean_ratio": 0.0,
    "era5_max_mean_ratio": 0.0,
    "gridded_max_agreement_pct": 0.0,
    "point_peak_hour_total_ratio": 0.0,
    "point_peak_hour_gpm_max_ratio": 0.0,
    "point_total_power_total_ratio": 0.0
  },
  "test_results": {
    "catalog_timing": "pass_or_fail",
    "gridded_rainfall": "pass_or_fail",
    "point_burst_rejection": "pass_or_fail",
    "daily_point_crosscheck": "pass_or_fail"
  },
  "score": 0,
  "max_score": 4,
  "final_label": "one_short_label",
  "one_sentence_interpretation": "one concise sentence tied to the computed values"
}
```

Use these pass rules: catalog timing passes if the country-event union covers at least 75% of the five-day event window and the two country spans overlap for at least two days; gridded rainfall passes if the two gridded maxima agree within 99.5% and both max-to-mean ratios exceed 2.0; point-burst rejection passes if the peak hour is no more than 15% of the point total and no more than 15% of the gridded maximum; daily point crosscheck passes if the point total is within 10% of the independent daily point total. The final label should be `regional_multiday_rainfall_timing_diagnosis` only if all four tests pass.
