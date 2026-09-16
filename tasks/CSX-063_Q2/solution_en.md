# Final Answer

```json
{
  "rows": [
    {
      "row_id": "burst_runoff_threshold",
      "inputs_used": ["reported_hourly_peak_mm", "runoff_coefficient", "normalization_denominator_m3_per_km2"],
      "formula": [
        "water_volume_m3_per_km2 = 201.9 * 1000",
        "runoff_volume_m3_per_km2 = 201900 * 0.85",
        "normalized_runoff_index = 171615 / 100000"
      ],
      "computed_values": {
        "reported_hourly_peak_mm": 201.9,
        "water_volume_m3_per_km2": 201900,
        "runoff_volume_m3_per_km2": 171615,
        "normalized_runoff_index": 1.716
      },
      "threshold_decision": "passes because normalized_runoff_index is greater than 1",
      "failed_substitution": "an event-window mean cannot replace the 201.9 mm peak-hour burst"
    },
    {
      "row_id": "event_window_loading",
      "inputs_used": ["reported_3day_total_mm", "reported_hourly_peak_mm", "annual_average_mm"],
      "formula": [
        "three_day_to_peak_hour_ratio = 617.1 / 201.9",
        "peak_hour_share = 201.9 / 617.1",
        "three_day_to_annual_average_ratio = 617.1 / 640.8"
      ],
      "computed_values": {
        "three_day_to_peak_hour_ratio": 3.056,
        "peak_hour_share": 0.327,
        "three_day_to_annual_average_ratio": 0.963
      },
      "threshold_decision": "requires both peak burst and multi-day loading",
      "failed_substitution": "peak-only logic drops the 0.963 annual-rainfall ratio, while total-only logic drops the 0.327 peak-hour share"
    },
    {
      "row_id": "gridded_precipitation_check",
      "inputs_used": ["gpm_event_mean_mm", "chirps_event_mean_mm", "era5_land_event_mean_mm", "reported_3day_total_mm"],
      "formula": [
        "multi_product_mean = mean(460.551, 245.924, 217.454)",
        "product_mean_range = 460.551 - 217.454",
        "strongest_mean_to_reported_3day_ratio = 460.551 / 617.1"
      ],
      "computed_values": {
        "gpm_event_mean_mm": 460.551,
        "chirps_event_mean_mm": 245.924,
        "era5_land_event_mean_mm": 217.454,
        "multi_product_mean_event_precip_mm": 307.976,
        "products_above_200mm": 3,
        "product_mean_range_mm": 243.098,
        "strongest_mean_to_reported_3day_ratio": 0.746
      },
      "threshold_decision": "supports broad rainfall loading but does not replace the reported burst-and-total pair",
      "failed_substitution": "the strongest gridded mean is only 0.746 of the reported three-day total"
    },
    {
      "row_id": "transport_receptor_check",
      "inputs_used": ["highway_total", "high_capacity_road_features", "bridge_tagged_features", "tunnel_tagged_features", "population_rounded", "reported_train_suspensions_over"],
      "formula": [
        "high_capacity_road_share = 398 / 618",
        "bridge_tagged_share = 172 / 618",
        "train_suspensions_per_million_population_lower_bound = 160 / 5263000 * 1000000"
      ],
      "computed_values": {
        "highway_total": 618,
        "high_capacity_road_features": 398,
        "high_capacity_road_share": 0.644,
        "bridge_tagged_features": 172,
        "bridge_tagged_share": 0.278,
        "tunnel_tagged_features": 2,
        "critical_service_features": 48,
        "population_rounded": 5263000,
        "train_suspensions_per_million_population_lower_bound": 30.4
      },
      "threshold_decision": "transport receptors describe exposure context rather than the rainfall classifier",
      "failed_substitution": "road and bridge counts do not supply the rainfall-runoff threshold"
    },
    {
      "row_id": "remote_change_check",
      "inputs_used": ["radar_mean_vv_change_db", "radar_p90_vv_change_db", "alphaearth_change", "truecolor_difference"],
      "formula": [
        "vv_p90_to_mean_ratio = 2.023 / abs(0.647)"
      ],
      "computed_values": {
        "radar_mean_vv_change_db": 0.647,
        "radar_p90_vv_change_db": 2.023,
        "radar_p90_to_mean_vv_change_ratio": 3.124,
        "alphaearth_mean_annual_change": 0.044,
        "alphaearth_max_annual_change": 0.341,
        "truecolor_mean_abs_rgb_difference": 13.74
      },
      "threshold_decision": "overhead change metrics are context metrics, not the primary rainfall-runoff test",
      "failed_substitution": "a 3.124 radar tail-to-mean ratio cannot replace the rainfall and transport-receptor ledger"
    }
  ],
  "final_label": "peak_burst_window_transport_context_ledger",
  "interpretation": "The event satisfies a peak-burst plus multi-day rainfall loading ledger, with transport receptor and overhead-change metrics acting as contextual checks rather than the primary physical classifier."
}
```

