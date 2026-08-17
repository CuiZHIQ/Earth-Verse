# CSX-013 Text-Numeric Alignment Audit

A benchmark reviewer is checking whether a model can align the NOAA report language for the June 25-July 1, 2021 Pacific Northwest heat wave with the package's machine-readable local heat evidence without over-claiming that a local point file proves every regional or city-specific statement.

Use only evidence from the local CSX-013 event package. Do not use web search, inactive tasks, hidden answers, or outside facts. Return package-relative paths only.

Construct a structured JSON answer that performs a text-numeric alignment audit:

1. Extract five compact claim records from the locked NOAA report: regional four-day record heat, Portland's three-day record sequence, Lytton/Canada's peak record sequence, the high-pressure/downslope mechanism, and Seattle/Portland air-conditioning vulnerability.
2. Recompute the local Open-Meteo point checks for the official event window and the report's June 26-29 heat window: daily Tmax sequence, local peak, days at or above 100 F, hot-hour count, heat-degree hours above 30 C, warm-night count using Tmin >= 16 C, peak wet-bulb temperature by the Stull approximation, and RH at the peak air-temperature hour.
3. For each claim, classify the alignment between the report text and the local/package evidence as one of: `aligned_local_numeric`, `partial_timing_not_magnitude`, `report_supported_not_local_numeric`, or `unsupported_by_package_machine_data`.
4. Build a source provenance reliability ladder for this specific audit, distinguishing direct local numeric evidence, locked report text, event anchor metadata, weak mechanism context, and wrong-modality decoys.
5. Include rejected or insufficient alternatives for common failure modes: treating the local point as Portland or Lytton, using ERA5 aggregate wind/temperature statistics as a pressure/downsloping proof, and using precipitation/catalog/remote-sensing files as direct heat-record evidence.

Use these formulas and rounding rules:

- `F = C * 9 / 5 + 32`
- `C = (F - 32) * 5 / 9`
- `HDD30 = sum(max(T - 30, 0))` over hourly temperature in degrees C.
- Stull wet-bulb approximation with hourly `T` in degrees C and `RH` in percent:

```text
WBT = T * atan(0.151977 * sqrt(RH + 8.313659))
      + atan(T + RH)
      - atan(RH - 1.676331)
      + 0.00391838 * RH^1.5 * atan(0.023101 * RH)
      - 4.686035
```

Round temperatures and temperature deltas to 1 decimal, HDD30 to 1 decimal, precipitation means/deltas to 3 decimals, population to 3 decimals, and wet-bulb/RH checks to 1 decimal.

Return only JSON with exactly these top-level keys:

`answer_type`, `audit_question`, `scope`, `claim_matrix`, `local_numeric_checks`, `source_reliability_ladder`, `counterfactuals`, `final_ruling`, `reference_trace`

Use fixed answer type `text_numeric_alignment_audit`. Use stable IDs in ordered lists: claims `C1`-`C5`, numeric checks `NC1`-`NC7`, sources `S1`-`S5`, counterfactuals `CF1`-`CF3`, and trace steps `T1`-`T6`.

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

For this task, use that object to emphasize report-vs-local numerical alignment and prevent the local point from being overextended to Portland, Lytton, or regional mechanisms.

