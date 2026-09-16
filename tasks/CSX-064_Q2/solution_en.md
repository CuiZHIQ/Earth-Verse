# Correct Answer

```json
{
  "answer": "weaker_three_product_rainfall_load",
  "target_family": "monsoon_flood_scenario_sensitivity_ranking",
  "computed_values": {
    "days": 31,
    "mean_mm": 301.068,
    "min_mean_mm": 279.79,
    "spread_ratio": 0.165,
    "gpm_chirps": 1.12,
    "max_mean": 1.63,
    "anchors": "7/7",
    "wind_max": 2.49
  },
  "scenario_scores": {
    "weaker_three_product_rainfall_load": 89.353,
    "loss_of_product_coherence": 88.393,
    "report_anchor_dropout": 85.714,
    "peak_burst_reinterpretation": 77.301,
    "shortened_monsoon_window": 64.516,
    "wind_led_reinterpretation": 0.0
  },
  "ranked_scenarios": [
    "weaker_three_product_rainfall_load",
    "loss_of_product_coherence",
    "report_anchor_dropout",
    "peak_burst_reinterpretation",
    "shortened_monsoon_window",
    "wind_led_reinterpretation"
  ],
  "top_sensitivity": {
    "scenario": "weaker_three_product_rainfall_load",
    "why": "10.6% rainfall weakening drops the lowest product below 250 mm"
  },
  "rejected_sensitivity": {
    "scenario": "wind_led_reinterpretation",
    "why": "2.49 m/s wind proxy needs a 301.6% increase to reach 10 m/s"
  },
  "evidence_paths": {
    "event_window": [
      "data/event_reports/event_reports_003_Locked_event_anchor_2020_South_and_East_Asia_monsoon_floods.json"
    ],
    "report_anchors": [
      "data/event_reports/event_reports_004_01_Locked_package_evidence_report.html.html"
    ],
    "precipitation_products": [
      "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
      "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
      "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json"
    ],
    "wind_proxy": [
      "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json"
    ]
  },
  "reasoning_path": [
    "compute baseline hazard and report margins",
    "convert each scenario to threshold-crossing change",
    "rank higher scores as smaller changes"
  ]
}
```

# Key Computations

The event window is inclusive from 2020-07-01 through 2020-07-31, so `duration_days = 31`.

Precipitation means are ERA5-Land `279.790 mm`, GPM `329.374 mm`, and CHIRPS `294.040 mm`. Therefore:

- `three_product_mean_mm = 301.068`
- `min_product_mean_mm = 279.790`
- `event_mean_daily_rate_mm_per_day = 301.068 / 31 = 9.712`
- `mean_spread_mm = 329.374 - 279.790 = 49.584`
- `spread_to_mean_ratio = 49.584 / 301.068 = 0.165`
- `gpm_to_chirps_mean_ratio = 329.374 / 294.040 = 1.12`

Product maxima are ERA5-Land `491.133 mm`, GPM `466.113 mm`, and CHIRPS `382.717 mm`, so the largest maximum is `491.133 mm` and `max_to_mean_ratio = 491.133 / 301.068 = 1.63`.

All seven report anchors are present, including the Poyang Lake level of `22.6 m` on `2020-07-13`. The wind proxies are:

- `max_wind_speed_proxy_m_per_s = sqrt(1.995^2 + 1.482^2) = 2.49`
- `mean_wind_speed_proxy_m_per_s = sqrt(1.229^2 + 0.895^2) = 1.52`

# Ranking Logic

The ranking uses `score = max(0, 100 * (1 - fractional_change_needed))`.

- `weaker_three_product_rainfall_load`: `1 - 250 / 279.790 = 0.106`, score `89.353`.
- `loss_of_product_coherence`: nearest failure is the GPM-to-CHIRPS ratio reaching `1.25`, so `1.25 / 1.12 - 1 = 0.116`, score `88.393`. The spread-ratio route needs a larger `0.212` change.
- `report_anchor_dropout`: losing one of seven anchors gives `1 / 7 = 0.143`, score `85.714`.
- `peak_burst_reinterpretation`: `2.0 / 1.63 - 1 = 0.227`, score `77.301`.
- `shortened_monsoon_window`: reducing a 31-day event to the first below-21-day duration removes `11` days, so `11 / 31 = 0.355`, score `64.516`.
- `wind_led_reinterpretation`: `10 / 2.49 - 1 = 3.016`, clipped to score `0.000`.

# Reasoning Path

The most sensitive diagnosis-changing perturbation is weaker three-product rainfall load because the lowest precipitation product is only about `10.6%` above the `250 mm` product threshold. Product coherence is nearly as sensitive, but it changes confidence across products rather than directly removing the sustained-rainfall load. Report-anchor dropout is third because one missing anchor breaks the complete routed-flooding report set. Peak-burst and shortened-window alternatives require larger perturbations. The wind-led reinterpretation remains rejected because the wind proxy is far below the `10 m/s` threshold.

# Scoring Rubric

- 3 points: Final ranking JSON. Full credit requires the requested compact JSON fields including `evidence_paths`, `weaker_three_product_rainfall_load` as the top sensitivity, and all six ranked scenarios. Partial credit: 1-2 points if the structure is mostly present but the top scenario or one required ranking field is missing.
- 4 points: Baseline rainfall calculations. Full credit requires 31 days, product means of `279.790`, `329.374`, and `294.040 mm`, the `301.068 mm` mean, `9.712 mm/day`, and the `279.790 mm` minimum product mean. Partial credit: 2-3 points for mostly correct rainfall arithmetic with minor rounding errors; 1 point if only one precipitation product is used.
- 3 points: Coherence and peak margins. Full credit requires the `49.584 mm` spread, `0.165` spread-to-mean ratio, `1.12` GPM-to-CHIRPS ratio, `491.133 mm` maximum, and `1.63` max-to-mean ratio. Partial credit: 1-2 points if either the coherence or peak calculations are correct but the other family is missing or not tied to thresholds.
- 3 points: Report and wind evidence. Full credit requires all seven report anchors, Poyang Lake at `22.6 m` on `2020-07-13`, and wind proxies of `2.49 m/s` maximum and `1.52 m/s` mean. Partial credit: 1-2 points if either the report anchors or the wind proxy is correct but not both.
- 4 points: Scenario sensitivity scoring. Full credit requires the threshold-crossing formula and scores `89.353`, `88.393`, `85.714`, `77.301`, `64.516`, and `0.000` for the six candidate perturbations. Partial credit: 2-3 points if the formula is right but one or two scores are rounded incorrectly; 1 point for a qualitative ranking without reproducible margins.
- 3 points: Interpretation and rejected alternative. Full credit explains that rainfall-load weakening is most sensitive, while wind-led reinterpretation is rejected because it needs a roughly `301.6%` proxy increase. Partial credit: 1-2 points if the interpretation is broadly consistent but omits either the top-sensitivity margin or the wind-led rejection margin.
