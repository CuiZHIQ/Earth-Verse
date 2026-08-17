# North Atlantic Marine Heatwave Persistence and Phase Diagnosis

A climate-risk methods team is reconstructing the 2023 global and North Atlantic marine heatwave as a basin-scale thermal episode. The central question is whether the evidence supports a persistent, record-context marine heatwave with phase evolution across the basin, or a much weaker explanation such as a brief SST pulse or a single-cause climate-mode episode.

Use only the local CSX-021 event package. Select package-relative evidence for the duration, record-context, anomaly, and phase-timing values you use.

Compute the following quantities:

- `mhw_min_months`: the minimum reported North Atlantic marine-heatwave duration in months.
- `duration_ratio`: convert that duration to days with `round(months * 365 / 12)`, then divide by the five-day marine-heatwave definition.
- `coverage_record_ratio`: average daily marine-heatwave coverage in 2023 divided by the previous record value.
- `mhw_days_record_ratio`: global mean marine-heatwave days in 2023 divided by the previous record value.
- `max_sst_anomaly_c`: the North Atlantic SST anomaly anchor.
- `phase_code`: a compact code describing the basin evolution from the north-east May peak to Caribbean conditions by autumn.
- `final_label`: the final diagnosis.
- `proof_sentence`: one sentence that links persistence, record ratios, anomaly magnitude, and phase timing.

Return only JSON:

```json
{
  "mhw_min_months": "<integer>",
  "duration_ratio": "<number>",
  "coverage_record_ratio": "<number>",
  "mhw_days_record_ratio": "<number>",
  "max_sst_anomaly_c": "<number>",
  "phase_code": "<short_code>",
  "final_label": "<short_label>",
  "proof_sentence": "<one sentence>",
  "evidence_paths": ["package-relative/path"]
}
```

Use `persistent_record_marine_heatwave` only when the duration, record-context ratios, SST anomaly, and basin phase timing jointly support a persistent record-scale marine heatwave rather than a brief pulse or a sole-driver explanation.
