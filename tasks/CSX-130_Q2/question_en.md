# Hurricane Ophelia European Wind-Risk Timing Proof

During 9-16 October 2017, Hurricane Ophelia moved from the eastern Atlantic toward Ireland and the United Kingdom after losing its purely tropical structure. A European wind-risk team is preparing a post-event timing proof: was the European phase best explained as transition-related wind risk, or should rainfall, imagery, population context, or catalog matching carry the diagnosis?

Build a compact proof ledger for the European phase. It must quantify the timing from post-tropical transition to the local wind peak, relate the gust peak to the pressure minimum and pressure falls, test gust persistence, show why rainfall is secondary locally, and keep image, population, and catalog facts as context rather than proof of local damage.

Return JSON with this shape:

```json
{
  "family": "ophelia_european_wind_risk_transition_timing_consistency_proof",
  "ledger": [
    {"row_id": "transition_to_wind_peak_timing", "calculation": "", "inference": ""},
    {"row_id": "pressure_fall_wind_severity", "calculation": "", "inference": ""},
    {"row_id": "gust_persistence", "calculation": "", "inference": ""},
    {"row_id": "rainfall_secondary_test", "calculation": "", "inference": ""},
    {"row_id": "image_population_guardrail", "calculation": "", "inference": ""}
  ],
  "final_stance": ""
}
```
