# Correct Answer

```json
{
  "answer": "pressure_surge_wave_coastal_flood_supported",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "compare coastal water-level, pressure, wave, rainfall, and exposure evidence to identify the dominant flood forcing",
  "computed_evidence": {
    "storm_surge_evidence_synthesis": [
      {
        "row_id": "pressure_inverse_barometer",
        "computed_value": {
          "pressure_drop_996_to_968_mb": 28,
          "pressure_drop_996_to_966_mb": 30,
          "pressure_drop_1013_to_966_mb": 47,
          "pressure_steps_mb": {
            "996_to_980": 16,
            "980_to_968": 12,
            "968_to_966": 2
          },
          "inverse_barometer_rise_m": 0.47,
          "inverse_barometer_to_three_m_surge_ratio": 0.157
        },
        "result": "supports_pressure_forcing_but_rejects_pressure_only"
      },
      {
        "row_id": "surge_wave_tide_amplification",
        "computed_value": {
          "reported_wind_force_text": "Force 10/11",
          "reported_surge_proxy_m": 3.0,
          "reported_waves_more_than_m": 8,
          "wave_to_surge_ratio_lower_bound": 2.667,
          "reported_ijmuiden_arrival": "around 4 a.m. on 1 February",
          "reported_surge_more_in_netherlands_than_norfolk": true
        },
        "result": "supports_compound_surge_wave_tide_chain"
      },
      {
        "row_id": "rainfall_runoff_rejection",
        "computed_value": {
          "reported_water_surges_and_huge_waves": true,
          "reported_coastal_defences_pounded_by_sea": true,
          "reported_water_overtopped_embankments": true,
          "reported_thames_water_inflow_m3": 640000,
          "reported_rainfall_runoff_trigger_in_event_narrative": false,
          "reported_surge_proxy_m": 3.0,
          "reported_waves_more_than_m": 8,
          "wave_to_surge_ratio_lower_bound": 2.667,
          "marine_process_evidence_count": 4
        },
        "result": "rejects_rainfall_runoff_dominance_from_reported_marine_process"
      },
      {
        "row_id": "historical_impact_calibration",
        "computed_value": {
          "england_flooded_hectares": 160000,
          "netherlands_flooded_hectares": 200000,
          "flooded_hectares_total": 360000,
          "england_deaths": 307,
          "netherlands_deaths": 1800,
          "deaths_total": 2107,
          "england_flooded_share": 0.444,
          "netherlands_flooded_share": 0.556,
          "england_death_share": 0.146,
          "netherlands_death_share": 0.854,
          "death_per_100000_flooded_ha_total": 585.3
        },
        "result": "calibrates_regional_severity"
      }
    ],
    "rejected_simplifications": [
      "rainfall_runoff_dominance",
      "wind_waves_only",
      "tide_only"
    ],
    "final_process_alignment_label": "compound_coastal_storm_surge_chain_supported"
  },
  "mechanism_chain": [
    "storm pressure or wind forcing",
    "surge/wave water-level amplification",
    "coastal exposure context",
    "rainfall-only rejection"
  ],
  "decisive_evidence": "Coastal water-level and wave evidence should dominate unless rainfall-runoff metrics clearly overturn the coastal mechanism.",
  "rejected_simplifications": "Reject rainfall-only, wind-only, or exposure-only explanations if they cannot explain the coastal flooding signature.",
  "bounded_interpretation": "The result is not a tide-gauge reconstruction, property-loss model, or building-level flood map.",
  "formula_derivation": "Use pressure-deficit or surge-amplification reasoning where available, e.g. pressure_deficit = reference_pressure - storm_pressure."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `storm_surge_evidence_synthesis`, `rejected_simplifications`, `final_process_alignment_label`.
3. Use the computed values to build the ordered mechanism chain: storm pressure or wind forcing -> surge/wave water-level amplification -> coastal exposure context -> rainfall-only rejection.
4. Weight decisive evidence against alternatives: Coastal water-level and wave evidence should dominate unless rainfall-runoff metrics clearly overturn the coastal mechanism.
5. Reject simpler explanations: Reject rainfall-only, wind-only, or exposure-only explanations if they cannot explain the coastal flooding signature.
6. Keep the interpretation bounded: The result is not a tide-gauge reconstruction, property-loss model, or building-level flood map.

Formula/scaling note: Use pressure-deficit or surge-amplification reasoning where available, e.g. pressure_deficit = reference_pressure - storm_pressure.

Key computed anchors from the package:

- `event_name` = `1953 North Sea storm surge flood`
- `hazard_family` = `river_coastal_flood`
- `temporal_window` = `{"start_date": "1953-01-31", "end_date": "1953-02-01", "source": "package_event_lock_targeted_refined_v4_repaired"}`
- `pressure_metrics` = `{"pressure_drop_996_to_968_mb": 28, "pressure_drop_996_to_966_mb": 30, "pressure_drop_1013_to_966_mb": 47, "pressure_steps_mb": {"996_to_980": 16, "980_to_968": 12, "968_to_966": 2}, "inverse_barometer_rise_m": 0.47, "inverse_barometer_to_t`
- `surge_wave_tide_metrics` = `{"reported_wind_force_text": "Force 10/11", "reported_surge_proxy_m": 3.0, "reported_waves_more_than_m": 8, "wave_to_surge_ratio_lower_bound": 2.667, "reported_ijmuiden_arrival": "around 4 a.m. on 1 February", "reported_surge_more_in_nether`
- `marine_process_metrics` = `{"reported_water_surges_and_huge_waves": true, "reported_coastal_defences_pounded_by_sea": true, "reported_water_overtopped_embankments": true, "reported_thames_water_inflow_m3": 640000, "reported_rainfall_runoff_trigger_in_event_narrative"`
- `impact_metrics` = `{"england_flooded_hectares": 160000, "netherlands_flooded_hectares": 200000, "flooded_hectares_total": 360000, "england_deaths": 307, "netherlands_deaths": 1800, "deaths_total": 2107, "england_flooded_share": 0.444, "netherlands_flooded_sha`
- `numeric_tolerances` = `{"ratio": 0.01, "depth_m": 0.01, "death_rate": 0.2}`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_1953_North_Sea_storm_surge_flood.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
