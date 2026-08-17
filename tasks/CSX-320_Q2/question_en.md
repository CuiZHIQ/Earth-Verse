# Mendenhall GLOF Release-Gate Consistency Test

A technical review is checking whether the August 6, 2024 Mendenhall River high-water numbers satisfy a release-dominance rule with a rainfall guardrail and usable corridor-change context.

Compute these quantities:

- `release_mcm = release_billion_gal * 3.785411784`
- `crest_excess_ft = reported_crest_ft - previous_record_crest_ft`
- `flow_floor_m3s = reported_streamflow_floor_cfs * 0.028316846592`
- `precip_mean_max_mm = max(event_window_reanalysis_mean_mm, event_window_satellite_mean_mm, daily_mean_mm)`, treating a missing daily mean as `0` for this maximum
- `radar_span_db = vv_post_minus_pre_max_db - vv_post_minus_pre_min_db`
- `coverage_balance = min(pre_count, post_count) / max(pre_count, post_count)`

Apply these gates:

- `release_gate`: `release_mcm >= 50`
- `river_gate`: `crest_excess_ft >= 1.0` and `flow_floor_m3s >= 900`
- `rainfall_guardrail`: `precip_mean_max_mm < 1.0` and the daily precipitation mean is missing
- `radar_context_gate`: `pre_count >= 5`, `post_count >= 5`, `radar_span_db >= 20`, and `coverage_balance >= 0.5`

Set `answer` to `mendenhall_glof_release_precip_radar_gate_pass` when all four gates pass; otherwise use `mendenhall_glof_release_precip_radar_gate_fail`.

Return compact JSON:

```json
{
  "target_family": "mendenhall_glof_release_precip_radar_gate_consistency",
  "metrics": {
    "release_mcm": 0.0,
    "crest_excess_ft": 0.0,
    "flow_floor_m3s": 0.0,
    "precip_mean_max_mm": 0.0,
    "radar_span_db": 0.0,
    "coverage_balance": 0.0
  },
  "gates": {
    "release_gate": false,
    "river_gate": false,
    "rainfall_guardrail": false,
    "radar_context_gate": false
  },
  "answer": "<label>",
  "computed_consequence": "<short consequence derived from the gates>"
}
```
