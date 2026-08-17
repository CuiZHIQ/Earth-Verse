# Storm Alexa Phase-Split Mechanism Competition

You are a winter-storm mechanism reviewer comparing competing explanations for the December 10-13, 2013 Middle East winter storm Alexa. The candidate mechanisms are:

- highland-snow branch;
- coastal heavy-rain branch;
- single hard-freeze snowfall event;
- local point windy-snow interpretation.

Use only the local CSX-038 event package. Select package-relative evidence for report snow anchors, point-weather snow and wind, hard-freeze checks, and precipitation-product context.

Compute the same support values for all candidates:

- `report_snow_score_0to3`: add 1 if Jerusalem reported at least 30 cm snow, add 1 if Amman reported at least 30 cm snow, and add 1 if the report says snow was mainly higher-elevation with mountain-road closure.
- `point_windy_snow_score_0to3`: add 1 if point snowfall total is greater than 0 cm, add 1 if snowfall occurs in at least 12 hourly records, and add 1 if maximum wind gust is at least 60 km/h.
- `hard_freeze_score_0to2`: add 1 if there are at least 24 hourly records at or below 0 C, and add 1 if at least one daily minimum is at or below 0 C.
- `rain_branch_score_0to3`: add 1 if the report gives Gaza flood displacement of at least 40000 people, add 1 if it says lower coastal elevations received torrential rain, and add 1 if any precipitation product has an event maximum of at least 20 mm.
- `jerusalem_point_snow_ratio_min = Jerusalem reported lower-bound snow cm / point snowfall total cm`
- `amman_point_snow_ratio = Amman reported snow cm / point snowfall total cm`
- `precip_max_spread_mm = max(product event precipitation maxima) - min(product event precipitation maxima)`

Return only compact JSON:

```json
{
  "answer": "",
  "mechanism_competition": [
    {"mechanism": "highland_snow_branch", "support_score": 0, "supporting_values": {}, "counter_evidence": ""},
    {"mechanism": "coastal_heavy_rain_branch", "support_score": 0, "supporting_values": {}, "counter_evidence": ""},
    {"mechanism": "single_hard_freeze_snowfall", "support_score": 0, "supporting_values": {}, "counter_evidence": ""},
    {"mechanism": "local_point_windy_snow", "support_score": 0, "supporting_values": {}, "counter_evidence": ""}
  ],
  "report_snow_score_0to3": 0,
  "point_windy_snow_score_0to3": 0,
  "hard_freeze_score_0to2": 0,
  "rain_branch_score_0to3": 0,
  "jerusalem_point_snow_ratio_min": 0.0,
  "amman_point_snow_ratio": 0.0,
  "precip_max_spread_mm": 0.0,
  "interpretation": "<one sentence>"
}
```

Use `phase_split_consistent` only when the highland-snow branch and coastal-rain branch are both supported while the single hard-freeze snowfall mechanism fails.
