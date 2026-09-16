# Correct Answer

```json
{
  "answer": "heavy_concentrated_rainfall_with_weak_mean_surface_change",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "reconstruct how rainfall concentration translates into pluvial or urban runoff pressure rather than a generic wet-period label",
  "computed_evidence": {
    "rain_window_days": 24,
    "rain_diagnostic_diagnostic_test": {
      "products_ge_150": 3,
      "max_product_mm": 258.84,
      "pass": true
    },
    "concentration": {
      "product": "gpm",
      "max_to_mean_ratio": 3.105,
      "pass": true
    },
    "surface_contrast": {
      "sentinel1_mean_db": 0.047,
      "sentinel1_min_db": -23.08,
      "dark_blue_pp": 0.81,
      "alphaearth_mean": 0.013,
      "label": "strong_local_weak_mean"
    },
    "receptor_evidence_synthesis": {
      "population": 269933,
      "highways": 330,
      "critical_amenities": 20,
      "diagnostic_diagnostic_test_hits": 3
    }
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
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `rain_window_days`, `rain_diagnostic_diagnostic_test.products_ge_150`, `rain_diagnostic_diagnostic_test.max_product_mm`, `rain_diagnostic_diagnostic_test.pass`, `concentration.product`, `concentration.max_to_mean_ratio`, `concentration.pass`, `surface_contrast.sentinel1_mean_db`.
3. Use the computed values to build the ordered mechanism chain: rainfall burst or accumulation -> duration/intensity or areal-load calculation -> urban runoff or receptor context -> single-number simplification rejection.
4. Weight decisive evidence against alternatives: Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.
5. Reject simpler explanations: Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.
6. Keep the interpretation bounded: The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals.

Key computed anchors from the package:

- `event_window` = `{"start": "2024-08-13", "end": "2024-09-05", "days": 24}`
- `tolerances` = `{"mm": 0.02, "ratio": 0.005, "db": 0.01, "pp": 0.02, "population": 1}`
- `formulas` = `{"duration_days": "inclusive calendar days from start to end", "max_to_mean_ratio": "product event-window local maximum / product event-window mean", "dark_blue_pp": "(event dark-blue proxy share - pre-event dark-blue proxy share) * 100", "`
- `precipitation_inputs` = `{"maxima_mm": {"era5_land": 171.63, "gpm": 258.84, "chirps": 171.054}, "means_mm": {"era5_land": 102.47, "gpm": 83.362, "chirps": 96.895}, "ratios": {"era5_land": 1.675, "gpm": 3.105, "chirps": 1.765}, "three_product_mean_mm": 94.242}`
- `threshold_results` = `{"rainfall_load_pass": true, "concentration_pass": true, "surface_label": "strong_local_weak_mean", "receptor_threshold_hits": 3}`
- `surface_inputs` = `{"sentinel1_pre_count": 38, "sentinel1_post_count": 46, "sentinel1_mean_db": 0.047, "sentinel1_min_db": -23.08, "dark_blue_pp": 0.81, "alphaearth_mean": 0.013, "pre_image": {"available": true, "width": 1024, "height": 768, "mean_rgb": [143.`
- `receptor_inputs` = `{"population": 269933, "highways": 330, "critical_amenities": 20, "element_count": 1000, "amenity_counts": {"hospital": 1, "police": 11, "school": 6, "shelter": 2}}`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_2024_Sudan_floods_and_Arba_at_Dam_flood.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_005_OpenStreetMap_Overpass_bounded_AOI_slice.json`
- `data/remote_sensing/remote_sensing_005_Sentinel-1_GRD_VV_pre_post_change.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/remote_sensing/remote_sensing_007_pre.jpg`
- `data/remote_sensing/remote_sensing_008_event.jpg`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
