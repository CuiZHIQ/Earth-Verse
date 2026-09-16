# Final Answer

```json
{
  "target_family": "mocoa_rain_window_runout_score_ledger",
  "metrics": {
    "window_days": 2,
    "local_two_day_mm": 61.7,
    "local_min_day_mm": 30.1,
    "local_day_max_to_min": 1.05,
    "grid_peak_mm": 51.711,
    "grid_peak_to_mean": 35.614,
    "report_markers": 4,
    "population_k": 38.608,
    "radar_total_images": 72
  },
  "gates": {
    "window_gate": true,
    "daily_distribution_gate": true,
    "grid_peak_gate": true,
    "report_chain_gate": true,
    "population_gate": true,
    "radar_context_gate": true
  },
  "source_comparison": {
    "local_series_two_day_mm": 61.7,
    "point_sample_two_day_mm": 36.51,
    "point_sample_min_day_mm": 4.28,
    "point_to_local_two_day_ratio": 0.592,
    "rainfall_gate_source_policy": "local_daily_series_controls_window_and_daily_distribution_gates",
    "source_conflict_flag": "independent_point_sample_reported_but_not_substituted_into_local_gates"
  },
  "chain_score": 6,
  "final_label": "mocoa_rain_window_runout_chain_confirmed",
  "computed_consequence": "six_passes_require_rain_window_grid_peak_report_markers_population_and_radar_context"
}
```

# Key Computations

The locked date window runs from 2017-03-31 through 2017-04-01, so the inclusive length is `2` days.

Local daily rainfall is 30.1 mm and 31.6 mm. The two-day total is `30.1 + 31.6 = 61.7 mm`, the minimum daily value is `30.1 mm`, and the day-balance ratio is `31.6 / 30.1 = 1.050`.

The independent point rainfall sample is 32.23 mm and 4.28 mm, for a two-day total of `36.51 mm`, a minimum day of `4.28 mm`, and a point-to-local total ratio of `36.51 / 61.7 = 0.592`. This point sample is reported as a source-comparison diagnostic and is not substituted into the local rain-window gates.

The gridded event maximum used for the peak test is 51.711 mm, with a mean of 1.452 mm. The peak-to-mean ratio is `51.711 / 1.452 = 35.614`, so the gridded peak test passes.

The four report markers are present: heavy rain trigger, mountain movement, mud across the city, and nearby river crossing. The marker count is therefore `4`.

The exposed population is 38,608.2819 people, so `population_k = 38.608`. The radar image count is `40 + 32 = 72`.

# Reasoning Path

The score is built from six independent gates. The window gate passes because the event window is exactly two days and the local two-day rainfall exceeds 60 mm. The daily-distribution gate passes because both local daily values are at least 30 mm and the maximum-to-minimum ratio is only 1.050. The separate point sample shows a lower and more uneven two-day value, so it is disclosed as a source comparison rather than silently changing the gate source.

The gridded peak gate passes because the event-window peak is above 50 mm and the peak-to-mean ratio is far above 20. The report-chain gate passes because all four fixed report markers are found. The population gate passes because the population value exceeds 25 thousand. The radar-context gate passes because the paired pre/post radar count totals 72 images.

All six gates pass, so `chain_score = 6`. Since the score is at least 5 and `report_chain_gate` is true, the deterministic label is `mocoa_rain_window_runout_chain_confirmed`.

# Computed Interpretation

The ledger is a numeric consistency test. It confirms that the Mocoa record joins a two-day rainfall window, a high gridded peak contrast, four report markers, a population threshold, and enough radar observations into one six-pass result.

The calculation does not hide the rainfall-source disagreement or depend on imagery alone. The final label follows from the declared local-series gate policy, fixed formulas, and thresholds, with the report markers acting as a required bridge between the rainfall window and the runout wording.

# Scoring Rubric

- 3 points: Requested JSON form. Full credit for compact JSON with `target_family`, `metrics`, `gates`, `chain_score`, `final_label`, and `computed_consequence`. Partial credit for minor key-name differences when all scored content is recoverable.
- 4 points: Window and local rainfall arithmetic. Full credit for `window_days = 2`, `local_two_day_mm = 61.7`, `local_min_day_mm = 30.1`, `local_day_max_to_min = 1.05`, and keeping the local daily series as the rain-window gate source. Partial credit for correct formulas with one rounding or date-window error.
- 3 points: Gridded rainfall proof and source comparison. Full credit for `grid_peak_mm = 51.711`, `grid_peak_to_mean = 35.614`, a passing grid peak gate, and reporting the independent point sample as a diagnostic rather than substituting it into the local gates. Partial credit for one correct value or for the right gate state with incomplete arithmetic.
- 3 points: Report marker count. Full credit for counting all four fixed markers and passing `report_chain_gate`. Partial credit for three markers or for a correct count with unclear marker naming.
- 2 points: Population and radar metrics. Full credit for `population_k = 38.608`, `radar_total_images = 72`, and both gates passing. Partial credit for one correct metric and its gate.
- 3 points: Gate score and final label. Full credit for six passed gates, `chain_score = 6`, and `mocoa_rain_window_runout_chain_confirmed`. Partial credit for the right label with one gate error, or the right score with a missing label.
- 2 points: Compact bounded computation. Full credit for keeping the result tied to formulas and thresholds without adding loss inventories or field actions. Partial credit for small extra prose that leaves the computed result unchanged.
