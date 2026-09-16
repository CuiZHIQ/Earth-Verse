# Solution

## Final Answer

```json
{
  "answer": "post_fire_rainfall_debris_flow_cascade",
  "priority": "highest_life_safety_and_asset_damage_priority",
  "cascade_priority_index": 100.0,
  "impact_chain": [
    "recent_burned_steep_catchments",
    "intense_rainfall",
    "debris_flows_on_alluvial_fans"
  ],
  "key_metrics": {
    "open_meteo_precip_mm": 62.4,
    "max_precip_support_mm": 68.2,
    "dnbr_mean": 0.26,
    "exposed_population": 120050,
    "critical_facilities": 52
  }
}
```

The correct answer is `post_fire_rainfall_debris_flow_cascade`. The priority label is `highest_life_safety_and_asset_damage_priority`, with a cascade priority index of `100.0`.

## Key Computations

- The anchor report states that intense rain above Montecito triggered debris flows from steep Santa Ynez Mountain catchments.
- The same report states those catchments had burned three weeks earlier in the Thomas Fire.
- It states that the debris flows traveled over 3 km down alluvial fans.
- It reports 23 deaths and damage to over 400 homes.
- The locked event metadata identifies the case as the 2018 Montecito post-fire debris flows on 2018-01-09 in Montecito and Carpinteria, California.

`compute_gt.py` extracts the report text flags, daily and gridded rainfall statistics, image-derived burn and surface-change values, population exposure, and OpenStreetMap service assets.

It computes:

- Rainfall support from Open-Meteo, ERA5-Land, GPM IMERG, and CHIRPS.
- A count of precipitation products or product statistics at or above 50 mm.
- Burn or surface-condition support from Sentinel-2 dNBR mean and maximum.
- Exposed population from WorldPop.
- Roads and critical facilities from the bounded OSM AOI slice.
- Text flags for intense rain, post-fire conditioning, steep catchments, alluvial fans, fatalities, and home damage.

The cascade priority index is a weighted score:

```text
100 * (0.35 * rainfall_score
     + 0.25 * burn_proxy_score
     + 0.20 * exposure_score
     + 0.20 * facility_score)
```

with each component capped at 1.0. For this package, all four components reach 1.0, so the index is `100.0`.

## Key Rainfall, Burn-Scar, Debris, Exposure, and Image Metrics

```json
{
  "event_date": "2018-01-09",
  "open_meteo_precip_mm": 62.4,
  "gpm_mean_mm": 52.1,
  "gpm_max_mm": 68.2,
  "chirps_max_mm": 62.8,
  "era5_mean_mm": 51.4,
  "era5_max_mm": 53.3,
  "rain_products_ge_50mm": 6,
  "mean_precip_support_mm": 55.3,
  "dnbr_mean": 0.26,
  "dnbr_max": 1.578,
  "alphaearth_change_mean": 0.088,
  "exposed_population": 120050,
  "roads": 947,
  "critical_facilities": 52
}
```

## Reasoning Path

1. The reported mechanism is not ordinary rainfall flooding alone: intense rain is tied to debris flows from steep catchments.
2. It is not an active-fire-only or burn-severity-only interpretation: the damaging event occurred when rainfall acted on catchments burned three weeks earlier.
3. It is not merely a generic exposed-assets case: exposure matters for priority, but exposure alone does not explain the disaster mechanism.
4. Independent precipitation products show substantial event rainfall, with Open-Meteo at 62.4 mm and several gridded metrics at or above 50 mm.
5. The dNBR mean of 0.26 supports a meaningful burn or surface-change condition, consistent with post-fire susceptibility.
6. The impact pathway runs from burned steep catchments to intense rainfall to debris flows on alluvial fans, with reported deaths and home damage.
7. The population and OSM facility counts make the response priority highest, but the priority is justified only when combined with the physical cascade.

## Final GT

```json
{
  "answer": "post_fire_rainfall_debris_flow_cascade",
  "priority": "highest_life_safety_and_asset_damage_priority",
  "cascade_priority_index": 100.0,
  "impact_chain": [
    "recent_burned_steep_catchments",
    "intense_rainfall",
    "debris_flows_on_alluvial_fans"
  ],
  "key_metrics": {
    "open_meteo_precip_mm": 62.4,
    "max_precip_support_mm": 68.2,
    "dnbr_mean": 0.26,
    "exposed_population": 120050,
    "critical_facilities": 52
  }
}
```

## Unsupported Overclaims

- Do not claim the local package proves the complete rainfall intensity-duration threshold for debris-flow initiation.
- Do not claim that the dNBR file alone maps the exact Thomas Fire perimeter or all burn severity classes.
- Do not infer building-by-building damage from the OSM exposure layer.
- Do not treat the WorldPop count as the number of people directly injured, evacuated, or killed.
- Do not use outside mortality, rainfall, or fire-perimeter sources.

## Disaster Interpretation

This is a process-chain diagnosis rather than a single hazard label. The disaster is best understood as a fire-conditioned, rainfall-triggered debris-flow cascade: recent burn altered hillslope runoff and sediment availability; intense rainfall crossed a practical support threshold in several precipitation products; steep catchments routed debris through channels and onto alluvial fans; and downstream exposure, roads, and critical facilities raised the emergency priority. Exposure amplifies consequences but does not define the mechanism, and dNBR/AlphaEarth metrics support susceptibility context rather than exact building-level damage.

## Scoring Rubric

Total: 20 points.

- 3 points: Correctly selects `post_fire_rainfall_debris_flow_cascade` rather than rainfall-only, fire-only, or exposure-only interpretations.
- 3 points: Explains antecedent wildfire and burn-scar conditioning, including the Thomas Fire timing and the susceptibility of steep catchments.
- 3 points: Uses rainfall intensity or threshold support, including Open-Meteo precipitation near 62.4 mm and multiple precipitation products or statistics at or above 50 mm.
- 2 points: Describes rapid runoff, sediment entrainment, and debris-flow routing through channels and onto alluvial fans.
- 2 points: Connects downstream exposure and service impact to the priority judgment, including reported fatalities, home damage, population exposure near 120050, and 52 critical facilities.
- 2 points: Interprets image-derived or remotely sensed metrics, especially dNBR mean near 0.26, dNBR maximum near 1.578, and annual surface-change support near 0.088.
- 2 points: Reports the compact GT values within tolerance: maximum precipitation support near 68.2 mm, cascade priority index near 100.0, and the expected three-stage impact chain.
- 2 points: Assigns the highest life-safety and asset-damage priority and explains why exposure amplifies priority rather than defining the mechanism.
- 1 point: Avoids unsupported overclaims about exact rainfall thresholds, precise damage attribution, directly affected population, or building-level loss.
