# Final Answer

```json
{
  "target_family": "bangladesh_2004_storm_flood_process_score_ledger",
  "tests": {
    "sequence_persistence": {
      "pass": true,
      "values": {
        "storm_start": "2004-04-09",
        "storm_end": "2004-04-19",
        "storm_days": 11,
        "event_days": 14,
        "storm_window_coverage_ratio": 0.786
      }
    },
    "storm_flood_causation_text": {
      "pass": true,
      "values": {
        "intense_thunderstorms_text": true,
        "floods_followed_storms_text": true,
        "upland_runoff_cause_text": true
      }
    },
    "displacement_anchor": {
      "pass": true,
      "values": {
        "reported_displaced_people": 500000
      }
    },
    "terrain_text": {
      "pass": true,
      "values": {
        "khasi_hills_text": true,
        "india_bangladesh_border_text": true
      }
    },
    "image_timing": {
      "pass": true,
      "values": {
        "image_date": "2004-04-26",
        "event_snapshot_date": "2004-04-15",
        "lag_after_storm_end_days": 7,
        "lag_after_event_end_days": 4,
        "resolution_m_per_pixel": 250
      }
    }
  },
  "score": 5,
  "answer": "multi_day_storm_flood_process_ledger_pass",
  "rejected_alternatives": ["single_day_storm", "storm_unlinked_flood_case", "snapshot_timing_label"],
  "interpretation": "The ledger supports a multi-day storm-flood process because an 11-day storm sequence is text-linked to upland runoff, cross-border flooding, 500000 displaced people, and a timely 250 m follow-up image."
}
```

# Key Computations

The event window is inclusive from 2004-04-09 to 2004-04-22, so `event_days = 14`. The storm sequence runs from 2004-04-09 through 2004-04-19, so `storm_days = 11` and `storm_window_coverage_ratio = 11 / 14 = 0.786`.

The report text supplies the process link: it describes a series of intense thunderstorms, states that the floods followed that sequence, and says the most obvious flooding was caused by water rushing out of the Khasi Hills. Those three text anchors make `storm_flood_causation_text.pass = true`.

Report and image anchors:

- Bangladesh displacement count: about half a million people, encoded as `500000`.
- The event text links the most prominent flood area to water from the Khasi Hills and the India-Bangladesh border area.
- The follow-up image date is `2004-04-26`, which is `7` days after the storm-sequence end and `4` days after the event-window end.
- The package metadata records an event snapshot date of `2004-04-15`.
- The image resolution is `250 m per pixel`.

# Reasoning Path

First, the sequence test rules out a single-day storm label: the storm period lasts `11` inclusive days and covers `0.786` of the `14`-day event window, passing both persistence conditions.

Second, the report text rules out a storm-unlinked flood label. The same source connects the storm sequence, subsequent flooding, and upland runoff from the Khasi Hills into one process chain.

Third, the displacement and terrain tests confirm that the process chain is tied to the Bangladesh flood impact and the India-Bangladesh border area, not only to a generic regional image.

Fourth, the image timing test places the follow-up observation after the storm sequence and close to the event window, with the required `250 m` resolution. With all five tests passing, the score is `5/5` and the answer is `multi_day_storm_flood_process_ledger_pass`.

# Computed Interpretation

The computed ledger supports a multi-day storm-flood process for April 2004 Bangladesh; the single-day storm, storm-unlinked flood case, and snapshot-timing label all fail against the combined timing, causal-text, displacement, terrain, and image-date checks.

# Scoring Rubric

- 3 points: Final ledger and answer. Full credit requires the target family, all five tests marked true, score `5`, answer `multi_day_storm_flood_process_ledger_pass`, and the three rejected alternatives. Partial credit: 1-2 points if the answer label is close but one test status, the score, or one rejected alternative is missing.
- 3 points: Sequence arithmetic. Full credit requires `storm_days = 11`, `event_days = 14`, `storm_window_coverage_ratio = 0.786`, and correct application of the 10-day and 0.75 thresholds. Partial credit: 1-2 points for correct dates but one missing inclusive-day or ratio calculation.
- 4 points: Storm-flood causation text. Full credit requires all three causal text anchors: series of intense thunderstorms, floods following that storm sequence, and upland runoff from the Khasi Hills as the flood cause. Partial credit: 2-3 points for two correct causal anchors; 1 point for only one anchor.
- 3 points: Displacement extraction. Full credit requires extracting about half a million displaced people in Bangladesh as `500000` and applying the `>= 400000` test. Partial credit: 1-2 points for a correct qualitative half-million reading without the numeric threshold.
- 2 points: Terrain text anchors. Full credit requires both the Khasi Hills and India-Bangladesh border area text anchors. Partial credit: 1 point for naming only one of the two anchors.
- 3 points: Image timing and resolution. Full credit requires `2004-04-26`, `7` days after storm end, `4` days after event end, `250 m per pixel`, and the correct pass state. Partial credit: 1-2 points for the correct image date and resolution but one missing lag calculation.
- 2 points: Compact computed interpretation. Full credit keeps the interpretation tied to the five calculations and does not add extra loss counts beyond the ledger. Partial credit: 1 point if the interpretation is broadly consistent but weakly tied to the computed values.
