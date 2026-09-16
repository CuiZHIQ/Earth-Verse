# Correct Answer

```json
{
  "answer": {
    "pre_mean_luminance": 84.432,
    "event_mean_luminance": 115.658,
    "luminance_delta": 31.226,
    "tan_fraction_delta": 0.0245,
    "red_excess_delta": 2.4108,
    "dry_wind_index": 11.639,
    "dust_veil_score": 4,
    "classification": "dry_wind_tan_brightening_dust_veil"
  },
  "interpretation": "All four tests pass, so the computed consequence is a dry, wind-supported tan brightening signal rather than a rainfall or wet-surface signal."
}
```

# Computation Path

The pre-event scene has mean luminance `84.432`; the event-window scene has mean luminance `115.658`, giving `luminance_delta = 115.658 - 84.432 = 31.226`.

The tan-pixel fraction rises from `0.1495` to `0.1740`, so `tan_fraction_delta = 0.0245`. Mean red-minus-blue excess rises from `8.1127` to `10.5235`, so `red_excess_delta = 2.4108`.

Event-window package point precipitation is `0.0 mm`. The maximum package point wind is `11.639 m/s`, so `dry_wind_index = 11.639 / (1 + 0.0) = 11.639`. This point weather is used as a dry-wind comparator, not as complete corridor wind evidence.

The four threshold tests all pass: `31.226 >= 25`, `0.0245 >= 0.02`, `2.4108 >= 2`, and `0.0 <= 0.5` with `11.639 >= 10`. The score is therefore `4`, which maps to `dry_wind_tan_brightening_dust_veil`.

# Scoring Rubric

- 3 points: Returns compact JSON with the requested numeric fields, classification, and one short interpretation.
- 3 points: Uses the luminance, tan-fraction, and red-excess formulas exactly as stated.
- 5 points: Reports the image deltas within tolerance: `luminance_delta = 31.226`, `tan_fraction_delta = 0.0245`, and `red_excess_delta = 2.4108`.
- 3 points: Computes package point-weather values `point_precip_total_mm = 0.0`, `max_point_wind_m_s = 11.639`, and `dry_wind_index = 11.639` while treating point weather as a dry-wind comparator.
- 4 points: Applies the four threshold tests correctly and returns `dust_veil_score = 4` with `dry_wind_tan_brightening_dust_veil`.
- 2 points: Rejects a rainfall or wet-surface reading from the computed dry-window values and avoids treating the image metric as calibrated dust concentration.
