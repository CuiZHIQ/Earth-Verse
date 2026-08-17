# India-Pakistan Heat Severity Anchor Hierarchy

A regional heat-risk group is reconstructing the physical evidence hierarchy for the 2015 India-Pakistan heat wave. The key problem is not to count isolated hot observations, but to decide which package-local signal should carry the severity diagnosis when regional heat fields, a much cooler point record, weak precipitation relief, missing surface-change pairing, and population exposure all appear in the same event package.

Use only the local CSX-016 event package. Select package-relative evidence for every value you use.

Build a five-part anchor hierarchy with these fixed test ids:

- `regional_heat_field_anchor`: compute the inclusive event-window length, the regional gridded Tmax mean margin above 40 C, the regional gridded Tmax absolute margin above 40 C, and the regional Tmax spatial range. This anchor is the primary heat-severity signal only when the window is 46 days, the mean margin is at least 4.5 C, and the absolute margin is at least 6.0 C.
- `cool_point_scale_anchor`: test whether the available point record is physically representative of the regional heat field. Compute whether the point lies inside the regional study box, its nearest-edge distance, its Tmax maximum, the two gaps from the regional Tmax maximum and regional Tmax mean maximum, its heat load above 25 C, and its longest Tmax >=25 C run. This anchor can represent regional heat only when the point lies inside the box and both temperature gaps are no more than 5 C.
- `precipitation_relief_anchor`: compute the three event precipitation totals as daily means over the 46-day window. Treat precipitation as heat-relief evidence only when at least two daily means reach 5.0 mm/day.
- `image_surface_anchor`: compute the pre/post surface-change scene counts and the matching event-catalog count. Treat imagery as a heat-surface anchor only when at least one pre scene, one post scene, and one matching catalog record exist.
- `exposure_denominator_anchor`: compute population in millions and `exposure_weighted_mean_margin = population_millions * mean_Tmax_margin_above_40C`. This is supporting context when the regional heat-field anchor is primary and the population denominator is positive; it is not a physical heat-intensity anchor by itself.

Return compact JSON only:

```json
{
  "event_window_days": 0,
  "candidate_tests": [
    {
      "test_id": "regional_heat_field_anchor",
      "computed_value": {},
      "evidence_result": "pass|fail",
      "role": "primary_heat_anchor|supporting_context|not_primary_heat_anchor"
    }
  ],
  "primary_heat_calibration": {
    "label": "",
    "primary_anchor": "",
    "supporting_context": [],
    "not_primary_heat_anchors": []
  },
  "one_sentence_interpretation": ""
}
```

The interpretation should explain the evidence hierarchy: which signal carries heat severity, which signals are scale-mismatched or under-supported, and why exposure scales the consequence context rather than replacing the physical heat field.
