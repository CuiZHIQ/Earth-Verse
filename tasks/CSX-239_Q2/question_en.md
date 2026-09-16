# Indian Ocean Tsunami Arrival-Window Ledger

Use the local CSX-239 package for the 26 December 2004 Indian Ocean tsunami. Build a calculation-only timing ledger from the GDACS event list, the USGS report text, and the event-day GPM precipitation summary.

Use the Red Indonesia earthquake in GDACS as the clock anchor. Extract the three stated tsunami lag windows for northern Sumatra, Thailand, and Sri Lanka from the USGS report, then convert those lag windows to UTC clock windows by adding them to the GDACS origin time.

Compute:

1. `origin_utc` from the GDACS clock anchor.
2. `sumatra_arrival_utc` from the 30-minute northern Sumatra lag.
3. `thailand_window_utc` from the 90-120 minute Thailand lag.
4. `sri_lanka_window_utc` from the 120-180 minute Sri Lanka lag.
5. `lag_span_min = latest_sri_lanka_lag_min - earliest_sumatra_lag_min`.
6. `gpm_mean_mm`, rounded to three decimals.
7. `catalog_counts` for GDACS EQ and FL features, plus the main EQ magnitude and alert color.

Set `answer` to `tsunami_timing_ledger_consistent` only if all three report windows are present, the GDACS clock anchor is a Red earthquake with magnitude at least 8.0, and rounded GPM mean precipitation is below 1 mm. Otherwise set it to `timing_ledger_incomplete`.

Return only compact JSON:

```json
{
  "answer": "",
  "origin_utc": "",
  "sumatra_arrival_utc": "",
  "thailand_window_utc": "",
  "sri_lanka_window_utc": "",
  "lag_span_min": 0,
  "gpm_mean_mm": 0.0,
  "catalog_counts": {
    "eq_features": 0,
    "fl_features": 0,
    "main_eq_magnitude": 0.0,
    "main_eq_alert": ""
  }
}
```

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

For this task, use that object to make the tsunami timing ledger explain why timing and low precipitation jointly reject rainfall as the arrival-window explanation.

