# 2022 Pakistan Monsoon Floods: Process-Chain Control Point Ranking

A hydrometeorology team is moving from a consistency ledger to a process-chain diagnosis for the 2022 Pakistan monsoon floods. The task is to rank which control points most govern the diagnosis from monsoon rainfall to routed floodplain impact.

Use only evidence in the local CSX-076 event package. Discover the relevant event anchor, flood catalog timing, daily precipitation series, gridded precipitation summaries, report text, and remote-sensing or surface-water change summaries available in the package.

Use the full daily point-precipitation series for the June-October event-window duration, total accumulation, antecedent accumulation, late-August pulse, and rainfall-to-flood timing lags. Use gridded precipitation products only for their declared package comparison window; do not treat those gridded summaries as full June-October totals.

Rank these candidate control points:

- `antecedent_monsoon_accumulation`
- `late_august_rainfall_pulse`
- `indus_routing_storage_lag`
- `surface_water_or_sar_change`
- `single_day_peak_rainfall_only`
- `generic_disaster_report_label`

Your ranking should be calculation-led. Compute the event-window duration, the full daily precipitation total, the accumulation before the late-August pulse, the late-August pulse total, peak-window fractions, flood-catalog and rainfall-peak lags, gridded precipitation consensus/spread, report-derived process flags, and any available SAR or surface-water change metric. Then score and rank the control points by how much they control the process-chain diagnosis, not by operational response priority.

Use these diagnostic control-score formulas. Let `cap(x) = min(max(x, 0), 1)`. `wet_norm = cap(wet_days_ge_1mm / 40)`, `grid_consensus_norm = cap(1 - grid_spread_frac)`, `antecedent_norm = cap(antecedent_frac / 0.65)`, and `sar_norm = cap(s1_signal_to_sd / 2)`.

- `antecedent_monsoon_accumulation = 100 * (0.60 * antecedent_norm + 0.20 * wet_norm + 0.20 * grid_consensus_norm)`
- `indus_routing_storage_lag = 100 * (0.50 * mean(cap(peak_to_end_lag_days / 45), cap(gdacs_to_end_lag_days / 35)) + 0.35 * route_report_flag_mean + 0.15 * sar_norm)`
- `late_august_rainfall_pulse = 100 * (0.55 * cap(late_aug18_25_frac / 0.50) + 0.25 * cap(max7_frac / 0.40) + 0.20 * cap((late_aug18_25_mm / max_daily_mm) / 4))`
- `surface_water_or_sar_change = 100 * 0.75 * (0.55 * sar_norm + 0.30 * surface_report_flag_mean + 0.15 * s1_post_fraction)`
- `single_day_peak_rainfall_only = 100 * (0.70 * cap(single_day_frac / 0.25) + 0.30 * cap(1 - peak_to_end_lag_days / event_days))`
- `generic_disaster_report_label = 100 * (0.10 * event_label_present + 0.05 * gdacs_red_alert)`

Return compact JSON in this exact top-level shape:

```json
{
  "answer": "",
  "target_family": "pakistan_monsoon_flood_process_chain_control_ranking",
  "computed_values": {},
  "control_point_scores": {},
  "ranked_control_points": [],
  "top_control_point": "",
  "rejected_control_point": "",
  "reasoning_path": []
}
```

Inside `computed_values`, include at minimum `event_days`, `point_total_mm`, `antecedent_mm`, `antecedent_frac`, `late_aug18_25_mm`, `late_aug18_25_frac`, `max7_frac`, `single_day_frac`, `peak_to_end_lag_days`, `gdacs_to_end_lag_days`, `gridded_comparison_window`, `grid_consensus_mean_mm`, `grid_spread_frac`, and `s1_signal_to_sd`.
