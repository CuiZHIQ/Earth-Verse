# Final Answer

Correct compact JSON:

```json
{
  "values": {
    "dnbr_mean": 0.156,
    "dnbr_max": 0.974,
    "dnbr_min": -1.074,
    "annual_mean": 0.028,
    "gray_pre": 71.233,
    "gray_event": 215.256,
    "delta_gray": 144.023,
    "texture_pre": 49.439,
    "texture_event": 28.625,
    "delta_texture": 20.814,
    "burn_post_end": "2019-11-30",
    "event_end": "2020-02-29",
    "gap_days": 91
  },
  "components": {"B": 2, "V": 2, "T": 1, "G": -1, "R": 3, "S": 1},
  "score": 8,
  "class_label": "strong smoke-fire consistency with incomplete-season burn period",
  "one_line_diagnosis": "Bright smoke-season imagery, local burn-change statistics, and report text agree on a strong fire-smoke signal, while the burn raster period ends before the late-season outbreaks."
}
```

# Key Computations

- Burn values: `dnbr_mean = 0.156`, `dnbr_max = 0.974`, `dnbr_min = -1.074`.
- Wider annual surface-change mean: `annual_mean = 0.028`.
- Image grayscale means: `gray_pre = 71.233`, `gray_event = 215.256`, so `delta_gray = 144.023`.
- Image texture means: `texture_pre = 49.439`, `texture_event = 28.625`, so `delta_texture = 20.814`.
- Date gap: `2020-02-29 - 2019-11-30 = 91` days.
- Text flags: smoke, pyrocumulonimbus or firestorm, stratosphere, long-range transport, and late outbreak dates all pass.

# Reasoning Path

The burn ledger earns `B = 2` because both burn thresholds pass. The image ledger earns `V = 2` from the large grayscale increase and `T = 1` from the texture drop. The date gap earns `G = -1` because the burn-change period ends 91 days before the event period ends. The parsed text earns `R = 3` because all five flags pass. The scale-contrast term earns `S = 1` because the annual mean is below `0.05` while the local burn maximum is above `0.80`.

The sum is `2 + 2 + 1 - 1 + 3 + 1 = 8`, which maps to the top class.

# Scoring Rubric

- 4 points: Reports final score `8` and the exact class label.
- 4 points: Extracts the burn and annual statistics with correct rounding: `0.156`, `0.974`, `-1.074`, and `0.028`.
- 3 points: Computes image means and differences: `71.233`, `215.256`, `144.023`, `49.439`, `28.625`, and `20.814`.
- 4 points: Applies the ledger components exactly: `B = 2`, `V = 2`, `T = 1`, `G = -1`, `R = 3`, `S = 1`.
- 2 points: Computes the 91-day date gap from the correct dates and applies the gap term.
- 2 points: Parses the five text flags with report-text evidence and ties them to the `R` score.
- 1 point: Returns compact structured JSON with numeric values rounded to three decimals and exact dates.
