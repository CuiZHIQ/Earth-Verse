# Correct Answer

```json
{
  "answer": "hotter_drier_fire_source_growth",
  "target_family": "wildfire_smoke_future_risk_amplification_ranking",
  "computed_values": {
    "avg_aod_clear_sky_ratio": 46.0,
    "source_pressure_score": 2.5,
    "estimated_out_of_control_fire_count": 21.75,
    "transport_window_days": 7,
    "high_aod_anchor_fraction": 1.0,
    "precip_recovery_gap": 0.15,
    "local_burn_change_ratio": 7.87
  },
  "pathway_scores": {
    "hotter_drier_fire_source_growth": 96.8,
    "aerosol_column_loading_increase": 89.7,
    "longer_smoke_transport_window": 83.7,
    "precipitation_recovery_delay": 56.7,
    "single_burn_area_only": 42.9,
    "generic_smoke_report_label": 15.0
  },
  "ranked_pathways": [
    "hotter_drier_fire_source_growth",
    "aerosol_column_loading_increase",
    "longer_smoke_transport_window",
    "precipitation_recovery_delay",
    "single_burn_area_only",
    "generic_smoke_report_label"
  ],
  "top_amplification_pathway": "hotter_drier_fire_source_growth",
  "rejected_pathway": "generic_smoke_report_label",
  "reasoning_path": "Source growth leads: 87 fires, 21.75 out of control, 10x burned area, expected growth, and heat outrank severe AOD, 7d transport, and weaker rain-delay evidence."
}
```

# Key Computations

The aerosol anchors give `avg_aod_clear_sky_ratio = 2.3 / 0.05 = 46.0`. All three AOD anchors are at least `1.0`, so `high_aod_anchor_fraction = 3 / 3 = 1.0`.

The source-fire metrics use `87` Alberta wildland fires and an out-of-control fraction of `0.25`: `estimated_out_of_control_fire_count = 87 * 0.25 = 21.75`. The burned-area anomaly is `10` times average, so `source_pressure_score = 10 * 0.25 = 2.5`.

The transport window is inclusive from the report's May 10 Maryland smoke arrival to the May 16 northern Plains AERONET smoke date: `7` days. The high-AOD anchor fraction is `3 / 3 = 1.0`.

The precipitation recovery term uses the mean of the GPM and CHIRPS event mean precipitation values: `(82.5455 + 86.9229) / 2 = 84.7342 mm`, so `precip_recovery_gap = 1 - 84.7342 / 100 = 0.15`. The local burn-change ratio is `0.35477110498290715 / 0.0451065067711521 = 7.87`.

# Ranking Logic

With the stated normalizations, the pathway scores are:

- `hotter_drier_fire_source_growth = 96.8`
- `aerosol_column_loading_increase = 89.7`
- `longer_smoke_transport_window = 83.7`
- `precipitation_recovery_delay = 56.7`
- `single_burn_area_only = 42.9`
- `generic_smoke_report_label = 15.0`

The top pathway is `hotter_drier_fire_source_growth` because it combines the 10x burned-area anomaly, 87 active fires, about 21.75 out-of-control fires, report text saying out-of-control fires were expected to grow, and continuing heat. Aerosol loading ranks second because the AOD column was already severe, but it is still downstream of source growth as a future amplifier. Transport ranks third because the report documents multi-day downwind spread, while precipitation recovery delay is weaker because the precipitation summaries and hot-continuation flag do not outrank source growth, aerosol loading, or transport persistence.

`generic_smoke_report_label` is rejected because it is only a label-level cue. It does not quantify source growth, aerosol-column loading, transport persistence, or recovery delay.

# Scoring Rubric

Total: 20 points.

- 4 points: Correct final ranking. Full credit ranks `hotter_drier_fire_source_growth`, `aerosol_column_loading_increase`, `longer_smoke_transport_window`, `precipitation_recovery_delay`, `single_burn_area_only`, and `generic_smoke_report_label` in that order. Partial credit: 2-3 points if the top pathway is correct but the middle order is partly reversed; 1 point for a physical pathway ranking with the wrong dominant pathway.
- 4 points: Correct fire-source calculations. Full credit computes `21.75` estimated out-of-control fires and `2.5` source-pressure score. Partial credit: 2-3 points for one correct source metric; 1 point for using the right report anchors without completing the calculation.
- 4 points: Correct aerosol-column calculations. Full credit computes the `46.0` AOD clear-sky ratio, high-AOD anchor fraction of `1.0`, and uses peak AOD near `3.0` in the aerosol score. Partial credit: 2-3 points for correct AOD ratios with an incomplete score; 1 point for recognizing severe aerosol loading without numeric support.
- 3 points: Correct transport evidence. Full credit computes the `7` day transport window and uses the report's wind/GOES downwind-smoke evidence plus continental scope. Partial credit: 1-2 points for identifying cross-border transport but missing the inclusive day calculation or scope flag.
- 3 points: Correct precipitation and burn-change context. Full credit computes high-AOD anchor fraction `1.0`, precipitation recovery gap near `0.15`, and burn-change ratio near `7.87`. Partial credit: 1-2 points for one or two of these context metrics; no credit for substituting point-weather, population, or AOI exposure.
- 2 points: Output discipline and rejected pathway. Full credit returns compact JSON with the requested keys, rejects `generic_smoke_report_label`, and avoids response-priority or advice framing. Partial credit: 1 point for correct physical reasoning with minor JSON or wording deviations.
