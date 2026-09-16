# Cyclone Freddy Load Ledger

Tropical Cyclone Freddy affected Madagascar, Mozambique, and Malawi during February-March 2023. A regional hazard-analysis team is checking whether the event clears a deterministic high-load cyclone screen based on persistence, peak wind, and local event-window rainfall.

Compute the ledger from the technical record using these rules:

- Persistence clears if `duration_days >= 30`.
- Wind clears if `peak_wind_kmh >= 200`.
- Rainfall clears if `local_event_rainfall_mm >= 300`; compute this rainfall total only over the package's locked event window, using hourly precipitation values whose UTC timestamps fall inside that window.
- `normalized_load_index = duration_days / 30 + peak_wind_kmh / 200 + local_event_rainfall_mm / 300`, rounded to three decimals.
- `threshold_pass_count` is the number of the three threshold tests that clear.

Return exactly one compact JSON object with these fields:

- `duration_days`
- `peak_wind_kmh`
- `local_event_rainfall_mm`
- `normalized_load_index`
- `threshold_pass_count`
- `severity_label`

Use `triple_threshold_high_cyclone_load` as the label only if all three thresholds clear and the normalized load index is at least 3.0.

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to make the cyclone load answer justify the label from persistence, wind, and locked-window rainfall rather than threshold count alone.

