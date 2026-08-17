# Typhoon Doksuri Haihe Rainfall-Runoff Routing Ledger

In late July and early August 2023, Typhoon Doksuri's remnant circulation produced exceptional rainfall across the Beijing-Tianjin-Hebei region and stressed the Haihe river system. A hydrology review team needs a calculation-led check of whether the record is best summarized as persistent remnant rainfall feeding runoff and downstream river routing, rather than as a single-hour peak or wind-dominant event.

Return only compact JSON with this structure:

```json
{
  "target_family": "doksuri_haihe_rainfall_runoff_routing_score_ledger",
  "score_ledger": [
    {"row_id": "rainfall_persistence_load", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": ""},
    {"row_id": "peak_hour_concentration_test", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": ""},
    {"row_id": "report_total_transfer_test", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": ""},
    {"row_id": "runoff_equivalent_load", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": ""},
    {"row_id": "wind_and_image_dominance_test", "formula": "", "computed_values": {}, "threshold_or_test": "", "result": ""}
  ],
  "final_label": ""
}
```

Use quantitative anchors for the rainfall totals, wet-window concentration, peak-hour fractions, report-total ratios, runoff-equivalent volumes, wind speed, and image-change summaries. The final label should be a concise routing diagnosis, not a general event narrative.
