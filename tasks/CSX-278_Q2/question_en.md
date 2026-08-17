# Horn of Africa ENSO Coupling Ledger

For the 2020-09-01 through 2023-03-31 Horn of Africa event, compute a numeric ENSO coupling ledger from the local package data.

Use these definitions:

- `cold_oni_month`: ONI <= -0.5.
- `positive_soi_month`: SOI > 0.
- `coupled_month`: both conditions in the same month.
- `strong_coupled_month`: ONI <= -0.8 and SOI >= 0.7.
- `coupled_persistence_score = coupled_months / event_months`.
- `short_slice_fraction = days_in_short_precipitation_slice / days_in_event_window`, using inclusive dates.
- `people_ratio_min = 20000000 / compact_aoi_population`.

Classify the event as `sustained_coupled_event` when `coupled_persistence_score >= 0.75`; otherwise use `mixed_event`.

Return compact JSON:

```json
{
  "answer": {
    "event_months": 0,
    "cold_oni_months": 0,
    "positive_soi_months": 0,
    "coupled_months": 0,
    "strong_coupled_months": 0,
    "coupled_persistence_score": 0.0,
    "short_slice_fraction": 0.0,
    "people_ratio_min": 0.0
  },
  "classification": "<label>",
  "calculation_note": "<one sentence with the formulas used>"
}
```
