# Final Answer

```json
{
  "target_family": "derna_rainfall_routing_exposure_score_ledger",
  "metrics": {
    "gpm_max_to_mean": 1.385,
    "grid_mean_spread_fraction": 1.7196,
    "power_total_mm": 120.33,
    "route_dam_markers": 5,
    "exposed_population_k": 56.113,
    "building_features": 25,
    "bridge_features": 6,
    "destroyed_highway_per_1000_roads": 3.099,
    "surface_contrast_index": 0.329
  },
  "gates": {
    "rain_load_gate": true,
    "rain_variability_gate": true,
    "route_dam_gate": true,
    "exposure_gate": true,
    "access_gate": true,
    "surface_contrast_gate": true
  },
  "chain_score": 6,
  "final_label": "rainfall_wadi_dam_exposure_chain",
  "computed_consequence": "score_requires_routing_exposure_and_surface_contrast"
}
```

# Key Computations

The high-resolution event precipitation summary gives 150.445 mm maximum and 108.628 mm mean, so `gpm_max_to_mean = 150.445 / 108.628 = 1.385`. The three gridded event means are 108.628, 77.286, and 1.309 mm, so their spread fraction is `(108.628 - 1.309) / 62.408 = 1.7196`. The two daily point precipitation values sum to `89.81 + 30.52 = 120.33 mm`.

The report text contains all five route/dam markers used by the scoring rule. The local exposure slice gives 56,113.05 people, 25 building-tagged elements, 968 highway-tagged elements, 6 bridge elements, and 3 damaged-road indicators. That yields `exposed_population_k = 56.113` and `destroyed_highway_per_1000_roads = 1000 * 3 / 968 = 3.099`.

For the surface term, the radar VV change range is `8.505 - (-10.254) = 18.759 dB` before rounding; multiplying by the annual embedding change mean `0.017515` gives `surface_contrast_index = 0.329`.

# Reasoning Path

The rainfall load gate passes because the high-resolution mean exceeds 100 mm, the daily point total exceeds 100 mm, and the max-to-mean ratio exceeds 1.20. The grid spread fraction is greater than 1.0, so the variability gate also passes. All five route/dam markers are present, exceeding the four-marker threshold required for the routed wadi/dam gate.

The exposure and access gates pass because the exposed population is above 50 thousand, building features exceed 20, bridge features exceed 5, and the damaged-road indicator rate is above 3.0 per 1000 highway features. The surface contrast gate passes because the contrast index is above 0.25 and the radar mean change is negative.

All six gates pass. Because `chain_score = 6` and `route_dam_gate = true`, the deterministic final label is `rainfall_wadi_dam_exposure_chain`.

# Computed Interpretation

The score is not just a heavy-rainfall flag: the final label requires the routed wadi/dam marker set, exposed urban assets, access-disruption indicators, and a surface-change term to pass together.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns compact JSON with `target_family`, `metrics`, `gates`, `chain_score`, `final_label`, and `computed_consequence`. Partial credit: 1-2 points when the response includes the core fields but omits one nested group or uses minor naming differences that do not obscure the score.
- 4 points: Computes the precipitation ledger correctly: `gpm_max_to_mean = 1.385`, `grid_mean_spread_fraction = 1.7196`, and `power_total_mm = 120.33`. Partial credit: about 1 point for each correct precipitation value; lose credit for wrong aggregation windows, missing units, or ratios outside tolerance.
- 3 points: Counts `route_dam_markers = 5` using the five specified report markers. Partial credit: 1-2 points for finding at least three route/dam markers; lose credit if the count is based on unrelated narrative details.
- 4 points: Computes the exposure/access ledger correctly: `exposed_population_k = 56.113`, `building_features = 25`, `bridge_features = 6`, and `destroyed_highway_per_1000_roads = 3.099`. Partial credit: about 1 point for each correct exposure or access metric; lose credit for confusing damaged highways with all highways or reporting raw population in thousands incorrectly.
- 3 points: Computes the surface term as `(8.505 - -10.254) * 0.017515 = 0.329` and applies the negative radar-mean condition. Partial credit: 1-2 points for the correct radar range or multiplication but not both; lose credit if the negative mean condition is ignored.
- 2 points: Applies all six gates correctly, returns `chain_score = 6`, and sets `final_label` to `rainfall_wadi_dam_exposure_chain`. Partial credit: 1 point if the gate count or final label is correct but the other is missing or inconsistent.
- 1 point: Keeps the consequence tied to the score and does not convert exposure counts into casualty counts or exact block-level damage. Partial credit: 0.5 points for a mostly bounded consequence with a small overstatement; award 0 for casualty, loss, or impact statements not derived from the ledger.
