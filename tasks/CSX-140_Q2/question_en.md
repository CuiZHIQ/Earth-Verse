# Atacama Rainfall Outlier Key Variable Ranking

A hydrometeorology team is reassessing the March 24-26, 2015 storm and flash floods in northern Chile's Atacama Desert. They need to know which intermediate variable has the greatest diagnostic leverage for deciding whether the record supports a local-climatology rainfall outlier rather than a uniformly extreme 50 mm precipitation-grid case.

Using only local evidence in the CSX-140 event package, identify the local rainfall normal, the report rainfall anchors, the gridded or statistical precipitation summaries, and the relevant impact-report counts. Rank these candidate variables by diagnostic leverage:

- `local_climatology_ratio`
- `report_total_and_station_share`
- `largest_grid_peak_below_report_total`
- `killed_missing_or_home_damage_counts`
- `uniform_50mm_grid_case`
- `loss_count_only`

Favor variables that are calculable, rainfall-specific, and able to separate a locally extraordinary Atacama rainfall event from a simple uniform 50 mm grid-threshold reading. Compute any needed intermediate values such as the Antofagasta rainfall-to-annual-average ratio, the report total rainfall anchor, the Antofagasta-to-report-total share, the largest event-window gridded/statistical precipitation maximum and below-report-total check, killed-plus-missing people, impacted homes, and swept-away home share.

Return only compact JSON in this shape:

```json
{
  "answer": "<top-ranked variable>",
  "target_family": "atacama_rainfall_outlier_key_intermediate_variable_ranking",
  "computed_values": {},
  "variable_scores": {},
  "ranked_variables": [],
  "key_variable": "<same as answer>",
  "rejected_variable": "<lowest-leverage variable>",
  "reasoning_path": []
}
```
