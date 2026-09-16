# Taan Fiord Landslide-Tsunami Source Dominance Model

Using the local CSX-313 event package, reconstruct the 17 October 2015 Taan Fiord glacier-adjacent landslide tsunami as a source-driven fjord hazard. Select package-relative evidence for every value or qualitative claim you use, and make clear which evidence is decisive versus contextual.

Return one valid JSON object with exactly these top-level keys:

- `source_paths`
- `process_model`
- `computed_metrics`
- `scenario_analysis`
- `scientific_use_notes`
- `final_interpretation`

Use these calculations and round numeric outputs as specified:

1. Extract the landslide mass in million tons and the maximum tsunami runup in meters from the strongest event report evidence. Compute `source_runup_load_million_ton_m = mass_million_tons * runup_m`, rounded to two decimals.
2. Compute `source_power_norm = clip(source_runup_load_million_ton_m / 40000, 0, 1)`, rounded to three decimals.
3. Evaluate five report-supported mechanism terms: `fjord_landslide_source`, `rock_mass_reported`, `tsunami_runup_reported`, `glacier_retreat_context`, and `deep_water_context`. Compute `report_mechanism_completeness` as the supported-term count divided by `5`, rounded to three decimals.
4. Set `glacier_retreat_context_flag` to `1` only if the event report explicitly links glacier retreat, unstable slopes, and deep water at the fjord margin; otherwise set it to `0`.
5. Compute `process_dominance_index = 100 * (0.65 * source_power_norm + 0.25 * report_mechanism_completeness + 0.10 * glacier_retreat_context_flag)`, rounded to two decimals.
6. For a fjord-sensitivity scenario, increase only the runup by 15 percent, recompute `scenario_runup_m`, `scenario_source_power_norm`, and `scenario_process_dominance_index`, and report `scenario_delta_index`, all rounded consistently.

Classify the event as `source_dominated_landslide_tsunami_report_confirmed` if `source_power_norm >= 0.75`, `report_mechanism_completeness >= 0.80`, and `glacier_retreat_context_flag == 1`; otherwise classify it as `mixed_or_underconstrained_fjord_hazard`.

In `scientific_use_notes`, briefly state which package evidence families were decisive, which were only weak context, and why this matters for disaster-process interpretation.

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

For this task, use that object to make the Taan Fiord model emphasize source dominance, fjord setting, glacier retreat context, and scenario sensitivity.

