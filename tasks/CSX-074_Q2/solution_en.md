# Correct Answer

```json
{
  "answer": "multiday_rainfall_to_river_routing_lag_consistent",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "test whether multiday rainfall loading translates into routed river or basin response instead of an instantaneous local anomaly",
  "computed_evidence": {
    "proof_blocks": [
      {
        "block_id": "event_window_and_alert_lags",
        "formula": [
          "inclusive_days*24",
          "alert_start-event_start",
          "lag/event_window_hours"
        ],
        "computed_values": {
          "event_window_hours": 120,
          "Germany_lag_hours": 25.0,
          "Belgium_lag_hours": 49.0,
          "Germany_lag_ratio": 0.208,
          "Belgium_lag_ratio": 0.408
        },
        "result": "lagged_alert_timing_pass"
      },
      {
        "block_id": "cross_border_alert_timing",
        "formula": [
          "max(alert_end)-min(alert_start)",
          "later_alert_start-earlier_alert_start",
          "alert_overlap_hours",
          "combined_window/event_window_hours",
          "overlap/combined_window",
          "onset_gap/event_window_hours"
        ],
        "computed_values": {
          "combined_alert_window_hours": 72.0,
          "alert_onset_gap_hours": 24.0,
          "alert_overlap_hours": 24.0,
          "combined_window_ratio": 0.6,
          "overlap_combined_ratio": 0.333,
          "onset_gap_ratio": 0.2
        },
        "result": "cross_border_timing_pass"
      },
      {
        "block_id": "gridded_rainfall_process alignment",
        "formula": [
          "satellite_max/satellite_mean",
          "reanalysis_max/reanalysis_mean",
          "abs(satellite_max-reanalysis_max)/mean(satellite_max,reanalysis_max)*100"
        ],
        "computed_values": {
          "satellite_max_mean_ratio": 2.279,
          "reanalysis_max_mean_ratio": 2.343,
          "gridded_max_difference_pct": 0.03
        },
        "result": "gridded_rainfall_consistency_pass"
      },
      {
        "block_id": "local_hourly_rain_spike_test",
        "formula": [
          "local_peak_hour/local_total",
          "longest_wet_run/event_window_hours",
          "wet_span/event_window_hours",
          "local_total/satellite_max"
        ],
        "computed_values": {
          "local_peak_share": 0.077,
          "longest_wet_run_ratio": 0.442,
          "wet_span_ratio": 0.808,
          "local_total_to_satellite_max_ratio": 1.815
        },
        "result": "single_hour_spike_fails"
      }
    ],
    "rejected_alternatives": [
      "single_local_hourly_spike",
      "rainfall_total_without_lag",
      "single_country_alert_sequence"
    ],
    "final_label": "multiday_rainfall_to_river_routing_lag_consistent"
  },
  "mechanism_chain": [
    "multiday rainfall loading",
    "basin or terrain routing",
    "river-response timing",
    "instantaneous simplification rejection"
  ],
  "decisive_evidence": "Timing, persistence, and basin-scale response are decisive; isolated rainfall maxima are anchors but not the whole process.",
  "rejected_simplifications": "Reject single-day, single-product, or same-hour response explanations if lagged or routed evidence is stronger.",
  "bounded_interpretation": "The package supports timing and process reasoning, not calibrated hydraulic forecasts or complete damage accounting.",
  "formula_derivation": "Compute routing lag as response_time - rainfall_peak_time where source fields permit it; compare ratios or differences across products."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `proof_blocks`, `rejected_alternatives`, `final_label`.
3. Use the computed values to build the ordered mechanism chain: multiday rainfall loading -> basin or terrain routing -> river-response timing -> instantaneous simplification rejection.
4. Weight decisive evidence against alternatives: Timing, persistence, and basin-scale response are decisive; isolated rainfall maxima are anchors but not the whole process.
5. Reject simpler explanations: Reject single-day, single-product, or same-hour response explanations if lagged or routed evidence is stronger.
6. Keep the interpretation bounded: The package supports timing and process reasoning, not calibrated hydraulic forecasts or complete damage accounting.

Formula/scaling note: Compute routing lag as response_time - rainfall_peak_time where source fields permit it; compare ratios or differences across products.

Key computed anchors from the package:

- `event_name` = `July 2021 Western Europe floods`
- `hazard_family` = `extreme_precip_pluvial_flood`
- `event_window_start` = `2021-07-12`
- `event_window_end` = `2021-07-16`
- `event_window_days` = `5`
- `event_window_hours` = `120`
- `alert_windows` = `{"Germany": {"start": "2021-07-13T01:00", "end": "2021-07-15T01:00"}, "Belgium": {"start": "2021-07-14T01:00", "end": "2021-07-16T01:00"}}`
- `alert_lag_hours` = `{"Germany": 25.0, "Belgium": 49.0}`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_July_2021_Western_Europe_floods.json`
- `data/event_catalogs/event_catalogs_001_GDACS_event_list_GeoJSON_API.json`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`
- `data/physical_hazard/physical_hazard_005_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_007_GPM_IMERG_V07_event_accumulated_precipitation.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
