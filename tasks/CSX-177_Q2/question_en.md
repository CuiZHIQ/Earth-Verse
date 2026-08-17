# Uljin-Samcheok Wildfire Mechanism Competition

You are a wildfire-process analyst comparing two competing mechanisms for the March 4-13, 2022 Uljin-Samcheok wildfire sequence in South Korea:

- early dry-wind spread controlled the fire and smoke-spread signal;
- later wind slackening and foggy conditions controlled the event-window diagnosis.

Use the local event package to extract the report anchors, event timing, early active-fire interval, and reported burned area. Build a quantitative mechanism competition using these definitions:

```text
early_spread_score = A * (E / N) * Hkha
late_moderation_score = M * ((N - E) / N) * 5 * C
```

where:

- `A` is the number of early spread anchors present among dry weather, strong winds, and westerly smoke transport toward southern Japan.
- `E` is the inclusive number of days from the event-window start through the report date when satellites still detected fire activity after winds slackened.
- `N` is the inclusive number of event-window days.
- `Hkha` is the reported charred area in thousand hectares.
- `M` is the number of late moderation anchors present among smoke thinning, winds slackening, and foggy weather.
- `C` is `0.5` when the same late passage says satellites continued to detect fire activity, otherwise `1.0`.

Return concise JSON:

```json
{
  "formula": "<mechanism score formulas>",
  "mechanism_competition": [
    {"mechanism": "early_dry_wind_fire_spread", "supporting_values": {}, "status": ""},
    {"mechanism": "late_wind_slackening_fog_moderation", "supporting_values": {}, "status": ""}
  ],
  "phase_scores": {"early_spread_score": 0.0, "late_moderation_score": 0.0, "early_late_ratio": 0.0},
  "top_evidence_stage": "",
  "first_moderation_day": "",
  "diagnosis": "",
  "computed_consequence": "<one sentence>"
}
```

Use `early_dry_wind_spread_dominant` only when the early score is higher than the late moderation score, the early/late ratio is at least 1.5, and the report still detects fire activity on the first moderation day.
