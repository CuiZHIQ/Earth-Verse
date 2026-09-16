# Correct Answer

The ledger total is `20`, with class label `full_threshold_rupture_scale_surface_change`.

```json
{
  "area_km2": 7875.0,
  "length_width_ratio": 3.889,
  "radar_range_db": 43.7037,
  "max_precip_mm": 5.5767,
  "component_scores": {"fault": 10, "shaking": 6, "radar": 3, "context": 1},
  "total_score": 20,
  "class_label": "full_threshold_rupture_scale_surface_change",
  "numeric_anchors": {
    "magnitude_mww": 7.5,
    "maximum_mmi": 8.793,
    "max_pga_g": 1.669,
    "max_pgv_cm_s": 120.336,
    "finite_fault_rake_deg": 120.0,
    "model_top_km": 0.4404,
    "radar_mean_change_db": -2.1567,
    "annual_embedding_mean_change": 0.0116,
    "population_millions": 2.485,
    "tsunami_flag": 1
  }
}
```

The finite-fault ledger gives all 10 fault points: rake 120 deg is in the 45-135 deg band, dip 35 deg is in the 20-50 deg band, model top is 0.4404 km, length is 175 km, area is 175*45 = 7875 km2, and length/width is 3.8889. The shaking ledger gives 6 points from MMI 8.793, PGA 1.669 g, and PGV 120.336 cm/s. The radar ledger gives 3 points from mean VV change -2.1567 dB, range 24.0731 - (-19.6306) = 43.7037 dB, and post count 2. The context point is earned because max precipitation is max(0.0009, 0.37, 5.5767) = 5.5767 mm, annual embedding mean change is 0.0116, and the tsunami flag is 1.

# Scoring Rubric

- 4 points: Extract the finite-fault dimensions, rake, dip, and model-top values from structured package data.
- 4 points: Compute area, length/width ratio, radar range, and max precipitation with correct rounding.
- 4 points: Apply the fault score flags exactly.
- 3 points: Apply the shaking score flags exactly.
- 2 points: Apply the radar score flags exactly.
- 1 point: Apply the context score flag exactly.
- 2 points: Return a compact JSON ledger with total score, class label, and all requested numeric anchors.

Total: 20 points.
