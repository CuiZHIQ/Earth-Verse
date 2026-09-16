# Correct Answer

```json
{
  "answer": "compound_volcanic_pressure_high",
  "bounded_interpretation": "Do not infer exact lahar discharge, plume mass, eruption dynamics, or evacuation outcomes unless directly sourced.",
  "computed_evidence": {
    "metrics": {
      "ash_excess_km": 6.3,
      "evidence_score": 6,
      "lahar_zone_ratio": 0.825,
      "pop_m": 11.071,
      "rain_conc": 1.47,
      "rain_mean_mm": 365.768,
      "rain_peak_mean_mm": 537.7
    },
    "rejected": "rain_only_lahar_dominance",
    "tests": {
      "ash": true,
      "lahar": true,
      "pop": true,
      "pyro": true,
      "rain_conc": true,
      "rain_load": true
    },
    "thr": {
      "ash_excess_km": 6,
      "evidence_score": 5,
      "lahar_ratio": 0.8,
      "pop_m": 10,
      "pyro_km": 20,
      "rain_conc": 1.4,
      "rain_mean_mm": 300
    },
    "tol": {
      "ash_excess_km": 0.01,
      "evidence_score": 0,
      "lahar_zone_ratio": 0.001,
      "pop_m": 0.001,
      "rain_conc": 0.001,
      "rain_mean_mm": 0.001,
      "rain_peak_mean_mm": 0.001
    }
  },
  "decisive_evidence": "The strongest answer links volcanic forcing with ash, lahar, rainfall, or surface signals rather than isolating one product.",
  "mechanism_chain": [
    "eruption or pyroclastic anchor",
    "ash or surface signal",
    "rainfall-lahar modifier",
    "single-hazard rejection"
  ],
  "mechanism_question": "diagnose whether multiple volcanic processes and rainfall modifiers form a compound pressure chain",
  "rejected_simplifications": "Reject ash-only, rain-only, or image-only explanations if a compound volcanic chain is required.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `metrics.ash_excess_km`, `metrics.evidence_score`, `metrics.lahar_zone_ratio`, `metrics.pop_m`, `metrics.rain_conc`, `metrics.rain_mean_mm`, `metrics.rain_peak_mean_mm`, `rejected`.
3. Use the computed values to build the ordered mechanism chain: eruption or pyroclastic anchor -> ash or surface signal -> rainfall-lahar modifier -> single-hazard rejection.
4. Weight decisive evidence against alternatives: The strongest answer links volcanic forcing with ash, lahar, rainfall, or surface signals rather than isolating one product.
5. Reject simpler explanations: Reject ash-only, rain-only, or image-only explanations if a compound volcanic chain is required.
6. Keep the interpretation bounded: Do not infer exact lahar discharge, plume mass, eruption dynamics, or evacuation outcomes unless directly sourced.

Key computed anchors from the package:

- `analysis_area_population` = `11071345.942`
- `derived_metrics` = `{"ash_excess_km": 6.3, "lahar_zone_ratio": 0.825, "pop_m": 11.071, "rain_conc": 1.47, "rain_mean_mm": 365.768, "rain_peak_mean_mm": 537.7, "score": 6}`
- `gate_tests` = `{"ash": true, "lahar": true, "pop": true, "pyro": true, "rain_conc": true, "rain_load": true}`
- `precipitation_inputs_mm` = `{"maxima": {"chirps_max": 516.813, "era5_max": 638.457, "gpm_max": 457.828}, "means": {"chirps_mean": 315.128, "era5_mean": 452.093, "gpm_mean": 330.084}}`
- `report_anchors` = `{"hazard_zone_radius_km": 20.0, "highest_ash_altitude_km_asl": 18.3, "maximum_lahar_deposit_distance_km": 16.5}`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_Merapi_eruption.json`
- `data/other/other_002_01_anchor.html.html`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
