# Canadian Wildfire-Smoke Future Risk Amplification Pathway Ranking

A climate-risk analyst is stress-testing the May 2023 Canadian wildfire-smoke episode under a plausible warmer and drier continuation over the next several days. Rank the physical pathways by how strongly the current evidence suggests each one could amplify future smoke risk.

Use only the local CSX-175 event package evidence. Ground the ranking in wildfire-smoke physical evidence: fire source pressure, AOD or aerosol-column clues, smoke transport descriptions, burn or landscape-change summaries, and precipitation/weather context.

Compute the following evidence metrics from the package:

- `avg_aod_clear_sky_ratio = Grand Forks average AOD / clear-sky AOD`
- `high_aod_anchor_fraction = count([Goddard average AOD, Grand Forks average AOD, Grand Forks peak AOD] >= 1.0) / 3`
- `estimated_out_of_control_fire_count = Alberta wildland fire count * out_of_control_fraction`
- `source_pressure_score = burned_area_average_multiple * out_of_control_fraction`
- `transport_window_days = inclusive day span from the first stated downwind smoke arrival to the later northern Plains AERONET smoke date`
- `precip_recovery_gap = max(0, 1 - mean(GPM mean event precipitation, CHIRPS mean event precipitation) / 100)`
- `local_burn_change_ratio = Sentinel-2 dNBR mean / annual embedding-change mean`

Then calculate pathway scores on a 0-100 scale using these normalizations:

- `source_norm = min(source_pressure_score / 2.5, 1)`
- `fire_count_norm = min(estimated_out_of_control_fire_count / 25, 1)`
- `burn_anomaly_norm = min(burned_area_average_multiple / 10, 1)`
- `aod_load_norm = min(avg_aod_clear_sky_ratio / 60, 1)`
- `peak_aod_norm = min(Grand Forks peak AOD / 3, 1)`
- `burn_change_norm = min(local_burn_change_ratio / 10, 1)`
- `transport_norm = min(transport_window_days / 10, 1)`
- `precip_gap_norm = min(precip_recovery_gap / 0.4, 1)`

Use binary flags from the report text where applicable: `growth_expectation_flag`, `hot_continuation_flag`, `transport_report_flag`, and `continental_scope_flag`.

Score the candidate pathways:

- `hotter_drier_fire_source_growth = 100 * (0.30*source_norm + 0.25*fire_count_norm + 0.20*burn_anomaly_norm + 0.15*growth_expectation_flag + 0.10*hot_continuation_flag)`
- `aerosol_column_loading_increase = 100 * (0.35*aod_load_norm + 0.25*peak_aod_norm + 0.20*high_aod_anchor_fraction + 0.10*source_norm + 0.10*burn_change_norm)`
- `longer_smoke_transport_window = 100 * (0.35*transport_norm + 0.25*aod_load_norm + 0.20*transport_report_flag + 0.10*continental_scope_flag + 0.10*hot_continuation_flag)`
- `precipitation_recovery_delay = 100 * (0.70*precip_gap_norm + 0.30*hot_continuation_flag)`
- `single_burn_area_only = 100 * (0.35*burn_anomaly_norm + 0.10*burn_change_norm)`
- `generic_smoke_report_label = 100 * (0.10*transport_report_flag + 0.05*high_aod_anchor_fraction)`

Rank pathways from highest to lowest score. Return compact JSON only:

```json
{
  "answer": "<top pathway or ordered pathway statement>",
  "target_family": "wildfire_smoke_future_risk_amplification_ranking",
  "computed_values": {
    "avg_aod_clear_sky_ratio": 0.0,
    "source_pressure_score": 0.0,
    "estimated_out_of_control_fire_count": 0.0,
    "transport_window_days": 0,
    "high_aod_anchor_fraction": 0.0,
    "precip_recovery_gap": 0.0,
    "local_burn_change_ratio": 0.0
  },
  "pathway_scores": {
    "hotter_drier_fire_source_growth": 0.0,
    "aerosol_column_loading_increase": 0.0,
    "longer_smoke_transport_window": 0.0,
    "precipitation_recovery_delay": 0.0,
    "single_burn_area_only": 0.0,
    "generic_smoke_report_label": 0.0
  },
  "ranked_pathways": ["<highest>", "<next>", "<...>"],
  "top_amplification_pathway": "<pathway>",
  "rejected_pathway": "<weakest or non-diagnostic pathway>",
  "reasoning_path": "<one concise evidence-based sentence>"
}
```
