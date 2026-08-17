# Correct Answer

```json
{
  "answer": "exceedance_duration",
  "target_family": "marine_heatwave_key_intermediate_variable_ranking",
  "computed_values": {
    "definition_days_min": 5,
    "threshold_percentile": 90,
    "regional_duration_months_min": 10,
    "mean_duration_days": 54,
    "mean_intensity_c": 0.52,
    "cumulative_degree_days": 28.08,
    "duration_record_ratio": 1.349,
    "na_sst_anomaly_c": 3.0,
    "peak_global_sst_c": 18.99,
    "global_ocean_fraction": 0.94
  },
  "variable_scores": {
    "exceedance_duration": 0.96,
    "cumulative_heat_load": 0.91,
    "sst_anomaly_intensity": 0.84,
    "threshold_choice": 0.72,
    "peak_sst_only": 0.38,
    "report_label_only": 0.14
  },
  "ranked_variables": [
    "exceedance_duration",
    "cumulative_heat_load",
    "sst_anomaly_intensity",
    "threshold_choice",
    "peak_sst_only",
    "report_label_only"
  ],
  "key_variable": "exceedance_duration",
  "rejected_variable": "report_label_only",
  "reasoning_path": [
    "thresholded persistence exceeds the 5-day MHW definition by months",
    "cumulative heat load integrates duration and intensity",
    "intensity and peaks support severity but cannot prove persistence alone",
    "labels without threshold, duration, or intensity have lowest leverage"
  ]
}
```

# Key Computations

The local ocean evidence defines a marine heatwave as at least 5 consecutive days above the 90th percentile, with the NOAA summary phrasing the same idea as the warmest 10 percent for at least five days. The North Atlantic evidence reports at least 10 months in marine heatwave state, equivalent to about `10 * 365 / 12 = 304.2` days on a month-equivalent basis.

The Copernicus marine-heatwave summary gives a mean duration of `54 d` and mean daily intensity of `0.52 C`, so `cumulative_degree_days = 54 * 0.52 = 28.08 C-day`. The global record comparison is `116 / 86 = 1.349`, using the 2023 global average marine heatwave days and the previous record. The ocean-temperature anchors add a North Atlantic anomaly of `3.0 C`, a global peak daily SST of `18.99 C`, and `94 percent` global ocean surface with at least one marine heatwave, converted to `0.94`.

# Ranking Logic

`exceedance_duration` ranks first because it directly tests the word "persistent": it is thresholded, time-resolved, and far beyond the 5-day minimum definition. `cumulative_heat_load` is second because it combines duration and intensity into an integrated heat burden, but it depends on the duration result. `sst_anomaly_intensity` supports severity, especially with the 3.0 C North Atlantic anomaly and 0.52 C threshold-relative mean intensity, but intensity alone could still be a short-lived event.

`threshold_choice` is important because the 90th-percentile and 5-day rule makes the diagnosis reproducible, yet it is a definition rather than the event outcome. `peak_sst_only` is weak because one all-time daily SST peak does not distinguish a persistent marine heatwave from a spike. `report_label_only` is rejected because a label without threshold, duration, intensity, or heat-load calculations has the least diagnostic leverage.

# Reasoning Path

The conclusion is a persistent marine heatwave, so the most leveraged intermediate variable must discriminate persistence from peak-only or label-only evidence. Duration above the MHW threshold does that most directly. Cumulative heat load and intensity then explain the severity of the persistent event, while threshold choice guards reproducibility. Peak SST and report labels are supporting context, not decisive intermediate variables.

# Scoring Rubric

- 4 points: Returns the requested compact JSON shape with answer, target_family, computed_values, variable_scores, ranked_variables, key_variable, rejected_variable, and reasoning_path.
- 4 points: Correctly identifies and ranks `exceedance_duration` first and explains why thresholded persistence is the key diagnostic variable.
- 3 points: Computes the MHW definition anchors correctly: 5-day minimum, 90th percentile threshold, and at least 10 months for the regional MHW state.
- 3 points: Computes integrated and comparative values correctly: `28.08 C-day` cumulative heat load and `1.349` global MHW-day record ratio.
- 2 points: Uses the ocean intensity anchors correctly: `0.52 C` mean MHW intensity, `3.0 C` North Atlantic anomaly, and `18.99 C` peak global SST as supporting rather than top-ranked evidence.
- 2 points: Rejects peak-only and label-only reasoning, especially `report_label_only`, as lower leverage than thresholded duration or cumulative heat load.
- 1 point: Uses only local ocean/heat evidence and does not require OSM, AOI, population, exposure, rainfall, dNBR, embedding-change, or land-surface proxy files.
- 1 point: Keeps units, rounding, and ranking order clear enough for deterministic checking.
