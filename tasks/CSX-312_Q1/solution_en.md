# Final Answer

```json
{
  "answer": {
    "target_family": "candidate_explanation_score_ledger",
    "metrics": {
      "fissure_km": 6.8,
      "lava_km2": 35.5,
      "rate_m3s": 100.0,
      "eq_mw": 6.9,
      "collapse_mw": [4.7, 5.4],
      "precip_mm": 193.836
    },
    "flags": {
      "orange_alert": true,
      "scale_200yr": true,
      "lava_extent": true,
      "effusion": true,
      "quake": true,
      "collapse_energy": true,
      "summit_sequence": true
    },
    "scores": {
      "integrated": 10,
      "rainfall_context": 2,
      "ash_only": 0,
      "earthquake_only": 0
    },
    "final_label": "integrated_lerz_lava_collapse_chain"
  },
  "computed_consequence": "The ledger makes the high-precipitation signal contextual because the coupled lower East Rift Zone lava, summit-collapse, and earthquake gates dominate every counter-score."
}
```

# Key Computations

The USGS event narrative gives lower East Rift Zone fissures extending about `6.8 km`, lava covering about `35.5 sq km`, lava effusion rates exceeding `100 m3/s`, a largest earthquake of about `Mw 6.9`, and near-daily summit-collapse energy equivalents of `Mw 4.7-5.4`. The GDACS volcano entry gives an Orange alert. The precipitation summary gives a maximum accumulated value of `193.836 mm`.

The boolean gates are therefore:

```json
{
  "orange_alert": true,
  "scale_200yr": true,
  "lava_extent": true,
  "effusion": true,
  "quake": true,
  "collapse_energy": true,
  "summit_sequence": true
}
```

The integrated score is:

```text
2*orange_alert + 2*scale_200yr + 2*lava_extent + 1*effusion
+ 1*quake + 1*collapse_energy + 1*summit_sequence
= 2 + 2 + 2 + 1 + 1 + 1 + 1
= 10
```

The counter-scores are `rainfall_context = 2` because precipitation exceeds 150 mm, `ash_only = 0` because lava-covered area is documented, and `earthquake_only = 0` because eruptive fissure opening is documented.

# Reasoning Path

The decision rule requires `integrated_score >= 8` and `integrated_score > max(counter_scores)`. Here, `10 >= 8` and `10 > max(2, 0, 0)`, so the deterministic answer is `integrated_lerz_lava_collapse_chain`.

The failed counter-tests matter because each one uses a real signal but cannot dominate the ledger. Rainfall has a nonzero contextual score, yet it does not explain fissure opening, the lava-covered footprint, summit-collapse energy, or the Mw 6.9 earthquake. Ash-only and earthquake-only readings fail their own gates because documented lava coverage and eruptive fissures are present.

# Computed Interpretation

The compact computed consequence is that the 2018 Kilauea record supports a coupled lower East Rift Zone lava-flow, summit-collapse, and earthquake chain; rainfall remains a context metric rather than the controlling classification.

# Scoring Rubric

Total: 20 points.

- 3 points: returns compact JSON with `target_family`, `metrics`, `flags`, `scores`, `final_label`, and one `computed_consequence`; partial credit if the final label is present but one ledger block is incomplete.
- 4 points: extracts the six numeric metrics correctly within tolerance: fissure length `6.8 km`, lava area `35.5 sq km`, rate `100 m3/s`, earthquake `Mw 6.9`, collapse range `Mw 4.7-5.4`, and precipitation `193.836 mm`; partial credit for at least four correct metrics with units or recognizable field names.
- 4 points: applies the integrated-score formula exactly; partial credit for the right gates with one weight or arithmetic error.
- 3 points: computes counter-scores as `rainfall_context = 2`, `ash_only = 0`, and `earthquake_only = 0`; partial credit for rejecting the counterlabels qualitatively while omitting one score.
- 3 points: applies the decision rule and returns `integrated_lerz_lava_collapse_chain`; partial credit when the label is correct but the threshold comparison is not shown.
- 2 points: gives a concise computed consequence tied to the ledger and keeps rainfall contextual; partial credit for one minor unsupported embellishment.
- 1 point: avoids unsupported response advice, casualty/loss totals, road-closure claims, gas concentrations, ashfall depths, or broad disaster interpretation.
