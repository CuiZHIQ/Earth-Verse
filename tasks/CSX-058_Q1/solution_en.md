# Final Answer

```json
{
  "answer": "annual_load_compression_pass",
  "target_family": "dubai_rainfall_load_uncertainty_propagation",
  "rainfall_anchors": {
    "peak_24h_mm": 250.0,
    "annual_high_mm": 200.0,
    "airport_mm": 119.0,
    "airport_reported_multiplier": 1.5
  },
  "computed_ratios": {
    "peak_vs_annual_high": 1.25,
    "airport_implied_annual_mm": 79.33,
    "airport_vs_implied_annual": 1.5
  },
  "uncertainty_margins": {
    "peak_vs_annual_high_margin_above_1": 0.25,
    "airport_vs_implied_annual_margin_above_1": 0.5,
    "most_sensitive_anchor": "peak_24h_mm_or_annual_high_mm",
    "robust_to_small_anchor_error": true
  },
  "decision_rule": "pass if peak_vs_annual_high >= 1.0 and airport_vs_implied_annual >= 1.0",
  "classification_result": "annual_load_compression_pass",
  "mechanism_label": "arid_urban_pluvial_runoff",
  "rejected_alternative": "coastal_surge_or_large_river_primary_driver"
}
```

# Key Computations

The rainfall anchors are `250 mm` in less than 24 hours, `200 mm` as the conservative high end of normal annual rainfall, `119 mm` at Dubai International Airport, and the airport report multiplier `1.5`.

The baseline ratios are:

- `peak_vs_annual_high = 250 / 200 = 1.25`
- `airport_implied_annual_mm = 119 / 1.5 = 79.33`
- `airport_vs_implied_annual = 119 / 79.33 = 1.50`

The margins above the decision boundary are `0.25` and `0.50`. The peak/annual-high ratio is the more sensitive branch because it has the smaller margin above 1.0.

# Reasoning Path

Both rainfall-load compression ratios remain above 1.0, so small report-scale perturbations would not immediately reverse the diagnosis. The mechanism remains arid urban pluvial runoff because the proof is based on rainfall delivered at an annual-load scale in a short window. The calculation does not support a coastal-surge or large-river-primary explanation.

# Scoring Rubric

- 3 points: Returns the requested uncertainty-propagation JSON and `annual_load_compression_pass`.
- 4 points: Extracts all four rainfall anchors correctly.
- 4 points: Computes the three baseline ratios correctly.
- 3 points: Computes margins above the 1.0 decision boundary and identifies the more sensitive anchor.
- 3 points: Links robustness to the arid-urban pluvial runoff mechanism.
- 2 points: Rejects coastal-surge or large-river-primary explanations using the rainfall proof.
- 1 point: Avoids unsupported flood-depth, damage, casualty, or response-plan claims.
