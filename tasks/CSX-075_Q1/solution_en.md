# Final Answer

```json
{
  "target_family": "zhengzhou_rainfall_scale_partition_ledger",
  "record_hour": {
    "margin_mm": 3.4,
    "ratio_to_previous_record": 1.017128,
    "threshold_state": "record_hour_threshold_crossed"
  },
  "point_series_load": {
    "event_total_mm": 332.2,
    "peak_hour_mm": 23.3,
    "reported_to_point_peak_ratio": 8.665,
    "max24h_mm": 172.5,
    "max72h_mm": 283.9,
    "max72h_fraction_of_total": 0.85461
  },
  "gridded_load": {
    "gpm_max_mm": 484.255,
    "chirps_max_mm": 307.595,
    "era5_max_mm": 261.561,
    "max_spread_mm": 222.694
  },
  "partition_tests": {
    "report_burst_to_gpm_max_ratio": 0.41693,
    "max72h_to_report_burst_ratio": 1.40614,
    "final_label": "dual_scale_record_burst_and_multiday_load"
  },
  "rejected_substitutions": [
    "burst_only",
    "accumulation_only",
    "point_peak_downgrade"
  ]
}
```

# Key Computations

The reported Zhengzhou one-hour burst is 201.9 mm, and the previous mainland one-hour record is 198.5 mm.

- Record margin: `201.9 - 198.5 = 3.4 mm`.
- Record ratio: `201.9 / 198.5 = 1.017128`.

The nearby hourly point series covers 168 hours and totals 332.2 mm.

- Point peak hour: 23.3 mm at `2021-07-20T02:00`.
- Reported burst to point peak: `201.9 / 23.3 = 8.665`.
- Maximum 24-hour rolling sum: 172.5 mm.
- Maximum 72-hour rolling sum: 283.9 mm.
- 72-hour share of point event total: `283.9 / 332.2 = 0.85461`.

The event-window gridded precipitation maxima are:

- GPM: 484.255 mm.
- CHIRPS: 307.595 mm.
- ERA5-Land: 261.561 mm.
- Max spread across those three maxima: `484.255 - 261.561 = 222.694 mm`.

Partition ratios:

- Reported one-hour burst to GPM maximum event accumulation: `201.9 / 484.2549893 = 0.41693`.
- Point maximum 72-hour load to reported one-hour burst: `283.9 / 201.9 = 1.40614`.

# Reasoning Path

The one-hour record test passes because the 201.9 mm burst is above the previous 198.5 mm record by 3.4 mm. That is a short-duration threshold crossing, not a substitute for the multi-day load.

The point hourly record does not reproduce the 201.9 mm city burst; its peak hour is only 23.3 mm, so the reported burst is 8.665 times larger than the point peak. The same point series still shows sustained load because its 72-hour maximum is 283.9 mm, or 85.461% of the 168-hour total.

The gridded products also show large event-window accumulation. GPM gives the largest maximum, 484.255 mm, while ERA5-Land gives the smallest maximum, 261.561 mm, so the spread is 222.694 mm. The report burst is only 0.41693 of the GPM event maximum, while the point 72-hour load is 1.40614 times the report burst. These ratios show that the event cannot be reduced to either a single burst or only a broad accumulation field.

# Computed Interpretation

The correct diagnosis is `dual_scale_record_burst_and_multiday_load`: the record one-hour Zhengzhou burst establishes the short-duration threshold crossing, and the rolling plus gridded totals establish sustained multi-day rainfall load.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "counterfactual_rejection": "A burst-only reading fails because the 72-hour point load exceeds the reported one-hour burst, while an accumulation-only reading misses the record-hour threshold crossing.",
    "evidence_weighting": "The reported one-hour record anchors the urban burst scale, while the point 72-hour load and gridded maxima anchor multiday accumulation scale.",
    "uncertainty_or_scale_caveat": "The nearby point peak should not be used to downgrade the reported city record because the task explicitly separates point and report scales."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

- 4 points: Returns the requested compact JSON structure, with the target family, four metric groups, final label, and rejected substitutions. Partial credit: up to 2 points for a recognizable but incomplete JSON object, or 1 point for a prose answer with the right final label.
- 4 points: Correctly computes the record-hour margin and ratio, including 201.9 mm, 198.5 mm, 3.4 mm, 1.017128, and the threshold-crossed state. Partial credit: up to 2 points for citing both depths with one correct derived value.
- 4 points: Correctly reports the point-series total, peak hour, reported-to-point ratio, 24-hour maximum, 72-hour maximum, and 72-hour fraction. Partial credit: 2-3 points for mostly correct point-series values with minor rounding or one missing window.
- 3 points: Correctly reports the three gridded maxima and max spread. Partial credit: up to 2 points if at least two gridded maxima and the high multi-day load are correct.
- 3 points: Correctly applies the partition tests, especially 0.41693 for burst/GPM and 1.40614 for 72-hour/report. Partial credit: up to 2 points for one correct partition ratio and a broadly correct dual-scale conclusion.
- 2 points: Rejects burst-only, accumulation-only, and point-peak-downgrade substitutions without adding uncomputed impact assertions. Partial credit: 1 point for rejecting at least two of the three substitutions.
