# 2023 Canadian Wildfire Smoke Threshold Ledger

During May 2023, wildfires in Alberta and western Canada sent smoke across parts of Canada and the northern United States. A climate-health analyst is checking whether a compact index should be driven more by transported aerosol loading, fire-source size, or land-surface change.

Compute this deterministic threshold ledger from the incident technical record:

- `smoke_load_score`: 2 points if the Goddard 2023-05-10 average AOD is at least 1.0; 2 points if the Grand Forks 2023-05-16 average AOD is at least 2.0; 1 point if the Grand Forks peak AOD is at least 3.0.
- `fire_source_score`: 2 points if burned area by 2023-05-16 is at least 400,000 hectares; 1 point if burned area is at least 1,500 square miles; 1 point if the Alberta active-fire count is at least 80.
- `surface_change_score`: 1 point if mean dNBR is at least 0.30; 1 point if maximum dNBR is at least 1.00; 1 point if annual embedding mean change is below 0.10 and maximum change is at least 0.75.
- `context_population_people`: the rounded compact population sum.

Set `top_score_family` to the family with the highest score. If there is a tie, use this sequence: `smoke_load`, `fire_source`, `surface_change`.

Return a compact JSON object with exactly these fields:

```json
{
  "smoke_load_score": 0,
  "fire_source_score": 0,
  "surface_change_score": 0,
  "composite_score": 0,
  "top_score_family": "",
  "context_population_people": 0
}
```
