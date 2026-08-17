# Correct Answer

```json
{
  "answer": {
    "date_offset_days": 22,
    "point_precip_mean_mm": 13.645,
    "regional_peak_precip_mm": 184.585,
    "peak_to_point_ratio": 13.528,
    "change_scene_total": 0,
    "rain_change_gate_score": 1,
    "classification": "source_proximal_ash_anchor_controls"
  },
  "interpretation": "Only the regional peak rain test passes, so the computed gate keeps the event anchored to the small Barren Island ash-plume observation."
}
```

# Computation Path

The locked event start is `2010-09-03`. The report image date is `2010-09-25`, so `date_offset_days = 22`.

The two point precipitation estimates are `13.99 mm` and `13.30 mm`. Their mean is `(13.99 + 13.30) / 2 = 13.645 mm`.

The gridded regional precipitation maxima are `39.192 mm`, `64.043 mm`, and `184.585 mm`, so `regional_peak_precip_mm = 184.585 mm`. The rain contrast is `184.585 / 13.645 = 13.528`.

The radar and optical change products each have `0` pre scenes and `0` post scenes, so `change_scene_total = 0 + 0 + 0 + 0 = 0`.

The four gate tests evaluate to false, true, false, false:

- `13.645 >= 25` is false.
- `184.585 >= 100` is true.
- `22 <= 3` is false.
- `0 >= 1` is false.

The score is therefore `1`, below the required score of `3`. The final label is `source_proximal_ash_anchor_controls`.

# Scoring Rubric

- 3 points: Returns compact JSON with the requested numeric fields, final classification, and one short computed consequence.
- 4 points: Computes the timing term correctly: report image date `2010-09-25`, locked start `2010-09-03`, and `date_offset_days = 22`.
- 4 points: Computes the precipitation terms within tolerance: `point_precip_mean_mm = 13.645`, `regional_peak_precip_mm = 184.585`, and `peak_to_point_ratio = 13.528`.
- 3 points: Computes `change_scene_total = 0` from the four pre/post scene counts.
- 4 points: Applies all four gate tests correctly and reports `rain_change_gate_score = 1`.
- 2 points: Gives the computed consequence that rain/change context does not control the diagnosis and avoids expanding the event into a mainland impact or lahar-dominant case.
