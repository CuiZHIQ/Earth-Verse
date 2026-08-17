# Correct Answer

```json
{
  "answer": "heat_load_recovery_failure_supported",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "separate cumulative heat stress from a single peak-temperature story by combining thermal load, persistence, recovery, and contextual evidence",
  "computed_evidence": {
    "proof_result": "persistent_heat_load_rule_pass",
    "diagnosis_label": "persistent_early_season_heat_health_load",
    "indices": {
      "event_window_days": 76,
      "days_tmax_ge40": 26,
      "longest_tmax_ge40_run_days": 9,
      "heat_load_gt40_c_day": 43.4,
      "hottest_3day_tmax_mean_c": 44.57,
      "hottest_3day_window": "2022-05-11 to 2022-05-13",
      "warm_night_recovery_ratio_ge28": 0.118,
      "peak_apparent_temperature_c": 42.8
    },
    "process_alignment_proof": "The persistent heat-load rule passes: 43.4 C-day is above the 40 C-day diagnostic gate, 26 event-window days reached at least 40 C, and the longest hot run lasted 9 days. The hottest 3-day Tmax mean was 44.57 C from 2022-05-11 to 2022-05-13, showing an acute phase embedded in a longer hot period. The 0.118 warm-night ratio and 42.8 C peak apparent temperature add recovery and body-stress context without replacing the dry-bulb persistence test.",
    "rejected_alternative": "single_peak_heat_only",
    "computed_interpretation": "The strongest computed diagnosis is sustained early-season heat-load accumulation with a mid-May peak, not a single-day diagnostic gate crossing."
  },
  "mechanism_chain": [
    "event-window thermal forcing",
    "accumulated heat-load calculation",
    "persistence or recovery constraint",
    "non-heat alternative rejection"
  ],
  "decisive_evidence": "Accumulated heat load, duration, and exposure scaling carry the mechanism decision; rainfall or image signals only test competing explanations.",
  "rejected_simplifications": "Reject peak-only, rainfall-led, and image-primary explanations when the computed heat-load chain is stronger.",
  "bounded_interpretation": "The result is a package-scale heat mechanism diagnosis, not exact mortality, outage, damage, or full regional attribution.",
  "formula_derivation": "Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `proof_result`, `diagnosis_label`, `indices.event_window_days`, `indices.days_tmax_ge40`, `indices.longest_tmax_ge40_run_days`, `indices.heat_load_gt40_c_day`, `indices.hottest_3day_tmax_mean_c`, `indices.hottest_3day_window`.
3. Use the computed values to build the ordered mechanism chain: event-window thermal forcing -> accumulated heat-load calculation -> persistence or recovery constraint -> non-heat alternative rejection.
4. Weight decisive evidence against alternatives: Accumulated heat load, duration, and exposure scaling carry the mechanism decision; rainfall or image signals only test competing explanations.
5. Reject simpler explanations: Reject peak-only, rainfall-led, and image-primary explanations when the computed heat-load chain is stronger.
6. Keep the interpretation bounded: The result is a package-scale heat mechanism diagnosis, not exact mortality, outage, damage, or full regional attribution.

Formula/scaling note: Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units.

Key computed anchors from the package:

- `event_window_days` = `76`
- `anchor_window` = `2022-03-01 to 2022-05-15`
- `first_day_ge_40c` = `2022-04-08`
- `days_ge_40c` = `26`
- `days_ge_42c` = `9`
- `days_ge_45c` = `1`
- `longest_hot_run_ge_40c_days` = `9`
- `heat_load_gt40_c_day` = `43.39999999999999`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.bin`
- `data/event_reports/event_reports_003_Locked_event_anchor_2022_India-Pakistan_early_heatwave.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
