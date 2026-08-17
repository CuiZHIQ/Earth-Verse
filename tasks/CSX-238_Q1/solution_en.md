# Correct Answer

```json
{
  "target_family": "christchurch_liquefaction_weighted_seismic_score",
  "terms": [
    {"term": "S", "value": 0.988, "threshold_result": "pass"},
    {"term": "G", "value": 33.431, "threshold_result": "pass"},
    {"term": "G_norm", "value": 0.951, "threshold_result": "pass"},
    {"term": "I", "value": 1.0, "threshold_result": "pass"},
    {"term": "R", "value": 1.359, "threshold_result": "pass"}
  ],
  "score": 96.5,
  "final_label": "shallow_liquefaction_weighted_urban_seismic_record",
  "numeric_note": "All five threshold terms pass; score 96.5 is driven by shallow high-intensity shaking, liquefaction-dominant ground-failure ratios, high reported impacts, and low precipitation loading."
}
```

Core values: `S=0.988`, `G=33.431`, `G_norm=0.951`, `I=1.000`, and `R=1.359`. The ground-failure ratios are `25000/500 = 50.000` and `38.0/1.7 = 22.353`; their square-root product gives `G=33.431`. The five precipitation values average `3.594 mm`, giving `R=1.359`. The weighted score is `100*(0.35*S + 0.35*G_norm + 0.25*I + 0.05/R) = 96.5`.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the requested JSON shape with target family, five term rows, score, final label, and a compact numeric note.
- 4 points: Parses the required source values: M6.1, 5.9 km depth, MMI 8.808, CDI 8.5, felt 229, 25000 and 500 population-alert values, 38.0 and 1.7 hazard values, 181 deaths, 1500 injuries, 100000 buildings, and five precipitation values.
- 5 points: Computes `S=0.988`, `G=33.431`, `G_norm=0.951`, `I=1.000`, and `R=1.359` within tolerance.
- 4 points: Applies the weighted formula and reports `score=96.5` within `0.1`.
- 2 points: Computes each threshold result from its stated gate, marks all five terms as passing, and assigns `shallow_liquefaction_weighted_urban_seismic_record` only when score and all five gates pass.
- 2 points: Presents units, ratios, and rounding clearly enough for numeric checking.
