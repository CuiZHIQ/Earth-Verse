# Correct Answer

```json
{
  "answer": "heat_load_process_supported",
  "bounded_interpretation": "The result is a package-scale heat mechanism diagnosis, not exact mortality, outage, damage, or full regional attribution.",
  "computed_evidence": {
    "evidence_synthesis": {
      "analysis_days": 46,
      "event_days": 61,
      "h40_c_day": 214.0,
      "image_damage_metric": "absent",
      "mean_tmax_c": 44.653,
      "peak_margin_c": 1.25,
      "peak_tmax_c": 46.247,
      "population_millions": 10.85,
      "rainfall_gap_mm": 13.0,
      "service_pressure_people_per_point": 452044
    },
    "rejected": [
      "rainfall_led_diagnosis",
      "image_damage_led_diagnosis"
    ],
    "tests": {
      "direct_image_damage_metric_absent": true,
      "h40_ge_150": true,
      "peak_margin_gt_0": true,
      "rainfall_gap_le_15": true,
      "service_pressure_ge_100000": true
    }
  },
  "decisive_evidence": "Accumulated heat load, duration, and exposure scaling carry the mechanism decision; rainfall or image signals only test competing explanations.",
  "formula_derivation": "Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units.",
  "mechanism_chain": [
    "event-window thermal forcing",
    "accumulated heat-load calculation",
    "persistence or recovery constraint",
    "non-heat alternative rejection"
  ],
  "mechanism_question": "separate cumulative heat stress from a single peak-temperature story by combining thermal load, persistence, recovery, and contextual evidence",
  "rejected_simplifications": "Reject peak-only, rainfall-led, and image-primary explanations when the computed heat-load chain is stronger.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `evidence_synthesis.analysis_days`, `evidence_synthesis.event_days`, `evidence_synthesis.h40_c_day`, `evidence_synthesis.image_damage_metric`, `evidence_synthesis.mean_tmax_c`, `evidence_synthesis.peak_margin_c`, `evidence_synthesis.peak_tmax_c`, `evidence_synthesis.population_millions`.
3. Use the computed values to build the ordered mechanism chain: event-window thermal forcing -> accumulated heat-load calculation -> persistence or recovery constraint -> non-heat alternative rejection.
4. Weight decisive evidence against alternatives: Accumulated heat load, duration, and exposure scaling carry the mechanism decision; rainfall or image signals only test competing explanations.
5. Reject simpler explanations: Reject peak-only, rainfall-led, and image-primary explanations when the computed heat-load chain is stronger.
6. Keep the interpretation bounded: The result is a package-scale heat mechanism diagnosis, not exact mortality, outage, damage, or full regional attribution.

Formula/scaling note: Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units.

Key computed anchors from the package:

- `amenity_counts` = `{"hospital": 22, "police": 1, "school": 1}`
- `analysis_days` = `46`
- `analysis_end` = `2015-06-15`
- `analysis_start` = `2015-05-01`
- `chirps_mean_mm` = `110.37099070034142`
- `event_days` = `61`
- `event_end` = `2015-06-30`
- `event_start` = `2015-05-01`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_006_Locked_event_anchor_2015_India-Pakistan_heat_wave.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_003_Overpass_small_roads_and_critical_amenities.json`
- `data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json`
- `metadata/files.csv`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
