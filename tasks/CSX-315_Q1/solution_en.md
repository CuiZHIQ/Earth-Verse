# Final Answer

The correct compact answer is `slow_onset_tropical_glacier_retreat_monitoring_priority`.

Expected structured answer:

```json
{
  "answer": "slow_onset_tropical_glacier_retreat_monitoring_priority",
  "priority_index": {
    "slow_onset_monitoring_score": 9,
    "acute_response_score": 0
  },
  "key_numeric_anchors": [
    {"name": "event_duration_days", "value": 183},
    {"name": "scene_mean_change_db", "value": -0.147},
    {"name": "matching_catalog_events", "value": 0},
    {"name": "critical_amenities_in_aoi", "value": 10}
  ],
  "impact_chain": [
    "tropical_cryosphere_warming",
    "slow_glacier_retreat_and_ice_loss",
    "monitoring_and_long_term_risk_management"
  ]
}
```

# Key Computations

The locked event anchor for CSX-315 identifies the Puncak Jaya glacier retreat episode in Papua, Indonesia, with a temporal window from 2015-10-01 to 2016-03-31. Inclusive duration:

```text
2015-10-01 through 2016-03-31 = 183 days
```

The response-priority index in `compute_gt.py` gives slow-onset monitoring 9 points and acute response 0 points. The slow-onset score is driven by the long event duration, the glacier-retreat event name, the slow-onset hazard match, the tropical cryosphere anchor, weak radar scene-change magnitude, and the lack of sufficient burn-severity scenes. The acute-response score remains 0 because there are no matching event-catalog hits, no ReliefWeb response reports, no strong radar disturbance, no usable post-event burn-severity scenes, and the count of critical amenities does not by itself cross the acute-response threshold.

The scoring rule is:

- slow-onset monitoring: `+2` for duration at least 90 days, `+2` for a glacier-retreat event name, `+2` for slow-onset glacier-retreat metadata framing, `+1` for cryosphere context in the event anchor, `+1` for Sentinel-1 mean-change magnitude below 0.5 dB, and `+1` for no sufficient Sentinel-2 burn-severity scenes;
- acute response: `+2` for matching catalog hits, `+2` for humanitarian response reports, `+1` for Sentinel-1 mean-change magnitude at least 3 dB, `+1` for usable post-event Sentinel-2 scenes, and `+1` for at least 20 critical amenities.

For this package, all six slow-onset components pass and all five acute-response components fail, giving `9` versus `0`.

Key anchors:

- `event_duration_days`: 183
- `scene_mean_change_db`: -0.147, with tolerance +/-0.02
- `matching_catalog_events`: 0
- `critical_amenities_in_aoi`: 10

Supporting metrics include gridded event precipitation context, short-window point weather, broad population context, and file-status counts. These support the diagnosis but are not enough to turn the event into a documented flood, avalanche, glacial-lake outburst, fire, casualty, evacuation, or infrastructure-damage event.

# Reasoning Path

The event is a tropical high-mountain cryosphere problem. The key decision is whether the briefing should emphasize long-duration glacier retreat and monitoring, or whether it should shift into an acute emergency posture such as avalanche, lake-outburst flood, rainfall flood, or fire response.

The 183-day window is much longer than the normal signature of a short-fuse avalanche, glacial-lake outburst, flash flood, or fire scar response. That duration matches slow glacier retreat and ice loss better than a rapid-onset emergency. The event metadata and locked anchor also point to snow and ice loss in the Puncak Jaya tropical cryosphere, so the physical process should be interpreted as retreat monitoring unless independent acute-impact evidence overrides it.

The local scene-change and report checks do not supply that override. The radar mean change is close to zero at -0.147 dB, which is not a strong acute surface-disturbance signal. The burn-severity scene check reports no sufficient scenes, so there is no basis for a fire or surface-scar priority. Event-catalog matching returns 0 relevant events, and the humanitarian-report check does not establish an acute response episode. Rainfall and exposure context are operationally relevant, but they remain contextual risk factors unless linked to observed impacts.

The correct impact chain is therefore tropical cryosphere warming leading to slow glacier retreat and ice loss, which calls for monitoring, long-term risk management, and preparedness communication rather than immediate evacuation or response framing.

# Disaster Interpretation

Puncak Jaya is one of the few tropical glacier settings in Southeast Asia. In this context, glacier retreat is a climate-sensitive, slow-onset hazard with important scientific and operational consequences: shrinking ice cover, changing high-mountain hydrology, loss of cryosphere indicators, and potential future instability concerns. A disaster-management briefing should therefore emphasize surveillance, trend interpretation, risk communication, and preparedness for secondary hazards.

The exposure context matters because nearby people, services, and infrastructure make continued monitoring consequential. However, exposure is not the same as observed damage. The evidence supports a monitoring priority, not claims of casualties, displacement, road closure, burn severity, confirmed flood impacts, or a documented glacial-lake outburst.

Major alternatives fail for substantive reasons:

- Acute avalanche or lake-outburst response is not supported by the long event window, weak scene-change signal, and lack of matching catalog or response-report evidence.
- Rainfall-flood response is not the dominant priority because wet tropical precipitation context is not observed flood damage.
- Fire or surface-scar response is not supported because the burn-severity check lacks sufficient scenes and the event framing is cryosphere retreat.
- Exact glacier-area loss should not be claimed because this task does not compute a glacier-area time series.

# Scoring Rubric

Total: 20 points.

- 4 points: Gives `slow_onset_tropical_glacier_retreat_monitoring_priority` or a clearly equivalent compact label, and reports the priority index with slow-onset monitoring higher than acute response by applying the visible scoring rule, ideally 9 versus 0.
- 5 points: Reports the four key numeric anchors with appropriate precision or tolerance: 183 event days, -0.147 dB scene mean change within +/-0.02, 0 matching catalog events, and 10 critical amenities.
- 4 points: Explains the physical mechanism linking tropical cryosphere warming, long-duration glacier retreat, and slow ice loss rather than treating the event as a sudden avalanche, glacial-lake outburst, flood, or fire.
- 3 points: Uses landscape-change, catalog, and report signals correctly: weak radar mean change, no sufficient burn-severity scenes, no matching catalog events, and no humanitarian response report that would justify an acute posture.
- 2 points: Builds an operational impact chain that moves from driver to hazard process to monitoring and long-term risk management, while treating exposure as a reason for preparedness rather than proof of damage.
- 2 points: Provides concise, valid JSON in the requested structure and avoids unsupported claims about exact ice-area loss, casualties, evacuation, road disruption, burn severity, observed infrastructure damage, or confirmed flood impacts.
