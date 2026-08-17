# Langtang Seismic-Avalanche Threshold Ledger

A mountain-hazard analyst is reviewing the 25 April 2015 Langtang Valley, Nepal avalanche/landslide after the central Nepal earthquake. The decision need is not a broad narrative summary; it is a compact calculation that tests whether the record fits a seismic snow-ice-rock avalanche chain, or whether event-day rainfall and image diagnostics would make that label fail.

Compute the ledger below from the technical record and quantitative diagnostics.

- `report_score` (0-4): add one point each when the report record states that earthquake shaking released ice or rock, Langtang village was buried by an avalanche, the minimum reported deaths are at least 200, and the deposit covered the Langtang River.
- `rain_score` (0-2): add one point when the maximum event-day precipitation value across the daily weather and precipitation products is `<= 25 mm`; add one point when the precipitation range width is `<= 20 mm`.
- `radar_optical_score` (0-3): add one point when Sentinel-1 has at least 10 pre-event and at least 10 post-event observations; add one point when `abs(mean VV change) <= 1 dB` and `max VV change >= 20 dB`; add one point when the Sentinel-2 change status is `no_sufficient_scenes`.
- `river_score` (0-1): add one point when the report record says no lake had yet been found behind the river blockage.
- `ledger_total = report_score + rain_score + radar_optical_score + river_score`.

Set `answer` to `seismic_avalanche_chain_confirmed` when `ledger_total >= 8`; otherwise set it to `rain_or_image_led_chain_not_met`.

Return only JSON:

```json
{
  "target_family": "langtang_seismic_avalanche_threshold_window_ledger",
  "answer": "<classification_label>",
  "ledger_total": "<number>",
  "score_breakdown": {
    "report": "<number>",
    "rain": "<number>",
    "radar_optical": "<number>",
    "river": "<number>"
  },
  "metrics": {
    "fatalities_min": "<number>",
    "precip_values_mm": {},
    "precip_range_mm": ["<number>", "<number>"],
    "precip_range_width_mm": "<number>",
    "s1_counts": {},
    "s1_vv_change_db": {},
    "s2_status": "<string>"
  },
  "gate_trace": ["<compact calculation trace>"],
  "threshold_result": "<total-versus-threshold statement>"
}
```

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

For this task, use that object to force the answer to distinguish seismic release, weak rainfall evidence, and image-status limits in the Langtang avalanche chain.

