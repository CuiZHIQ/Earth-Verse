# Final Answer

```json
{
  "event_window": "2013-06-15 to 2013-06-18",
  "point_total_mm": 300.4,
  "peak_2day_share": 0.869,
  "grid_max_mm": 569.32,
  "grid_pair_ratio": 0.992,
  "bridge_per_100_highway": 20.4,
  "service_node_count": 44,
  "final_state": "passes_concentrated_mountain_exposure_test"
}
```

# Key Computations

- Event window: 2013-06-15 to 2013-06-18.
- Point rainfall by day: 37.8 mm, 132.7 mm, 128.4 mm, and 1.5 mm, giving a four-day total of 300.4 mm.
- Peak two-day share: `(132.7 + 128.4) / 300.4 = 0.869`.
- Gridded accumulated-rainfall maxima: 564.49 mm and 569.32 mm. The maximum is 569.32 mm, and the pair ratio is `564.49 / 569.32 = 0.992`.
- Package mapped-context transport and service counts: 147 highway elements, 30 bridge elements, 13 hospitals, 19 shelters, and 12 tourism hotels.
- Bridge density: `30 / 147 * 100 = 20.4` bridges per 100 highway elements.
- Service-node count: `13 + 19 + 12 = 44`.

# Reasoning Path

1. The point rainfall total clears the 300 mm minimum because 300.4 mm is above the threshold.
2. Rainfall was highly concentrated in the middle of the event: the June 16-17 share is 0.869, above the 0.85 threshold.
3. The two gridded peak rainfall estimates agree closely: 0.992 is above the 0.98 threshold.
4. The transport feature test passes because 20.4 bridges per 100 highway elements is above the threshold of 15.
5. The service-feature test passes because 44 hospitals, shelters, and tourism hotels is above the threshold of 40.
6. All five tests pass, so the final state is `passes_concentrated_mountain_exposure_test`.

# Computed Interpretation

The ledger indicates a short-window rainfall concentration combined with dense mountain transport and service features, which is the computed basis for the concentrated mountain-rainfall exposure diagnosis.

# Scoring Rubric

Total: 20 points.

- 4 points: Final numeric ledger and state. Full credit returns the requested compact JSON with the event window, six computed values, and `final_state` equal to `passes_concentrated_mountain_exposure_test`. Partial credit: 2-3 points if the final state is correct but one or two fields are missing; 1 point for a correct general pass statement without the ledger.
- 4 points: Rainfall totals and peak concentration. Full credit computes `point_total_mm` as 300.4 and `peak_2day_share` as 0.869 using June 16 plus June 17 rainfall divided by the four-day point total. Partial credit: 2-3 points for correct rainfall totals with a rounding or denominator error; 1 point for using only a qualitative heavy-rain statement.
- 3 points: Gridded peak agreement. Full credit uses the 564.49 mm and 569.32 mm gridded maxima to report `grid_max_mm` of 569.32 and `grid_pair_ratio` of 0.992. Partial credit: 1-2 points for citing one gridded maximum or reversing the ratio while keeping the values recognizable.
- 3 points: Exposure density arithmetic. Full credit computes 30 bridges across 147 highway elements as 20.4 bridges per 100 highway elements and counts 44 service nodes from hospitals, shelters, and hotels. Partial credit: 1-2 points for naming the correct component counts but not deriving one of the requested metrics.
- 3 points: Threshold test logic. Full credit applies all five thresholds correctly: point total at least 300 mm, two-day share at least 0.85, grid ratio at least 0.98, bridge density at least 15, and service nodes at least 40. Partial credit: 1-2 points if most thresholds are applied but one threshold or comparison direction is wrong.
- 2 points: Final-state field discipline. Full credit uses `final_state` to express the computed outcome without adding schema-external interpretation fields. Partial credit: 1 point if the final state is correct but the response adds a small amount of extra prose outside the requested JSON.
- 1 point: Avoids non-computed expansion. Full credit does not add uncomputed flood depth, mapped area, debris volume, road-loss length, casualty totals, facility outage, or radar-derived flood extent. Partial credit: 0.5 points for a minor extra inference that does not change the numeric answer.
