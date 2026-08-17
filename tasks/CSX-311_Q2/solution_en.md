# Correct Answer

```json
{
  "answer": "sudden summit phreatic plume signal",
  "text_anchor_score": 1.0,
  "image_byte_ratio": 4.356742,
  "max_precip_mm": 0.536591,
  "surface_pre_scene_total": 0,
  "ledger_score": 4,
  "consistency_note": "All four tests pass: complete text anchors, image contrast above 3, precipitation below 1 mm, and zero pre-event scenes for surface-change reconstruction."
}
```

# Computation

The report paragraph and locked notes contain all five anchors: `unexpectedly`, `gas and steam`, `phreatic eruption`, `ash`, and `little warning`, so `text_anchor_score = 5 / 5 = 1.0`.

The manifest byte counts are 98,702 for the event-day image and 22,655 for the pre-event image, so `image_byte_ratio = 98702 / 22655 = 4.356742`.

The event-day precipitation values are 0.01, 0.0, 0.5365908145904541, 0.11499999463558197, and 0.0 mm. Their maximum is `0.536591 mm`, below the 1 mm threshold.

The Sentinel-1 and Sentinel-2 pre-event scene counts are both 0, so `surface_pre_scene_total = 0 + 0 = 0`.

The four threshold tests are true: `1.0 == 1`, `4.356742 >= 3`, `0.536591 < 1`, and `0 == 0`. Therefore `ledger_score = 4`, supporting the label `sudden summit phreatic plume signal`.

# Scoring Rubric

- 3 points: Returns the requested compact JSON fields with numeric values rounded to 6 decimals where applicable.
- 4 points: Computes the 5-of-5 text anchor score correctly and ties it to the named anchors.
- 4 points: Computes the image byte ratio correctly from 98,702 and 22,655.
- 3 points: Computes the precipitation maximum correctly and applies the `< 1 mm` threshold.
- 2 points: Computes the surface pre-scene total from Sentinel-1 and Sentinel-2 counts.
- 2 points: Applies all four ledger tests correctly and gives `ledger_score = 4`.
- 1 point: Gives the concise label `sudden summit phreatic plume signal` or an equivalent wording.
- 1 point: Keeps the consistency note limited to the four computed tests without adding unmeasured impacts.
