# Greece Wildfire Smoke-Transport Score Ledger

For the late-August phase of the 2023 Greece wildfires, a technical review team needs a compact score ledger for the August 22-23 narrative. The goal is to decide which candidate line has the strongest direct signal: smoke transport with Athens-area urban impact, national burn severity, national health burden, or drought-index primacy.

Using the incident narrative, compute the deterministic ledger below for August 22-23, 2023. Parse only paragraph, heading, and figure-caption narrative blocks from the local incident article; ignore navigation, related-content, and footer text.

Definitions:

- `event_blocks`: count the parsed incident-narrative blocks containing at least one of these lower-case phrases: `dozens more fires`, `alexandroupolis`, `plume`, `athens`, `extreme fire weather`, `mediterranean sea`, `effis`.
- `smoke_blocks`: among those event blocks, count blocks containing `smoke` or `plume`.
- `urban_blocks`: among those event blocks, count blocks containing `homes`, `cars`, or `athens`.
- `fire_weather_blocks`: among those event blocks, count blocks containing `hot`, `dry`, or `windy`.
- `main_transport_gate`: 1 when the narrative links Alexandroupolis with transport southwest toward Italy; otherwise 0.
- `aug23_extent_gate`: 1 when the narrative says smoke was detected over Italy and across the Mediterranean Sea in northern Africa by August 23; otherwise 0.
- `burn_phrase_gate`: 1 when an event block reports burning or burned objects; otherwise 0.
- `national_burn_value_gate`: 1 only if the event blocks contain a numeric national burned-area or burn-severity value; otherwise 0.
- `hospital_or_casualty_value_gate`: 1 only if the event blocks contain a numeric hospital-burden or casualty value; otherwise 0.
- `drought_index_value_gate`: 1 only if the event blocks contain a computed drought-index value; otherwise 0.

Candidate scores:

- `smoke_transport_urban = 2 * [smoke_blocks >= 3] + [urban_blocks >= 1] + [fire_weather_blocks >= 1] + main_transport_gate + aug23_extent_gate`
- `national_burn_severity = burn_phrase_gate + national_burn_value_gate`
- `national_health_burden = [urban_blocks >= 1] + hospital_or_casualty_value_gate`
- `drought_index_primary = [fire_weather_blocks >= 1] + drought_index_value_gate`

Return compact JSON:

```json
{
  "answer": {
    "target_family": "greece_wildfire_smoke_transport_score_ledger",
    "event_window": "2023-08-22_to_2023-08-23",
    "signal_counts": {
      "event_blocks": 0,
      "smoke_blocks": 0,
      "urban_blocks": 0,
      "fire_weather_blocks": 0
    },
    "candidate_scores": {
      "smoke_transport_urban": 0,
      "national_burn_severity": 0,
      "national_health_burden": 0,
      "drought_index_primary": 0
    },
    "top_candidate": "",
    "dominance_margin": 0,
    "classification": ""
  },
  "interpretation": "<one sentence tied to the computed ledger>"
}
```
