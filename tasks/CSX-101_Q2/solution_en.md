# Correct Answer

```json
{
  "answer": "north_sea_surge_amplification_supported",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "compare coastal water-level, pressure, wave, rainfall, and exposure evidence to identify the dominant flood forcing",
  "computed_evidence": {
    "surge_proof": {
      "pressure_gap": {
        "inverse_barometer_m": 0.47,
        "reported_surge_m": 3.0,
        "surge_to_inverse_barometer_ratio": 6.38,
        "inverse_barometer_fraction_of_surge": 0.157,
        "pressure_only_test": "fails"
      },
      "synoptic_forcing": {
        "storm_deepening_mb": 30,
        "ridge_to_low_gradient_mb": 64,
        "gradient_to_deepening_ratio": 2.133,
        "force_10_11_northerly_winds_reported": true,
        "north_sea_propagation_reported": true,
        "ijmuiden_arrival_hour_feb1": 4,
        "synoptic_forcing_test": "passes"
      },
      "local_weather_replacement": {
        "reported_water_surges_and_huge_waves": true,
        "reported_coastal_defences_pounded_by_sea": true,
        "reported_water_overtopped_embankments": true,
        "reported_thames_water_inflow_m3": 640000,
        "marine_process_evidence_count": 4,
        "local_weather_only_replacement_test": "fails"
      },
      "impact_density_check": {
        "england_death_density_per_1000ha": 1.919,
        "netherlands_death_density_per_1000ha": 9.0,
        "nl_to_england_density_ratio": 4.69,
        "england_flooded_share": 0.444,
        "netherlands_flooded_share": 0.556,
        "england_death_share": 0.146,
        "netherlands_death_share": 0.854,
        "single_country_density_replacement_test": "fails"
      }
    },
    "failed_replacement_tests": [
      "pressure_only",
      "local_weather_only",
      "single_country_impact_density_only"
    ],
    "final_process_alignment_label": "wind_driven_north_sea_surge_amplification_supported"
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
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `surge_proof.pressure_gap.inverse_barometer_m`, `surge_proof.pressure_gap.reported_surge_m`, `surge_proof.pressure_gap.surge_to_inverse_barometer_ratio`, `surge_proof.pressure_gap.inverse_barometer_fraction_of_surge`, `surge_proof.pressure_gap.pressure_only_test`, `surge_proof.synoptic_forcing.storm_deepening_mb`, `surge_proof.synoptic_forcing.ridge_to_low_gradient_mb`.
3. Use the computed values to build the ordered mechanism chain: storm pressure or wind forcing -> surge/wave water-level amplification -> coastal exposure context -> rainfall-only rejection.
4. Weight decisive evidence against alternatives: Coastal water-level and wave evidence should dominate unless rainfall-runoff metrics clearly overturn the coastal mechanism.
5. Reject simpler explanations: Reject rainfall-only, wind-only, or exposure-only explanations if they cannot explain the coastal flooding signature.
6. Keep the interpretation bounded: The result is not a tide-gauge reconstruction, property-loss model, or building-level flood map.

Key computed anchors from the package:

- `pressure_min_mb` = `966`
- `pressure_initial_mb` = `996`
- `high_pressure_ridge_mb` = `1030`
- `inverse_barometer_m` = `0.47`
- `reported_surge_m` = `3.0`
- `surge_to_inverse_barometer_ratio` = `6.38`
- `inverse_barometer_fraction_of_surge` = `0.157`
- `storm_deepening_mb` = `30`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_1953_North_Sea_storm_surge_flood.json`
- `data/event_reports/event_reports_005_Met_Office_1953_east_coast_floods_case_study.html`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
