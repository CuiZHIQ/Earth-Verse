# Final Answer

```json
{
  "event_span_days": 68,
  "progression_days": 53,
  "progression_share": 0.779,
  "precip_mean_mm": 436.451,
  "precip_range_mm": 154.859,
  "precip_window_share": 0.676,
  "dnbr": {
    "mean": -0.074973,
    "max": 0.696927,
    "areawide_high": false
  },
  "embedding_change": {
    "mean": 0.019309,
    "max": 0.502403,
    "concentration_ratio": 26.019,
    "localized_change": true
  },
  "final_score": "5/5"
}
```

# Key Computations

The incident record gives 221,835 acres, 68 active days, and 1,005 structures destroyed. The large long-duration test is therefore true under the `acres >= 200000`, `active_days >= 60`, and `structures_destroyed >= 1000` thresholds.

The dated spread record runs from August 15 through October 6, 2021. Inclusive length is `(2021-10-06 - 2021-08-15) + 1 = 53` days. The active-span share is `53 / 68 = 0.779`, and the stated update interval is 12 hours.

The three event-accumulated precipitation means are 499.579 mm, 344.720 mm, and 465.054 mm. Their mean is `436.451` mm and their range is `154.859` mm. The precipitation summaries span August 14 through September 28, 2021, or 46 inclusive days, so `46 / 68 = 0.676`.

The dNBR summary has mean `-0.074973` and maximum `0.696927`. The areawide-high rule requires both `mean_dnbr > 0.2` and `max_dnbr >= 0.7`; the pair is not satisfied, so `areawide_high` is false.

The annual embedding-change summary has mean `0.019309` and maximum `0.502403`. The concentration ratio is `0.502403 / 0.019309 = 26.019`, so `localized_change` is true under the three-part rule.

# Reasoning Path

The ledger awards one point for each threshold test. The incident scale test passes because all three size and duration anchors meet their thresholds. The spread record test passes because it is at least 50 days long, uses 12-hour steps, and covers at least 75% of the 68-day active span. The precipitation test passes because its window share is below 0.75, marking it as a shorter-window hydrometeorological context diagnostic.

The burn-index test is scored as a negative threshold: the ledger asks for no areawide high dNBR result, and the dNBR mean and maximum do not jointly meet the high rule. The embedding-change test passes because the mean is low while the maximum is just above 0.5 and the max-to-mean ratio exceeds 20. All five tests pass, so `final_score` is `5/5`.

# Computed Interpretation

The computed answer is a threshold score ledger: the Caldor Fire record passes the duration, spread-window, shorter precipitation-window, low areawide dNBR, and localized embedding-change tests, giving a compact score of `5/5`.

# Scoring Rubric

Award up to 20 points:

- 3 points for returning the requested JSON structure with all numeric and boolean fields present; partial credit for minor nesting or naming mistakes that do not hide the values.
- 3 points for the incident span and scale test: 68 active days, 221,835 acres, 1,005 structures destroyed, and a true large long-duration result; partial credit for using the duration without both size anchors.
- 3 points for the spread-window reconstruction: August 15 to October 6 inclusive, 53 days, 12-hour steps, and progression share 0.779; partial credit for correct dates with one arithmetic or rounding error.
- 3 points for the precipitation ledger: three-product mean 436.451 mm, range 154.859 mm, 46-day window, and window share 0.676; partial credit for correct precipitation means without the window-share test.
- 3 points for the dNBR threshold logic: mean -0.074973, maximum 0.696927, and `areawide_high = false` under the stated thresholds; partial credit for the false result without both numeric dNBR anchors.
- 3 points for the embedding-change calculation: mean 0.019309, maximum 0.502403, concentration ratio 26.019, and `localized_change = true`; partial credit for the correct boolean result with one missing component value.
- 2 points for the final `5/5` score and a concise reading tied to the five stated tests; partial credit for a correct score with one weak component explanation.
