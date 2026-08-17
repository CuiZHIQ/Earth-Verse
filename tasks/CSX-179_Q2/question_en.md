# Southeast Asia Haze Gas-Signal Ledger

An air-quality science team is checking the 2015 Southeast Asia haze episode affecting Indonesia and downwind areas including Singapore and Malaysia during 2015-08-01 to 2015-11-30. The team needs a compact signal ledger that decides whether the evidence is led by carbon-monoxide-rich fire smoke, a burn-perimeter exercise, or a rainfall-total anomaly.

Using the technical record and quantitative diagnostics, return only JSON. Keep rainfall diagnostics bounded to the available package windows and use them only as a secondary context check.

```json
{
  "classification": "<compact classification label>",
  "co_signal": {
    "usual_surface_ppb": "<number>",
    "peak_surface_borneo_ppb_nearly": "<number>",
    "peak_to_usual_multiplier": "<number>"
  },
  "vertical_transport": {
    "calipso_plume_km": "<number>",
    "airs_co_km": "<number>",
    "mls_co_km": "<number>",
    "mls_to_calipso_ratio": "<number>"
  },
  "context_checks": {
    "rainfall_totals_secondary": "<boolean>",
    "burn_perimeter_from_dnbr": "<established or not_established>"
  },
  "image_reading": "<one sentence connecting the before/during true-color views to the ledger>",
  "computed_interpretation": "<one concise sentence tied only to the ledger>"
}
```

Keep the interpretation compact. Do not add action steps, realized-loss totals, or broad policy advice.
