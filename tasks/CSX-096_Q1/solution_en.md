# Correct Answer

```json
{
  "answer": "national_scale_persistent_monsoon_flood_supported",
  "bounded_interpretation": "The package supports timing and process reasoning, not calibrated hydraulic forecasts or complete damage accounting.",
  "computed_evidence": {
    "core_metrics": {
      "disruption": [
        41614.12,
        30303.03,
        33.33
      ],
      "flood": [
        9.46,
        64.71,
        26470,
        35.29
      ],
      "local_spread": [
        54.061,
        0.066
      ],
      "rain_mult": [
        3.43,
        2.9,
        8.26,
        6.9,
        6.0
      ],
      "window": [
        109,
        79,
        91,
        0.725,
        0.835
      ]
    },
    "decision_rule": "first four rows pass and the local row remains context",
    "rejected_frames": [
      "local_slice_dominance",
      "rainfall_only_anomaly",
      "crop_only_impact_framing",
      "late_window_surface_change_dominance",
      "catalog_alert_only_severity",
      "surface_mapping_led_diagnosis"
    ],
    "required_row_ids": [
      "rainfall_anomaly_severity",
      "floodwater_extent_partition",
      "event_window_process alignment",
      "reported_disruption_load",
      "local_remote_context_guardrail"
    ],
    "tolerances": {
      "integer_counts": 0,
      "local_spread_fraction": 0.002,
      "percent_values": 0.05,
      "ratio_values": 0.005
    }
  },
  "decisive_evidence": "Timing, persistence, and basin-scale response are decisive; isolated rainfall maxima are anchors but not the whole process.",
  "mechanism_chain": [
    "multiday rainfall loading",
    "basin or terrain routing",
    "river-response timing",
    "instantaneous simplification rejection"
  ],
  "mechanism_question": "test whether multiday rainfall loading translates into routed river or basin response instead of an instantaneous local anomaly",
  "rejected_simplifications": "Reject single-day, single-product, or same-hour response explanations if lagged or routed evidence is stronger.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `core_metrics.disruption`, `core_metrics.flood`, `core_metrics.local_spread`, `core_metrics.rain_mult`, `core_metrics.window`, `decision_rule`, `rejected_frames`, `required_row_ids`.
3. Use the computed values to build the ordered mechanism chain: multiday rainfall loading -> basin or terrain routing -> river-response timing -> instantaneous simplification rejection.
4. Weight decisive evidence against alternatives: Timing, persistence, and basin-scale response are decisive; isolated rainfall maxima are anchors but not the whole process.
5. Reject simpler explanations: Reject single-day, single-product, or same-hour response explanations if lagged or routed evidence is stronger.
6. Keep the interpretation bounded: The package supports timing and process reasoning, not calibrated hydraulic forecasts or complete damage accounting.

Key computed anchors from the package:

- `alert_catalog` = `{"alertlevel": "Red", "eventid": 1101522, "fromdate": "2022-06-14T01:00:00", "iso3": "PAK", "todate": "2022-08-31T01:00:00"}`
- `event_name` = `2022 Pakistan monsoon floods`
- `flood_extent_report` = `{"analyzed_area_km2_about": 793000, "flood_water_affected_land_km2_about": 75000, "flooded_croplands_km2": 48530}`
- `hazard_family` = `river_coastal_flood`
- `local_context` = `{"embedding_1_minus_cosine_mean": 0.022096, "local_rainfall_means_mm": {"chirps": 815.383, "era5": 846.553, "gpm": 792.492}, "local_slice_area_deg2": 9.0, "local_slice_height_deg": 3.0, "local_slice_width_deg": 3.0, "surface_post_count": 61`
- `nasa_report` = `{"affected_people_more_than": 33000000, "balochistan_sindh_rainfall_multiple_range": [5, 6], "houses_destroyed_or_damaged_more_than": 1000000, "killed_at_least": 1100, "qambar_shikarpur_rainfall_above_average_percent": 500}`
- `package_temporal_window` = `{"duration_days": 109, "end": "2022-09-30", "start": "2022-06-14"}`
- `wmo_report` = `{"affected_crops_orchards_acres": 2000000, "as_of_27_august_national_average_multiple": 2.9, "august_national_rainfall_above_average_percent": 243, "balochistan_august_above_average_percent": 590, "extreme_rainfall_increase_percent_range": `

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/event_reports/event_reports_002_HDX_CKAN_package_search.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_2022_Pakistan_monsoon_floods.json`
- `data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Devastating_floods_in_Pakistan.html`
- `data/geospatial_context/geospatial_context_003_compact_per-event_AOI_derived_from_event_bbox.json`
- `data/physical_hazard/physical_hazard_005_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_006_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/remote_sensing/remote_sensing_004_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/remote_sensing/remote_sensing_005_Sentinel-1_GRD_VV_pre_post_change.json`
- `data/event_catalogs/event_catalogs_001_GDACS_event_list_GeoJSON_API.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
