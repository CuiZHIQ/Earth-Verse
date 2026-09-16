# Mount Ontake Signal Ledger

For the 2014-09-27 Mount Ontake eruption, reconstruct a compact numeric ledger that tests whether the available record is dominated by a sudden summit phreatic plume signal rather than a rainfall or surface-change signal.

Compute:

1. `text_anchor_score`: required report anchors present divided by 5. The required anchors are `unexpectedly`, `gas and steam`, `phreatic eruption`, `ash`, and `little warning`; count an anchor as present if it appears in the event report paragraph or locked event notes.
2. `image_byte_ratio`: event-day image byte count divided by pre-event image byte count, using package manifest byte counts.
3. `max_precip_mm`: maximum of the event-day precipitation values from the point, archive, hourly grid, GPM, and CHIRPS summaries.
4. `surface_pre_scene_total`: Sentinel-1 pre-event count plus Sentinel-2 pre-event count.
5. `ledger_score`: one point each for `text_anchor_score == 1`, `image_byte_ratio >= 3`, `max_precip_mm < 1`, and `surface_pre_scene_total == 0`.

Return compact JSON rounded to 6 decimals where applicable:

```json
{
  "answer": "<concise signal label>",
  "text_anchor_score": 0.0,
  "image_byte_ratio": 0.0,
  "max_precip_mm": 0.0,
  "surface_pre_scene_total": 0,
  "ledger_score": 0,
  "consistency_note": "<one sentence tied to the four tests>"
}
```
