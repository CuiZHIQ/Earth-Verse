# 2022 China Heat-Drought Mechanism Dominance Ranking

A hydrometeorology review team wants to move beyond a pass/fail ledger for the summer 2022 China heat wave and drought over the Poyang Lake-Yangtze River system. The task is to rank physical mechanisms by explanatory dominance for the heat-drought diagnosis.

Use only local evidence in the CSX-015 event package. You should read across available weather time series, hydrologic and drought reports, precipitation summaries, and gridded or remote-sensing summaries when present.

Rank these candidate mechanisms:

- `persistent_heat_load`
- `evaporative_demand`
- `hydrologic_low_water_timing`
- `precipitation_deficit_only`
- `reported_loss_or_exposure_only`

Compute the evidence needed to support the ranking, including heat persistence, warm-night or apparent-heat persistence, humidity-derived evaporative demand, Poyang/Yangtze low-water timing, and precipitation timing context. Return compact JSON in this shape:

```json
{
  "answer": "<compact_label>",
  "target_family": "heat_drought_mechanism_dominance_ranking",
  "computed_values": {
    "<metric_name_with_unit_if_needed>": <number>
  },
  "mechanism_scores": {
    "<mechanism_name>": <integer_score>
  },
  "ranked_mechanisms": ["<highest_dominance>", "...", "<lowest_dominance>"],
  "dominant_mechanism": "<mechanism_name>",
  "rejected_mechanism": "<mechanism_name>",
  "reasoning_path": "<compact calculation-based rationale>"
}
```

Add no more than one sentence after the JSON.
