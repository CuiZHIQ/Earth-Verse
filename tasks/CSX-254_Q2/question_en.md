# Black Summer Fire-Smoke Consistency Score

During the 2019-2020 Australian Black Summer, analysts need a calculation-first check of whether a bright fire-season scene, local burn-change statistics, wider annual surface-change context, and late-season text record form a coherent smoke-fire signal.

Derive these quantities from the technical record:

- `dnbr_mean`, `dnbr_max`, and `dnbr_min` from the local burn-change summary.
- `annual_mean` from the wider annual surface-change summary.
- `gray_pre` and `gray_event` as the mean of the RGB channel means for the pre-event and event images, with `delta_gray = gray_event - gray_pre`.
- `texture_pre` and `texture_event` as the mean of the RGB channel standard deviations for the same images, with `delta_texture = texture_pre - texture_event`.
- `gap_days = event_end - burn_post_end`, using calendar days.
- Five text flags: smoke, pyrocumulonimbus or firestorm, stratosphere, long-range transport, and late outbreak dates after `burn_post_end`.

Compute the score ledger:

- `B = 2` if `dnbr_mean > 0.10` and `dnbr_max > 0.80`; `B = 1` if exactly one threshold passes; otherwise `B = 0`.
- `V = 2` if `delta_gray > 100`; `V = 1` if `delta_gray > 50`; otherwise `V = 0`.
- `T = 1` if `delta_texture > 10`; otherwise `T = 0`.
- `G = -1` if `gap_days >= 60`; otherwise `G = 0`.
- `R = 3` if all five text flags pass; `R = 2` if four pass; `R = 1` if two or three pass; otherwise `R = 0`.
- `S = 1` if `annual_mean < 0.05` and `dnbr_max > 0.80`; otherwise `S = 0`.
- `score = B + V + T + G + R + S`.

Class labels:

- `score >= 7`: `strong smoke-fire consistency with incomplete-season burn period`
- `score 4-6`: `moderate consistency`
- `score <= 3`: `weak consistency`

Return JSON only:

```json
{
  "values": {},
  "components": {"B": 0, "V": 0, "T": 0, "G": 0, "R": 0, "S": 0},
  "score": 0,
  "class_label": "",
  "one_line_diagnosis": ""
}
```
