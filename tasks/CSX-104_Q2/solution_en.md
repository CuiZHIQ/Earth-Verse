# Correct Answer

```json
{
  "answer": "persistent_rainfall_corridor_loading",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "diagnose whether persistent rainfall over steep terrain supports a flood, debris, or landslide hazard chain rather than a short shower",
  "computed_evidence": {
    "metrics": {
      "event_precip_mm": 300.4,
      "wettest_48h_mm": 279.5,
      "share_48h": 0.93,
      "peak_hour_share": 0.026,
      "persistence_margin": 36.3,
      "wet_run_hours": 67,
      "gridded_max_ratio": 2.46,
      "near_context_count": 105
    },
    "passes": {
      "share_48h": true,
      "persistence_margin": true,
      "wet_run_hours": true,
      "gridded_max_ratio": true,
      "near_context_count": true
    },
    "diagnostic_diagnostic_test_proof": "All five clauses pass: 0.930 >= 0.90, 36.3 >= 30, 67 >= 48, 2.46 >= 2.0, and 105 >= 100."
  },
  "mechanism_chain": [
    "persistent mountain rainfall",
    "terrain-enhanced runoff or slope response",
    "flood-landslide pathway",
    "short-burst simplification rejection"
  ],
  "decisive_evidence": "Duration and mountain-process context should dominate over a single local precipitation value.",
  "rejected_simplifications": "Reject a short convective shower or flat-basin explanation if terrain and persistence are required by the evidence.",
  "bounded_interpretation": "The answer should not infer complete landslide inventories, exact valley hydraulics, or all losses."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `metrics.event_precip_mm`, `metrics.wettest_48h_mm`, `metrics.share_48h`, `metrics.peak_hour_share`, `metrics.persistence_margin`, `metrics.wet_run_hours`, `metrics.gridded_max_ratio`, `metrics.near_context_count`.
3. Use the computed values to build the ordered mechanism chain: persistent mountain rainfall -> terrain-enhanced runoff or slope response -> flood-landslide pathway -> short-burst simplification rejection.
4. Weight decisive evidence against alternatives: Duration and mountain-process context should dominate over a single local precipitation value.
5. Reject simpler explanations: Reject a short convective shower or flat-basin explanation if terrain and persistence are required by the evidence.
6. Keep the interpretation bounded: The answer should not infer complete landslide inventories, exact valley hydraulics, or all losses.

Key computed anchors from the package:

- `event_name` = `June 2013 Kedarnath and Uttarakhand flash floods`
- `event_window` = `2013-06-15 to 2013-06-18`
- `wettest_hour_mm` = `7.7`
- `wettest_hour_time` = `2013-06-17T11:00`
- `wettest_48h_start` = `2013-06-15T19:00`
- `gridded_inputs` = `{"gpm_max_mm": 564.49, "gpm_mean_mm": 231.22, "chirps_max_mm": 569.32, "chirps_mean_mm": 146.65, "gridded_max_ratio": 2.46}`
- `near_context_inputs` = `{"building_features": 59, "waterway_features": 46, "tourism_hotel_features": 12, "category_hit_total": 117, "overlapping_category_hits": 12, "near_context_count": 105}`
- `thresholds` = `{"share_48h_min": 0.9, "persistence_margin_min": 30.0, "wet_run_hours_min": 48, "gridded_max_ratio_min": 2.0, "near_context_count_min": 100}`

# Source Paths

- `metadata/event.json`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`
- `data/physical_hazard/physical_hazard_006_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/exposure_impact/exposure_impact_005_OpenStreetMap_Overpass_bounded_AOI_slice.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
