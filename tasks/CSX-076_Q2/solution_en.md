# Correct Answer

```json
{
  "answer": "antecedent_monsoon_accumulation",
  "target_family": "pakistan_monsoon_flood_process_chain_control_ranking",
  "computed_values": {
    "event_days": 110,
    "point_total_mm": 1493.3,
    "antecedent_mm": 962.7,
    "antecedent_frac": 0.645,
    "late_aug18_25_mm": 522.4,
    "late_aug18_25_frac": 0.35,
    "max7_frac": 0.324,
    "single_day_frac": 0.101,
    "peak_to_end_lag_days": 44,
    "gdacs_to_end_lag_days": 31,
    "gridded_comparison_window": {
      "start_date": "2022-06-14",
      "end_date": "2022-07-29"
    },
    "grid_consensus_mean_mm": 818.1,
    "grid_spread_frac": 0.066,
    "s1_signal_to_sd": 1.808
  },
  "control_point_scores": {
    "antecedent_monsoon_accumulation": 98.2,
    "indus_routing_storage_lag": 95.1,
    "late_august_rainfall_pulse": 76.1,
    "surface_water_or_sar_change": 66.6,
    "single_day_peak_rainfall_only": 46.2,
    "generic_disaster_report_label": 15.0
  },
  "ranked_control_points": [
    "antecedent_monsoon_accumulation",
    "indus_routing_storage_lag",
    "late_august_rainfall_pulse",
    "surface_water_or_sar_change",
    "single_day_peak_rainfall_only",
    "generic_disaster_report_label"
  ],
  "top_control_point": "antecedent_monsoon_accumulation",
  "rejected_control_point": "generic_disaster_report_label",
  "reasoning_path": [
    "accumulation_sets_wet_basin",
    "late_aug_pulse_amplifies_only",
    "lags_route_storage_to_plain",
    "sar_confirms_downstream_water",
    "peak_and_label_rejected"
  ]
}
```

# Key Computations

- Inclusive event window: 2022-06-14 through 2022-10-01 is 110 days.
- Daily point precipitation total: 1493.3 mm.
- Antecedent accumulation before 2022-08-18: 962.7 mm, which is 0.645 of the event total.
- Late-August pulse from 2022-08-18 through 2022-08-25: 522.4 mm, which is 0.350 of the event total.
- Maximum daily precipitation: 150.3 mm on 2022-08-18, which is only 0.101 of the event total.
- Maximum 7-day precipitation: 484.5 mm, so the max-7-day fraction is 0.324.
- Timing lags: the daily rainfall peak precedes the event-anchor end by 44 days, and the Pakistan GDACS flood record end precedes the anchor end by 31 days.
- Gridded precipitation means are evaluated only over their declared package comparison window, 2022-06-14 through 2022-07-29. ERA5-Land is 846.6 mm, GPM is 792.5 mm, and CHIRPS is 815.4 mm. Their consensus mean is 818.1 mm and the spread fraction is 0.066.
- Sentinel-1 VV post-minus-pre mean change is 2.326 dB with 1.287 dB standard deviation, giving a signal-to-standard-deviation ratio of 1.808. The SAR windows include 39 pre-event and 61 post-event scenes.
- Report flags pass for torrential monsoon rain, Indus focus, floodplain/lake-like plains, out-of-bank rivers, rain and meltwater, reservoir/channel pressure, glacier melt, and satellite-detected water extents.

# Ranking Logic

The score is a diagnostic control score, not an action score. Antecedent accumulation ranks first because most of the precipitation occurred before the late-August pulse, the wet-day count supports persistent forcing, and the gridded products agree closely. Indus routing/storage lag ranks second because the 44-day and 31-day lags, plus report evidence for the Indus, floodplains, out-of-bank rivers, reservoirs/channels, rain/meltwater, and glacier melt, explain why the flood diagnosis extends beyond the rainfall peak.

The late-August pulse is important but not dominant: it contributes 0.350 of the total and amplifies an already wet basin. SAR or surface-water change is strong downstream confirmation, but it is an observed impact state rather than the upstream control. Single-day peak rainfall is a weak physical decoy because one day contributes only 0.101 of the total and is followed by a 44-day lag. A generic disaster/report label is rejected because it names the event but does not control the process chain.

The control-score formulas normalize the values before ranking: antecedent accumulation combines antecedent fraction, wet-day persistence, and gridded-product agreement; routing/storage combines rainfall and catalog lags, Indus/floodplain/channel/meltwater report flags, and SAR strength; the late-August pulse combines pulse fraction, max-7-day concentration, and pulse-to-peak ratio; surface-water/SAR is damped because it confirms an impact state rather than the upstream control; single-day peak rainfall is penalized by its small event-total fraction and long lag; the generic label receives only a low naming score.

# 20-Point Rubric

- 2 points: Required compact JSON and task family. Full credit returns JSON with answer, target_family, computed_values, control_point_scores, ranked_control_points, top_control_point, rejected_control_point, and reasoning_path. Partial credit: 1 point for mostly valid JSON with one missing top-level field.
- 3 points: Package evidence discovery. Full credit uses local event anchor/catalog, daily precipitation, gridded precipitation summaries, report process text, and SAR or surface-water change evidence without external files. Partial credit: 1-2 points if several required evidence families are used but one major family is missing.
- 4 points: Rainfall accumulation and pulse calculations. Full credit computes 1493.3 mm total, 962.7 mm antecedent accumulation, 522.4 mm late-August pulse, and the 0.645, 0.350, 0.324, and 0.101 fractions. Partial credit: 2-3 points for correct formulas with minor rounding or one missing fraction; at most 1 point for unnormalized totals only.
- 4 points: Routing lag and process-chain interpretation. Full credit computes the 44-day rainfall-peak-to-anchor-end lag and 31-day GDACS-to-anchor-end lag, then uses the Indus/floodplain/out-of-bank/rain-meltwater/reservoir-channel/glacier-melt report flags. Partial credit: 1-3 points for correct lag arithmetic or process terms without tying them to routed flood diagnosis.
- 3 points: Grid and remote-sensing support. Full credit uses the declared 2022-06-14 to 2022-07-29 gridded comparison window and computes the 818.1 mm gridded consensus, 0.066 spread fraction, 2.326 dB Sentinel-1 mean change, and 1.808 signal-to-standard-deviation ratio. Partial credit: 1-2 points if either the grid consensus or SAR calculation is correct but not both.
- 3 points: Control-point ranking. Full credit returns the ranking shown above. Partial credit: 1-2 points if the top control point is right but middle or low-ranking decoys are misplaced.
- 1 point: Rejection discipline. Full credit identifies `generic_disaster_report_label` as the rejected non-control candidate and treats single-day peak rainfall as a weak physical decoy rather than the primary control point. No partial credit.
