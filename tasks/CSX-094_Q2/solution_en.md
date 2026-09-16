# Correct Answer

```json
{
  "answer": "storm_boris_rainfall_river_timing_supported",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "test whether multiday rainfall loading translates into routed river or basin response instead of an instantaneous local anomaly",
  "computed_evidence": {
    "final_process_alignment_label": "sustained_cutoff_low_rainfall_to_river_routing_supported",
    "required_row_ids": [
      "sustained_forcing",
      "river_timing_and_severity",
      "regional_local_rainfall_contrast",
      "branch_loss_share",
      "context_signal_check"
    ],
    "core_metrics": {
      "alert_rain_ratio": 2.0,
      "warning_mean_to_rain_ratio": 1.0,
      "station_to_local_ratios": [
        8.31,
        8.84
      ],
      "romania_flash_loss_share": 0.259
    },
    "tolerances": {
      "ratio_abs": 0.02,
      "share_abs": 0.002,
      "intensity_abs": 0.02
    }
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
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `final_process_alignment_label`, `required_row_ids`, `core_metrics.alert_rain_ratio`, `core_metrics.warning_mean_to_rain_ratio`, `core_metrics.station_to_local_ratios`, `core_metrics.romania_flash_loss_share`, `tolerances.ratio_abs`, `tolerances.share_abs`.
3. Use the computed values to build the ordered mechanism chain: multiday rainfall loading -> basin or terrain routing -> river-response timing -> instantaneous simplification rejection.
4. Weight decisive evidence against alternatives: Timing, persistence, and basin-scale response are decisive; isolated rainfall maxima are anchors but not the whole process.
5. Reject simpler explanations: Reject single-day, single-product, or same-hour response explanations if lagged or routed evidence is stronger.
6. Keep the interpretation bounded: The package supports timing and process reasoning, not calibrated hydraulic forecasts or complete damage accounting.

Formula/scaling note: Compute routing lag as response_time - rainfall_peak_time where source fields permit it; compare ratios or differences across products.

Key computed anchors from the package:

- `event_name` = `Storm Boris Central and Eastern Europe floods`
- `event_window` = `2024-09-11 to 2024-09-20`
- `rain_window_hours` = `72.0`
- `station_3day_max_mm` = `442.0`
- `flood_alert_duration_hours` = `144.0`
- `reported_lives_lost` = `27`
- `romania_flash_flood_fatalities` = `7`
- `metrics` = `{"alert_rain_ratio": 2.0, "station_mm_per_day": 147.33, "station_mm_per_hour": 6.139, "affected_country_count": 6, "warning_lead_range_hours": [60.0, 84.0], "warning_lead_mean_hours": 72.0, "warning_mean_to_rain_ratio": 1.0, "warning_min_to`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_Storm_Boris_Central_and_Eastern_Europe_floods.json`
- `data/event_reports/event_reports_002_Wikipedia_Storm_Boris.json`
- `data/other/other_001_ECMWF_-_Storm_Boris_and_European_flooding_September_2024.html`
- `data/event_catalogs/event_catalogs_001_GDACS_event_list_GeoJSON_API.json`
- `data/physical_hazard/physical_hazard_005_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_006_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/geospatial_context/geospatial_context_003_compact_per-event_AOI_derived_from_event_bbox.json`
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json`
- `data/remote_sensing/remote_sensing_005_Sentinel-1_GRD_VV_pre_post_change.json`
- `data/remote_sensing/remote_sensing_004_Google_Satellite_Embedding_annual_cosine-change_stats.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
