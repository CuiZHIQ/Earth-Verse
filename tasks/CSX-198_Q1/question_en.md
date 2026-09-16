# Caldor Fire Threshold Score Ledger

A technical review team is checking a compact numeric ledger for the 2021 Caldor Fire near South Lake Tahoe. Compute the requested window, precipitation, burn-index, and annual embedding-change diagnostics, then apply the stated threshold tests.

Rules:

- `event_span_days` is the official active duration.
- `large_long_fire` earns one score point only when the incident record jointly supports at least 200,000 burned acres, at least 60 active days, and at least 1,000 structures destroyed.
- `progression_days` is the inclusive length of the dated spread record, and `progression_share` is `progression_days / event_span_days`.
- `precip_mean_mm` is the mean of the three event-accumulated precipitation means; `precip_range_mm` is their maximum minus minimum; `precip_window_share` is the precipitation-window length divided by `event_span_days`.
- `areawide_high` is true only when `mean_dnbr > 0.2` and `max_dnbr >= 0.7`.
- `concentration_ratio` is `embedding_change_max / embedding_change_mean`, and `localized_change` is true only when `embedding_change_mean < 0.05`, `embedding_change_max >= 0.5`, and `concentration_ratio >= 20`.
- `final_score` is out of five: one point each for a large long-duration fire, a spread record at least 50 days long with 12-hour steps and at least 75% active-span coverage, precipitation summaries covering under 75% of the active duration, no areawide high dNBR result, and a localized annual embedding-change signal.

Return only compact JSON in this shape:

```json
{
  "event_span_days": 0,
  "progression_days": 0,
  "progression_share": 0.0,
  "precip_mean_mm": 0.0,
  "precip_range_mm": 0.0,
  "precip_window_share": 0.0,
  "dnbr": {
    "mean": 0.0,
    "max": 0.0,
    "areawide_high": false
  },
  "embedding_change": {
    "mean": 0.0,
    "max": 0.0,
    "concentration_ratio": 0.0,
    "localized_change": false
  },
  "final_score": "0/5"
}
```
