# Correct Answer

```json
{
  "wind_ratio": 1.41,
  "precip_mean_mm": 11.3,
  "precip_max_mm": 60.9,
  "precip_concentration": 5.38,
  "scene_l1_delta": 0.112,
  "population_m": 3.85,
  "control_counts": {
    "road_facility_elements": 0,
    "dnbr_scene_count": 0
  },
  "coastal_consistency_score": 5,
  "final_label": "coastal_flood_power_signal_consistent"
}
```

# Computation

The Sandy catalog wind speed is `167.371776 km/h`. Dividing by the hurricane threshold gives `167.371776 / 119 = 1.41`, so the storm-wind gate passes.

The GPM and CHIRPS accumulated precipitation means are `6.616719 mm` and `15.995677 mm`. Their average is `11.3 mm`. The larger precipitation maximum is the CHIRPS value, `60.9 mm`. The concentration ratio is `60.862160 / ((6.616719 + 15.995677) / 2) = 5.38`. This gives a concentrated rain signal, while the mean remains below the `25 mm` rainfall-only gate threshold.

The image calculation uses the resized `256 x 192` RGB scenes. Rounded pre-event fractions are dark `0.158`, bright `0.214`, water-blue `0.077`; rounded event fractions are dark `0.221`, bright `0.183`, water-blue `0.095`. The deltas are `+0.063`, `-0.031`, and `+0.018`, so `scene_l1_delta = 0.063 + 0.031 + 0.018 = 0.112`.

The exposed population is `3,848,078`, or `3.85` million. The OSM road/facility slice has `0` elements because the local OSM control file reports a query failure, and the dNBR pre/post scene count is `0 + 0 = 0` because the dNBR control reports no sufficient scenes. These counts are reported as unavailable control context, not scored as proof of true absence.

All five substantive gates pass: wind ratio, mean precipitation below `25 mm`, precipitation concentration, image change, and dense exposure. The final score is `5/5`, producing the label `coastal_flood_power_signal_consistent`.

# Scoring Rubric

Total: 20 points.

- 3 points: JSON shape. Full credit for the requested fields and compact numeric values; partial credit for a readable object with one or two missing fields.
- 4 points: Storm wind test. Full credit for `167.371776 km/h`, threshold `119 km/h`, ratio `1.41`, and a passing wind gate; partial credit for only part of this calculation.
- 4 points: Precipitation ledger. Full credit for `11.3 mm`, `60.9 mm`, `5.38`, and the two precipitation gates; partial credit for arithmetic or rounding errors that preserve the main sign tests.
- 4 points: Image change metric. Full credit for the three rounded pixel-fraction deltas and `scene_l1_delta = 0.112`; partial credit for correct pixel classes with incomplete delta arithmetic.
- 3 points: Exposure and control counts. Full credit for `3.85` million people, `0` OSM road/facility elements, `0` dNBR scenes, and treating unavailable OSM/dNBR controls as reported context rather than scored evidence of absence; partial credit for only one or two correct anchors.
- 2 points: Final label. Full credit for score `5/5` and `coastal_flood_power_signal_consistent`; partial credit for the right label with a minor score or naming error.
