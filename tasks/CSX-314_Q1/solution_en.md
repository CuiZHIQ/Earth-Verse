# Correct Answer

```json
{
  "answer": {
    "process_hits": 9,
    "object_hits": 7,
    "mechanism_coverage": 1.0,
    "impact_coverage": 1.0,
    "cascade_score": 100.0,
    "classification": "rock_ice_debris_flow_cascade_report_consistent"
  },
  "interpretation": "The report text supports a rock-ice-sediment-water cascade that connects source mechanics to hydropower, settlement, tunnel, bridge, and road impacts."
}
```

# Calculation Path

The reference calculation uses the local event metadata, the locked event anchor, and the NASA/event report HTML. It strips HTML, case-folds the narrative, and compresses whitespace before counting phrase hits.

All 9 process phrases occur at least once:

`rock`, `ice`, `sediment`, `water`, `hanging glacier`, `freefalling`, `landslide`, `slurry`, `rishiganga river valley`.

All 7 object phrases occur at least once:

`hydropower stations`, `villages`, `workers`, `tunnels`, `homes`, `bridges`, `roads`.

`mechanism_coverage = 9 / 9 = 1.000`.

`impact_coverage = 7 / 7 = 1.000`.

`cascade_score = 100 * (0.65 * 1.000 + 0.35 * 1.000) = 100.00`.

Because `process_hits >= 8` and `object_hits >= 6`, the classification is `rock_ice_debris_flow_cascade_report_consistent`.

# Scoring Rubric

- 3 points: Returns the requested compact JSON shape with all six fields under `answer` plus a one-sentence interpretation.
- 3 points: Uses the local event report text, strips HTML, case-folds, and normalizes whitespace before phrase counting.
- 4 points: Counts `process_hits = 9` from the stripped event narrative text.
- 4 points: Counts `object_hits = 7` from the stripped event narrative text.
- 3 points: Computes `mechanism_coverage = 1.000`, `impact_coverage = 1.000`, and `cascade_score = 100.00`.
- 2 points: Returns `rock_ice_debris_flow_cascade_report_consistent` and ties it to the source-to-impact chain.
- 1 point: Avoids unsupported rainfall-trigger, lake-breach, precise-casualty, or auxiliary-product claims.
