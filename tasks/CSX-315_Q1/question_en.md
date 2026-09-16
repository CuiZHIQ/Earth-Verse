# Puncak Jaya Tropical Glacier Retreat Priority

A cryosphere risk team is preparing a short technical note for disaster-management partners in Papua, Indonesia, after reviewing the October 2015-March 2016 Puncak Jaya glacier retreat episode. The team needs to decide what response posture should frame the briefing: long-duration tropical glacier-retreat monitoring, acute ice or lake-outburst response, rainfall-flood response, or fire and surface-scar response.

Make the priority call by connecting the event window, tropical high-mountain setting, snow-and-ice loss process, landscape-change clues, and implications for nearby exposed places. Use the package event window from `2015-10-01` through `2016-03-31` inclusively. Your answer should distinguish slow cryosphere retreat from short-fuse emergency triggers, and it should use quantitative anchors where they are important to the decision.

Use this priority-index rule. Add to `slow_onset_monitoring_score`: `+2` if event duration is at least 90 days, `+2` if the event name identifies glacier retreat, `+2` if package metadata frames the hazard as slow-onset glacier retreat, `+1` if the event anchor notes cryosphere/ice-loss context, `+1` if the Sentinel-1 mean scene change magnitude is below 0.5 dB, and `+1` if the Sentinel-2 burn-severity product has no sufficient scenes. Add to `acute_response_score`: `+2` if matching event-catalog hits are present, `+2` if humanitarian response reports are present, `+1` if Sentinel-1 mean scene change magnitude is at least 3 dB, `+1` if usable post-event Sentinel-2 burn-severity scenes exist, and `+1` if critical amenities reach at least 20. Choose the posture with the higher score.

Return your answer as JSON:

```json
{
  "answer": "<compact_priority_label>",
  "priority_index": {
    "slow_onset_monitoring_score": "<value>",
    "acute_response_score": "<value>"
  },
  "key_numeric_anchors": [
    {"name": "<anchor>", "value": "<value>"}
  ],
  "impact_chain": ["<driver>", "<hazard_process>", "<priority>"],
  "rationale": "<brief explanation>"
}
```
