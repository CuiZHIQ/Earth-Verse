# April 2004 Bangladesh Storm-Flood Process-Chain Control Ranking

A hydrometeorology team is turning the April 2004 Bangladesh severe-storm and flood record from a classification ledger into a process-chain diagnosis. Rank which control points most govern the diagnosis from severe-storm rainfall to later floodplain flooding.

Use only evidence in the local CSX-147 event package. Discover the relevant event anchor, storm and flood timing text, gridded precipitation summaries, report process flags, and any local catalog context available in the package.

Rank these candidate control points:

- `rainfall_to_flood_timing`
- `multi_day_rainfall_accumulation`
- `river_or_storage_response`
- `single_peak_rainfall_only`
- `reported_damage_only`
- `wind_or_storm_label_only`

Your ranking should be calculation-led. Compute the event-window duration, storm-sequence duration, storm-to-flood lags, gridded precipitation maxima and max-to-mean ratios, gridded spread, report-derived runoff or river flags, Bangladesh displacement consistency, and local catalog support if present. Rank the controls by how much they govern the storm-to-flood classification, not by operational response priority or advice.

Return compact JSON in this exact top-level shape:

```json
{
  "answer": "",
  "target_family": "bangladesh_storm_flood_process_chain_control_ranking",
  "computed_values": {},
  "control_point_scores": {},
  "ranked_control_points": [],
  "top_control_point": "",
  "rejected_control_point": "",
  "reasoning_path": []
}
```
