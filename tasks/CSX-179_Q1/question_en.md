# Southeast Asia Haze Severity and Transport Check

A regional air-quality analysis team is reviewing the 2015 Southeast Asia haze episode from Indonesian fires during the August-November incident window. The briefing needs a compact classification that reconciles fire activity, smoke-layer behavior, downwind transport, and air-quality severity without turning local receptor counts or broad imagery into an independent loss estimate.

Using the incident record and quantitative diagnostics, decide whether the episode is best treated as a cross-border fire-smoke air-quality event, ordinary weather haze, a local burn-area mapping problem, or a population-counting exercise. Support the choice with numeric anchors that show why the classification is stronger than the alternatives.

Return compact JSON:

```json
{
  "classification": "<compact label>",
  "severity_ledger": {
    "hotspots_min": <integer>,
    "psi_ratio_min": <number>,
    "aerosol_multiplier": <number>,
    "co_ratio_nearly": <number>
  },
  "transport_check": "<one sentence>",
  "rationale": "<2-3 concise sentences>"
}
```
