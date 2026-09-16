# Sao Sebastiao Rainfall Threshold Ledger

A hydrometeorology reviewer is checking whether the February 2023 Sao Sebastiao, Brazil floods and landslides meet a conservative rainfall-saturation ledger for a combined slope-failure and flash-flood diagnosis. Use the reported storm facts and event timing to compute the ledger. Treat the documented one-day rainfall amount as a lower-bound storm load, not as an exact event total.

Return only JSON in this shape:

```json
{
  "answer": "<final_state>",
  "rainfall_mm_lower_bound": <integer>,
  "event_window_days": <integer>,
  "window_mean_lower_bound_mm_per_day": <number>,
  "rainfall_threshold_multiple": <number>,
  "post_image_lag_days": <integer>,
  "pass_count": <integer>,
  "interpretation": "<one sentence>"
}
```

Decision checks:

- extreme rain: rainfall lower bound >= 500 mm;
- compact event window: inclusive event-window duration <= 4 days;
- high lower-bound window mean: rainfall lower bound / event-window days >= 100 mm/day;
- timely aftermath image: post-storm image lag from the February 19 rainfall trigger <= 10 days.

Set `answer` to `compound_rainfall_saturation_pass` only if all four checks pass; otherwise set it to `ledger_not_fully_met`.
