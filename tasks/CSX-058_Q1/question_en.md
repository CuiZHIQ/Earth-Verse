# UAE Rainfall-Load Compression Uncertainty Propagation

You are a hydrometeorological uncertainty analyst evaluating the April 15-17, 2024 UAE and Dubai record-rainfall flood. The question is whether the rainfall-load compression mechanism remains robust when the reported rainfall anchors are treated as uncertain inputs.

Use only the local CSX-058 event package. Select package-relative evidence for each rainfall anchor and mechanism claim.

Compute the baseline ratios:

- `peak_vs_annual_high = peak_24h_mm / annual_high_mm`
- `airport_implied_annual_mm = airport_mm / airport_reported_multiplier`
- `airport_vs_implied_annual = airport_mm / airport_implied_annual_mm`

Then propagate uncertainty by reporting each ratio's margin above the decision boundary of 1.0. Identify which input anchor would be most sensitive to small perturbations and whether the mechanism label would remain stable under small report-scale errors.

Return JSON only:

```json
{
  "answer": "<same as classification_result>",
  "target_family": "dubai_rainfall_load_uncertainty_propagation",
  "rainfall_anchors": {
    "peak_24h_mm": 0,
    "annual_high_mm": 0,
    "airport_mm": 0,
    "airport_reported_multiplier": 0
  },
  "computed_ratios": {
    "peak_vs_annual_high": 0,
    "airport_implied_annual_mm": 0,
    "airport_vs_implied_annual": 0
  },
  "uncertainty_margins": {
    "peak_vs_annual_high_margin_above_1": 0,
    "airport_vs_implied_annual_margin_above_1": 0,
    "most_sensitive_anchor": "<short label>",
    "robust_to_small_anchor_error": true
  },
  "decision_rule": "...",
  "classification_result": "pass_or_fail_label",
  "mechanism_label": "...",
  "rejected_alternative": "..."
}
```

The final mechanism label should remain tied to rainfall-load compression and arid-urban pluvial runoff, not to coastal surge, large-river flooding, or an exposure-only explanation.
