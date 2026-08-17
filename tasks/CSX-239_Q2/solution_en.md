# Correct Answer

```json
{
  "answer": "tsunami_timing_ledger_consistent",
  "origin_utc": "2004-12-26T00:58:50",
  "sumatra_arrival_utc": "2004-12-26T01:28:50",
  "thailand_window_utc": "2004-12-26T02:28:50/2004-12-26T02:58:50",
  "sri_lanka_window_utc": "2004-12-26T02:58:50/2004-12-26T03:58:50",
  "lag_span_min": 150,
  "gpm_mean_mm": 0.214,
  "catalog_counts": {
    "eq_features": 5,
    "fl_features": 1,
    "main_eq_magnitude": 8.5,
    "main_eq_alert": "Red"
  }
}
```

# Calculation Path

The GDACS clock anchor is the Red Indonesia EQ entry at `2004-12-26T00:58:50`, magnitude `8.5`. The same GDACS package window contains `5` EQ features and `1` FL feature.

The USGS report gives lag bounds of `30` minutes for northern Sumatra, "an hour and a half to two hours" for Thailand (`90-120` minutes), and "two to three hours" for Sri Lanka (`120-180` minutes). Adding those parsed lags to `2004-12-26T00:58:50` gives:

- Sumatra: `2004-12-26T01:28:50`
- Thailand: `2004-12-26T02:28:50/2004-12-26T02:58:50`
- Sri Lanka: `2004-12-26T02:58:50/2004-12-26T03:58:50`

The lag span is `180 - 30 = 150` minutes. GPM mean precipitation is `0.21391763732970523 mm`, rounded to `0.214 mm`, which is below the 1 mm threshold. All stated tests are satisfied, so the label is `tsunami_timing_ledger_consistent`.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "counterfactual_rejection": "A rainfall-flood timing explanation fails because the rounded GPM mean is below 1 mm while the report supplies coherent tsunami lag windows.",
    "evidence_weighting": "GDACS origin time and USGS lag text are decisive for arrival windows; GPM precipitation is an exclusion check against rainfall-driven timing.",
    "uncertainty_or_scale_caveat": "The GDACS magnitude is used as the local clock anchor and should not be confused with the USGS magnitude used in broader mechanism discussion."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

Total: 20 points.

- 4 points: Uses the GDACS Red Indonesia EQ clock anchor with origin `2004-12-26T00:58:50`, magnitude `8.5`, and catalog counts `5` EQ and `1` FL.
- 4 points: Parses all three report lag windows from text: northern Sumatra `30`, Thailand `90-120`, and Sri Lanka `120-180` minutes.
- 4 points: Correctly reconstructs the three UTC arrival fields with seconds preserved.
- 4 points: Computes `lag_span_min = 150` and rounds `gpm_mean_mm` to `0.214`.
- 4 points: Returns compact JSON with `answer = tsunami_timing_ledger_consistent` and limits conclusions to computed timing fields.
