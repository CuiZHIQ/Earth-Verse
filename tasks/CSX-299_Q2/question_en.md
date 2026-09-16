# Patagonian Dust Streamer Source-Gate Check

For the 6 February 2020 Patagonian dust streamer event near Comodoro Rivadavia, test a counterfactual mechanism calibration: the same dry event-day numeric conditions occur, and the NASA report provides report-context downwind transport evidence, but the exposed dry fine sediment at the lakebed source is absent.

Use this deterministic gate:

`score = source_gate * lift_gate * wind_align_gate * dry_precip_gate * transport_gate`

Set the observed source gate from the event's source-material indicators. For the counterfactual calculation, force `source_gate = 0`. Set `dry_precip_gate = 1` only when both event-day precipitation means are at or below 0.1 mm, and set `transport_gate = 1` only when the report-context eastward reach is at least 120 km. Compute the observed score and the counterfactual score. Also report the annual maximum-to-mean surface-change ratio as a timing check; it must not replace the event-day source gate.

Return compact JSON:

```json
{
  "evidence_windows": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "precip_wind_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "transport_report_context_date": "YYYY-MM-DD_or_report_context"
  },
  "answer": "<source_gate_pass or source_gate_fail>",
  "observed_chain_score": 0,
  "counterfactual_chain_score": 0,
  "source_flags_present": 0,
  "dry_precip_product_count": 0,
  "transport_distance_km_lower_bound": 0,
  "annual_change_max_to_mean_ratio": 0.0
}
```

Round the annual ratio to two decimals. Keep any interpretation to one short computed consequence.
