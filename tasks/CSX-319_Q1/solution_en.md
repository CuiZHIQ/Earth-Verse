# Final Answer

Correct core answer: `cryosphere_glacier_collapse_monitoring_priority`.

Expected structured core:

```json
{
  "answer": "cryosphere_glacier_collapse_monitoring_priority",
  "mechanism": "cryosphere_glacier_collapse_mass_movement",
  "evidence_strength": "high_event_anchor_support",
  "priority": "high_cryosphere_monitoring_priority",
  "key_metrics": {
    "event_window_days": 67,
    "correspondence_score": 94,
    "mechanism_term_count": 5,
    "lock_confidence": "high"
  },
  "impact_chain": [
    "rare_catastrophic_glacier_collapse",
    "ice_avalanche_or_debris_flow_runout",
    "cryosphere_monitoring_and_downstream_screening_priority"
  ]
}
```

# Key Computations

The event anchor gives a window from `2016-07-17` through `2016-09-21`, so the inclusive duration is `67` days.

The event metadata gives `correspondence_score = 94`, and the locked NASA event anchor has `lock_confidence = high`.

The mechanism term count is 5 because the combined event name, hazard family/label, location, and lock notes support:

`cryosphere`, `glacier`, `avalanche`, `collapse`, and `High Asia/Tibet`.

Because lock confidence is high, correspondence is at least 90, and the mechanism term count is at least 4, the evidence strength is `high_event_anchor_support` and the priority is `high_cryosphere_monitoring_priority`.

# Scoring Rubric

- 4 points: Gives the cryosphere glacier-collapse monitoring interpretation and high monitoring priority.
- 3 points: Reports the 2016-07-17 to 2016-09-21 event window and computes 67 inclusive days.
- 4 points: Uses high lock confidence and correspondence_score = 94 as event-anchor support.
- 4 points: Counts the cryosphere, glacier, avalanche, collapse, and High Asia/Tibet mechanism terms, giving mechanism_term_count = 5.
- 3 points: Connects rare glacier collapse to ice-avalanche/debris-flow runout and monitoring relevance while rejecting rainfall-only, vegetation-change, and low-priority framings.
- 2 points: Returns the requested JSON-like structure and avoids unsupported trigger, casualty, displacement, mapped-volume, precipitation, radar, or population-impact claims.
