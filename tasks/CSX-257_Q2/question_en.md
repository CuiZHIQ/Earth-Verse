# Hurricane Sandy Coastal Corridor Consistency Ledger

Compute a compact numeric ledger for Hurricane Sandy in the New York City and New Jersey coastal corridor during October 29-30, 2012. The ledger should test whether the event data are more consistent with a coastal flood plus power-disruption signal than with a rainfall-only or land-surface-change-only reading.

Return JSON only in this form:

```json
{
  "wind_ratio": 0.0,
  "precip_mean_mm": 0.0,
  "precip_max_mm": 0.0,
  "precip_concentration": 0.0,
  "scene_l1_delta": 0.0,
  "population_m": 0.0,
  "control_counts": {
    "road_facility_elements": 0,
    "dnbr_scene_count": 0
  },
  "coastal_consistency_score": 0,
  "final_label": ""
}
```

Use these definitions:

- `wind_ratio` = Sandy catalog maximum wind speed divided by `119 km/h`.
- `precip_mean_mm` = the average of the event-window GPM and CHIRPS accumulated precipitation means.
- `precip_max_mm` = the larger of the event-window GPM and CHIRPS accumulated precipitation maxima.
- `precip_concentration` = `precip_max_mm / precip_mean_mm`, using the unrounded source values.
- `scene_l1_delta` = `abs(delta_dark) + abs(delta_bright) + abs(delta_water_blue)` from the pre-event and event RGB scenes after resizing each to `256 x 192`. Dark pixels have `r < 70`, `g < 70`, and `b < 70`; bright pixels have `r > 180`, `g > 180`, and `b > 180`; water-blue pixels have `b > r + 10`, `b > g + 5`, and `b > 60`.
- `population_m` = exposed population divided by `1,000,000`.
- `control_counts` reports the OSM road/facility element count and the sum of dNBR pre/post scene counts. If the OSM file reports a query failure or the dNBR file reports no sufficient scenes, treat those counts as unavailable control context, not as evidence of true absence.

Give one point for each satisfied substantive gate: `wind_ratio >= 1`, `precip_mean_mm < 25`, `precip_concentration >= 4`, `scene_l1_delta >= 0.05`, and `population_m >= 1`. Report `control_counts`, but do not add or subtract points for unavailable OSM or dNBR controls. Use `coastal_flood_power_signal_consistent` when the score is at least `4` and the wind gate is satisfied; otherwise use `mixed_hydro_signal`.
