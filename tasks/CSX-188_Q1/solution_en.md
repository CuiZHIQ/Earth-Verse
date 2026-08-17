# Final Answer

```json
{
  "answer_type": "greece_reported_wildfire_smoke_response_model",
  "window_days": 62,
  "stage_offsets": {
    "image_day_offset_ratio": 0.855,
    "forecast_day_offset_ratio": 0.871
  },
  "process_indices": {
    "fire_weather_signal_index": 98.1,
    "smoke_transport_index": 97.8,
    "response_impact_index": 97.4,
    "combined_response_priority": 97.8
  },
  "direct_damage_reported": true,
  "classification": {
    "response_priority_class": "high_smoke_response_priority",
    "dominant_process": "long_range_smoke_transport_with_urban_damage_context"
  },
  "formula_check": "pass"
}
```

The formula check is `pass`: the indices reproduce from the report-supported signals, and the report explicitly says fires near Athens burned homes and cars.

# Key Computations

The event window is 2023-07-01 through 2023-08-31, giving `window_days = 62`.

The VIIRS image date is 2023-08-22:

`image_day_offset_ratio = 53 / 62 = 0.855`

The extreme-fire-weather forecast date is 2023-08-23:

`forecast_day_offset_ratio = 54 / 62 = 0.871`

Fire-weather signal:

- hot/dry/windy terms are all present, so `hot_dry_windy_fraction = 1`
- extreme fire-weather forecast is present
- burned-area record signal is present
- `fire_weather_signal_index = 100 * (0.45 * 1 + 0.25 * 1 + 0.15 * 0.871 + 0.15 * 1) = 98.1`

Smoke-transport signal:

- long smoke plume is present
- cross-Mediterranean smoke is present
- capital-city smoke is present
- `smoke_transport_index = 100 * (0.40 + 0.25 + 0.20 + 0.15 * 0.855) = 97.8`

Response-impact signal:

- the report says fires near Athens burned homes and cars and sent smoke over the capital
- the report references 18 bodies found during the wildfire response
- dozens more fires ignited within 24 hours
- `response_impact_index = 100 * (0.35 + 0.25 + 0.20 + 0.20 * 0.871) = 97.4`

Combined response priority:

`0.45 * 97.8 + 0.30 * 97.4 + 0.25 * 98.1 = 97.8`

# Reasoning Path

The report supports a high smoke-response priority because the smoke plume was long-range, crossed the Mediterranean, and affected the capital-city context while fires near Athens caused direct damage to homes and cars. The formula uses only report-supported signals and event-anchor timing, so the classification is `high_smoke_response_priority`.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "counterfactual_rejection": "A generic burn-scar or local-weather-index answer fails because the report directly supports smoke transport, Athens damage, fire clustering, and casualty signals.",
    "evidence_weighting": "NASA report text and event-anchor timing are decisive; off-event AOI weather, dNBR, gridded precipitation, and exposure products are not used in the scoring path.",
    "uncertainty_or_scale_caveat": "The formula summarizes reported process signals and should not be used as an exact burned-area, casualty, or air-quality measurement."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

Total: 20 points.

- 3 points: Computes the July 1-August 31 event window as 62 days, image offset ratio `0.855`, and forecast offset ratio `0.871`.
- 4 points: Finds hot/dry/windy, extreme fire-weather forecast, and burned-area record signals, and computes `fire_weather_signal_index = 98.1`.
- 4 points: Finds the long plume, cross-Mediterranean smoke, capital-city smoke, and image-stage offset, and computes `smoke_transport_index = 97.8`.
- 3 points: Finds Athens homes/cars plus smoke, casualty signal, dozens of fires within 24 hours, and forecast offset, and computes `response_impact_index = 97.4`.
- 3 points: Reports `direct_damage_reported = true`, `combined_response_priority = 97.8`, and `high_smoke_response_priority`.
- 2 points: Bases the assessment on report-supported signals and does not use off-event AOI weather, dNBR, image-change, or gridded precipitation values.
- 1 point: Returns the requested compact JSON plus a short formula-check sentence.
