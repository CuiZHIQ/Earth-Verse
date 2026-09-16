# North Atlantic Marine Heatwave Key Variable Ranking

A climate diagnostics team is reassessing the 2023 global/North Atlantic marine heatwave package. They need to know which intermediate variable has the greatest diagnostic leverage for deciding whether the record supports a persistent marine heatwave rather than a single SST peak or a report label.

Using only local evidence in the CSX-021 event package, identify the marine-heatwave definition, time-series or gridded summary evidence, and ocean-temperature report anchors. Rank these candidate variables by diagnostic leverage:

- `exceedance_duration`
- `sst_anomaly_intensity`
- `cumulative_heat_load`
- `peak_sst_only`
- `threshold_choice`
- `report_label_only`

Favor variables that are thresholded, time-resolved, and calculable from package values. Compute any needed intermediate values such as the MHW threshold definition, duration, anomaly or intensity, cumulative heat load, and duration-record ratio; express the peak-only contrast through the variable score/ranking and reasoning path rather than as a separate required field.

Return compact JSON in this shape:

```json
{
  "answer": "<top-ranked variable>",
  "target_family": "marine_heatwave_key_intermediate_variable_ranking",
  "computed_values": {},
  "variable_scores": {},
  "ranked_variables": [],
  "key_variable": "<same as answer>",
  "rejected_variable": "<lowest-leverage variable>",
  "reasoning_path": []
}
```