# Key Computations

The reported peak-hour rainfall is `201.9 mm`. Over `1 km2`, this is `201.9 * 1000 = 201900 m3/km2`. With runoff coefficient `0.85`, the runoff proxy is `201900 * 0.85 = 171615 m3/km2`, so `normalized_runoff_index = 171615 / 100000 = 1.716`.

The event-window ratios are `617.1 / 201.9 = 3.056`, `201.9 / 617.1 = 0.327`, and `617.1 / 640.8 = 0.963`.

The gridded event precipitation means are `460.551 mm`, `245.924 mm`, and `217.454 mm`. Their mean is `307.976 mm`; all three exceed `200 mm`; their range is `243.098 mm`; and the strongest mean divided by the reported three-day total is `460.551 / 617.1 = 0.746`.

The transport receptor metrics are `398 / 618 = 0.644` for high-capacity roads and `172 / 618 = 0.278` for bridge-tagged roads. The record has `2` tunnel-tagged features, `48` critical service features, rounded population `5,263,000`, and a lower-bound train-suspension rate of `160 / 5263000 * 1000000 = 30.4` per million residents.

The remote-change metrics are `2.023 / abs(0.647) = 3.124` for the radar VV tail-to-mean ratio, annual embedding mean/max changes of `0.044` and `0.341`, and true-color mean absolute RGB difference of `13.740`.

# Reasoning Path

The burst runoff row passes its threshold because the normalized index is greater than `1`. The window row shows that the event cannot be reduced to a single-hour burst or a multi-day total alone: the peak hour is about one-third of the three-day total, while the three-day total is almost a full annual-average rainfall amount.

The gridded precipitation row supports broad event-window loading, but even the strongest gridded mean is only `0.746` of the reported three-day total, so it should not replace the reported burst-and-total pair. The transport row places the disruption in a dense receptor setting but does not provide the physical rainfall-runoff classifier. The remote-change row adds surface-change context, while the rainfall and receptor ledger supplies the decisive threshold structure.

# Computed Interpretation

The computed ledger supports `peak_burst_window_transport_context_ledger`: a peak-hour rainfall burst, near-annual three-day rainfall load, broad gridded precipitation signal, dense transport receptor context, and measurable overhead change are all present, but only the rainfall/runoff rows define the primary physical threshold.

# Scoring Rubric

Total: 20 points.

- Output ledger and final label, 3 points: full credit for valid JSON with all five required row ids, formulas, computed values, threshold decisions, failed substitutions, and final label `peak_burst_window_transport_context_ledger`. Partial credit for a parsable ledger that misses one required row or has minor naming drift while preserving the intended structure.
- Burst runoff threshold, 4 points: full credit for `201.9 mm`, `201900 m3/km2`, `171615 m3/km2`, and normalized runoff index `1.716`, with the threshold stated as greater than `1`. Partial credit for correct formula with one arithmetic or rounding error that does not reverse the pass result.
- Event-window loading, 3 points: full credit for ratios `3.056`, `0.327`, and `0.963`, plus the conclusion that both peak burst and multi-day load are needed. Partial credit for two correct ratios or a correct qualitative conclusion with one missing ratio.
- Gridded precipitation check, 4 points: full credit for means `460.551`, `245.924`, `217.454`, multi-product mean `307.976`, three products above `200 mm`, range `243.098`, strongest-to-reported ratio `0.746`, and the no-substitution conclusion. Partial credit for most values correct but one missing aggregation or a weak substitution explanation.
- Transport receptor check, 3 points: full credit for `398/618 = 0.644`, `172/618 = 0.278`, tunnel count `2`, critical service count `48`, population `5,263,000`, and train-suspension lower bound about `30.4` per million. Partial credit for correct counts with one missing derived share or the rate omitted.
- Remote-change check, 2 points: full credit for radar ratio `3.124`, annual embedding values `0.044` and `0.341`, and true-color difference `13.740`, while keeping these as context metrics. Partial credit for two of the three metric groups correct.
- Reasoning discipline, 1 point: full credit for concise reasoning that rejects peak-only, total-only, gridded-mean-only, receptor-count-only, and remote-change-only substitutions. Partial credit for rejecting at least three of these substitutions without adding extra uncomputed claims.
