# Early Wet-Season Event-Consistency Score

During the September-October 2019 rainfall-data window for an East Africa wet-season flood context, a technical team wants a calculation-first audit of whether the quantitative record forms a coherent high wet-season signal rather than a single-measure artifact. The climate gate uses only the ONI and SOI files specified by the package formula; do not infer an Indian Ocean Dipole term unless an IOD value is explicitly provided.

Compute the Event Consistency Score (ECS) from the event records:

- Let `R` be the three regional accumulated-rainfall means in millimeters. Compute `R_bar = mean(R)`, `R_range = max(R) - min(R)`, and rainfall agreement `C = 1 - R_range / R_bar`.
- Let `O` be the September-December mean ONI and `S` be the September-December mean SOI. Set the climate gate `G = 1` if `O < 0.5` and `S < 0`; otherwise set `G = 0`.
- Let `P` be the local population sum and `B` be the bounded-map building count. Compute receptor concentration `X = 0.5 * min(P / 50000, 1) + 0.5 * min(B / 600, 1)`.
- Let `A` be the annual embedding-change mean. Compute image-stability score `Y = max(0, 1 - A / 0.02)`.
- Compute `ECS = 100 * (0.30 * min(R_bar / 300, 1) + 0.25 * C + 0.15 * G + 0.20 * X + 0.10 * Y)`.

Use class `high` for `ECS >= 80`, `mixed` for `60 <= ECS < 80`, and `low` for `ECS < 60`.

Return strict JSON with this shape:

```json
{
  "rainfall": {"mean_mm": 0, "range_mm": 0, "agreement": 0},
  "climate_gate": {"oni_mean": 0, "soi_mean": 0, "gate": 0},
  "receptor_score": 0,
  "image_score": 0,
  "event_consistency_score": 0,
  "class": "",
  "window_scope": {
    "rainfall_products": "<date range and role>",
    "climate_gate": "<date range and role>"
  },
  "consistency_proof": ""
}
```
