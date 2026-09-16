# Correct Answer

`long_window_retreat_consistency_pass`

```json
{
  "event_span": {"days": 7305, "years": 20.0},
  "met_window": {"days": 46, "fraction": 0.006297},
  "weather_contrast": {"precip_max_mean_ratio": 2.8095, "temp_peak_minus_mean_c": 5.2011},
  "image_checks": {"pre_black_pct": 100.0, "event_bright_pct": 82.6421, "formal_no_scene_pairs": 2},
  "ksci_0_10": 10,
  "consistency_label": "long_window_retreat_consistency_pass",
  "computed_consequence": "short_weather_single_scene_counterweights_fail"
}
```

# Computation Path

The event span is `2020-02-21 - 2000-02-21 = 7305` days. Dividing by `365.25` gives `20.0` years. The regional hourly-summary window runs from `2000-02-21` through `2000-04-06`, so its inclusive length is `46` days and `met_fraction = 46 / 7305 = 0.006297`.

For the regional daily precipitation summary, `precip_max_mean_ratio = 559.2912 / 199.0733 = 2.8095`. For the regional maximum-temperature summary, `temp_peak_minus_mean_c = 36.8061 - 31.6050 = 5.2011 C`.

The image check converts each preview to RGB and uses all pixels. A black pixel has all three channels `<= 5`; a bright pixel has all three channels `>= 200`. The pre-scene is `100.0` percent black by that rule, while the event-scene bright-pixel share is `82.6421` percent. The radar and optical scene-pair summaries both report `no_sufficient_scenes`, so `formal_no_scene_pairs = 2`.

The gates are therefore `span_score_0_4 = 4`, `weather_window_score_0_2 = 2`, `weather_contrast_score_0_1 = 1`, and `scene_pair_score_0_3 = 3`. Thus `KSCI = 4 + 2 + 1 + 3 = 10`. Since KSCI is at least `9` and the span and scene-pair gates pass, the final label is `long_window_retreat_consistency_pass`.

# Scoring Rubric

- 3 points: Returns the requested compact JSON fields with numeric values in the expected units and the final label. Partial credit: 1-2 points if the JSON is parseable but omits one or two requested fields.
- 4 points: Computes `7305` span days, `20.0` span years, `46` regional-summary days, and `0.006297` window fraction. Partial credit: 1 point each for span days, span years, regional-summary days, and fraction.
- 4 points: Computes precipitation max/mean ratio as `2.8095` and maximum-temperature contrast as `5.2011 C`. Partial credit: 2 points for each correct contrast value within tolerance.
- 4 points: Uses the stated RGB pixel thresholds to report `100.0` percent pre-scene black pixels, `82.6421` percent event-scene bright pixels, and two `no_sufficient_scenes` statuses. Partial credit: 1 point for pre-scene black percent, 1 point for event-scene bright percent, and 2 points for the two scene-pair statuses.
- 3 points: Applies all four gates, computes KSCI as `10`, and returns `long_window_retreat_consistency_pass`. Partial credit: 1 point for gates, 1 point for KSCI, and 1 point for the label.
- 1 point: Keeps the consequence short and tied to the computed gates. Partial credit: 0.5 points for a consequence that is directionally correct but too verbose.
- 1 point: Does not convert single-scene brightness or mapped counts into measured area or affected-population totals.
