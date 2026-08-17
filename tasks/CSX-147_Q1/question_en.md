# Bangladesh Storm-Flood Process Evidence Ledger

A hydrometeorology analyst is checking the April 2004 severe storms and floods in northern and northeastern Bangladesh. The question is whether the record supports a multi-day storm-driven flood process ledger, rather than a single-day storm label, a storm-unlinked flood interpretation, or a pure snapshot-timing label.

Build a five-test score ledger for the 2004-04-09 through 2004-04-22 event window. Return one compact JSON object with this structure:

```json
{
  "target_family": "bangladesh_2004_storm_flood_process_score_ledger",
  "tests": {
    "sequence_persistence": {"pass": true, "values": {}},
    "storm_flood_causation_text": {"pass": true, "values": {}},
    "displacement_anchor": {"pass": true, "values": {}},
    "terrain_text": {"pass": true, "values": {}},
    "image_timing": {"pass": true, "values": {}}
  },
  "score": 5,
  "answer": "multi_day_storm_flood_process_ledger_pass",
  "rejected_alternatives": ["single_day_storm", "storm_unlinked_flood_case", "snapshot_timing_label"],
  "interpretation": "one concise sentence tied to the computed ledger"
}
```

Use these deterministic tests:

- `sequence_persistence`: compute the inclusive storm-sequence length, the inclusive event-window length, and the storm-window coverage ratio. Pass if the storm sequence lasts at least 10 days and covers at least 0.75 of the event window.
- `storm_flood_causation_text`: check whether the report ties the flood to a series of intense thunderstorms, places the flooding after that storm sequence, and describes runoff from uplands as a direct flood cause. Pass only when all three causal text anchors are present.
- `displacement_anchor`: extract the Bangladesh displacement count expressed as about half a million people. Pass if the count is at least 400,000.
- `terrain_text`: check whether the event text ties the most prominent flood area to water from the Khasi Hills and the India-Bangladesh border area. Pass only when both text anchors are present.
- `image_timing`: compute the follow-up image lag after the storm-sequence end and after the event-window end, and extract the image resolution. Pass if the image is after the storm sequence, within 7 days after the event window, and has 250 m per pixel resolution.

Round ratios to three decimals and day counts to integers.
