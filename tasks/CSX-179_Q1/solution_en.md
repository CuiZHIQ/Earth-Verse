# Final Answer

```json
{
  "classification": "transboundary_fire_smoke_air_quality",
  "severity_ledger": {
    "hotspots_min": 120000,
    "psi_ratio_min": 5.71,
    "aerosol_multiplier": 6,
    "co_ratio_nearly": 13.0
  },
  "transport_check": "Smoke was usually below 3 km, a central Kalimantan plume reached 2 km, and upper-level northwesterly transport could carry smoke toward Malaysia, Singapore, southern Thailand, southern Cambodia, and Vietnam.",
  "rationale": "The more-than-120000 Indonesian hot spots, PSI ratio of at least 5.71, 6-fold aerosol increase, and near-13.0 CO ratio support a cross-border fire-smoke air-quality classification. Ordinary weather haze, local burn-area mapping, and population counting are weaker because they do not jointly explain the fire, chemical, air-quality, and transport anchors."
}
```

# Key Computations

The event metadata identifies the 2015 Southeast Asia haze from Indonesian fires, with the incident window 2015-08-01 to 2015-11-30 and hazard family `wildfire_burn_smoke`.

Report extractions and derived checks:

- MODIS detected more than 120000 hot spots in Indonesia during 2015.
- PSI in parts of southern Sumatra and Borneo rose above 2000, while any score above 350 is hazardous. The minimum ratio is `2000 / 350 = 5.71`.
- The Palangkaraya AERONET station detected a 6-fold particle increase compared with usual September-October levels.
- Typical Indonesian smoke remained between the surface and 3 km, and a central Kalimantan plume on 2015-10-04 reached 2 km.
- Upper-level winds could move some smoke northwest toward Malaysia, Singapore, southern Thailand, southern Cambodia, and Vietnam.
- Surface carbon monoxide was usually about 100 ppb, while Borneo values reached nearly 1300 ppb. The near-peak ratio is `1300 / 100 = 13.0`.

# Reasoning Path

The classification follows from the alignment of fire, air-quality, and transport indicators. The hot-spot count anchors a large Indonesian fire season rather than ordinary background haze. The PSI ratio, aerosol multiplier, and carbon-monoxide ratio independently show extreme air-pollution intensity.

The vertical and wind checks explain why the episode should not be reduced to a local burn-area mapping task. Most smoke stayed low, but enough smoke reached faster winds aloft to affect downwind countries. That combination supports a cross-border fire-smoke air-quality classification.

Broad scene imagery can support the haze setting, but the numeric classification should come from the reported fire, air-quality, chemical, and plume-height anchors.

# Computed Interpretation

The computed ledger points to a regional air-quality episode driven by Indonesian fire smoke: high fire activity, PSI at least 5.71 times the hazardous threshold, 6-fold aerosol loading, near-13.0 surface CO enrichment, and plausible northwest smoke transport all agree on the same classification.

# Scoring Rubric

Total: 20 points.

- Final classification, 4 points: gives `transboundary_fire_smoke_air_quality` or an equivalent cross-border Indonesian fire-smoke air-quality label. Partial credit for a generic wildfire-smoke label that omits the cross-border or air-quality emphasis.
- Fire and event anchors, 3 points: identifies the Indonesian 2015 haze window and uses the more-than-120000 hot-spot anchor with Sumatra and Kalimantan as key burning regions. Partial credit for only the event window or only the hot-spot count.
- Severity ledger arithmetic, 5 points: reports PSI above 2000, hazardous threshold above 350, `2000 / 350 = 5.71`, 6-fold aerosol increase, and near-13.0 CO ratio. Partial credit for correct raw values without ratios or for one missing severity metric.
- Smoke-layer and transport check, 4 points: connects mostly low smoke below 3 km, the 2 km central Kalimantan plume, and northwest movement toward Malaysia, Singapore, southern Thailand, southern Cambodia, and Vietnam. Partial credit for mentioning downwind movement without height or direction.
- Rejection of weaker readings, 2 points: explains why ordinary weather haze, local burn-area mapping, and population-counting interpretations are weaker than the combined numeric record. Partial credit for rejecting only one alternative.
- Output control, 2 points: returns compact JSON with the requested fields and avoids extra-data independent loss, dose-response, or complete burn-map claims. Partial credit for minor formatting issues or one mild overstatement.
