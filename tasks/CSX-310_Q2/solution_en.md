# Correct Answer

```json
{
  "target_family": "hunga_tonga_surface_change_weather_null_consistency",
  "metrics": {
    "s1_abs_change_db": 13.2633,
    "s1_signal_to_std": 16.243,
    "optical_peak_to_mean": 21.1138,
    "event_precip_max_mm": 0.005,
    "coverage_balance": 0.8889,
    "event_anchor_score": 2
  },
  "gates": {
    "all_weather_gate": true,
    "optical_support_gate": true,
    "weather_null_gate": true,
    "event_anchor_gate": true
  },
  "final_label": "event_window_surface_change_weather_null_pass",
  "computed_consequence": "weather_variability_rejected_by_precip_gate"
}
```

# Computation Path

The all-weather VV extrema are -11.0084 dB and 13.2633 dB, so `max(abs(min), abs(max)) = 13.2633 dB`. Dividing by the VV change standard deviation gives `13.2633 / 0.8166 = 16.243`. The pre/post counts are 18 and 16, so the coverage balance is `16 / 18 = 0.8889`.

The optical peak-to-mean ratio is `0.7742 / 0.0367 = 21.1138`. The event-day precipitation guardrail uses the larger of the gridded and reanalysis precipitation maxima: `max(0.0050, 0.0000) = 0.005 mm`. The event anchor score is `I(3.0 >= 3.0) + I(50.0 >= 40.0) = 2`.

All four gates pass: all-weather change is above 10 dB and 10 standard deviations, optical contrast is above both thresholds, event-day precipitation is below 1 mm, and the two-part event anchor is complete. The compact consequence is therefore a surface-change pass with the weather-variability explanation rejected by the precipitation guardrail.

# Scoring Rubric

- 4 points: Returns compact JSON with `target_family`, `metrics`, `gates`, `final_label`, and `computed_consequence`.
- 5 points: Computes the numeric anchors correctly: 13.2633 dB, 16.243, 21.1138, 0.005 mm, 0.8889, and event anchor score 2.
- 4 points: Applies the four threshold gates correctly and reports `event_window_surface_change_weather_null_pass`.
- 3 points: Shows the component formulas for the max-absolute value, ratio, precipitation maximum, coverage balance, and indicator score.
- 2 points: Derives the weather-variability rejection from `event_precip_max_mm < 1.0` together with passing surface-change gates.
- 1 point: Keeps the event-process consequence short and tied to the computed gates.
- 1 point: Avoids overreach such as treating plume height alone, exposure context, or a single image metric as confirmed loss accounting.
