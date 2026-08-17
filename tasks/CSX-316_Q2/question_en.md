# Kilimanjaro Retreat Window-Scene Consistency Index

A technical review team is checking whether the Kilimanjaro ice-field retreat satisfies a compact long-window consistency index, KSCI, when compared with same-window regional weather summaries and scene-pair status checks.

Compute KSCI using these rules:

- `event_span_days = end_date - start_date` as a calendar-day difference, and `event_span_years = event_span_days / 365.25`.
- `met_window_days` is the inclusive length of the regional hourly-summary window, and `met_fraction = met_window_days / event_span_days`.
- `precip_max_mean_ratio = regional daily precipitation maximum / regional daily precipitation mean`.
- `temp_peak_minus_mean_c = regional maximum-temperature maximum - regional maximum-temperature mean`.
- `span_score_0_4 = 4` if `event_span_years >= 15`, otherwise `0`.
- `weather_window_score_0_2 = 2` if `met_fraction <= 0.01`, otherwise `0`.
- `weather_contrast_score_0_1 = 1` if `precip_max_mean_ratio < 3` and `temp_peak_minus_mean_c < 6`, otherwise `0`.
- `scene_pair_score_0_3 = 3` if the pre-scene black-pixel percentage is at least `99` and exactly two formal scene-pair summaries have `no_sufficient_scenes` status, otherwise `0`.
- `KSCI = span_score_0_4 + weather_window_score_0_2 + weather_contrast_score_0_1 + scene_pair_score_0_3`.

For image checks, convert each preview image to RGB and use all pixels. A black pixel has `R <= 5`, `G <= 5`, and `B <= 5`; a bright pixel has `R >= 200`, `G >= 200`, and `B >= 200`. Report pixel percentages as `100 * matching_pixels / total_pixels`, rounded to four decimals.

Return one compact JSON object with exactly these fields:

```json
{
  "event_span": {"days": 0, "years": 0},
  "met_window": {"days": 0, "fraction": 0},
  "weather_contrast": {"precip_max_mean_ratio": 0, "temp_peak_minus_mean_c": 0},
  "image_checks": {"pre_black_pct": 0, "event_bright_pct": 0, "formal_no_scene_pairs": 0},
  "ksci_0_10": 0,
  "consistency_label": "",
  "computed_consequence": ""
}
```

Use `long_window_retreat_consistency_pass` only if KSCI is at least `9` and both the span and scene-pair gates pass. Keep `computed_consequence` to one short computed phrase.
