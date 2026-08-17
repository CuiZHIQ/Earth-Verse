# Zhengzhou Rainfall-Transport Role Diagnostic

A hydrometeorology team is reviewing the July 17-23, 2021 Henan/Zhengzhou extreme rainfall and flood. The team needs a compact role diagnostic that tests whether the transport-impact context is consistent with a peak rainfall burst plus multi-day loading diagnosis, while keeping transport receptors and overhead change metrics in their proper supporting roles.

Return only a JSON object with this shape:

```json
{
  "rows": [
    {
      "row_id": "<required row id>",
      "inputs_used": ["<metric names>"],
      "formula": ["<formula strings>"],
      "computed_values": {"<metric>": 0.0},
      "threshold_decision": "<pass/fail or role statement>",
      "failed_substitution": "<one short numeric reason>"
    }
  ],
  "final_label": "<compact diagnosis label>",
  "interpretation": "<one sentence>"
}
```

Required rows and calculations:

1. `burst_runoff_threshold`: convert the reported peak-hour rainfall depth from millimeters over 1 square kilometer to cubic meters using `water_volume = rainfall_mm * 1000`; compute `runoff_volume = water_volume * 0.85`; compute `normalized_runoff_index = runoff_volume / 100000`.
2. `event_window_loading`: compute `reported_3day_total_mm / reported_hourly_peak_mm`, `reported_hourly_peak_mm / reported_3day_total_mm`, and `reported_3day_total_mm / annual_average_mm`; decide whether the rainfall diagnosis needs both the hourly burst and the multi-day load.
3. `gridded_precipitation_check`: compare the three event-window gridded precipitation means, compute their mean, count how many exceed 200 mm, compute their range, and compute the strongest mean divided by the reported three-day total.
4. `transport_receptor_check`: compute the high-capacity road share, bridge-tagged road share, tunnel count, critical service feature count, and the lower-bound train suspensions per million residents using the reported `>160` train suspensions.
5. `remote_change_check`: compute the radar `p90 / abs(mean)` VV change ratio, and include the annual embedding mean/max change plus the true-color mean absolute RGB difference.

Use `peak_burst_window_transport_context_ledger` as the final label only if all five rows preserve that role separation. Do not add narrative outside the JSON.
