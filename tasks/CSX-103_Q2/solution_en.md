# Correct Answer

```json
{
  "answer": "surge_wave_coastal_flooding_primary",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "compare coastal water-level, pressure, wave, rainfall, and exposure evidence to identify the dominant flood forcing",
  "computed_evidence": {
    "required_fields": [
      "coastal_signal",
      "cyclone_forcing",
      "rainfall_test",
      "local_wind_test",
      "grid_precip_context",
      "final_label"
    ],
    "required_flags": {
      "coastal_signal_passes": true,
      "rainfall_only_passes": false,
      "local_wind_only_passes": false
    },
    "canonical_values": {
      "state_count": 3,
      "coastal_terms": 5,
      "duration_ratio": 0.725,
      "wettest_fraction": 0.824,
      "local_wind_ratio": 0.362,
      "grid_mean_mm": 71.07
    },
    "tolerances": {
      "mm": 0.05,
      "ratios": 0.005,
      "wind_proxy": 0.5,
      "counts": 0
    }
  },
  "mechanism_chain": [
    "storm pressure or wind forcing",
    "surge/wave water-level amplification",
    "coastal exposure context",
    "rainfall-only rejection"
  ],
  "decisive_evidence": "Coastal water-level and wave evidence should dominate unless rainfall-runoff metrics clearly overturn the coastal mechanism.",
  "rejected_simplifications": "Reject rainfall-only, wind-only, or exposure-only explanations if they cannot explain the coastal flooding signature.",
  "bounded_interpretation": "The result is not a tide-gauge reconstruction, property-loss model, or building-level flood map."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `required_fields`, `required_flags.coastal_signal_passes`, `required_flags.rainfall_only_passes`, `required_flags.local_wind_only_passes`, `canonical_values.state_count`, `canonical_values.coastal_terms`, `canonical_values.duration_ratio`, `canonical_values.wettest_fraction`.
3. Use the computed values to build the ordered mechanism chain: storm pressure or wind forcing -> surge/wave water-level amplification -> coastal exposure context -> rainfall-only rejection.
4. Weight decisive evidence against alternatives: Coastal water-level and wave evidence should dominate unless rainfall-runoff metrics clearly overturn the coastal mechanism.
5. Reject simpler explanations: Reject rainfall-only, wind-only, or exposure-only explanations if they cannot explain the coastal flooding signature.
6. Keep the interpretation bounded: The result is not a tide-gauge reconstruction, property-loss model, or building-level flood map.

Key computed anchors from the package:

- `event_name` = `Hurricane Sandy New York-New Jersey coastal flooding`
- `event_window` = `2012-10-22 to 2012-10-31`
- `event_days` = `10`
- `event_hours` = `240`
- `named_state_count` = `3`
- `coastal_term_count` = `5`
- `coastal_signal_passes` = `True`
- `catalog_duration_hours` = `174.0`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_Hurricane_Sandy_New_York-New_Jersey_coastal_flooding.json`
- `data/event_catalogs/event_catalogs_001_GDACS_event_list_GeoJSON_API.json`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`
- `data/physical_hazard/physical_hazard_005_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_006_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
