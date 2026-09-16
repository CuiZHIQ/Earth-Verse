# Indonesian Fire-Haze Remote-Sensing Briefing

During the 2015-2016 El Nino, drought helped intensify Indonesia's fire season and the late-2015 smoke-haze crisis across tropical Southeast Asia. A regional emergency-management briefing team needs a concise expert diagnosis of what the satellite context can and cannot support.

Prepare a short structured briefing that decides whether the event-period visual signal should be interpreted primarily as regional smoke haze with visibility and transport consequences, or as another hazard interpretation such as floodwater mapping, cyclone cloud tracking, heat-only stress, or parcel-level fire-responsibility attribution. Tie the conclusion to the timing and scale of the image context, the reported impact chain, and the limits of assigning blame from imagery alone.

Return compact JSON:

```json
{
  "answer": "<short_diagnosis_label>",
  "remote_sensing_role": ["<observable_context>", "<impact_interpretation>", "<attribution_caveat>"],
  "key_metrics": {
    "pre_snapshot_date": "<YYYY-MM-DD>",
    "event_snapshot_date": "<YYYY-MM-DD>",
    "snapshot_gap_days": 0,
    "snapshot_dimensions": "<width>x<height>"
  },
  "interpretation": "<one or two sentences linking the visual diagnosis, impact chain, and attribution caution>"
}
```

Keep the answer focused on supported disaster reasoning, and avoid unsupported legal, parcel-level, mortality, economic-loss, or burned-area claims.
