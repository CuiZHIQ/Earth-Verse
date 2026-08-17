# Chamoli Rock-Ice Cascade Consistency Model

For the 7 February 2021 Chamoli event in Uttarakhand, use the local event report evidence to test whether the narrative supports a rock-ice-sediment-water cascade interpretation rather than a generic flood or ordinary weather framing.

Use the one-day event window. Strip HTML from the event narrative, case-fold it, and compress whitespace before counting phrase hits.

Definitions:

- `process_hits`: count how many of these lower-case phrases occur at least once in the stripped event narrative text: `rock`, `ice`, `sediment`, `water`, `hanging glacier`, `freefalling`, `landslide`, `slurry`, `rishiganga river valley`.
- `object_hits`: count how many of these lower-case phrases occur at least once in the stripped event narrative text: `hydropower stations`, `villages`, `workers`, `tunnels`, `homes`, `bridges`, `roads`.
- `mechanism_coverage`: `process_hits / 9`, rounded to three decimals.
- `impact_coverage`: `object_hits / 7`, rounded to three decimals.
- `cascade_score`: `100 * (0.65 * mechanism_coverage + 0.35 * impact_coverage)`, rounded to two decimals.
- `classification`: use `rock_ice_debris_flow_cascade_report_consistent` only when `process_hits >= 8` and `object_hits >= 6`; otherwise use `underconstrained_report_cascade`.

Return compact JSON:

```json
{
  "answer": {
    "process_hits": 0,
    "object_hits": 0,
    "mechanism_coverage": 0.0,
    "impact_coverage": 0.0,
    "cascade_score": 0.0,
    "classification": ""
  },
  "interpretation": "<one sentence tied to the report-supported cascade>"
}
```
