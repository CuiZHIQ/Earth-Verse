# Correct Answer

```json
{
  "answer": "post_tropical_rainfall_chain_consistent",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "reconstruct how rainfall concentration translates into pluvial or urban runoff pressure rather than a generic wet-period label",
  "computed_evidence": {
    "required_fields": [
      "target_family",
      "values",
      "tests",
      "rejected_alternatives",
      "final_label"
    ],
    "key_values": {
      "regional_floor_mm": 254.0,
      "record_hour_mm": 88.1,
      "record_hour_mm_unrounded": 88.138,
      "event_total_mm": 133.9,
      "wettest_6h_mm": 98.3,
      "six_hour_concentration": 0.734,
      "wet_hours": 23,
      "longest_wet_run_hours": 23,
      "max_wind_kmh": 45.2
    },
    "required_passes": [
      "regional_rainfall_floor",
      "record_hour_burst",
      "six_hour_concentration",
      "wet_run_persistence",
      "secondary_wind_context"
    ],
    "required_rejections": [
      "single_hour_only",
      "wind_primary"
    ]
  },
  "mechanism_chain": [
    "rainfall burst or accumulation",
    "duration/intensity or areal-load calculation",
    "urban runoff or receptor context",
    "single-number simplification rejection"
  ],
  "decisive_evidence": "Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.",
  "rejected_simplifications": "Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.",
  "bounded_interpretation": "The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `required_fields`, `key_values.regional_floor_mm`, `key_values.record_hour_mm`, `key_values.record_hour_mm_unrounded`, `key_values.event_total_mm`, `key_values.wettest_6h_mm`, `key_values.six_hour_concentration`.
3. Use the computed values to build the ordered mechanism chain: rainfall burst or accumulation -> duration/intensity or areal-load calculation -> urban runoff or receptor context -> single-number simplification rejection.
4. Weight decisive evidence against alternatives: Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.
5. Reject simpler explanations: Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.
6. Keep the interpretation bounded: The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals.

Key computed anchors from the package:

- `regional_floor_mm` = `254.0`
- `record_hour_mm` = `88.1`
- `record_hour_mm_unrounded` = `88.138`
- `event_total_mm` = `133.9`
- `wettest_6h_mm` = `98.3`
- `six_hour_concentration` = `0.734`
- `wet_hours` = `23`
- `longest_wet_run_hours` = `23`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_September_2021_Hurricane_Ida_Northeast_flooding.json`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
