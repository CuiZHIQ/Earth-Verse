# Greece Wildfire Smoke-Response Process Model

Use the local CSX-188 event package to build a report-grounded disaster-science assessment of the 2023 Greece wildfire episode. Separate three linked processes:

1. fire-weather escalation described by the report;
2. long-range smoke transport over the Mediterranean;
3. emergency-response relevance from urban smoke, direct damage wording, fire clustering, and casualty signals.

Infer the inclusive event window from the event anchor. Compute:

- `window_days`;
- `image_day_offset_ratio`: inclusive day number of the reported August 22 satellite image divided by `window_days`;
- `forecast_day_offset_ratio`: inclusive day number of the reported August 23 extreme-fire-weather forecast divided by `window_days`.

Then compute:

```text
hot_dry_windy_fraction = present terms among hot, dry, and windy / 3

fire_weather_signal_index =
100 * (0.45 * hot_dry_windy_fraction
     + 0.25 * extreme_fire_weather_forecast
     + 0.15 * forecast_day_offset_ratio
     + 0.15 * burned_area_record_signal)
```

```text
smoke_transport_index =
100 * (0.40 * long_plume_signal
     + 0.25 * cross_mediterranean_signal
     + 0.20 * capital_city_smoke_signal
     + 0.15 * image_day_offset_ratio)
```

```text
response_impact_index =
100 * (0.35 * athens_damage_and_smoke_signal
     + 0.25 * casualty_signal
     + 0.20 * dozens_of_fires_signal
     + 0.20 * forecast_day_offset_ratio)
```

Finally compute:

```text
combined_response_priority =
0.45 * smoke_transport_index
+ 0.30 * response_impact_index
+ 0.25 * fire_weather_signal_index
```

Use `high_smoke_response_priority` if `combined_response_priority >= 85`, `moderate_smoke_response_priority` if it is at least 60, otherwise `low_smoke_response_priority`.

Set `direct_damage_reported` to true only if the local report explicitly says homes, cars, buildings, property, or critical facilities burned or were damaged.

Return one valid JSON object with exactly these top-level keys:

```json
{
  "answer_type": "greece_reported_wildfire_smoke_response_model",
  "window_days": 0,
  "stage_offsets": {"image_day_offset_ratio": 0.0, "forecast_day_offset_ratio": 0.0},
  "process_indices": {
    "fire_weather_signal_index": 0.0,
    "smoke_transport_index": 0.0,
    "response_impact_index": 0.0,
    "combined_response_priority": 0.0
  },
  "direct_damage_reported": false,
  "classification": {"response_priority_class": "", "dominant_process": ""},
  "formula_check": "pass_or_fail"
}
```

Round offset ratios to three decimals and index values to one decimal. Keep the response to the JSON object plus one short formula-check sentence.

## Reasoning-depth requirement

Add a top-level `reasoning_depth` object to the returned JSON with exactly these string fields:

```json
{
  "reasoning_depth": {
    "evidence_weighting": "<which evidence is decisive versus contextual>",
    "counterfactual_rejection": "<which tempting simpler explanation fails and why>",
    "uncertainty_or_scale_caveat": "<what the evidence should not be over-interpreted to prove>"
  }
}
```

For this task, use that object to make the Greece wildfire answer separate report-supported fire weather, smoke transport, and response impact stages.

