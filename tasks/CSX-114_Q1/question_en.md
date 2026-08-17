# Cyclone Gonu Oman Severity Ledger

Cyclone Gonu crossed the Arabian Sea in early June 2007, struck Oman, and then affected Iran. A cyclone-risk analyst is preparing an Oman-focused numerical check of whether the recorded storm intensity, Oman rainfall concentration timing, coastal wind-wave values, and cross-country impacts form one internally consistent severity ledger.

Use the technical record and quantitative diagnostics to reconstruct a five-row computation ledger. Each row must compute the relevant values and report `pass` or `fail`:

- `intensity_conversion`: convert the official peak wind from knots to km/h using `1 kt = 1.852 km/h`; include the lowest pressure and super-cyclone duration; pass if the original peak wind is at least `64 kt`.
- `rainfall_timing`: compute the 2007-06-06 point-rainfall share of point event precipitation, the peak-hour share of event precipitation, and the wet-hour count; pass only if the 2007-06-06 share is at least `0.80`, the peak-hour share is below `0.15`, and wet hours are at least `24`.
- `coastal_wind_wave`: report the Oman wave height, Muscat wind, and point gust; pass if waves are at least `5 m` and at least one wind or gust value is at least `100 km/h`.
- `oman_iran_impact_ratio`: convert Oman damage to USD million, then compute Oman/Iran damage and death ratios; pass if both ratios exceed `1`.
- `rainfall_measurement_contrast`: compare the reported Oman coastal rainfall maximum with the point event total and the gridded precipitation maximum; pass only if the lower point and gridded totals are not substituted for the reported coastal maximum.

Return compact JSON in this shape:

```json
{
  "ledger": [
    {
      "row_id": "intensity_conversion",
      "formula_or_check": "<formula or inequality>",
      "computed_values": {},
      "result": "pass|fail",
      "proof_note": "<one short sentence>"
    }
  ],
  "final_classification": "<short label>",
  "caution_note": "<one short sentence>"
}
```

Use all five row IDs exactly once. Round ratios and shares to three decimals or percentages to one decimal place. Keep the proof calculation-led; do not infer exact local losses from point or gridded rainfall values.

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

For this task, use that object to separate cyclone intensity, rainfall timing, coastal wind-wave forcing, cross-country impacts, and measurement-scale contrast before giving the severity label.

