# Correct Answer

```json
{
  "max_wind_ms": 11.64,
  "point_precip_total_mm": 0.0,
  "regional_precip_mm": {"mean": 0.0152, "max": 2.165},
  "receptors": {"major_roads": 170, "critical_amenities": 53, "local_population": 6086.444},
  "component_scores": {"wind": 0.91, "dryness": 0.848, "transport": 1.0, "facility": 1.0, "population": 0.609},
  "dust_wind_index": 90.32,
  "threshold_result": "dust_transport_consistent"
}
```

# Key Computations

The maximum available wind is the larger of 9.06 m/s and 41.9 km/h converted to 11.6389 m/s, so `max_wind_ms = 11.64`. Point precipitation totals are zero in both point series, so `point_precip_total_mm = 0.0`.

The gridded event-window mean precipitation values are 0.0025303 mm, 0.0431500 mm, and 0.0 mm. Their mean is 0.0152268 mm, rounded to `0.0152`. The largest gridded maximum is `2.165` mm.

Receptor-context metrics are `major_roads = 170`, `critical_amenities = 53`, and `local_population = 6086.444`. They enter only the receptor components of the index; the point-weather wind and precipitation gates are separate evidence roles. The component scores are:

- `wind_score = clip((11.6389 - 8.0) / 4.0) = 0.910`
- `dryness_score = clip(1.0 - 0.0152268 / 0.1) = 0.848`
- `transport_score = clip(170 / 150.0) = 1.000`
- `facility_score = clip(53 / 50.0) = 1.000`
- `population_score = clip(6086.444 / 10000.0) = 0.609`

`dust_wind_index = 100 * (0.35 * 0.9097 + 0.30 * 0.8477 + 0.20 * 1.0 + 0.10 * 1.0 + 0.05 * 0.6086) = 90.32`.

# Reasoning Path

All numeric gates pass: wind is at least 8.0 m/s, point precipitation is exactly 0.0 mm, regional mean precipitation is below 0.1 mm, regional maximum precipitation is below 3.0 mm, and the index exceeds 70.0. The compact computed consequence is therefore `dust_transport_consistent`; a wetness-led reading fails the precipitation gates.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "counterfactual_rejection": "A wetness-led interpretation fails because point precipitation is zero and regional mean precipitation is far below the dryness gate.",
    "evidence_weighting": "Wind and regional dryness provide the physical dust-transport evidence; road, amenity, and population values are receptor context rather than dust-generation evidence.",
    "uncertainty_or_scale_caveat": "Receptor counts help prioritize disruption context but do not prove observed dust concentration or health impacts."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

- 3 points: Returns the requested compact JSON fields with numeric values and the final threshold string.
- 5 points: Extracts and converts the core event-window values correctly: 11.64 m/s maximum wind, 0.0 mm point precipitation, 0.0152 mm regional mean precipitation, 2.165 mm regional maximum precipitation, 170 major roads, 53 critical amenities, and 6086.444 people, while keeping point-weather and receptor-context roles separate.
- 4 points: Applies the five component formulas with clipping and reports scores within tolerance: wind 0.91, dryness 0.848, transport 1.0, facility 1.0, and population 0.609.
- 3 points: Computes `dust_wind_index = 90.32` within 0.05 and keeps the stated weighting.
- 3 points: Tests all five gates and gives `dust_transport_consistent` only because every gate passes.
- 1 point: Keeps the mechanism label to the short computed consequence of the threshold test.
- 1 point: Does not add measured road closures, health thresholds, direct losses, or wet-event dominance beyond the computed gates.
