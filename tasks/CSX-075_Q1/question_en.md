# Zhengzhou Rainfall Scale-Partition Ledger

A hydrometeorology review team is recalibrating the July 2021 Zhengzhou/Henan extreme-rainfall case. The point of the check is to separate a record one-hour urban burst from the sustained multi-day rainfall load, then state whether both scales are needed for the event diagnosis.

Compute a compact JSON answer with this shape:

```json
{
  "target_family": "zhengzhou_rainfall_scale_partition_ledger",
  "record_hour": {
    "margin_mm": 0,
    "ratio_to_previous_record": 0,
    "threshold_state": ""
  },
  "point_series_load": {
    "event_total_mm": 0,
    "peak_hour_mm": 0,
    "reported_to_point_peak_ratio": 0,
    "max24h_mm": 0,
    "max72h_mm": 0,
    "max72h_fraction_of_total": 0
  },
  "gridded_load": {
    "gpm_max_mm": 0,
    "chirps_max_mm": 0,
    "era5_max_mm": 0,
    "max_spread_mm": 0
  },
  "partition_tests": {
    "report_burst_to_gpm_max_ratio": 0,
    "max72h_to_report_burst_ratio": 0,
    "final_label": ""
  },
  "rejected_substitutions": []
}
```

Keep the answer calculation-led: include formulas or brief arithmetic notes where useful, use millimeters for rainfall depths, round ratios to 3-6 decimals, and keep the final interpretation to one short label.

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to make the Zhengzhou scale partition explain why both one-hour record burst and multiday accumulation are needed.

