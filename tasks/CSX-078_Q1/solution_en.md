# Correct Answer

```json
{
  "answer": "localized_arbaat_dam_cascade_supported",
  "bounded_interpretation": "Do not estimate breach hydrographs, exact wave heights, engineering fault, or complete loss totals unless sourced.",
  "computed_evidence": {
    "component_evidence_scores": {
      "dam_impact_record": 3,
      "duration_window": 2,
      "image_change_context": 1,
      "rainfall_accumulation": 2
    },
    "diagnosis_label": "rainfall_conditioned_dam_impact_chain",
    "diagnostic_diagnostic_test_result": "passes: total_score >= 6 and dam_impact_record = 3",
    "event_window_days": 24,
    "impact_diagnostic_diagnostic_tests_met": 7,
    "one_sentence_interpretation": "The evidence synthesis supports a rainfall-conditioned dam-impact chain: the long wet window and accumulated rainfall set the flood context, while the report-count diagnostic gates make the dam-linked impact path decisive.",
    "rainfall_anchors_mm": {
      "chirps_max": 103.777,
      "chirps_mean": 88.433,
      "gpm_max": 124.095,
      "gpm_mean": 89.272
    },
    "total_evidence_score": 8
  },
  "decisive_evidence": "The mechanism must connect forcing with pathway amplification; rainfall magnitude alone is not a complete explanation.",
  "mechanism_chain": [
    "storm or rainfall loading",
    "dam-area pathway or storage release",
    "downstream flood-wave amplification",
    "regional-rainfall-only rejection"
  ],
  "mechanism_question": "connect rainfall or report anchors to a localized dam-area cascade and downstream flood-wave pathway",
  "rejected_simplifications": "Reject regional-rainfall-only or exposure-only explanations if they do not explain the cascade pathway.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `component_evidence_scores.dam_impact_record`, `component_evidence_scores.duration_window`, `component_evidence_scores.image_change_context`, `component_evidence_scores.rainfall_accumulation`, `diagnosis_label`, `diagnostic_diagnostic_test_result`, `event_window_days`, `impact_diagnostic_diagnostic_tests_met`.
3. Use the computed values to build the ordered mechanism chain: storm or rainfall loading -> dam-area pathway or storage release -> downstream flood-wave amplification -> regional-rainfall-only rejection.
4. Weight decisive evidence against alternatives: The mechanism must connect forcing with pathway amplification; rainfall magnitude alone is not a complete explanation.
5. Reject simpler explanations: Reject regional-rainfall-only or exposure-only explanations if they do not explain the cascade pathway.
6. Keep the interpretation bounded: Do not estimate breach hydrographs, exact wave heights, engineering fault, or complete loss totals unless sourced.

Key computed anchors from the package:

- `decision_rule` = `answer is rainfall_conditioned_dam_impact_chain when total_score >= 6 and dam_impact_record = 3`
- `event_window` = `{"days": 24, "end_date": "2024-09-05", "start_date": "2024-08-13"}`
- `impact_counts` = `{"collapsed_borehole_wells": 84, "fatalities_at_least": 30, "missing_livestock_over": 10000, "schools_damaged_or_destroyed": 70, "severely_affected_people": 50000, "villages_destroyed": 20, "villages_impacted": 70}`
- `impact_tests` = `{"collapsed_borehole_wells_ge_50": true, "fatalities_at_least_ge_25": true, "missing_livestock_over_ge_10000": true, "schools_damaged_or_destroyed_ge_50": true, "severely_affected_people_ge_40000": true, "villages_destroyed_ge_10": true, "v`
- `radar_context` = `{"abs_change_max_db": 0.5, "mean_vv_post_minus_pre_db": 0.115, "post_count": 5, "pre_count": 5}`
- `rainfall_rule` = `{"gpm_max_min_mm": 100, "gpm_mean_min_mm": 75, "mean_crosscheck_max_abs_diff_mm": 10, "observed_mean_abs_diff_mm": 0.839}`

# Source Paths

- `data/event_reports/event_reports_003_Locked_event_anchor_2024_Sudan_floods_and_Arba_at_Dam_flood.json`
- `data/other/other_001_UN_Geneva_OCHA_-_Flooding_from_Sudan_dam_collapse_worsens_humanitarian_crisis.html`
- `data/physical_hazard/physical_hazard_007_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_009_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/remote_sensing/remote_sensing_006_Sentinel-1_GRD_VV_pre_post_change.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
