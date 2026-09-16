# Final Answer

```json
{
  "answer": "basin_river_flood_dominant",
  "score": 4,
  "three_day_rain_mm": 442,
  "oder_rp_years_min": 20,
  "river_length_gt2x_aam_km": 8500,
  "romania_fatality_share": 0.259,
  "flash_only_test": "rejected"
}
```

# Key Computations

- Maximum three-day rainfall: 442 mm. This passes the 300 mm multiday rainfall threshold.
- Oder River basin severity: at least a 20-year return-period signal. This passes the 20-year threshold.
- River amplification extent: 8,500 km of rivers beyond twice the average annual maximum flow. This passes the 5,000 km threshold.
- Romania short-duration flood fatality share: `7 / 27 = 0.259259...`, rounded to `0.259`. Because this is below one third, the flash-flood-only classification is rejected.
- Ledger score: all four tests support `basin_river_flood_dominant`, so the score is `4`.

# Reasoning Path

1. The rainfall threshold is satisfied because the 442 mm three-day maximum is well above 300 mm, so the event has a strong multiday storm-forcing anchor.
2. The Oder threshold is satisfied because the report gives an at-least-20-year signal, meeting the severe river-basin criterion.
3. The river-amplification threshold is satisfied because 8,500 km is above the 5,000 km extent cutoff and reflects widespread routed high flow.
4. The short-duration Romania component is important but not sufficient to classify the whole event as flash-flood-only: `7 / 27 = 0.259`, which is below the one-third rejection threshold.
5. With all four tests passing, the deterministic ledger result is `basin_river_flood_dominant`.

# Computed Interpretation

The numbers show a multiday rainfall event that propagated into widespread river-basin flooding, while the Romania short-duration component remains a smaller embedded part of the reported fatality record.

# Scoring Rubric

Total: 20 points.

- Final ledger result, 4 points: returns `basin_river_flood_dominant` with a score of 4 out of 4. Partial credit: 2 points for the right label with no score or a score off by one; 1 point for a vague river-flood conclusion.
- Rainfall threshold test, 3 points: uses the 442 mm three-day rainfall value and correctly marks the 300 mm threshold test as passed. Partial credit: 1-2 points for a correct extreme-rain claim with a missing threshold, wrong unit, or minor value error.
- Oder severity test, 3 points: uses the at-least-20-year Oder River basin signal and correctly marks the return-period threshold test as passed. Partial credit: 1-2 points for recognizing severe Oder flooding but omitting the at-least qualifier or threshold comparison.
- River amplification test, 3 points: uses 8,500 km of rivers beyond twice average annual maximum flow and correctly marks the 5,000 km extent test as passed. Partial credit: 1-2 points for mentioning widespread high flows with an incomplete value or comparison.
- Flash-only rejection, 3 points: computes 7 divided by 27 as about 0.259 and rejects a flash-flood-only explanation because it is below one third. Partial credit: 1-2 points for using the 7 and 27 counts but missing the ratio or the one-third comparison.
- Formula and threshold clarity, 2 points: states or clearly applies the four pass/fail tests and the all-four-pass decision rule. Partial credit: 1 point if the tests are implicit but the arithmetic mostly supports the final label.
- Concise constrained output, 2 points: returns a compact JSON-style answer with the requested fields and no action advice or broad event essay. Partial credit: 1 point for a readable answer that has minor formatting problems or extra prose but remains scoreable.
