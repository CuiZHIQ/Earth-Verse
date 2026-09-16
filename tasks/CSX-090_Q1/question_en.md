# Derna Rainfall-Routing Exposure Score Ledger

A hydrology review team is checking a proposed deterministic chain score for the September 2023 Storm Daniel flood in Derna, Libya. The score is meant to test whether the technical record supports a rainfall load, routed wadi/dam failure pathway, exposed urban assets, access disruption, and mapped surface-change signal as one linked event pattern.

Compute the score ledger using the fixed formulas below.

Metrics:

- `gpm_max_to_mean = high_resolution_event_precip_max_mm / high_resolution_event_precip_mean_mm`
- `grid_mean_spread_fraction = (max(gridded_event_precip_means_mm) - min(gridded_event_precip_means_mm)) / mean(gridded_event_precip_means_mm)`
- `power_total_mm = sum(two daily point precipitation values)`
- `route_dam_markers = count of these five report markers present: Wadi Derna, two upstream dams, long narrow valley, near-city dam, flood-wave height`
- `exposed_population_k = exposed_population / 1000`
- `building_features = count(local map elements with a building tag)`
- `bridge_features = count(local map elements with bridge=yes)`
- `destroyed_highway_per_1000_roads = 1000 * destroyed_highway_features / highway_features`
- `surface_contrast_index = (radar_vv_change_max_db - radar_vv_change_min_db) * annual_embedding_change_mean`

Gates:

- `rain_load_gate`: `high_resolution_event_precip_mean_mm >= 100`, `power_total_mm >= 100`, and `gpm_max_to_mean >= 1.20`
- `rain_variability_gate`: `grid_mean_spread_fraction >= 1.0`
- `route_dam_gate`: `route_dam_markers >= 4`
- `exposure_gate`: `exposed_population_k >= 50` and `building_features >= 20`
- `access_gate`: `bridge_features >= 5` and `destroyed_highway_per_1000_roads >= 3.0`
- `surface_contrast_gate`: `surface_contrast_index >= 0.25` and `radar_vv_change_mean_db < 0`

Set `chain_score` to the number of passed gates. Set `final_label` to `rainfall_wadi_dam_exposure_chain` when `chain_score >= 5` and `route_dam_gate` is true; otherwise use `insufficient_chain_score`.

Return compact JSON:

```json
{
  "target_family": "derna_rainfall_routing_exposure_score_ledger",
  "metrics": {
    "gpm_max_to_mean": 0.0,
    "grid_mean_spread_fraction": 0.0,
    "power_total_mm": 0.0,
    "route_dam_markers": 0,
    "exposed_population_k": 0.0,
    "building_features": 0,
    "bridge_features": 0,
    "destroyed_highway_per_1000_roads": 0.0,
    "surface_contrast_index": 0.0
  },
  "gates": {
    "rain_load_gate": false,
    "rain_variability_gate": false,
    "route_dam_gate": false,
    "exposure_gate": false,
    "access_gate": false,
    "surface_contrast_gate": false
  },
  "chain_score": 0,
  "final_label": "<label>",
  "computed_consequence": "<short consequence derived from the score>"
}
```
