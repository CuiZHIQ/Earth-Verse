# Kilauea Volcanic Chain Score Ledger

For the May-August 2018 Kilauea eruption on Hawai'i Island, compute a deterministic score ledger that tests whether the event is best classified as an integrated lower East Rift Zone lava and summit-collapse chain rather than a rainfall-context, ash-only, or earthquake-only explanation.

Use the technical record to extract these values: fissure length in kilometers, lava-covered area in square kilometers, minimum high lava-effusion rate in cubic meters per second, largest earthquake moment magnitude, summit-collapse energy-equivalent Mw range, maximum accumulated precipitation in millimeters, and the volcano alert level.

Definitions:

- `orange_alert`: true when the volcano alert level is Orange.
- `scale_200yr`: true when the record states that the event was the largest lower East Rift Zone eruption and caldera collapse in at least 200 years.
- `lava_extent`: true when fissure length is at least 5 km and lava-covered area is at least 30 sq km.
- `effusion`: true when the minimum stated high lava-effusion rate is at least 100 m3/s.
- `quake`: true when the largest earthquake is at least Mw 6.5.
- `collapse_energy`: true when the summit-collapse energy-equivalent range has minimum at least Mw 4.5 and maximum at least Mw 5.0.
- `summit_sequence`: true when both minor explosions and near-daily collapses are described.
- `integrated_score`: `2*orange_alert + 2*scale_200yr + 2*lava_extent + 1*effusion + 1*quake + 1*collapse_energy + 1*summit_sequence`.
- `rainfall_context_score`: 2 if maximum accumulated precipitation is at least 150 mm, otherwise 0.
- `ash_only_score`: 1 if the volcano alert is Green or Orange and lava-covered area is not documented, otherwise 0.
- `earthquake_only_score`: 2 if the largest earthquake is at least Mw 6.5 and eruptive fissure opening is not documented, otherwise 0.
- `answer`: use `integrated_lerz_lava_collapse_chain` only when `integrated_score >= 8` and `integrated_score` is greater than every counter-score; otherwise use `not_integrated_lerz_lava_collapse_chain`.

Return compact JSON:

```json
{
  "answer": {
    "target_family": "candidate_explanation_score_ledger",
    "metrics": {
      "fissure_km": 0.0,
      "lava_km2": 0.0,
      "rate_m3s": 0.0,
      "eq_mw": 0.0,
      "collapse_mw": [0.0, 0.0],
      "precip_mm": 0.0
    },
    "flags": {
      "orange_alert": false,
      "scale_200yr": false,
      "lava_extent": false,
      "effusion": false,
      "quake": false,
      "collapse_energy": false,
      "summit_sequence": false
    },
    "scores": {
      "integrated": 0,
      "rainfall_context": 0,
      "ash_only": 0,
      "earthquake_only": 0
    },
    "final_label": ""
  },
  "computed_consequence": "<one sentence tied to the ledger>"
}
```
