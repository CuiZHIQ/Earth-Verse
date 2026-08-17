# Tropical Cyclone Freddy Mozambique Phase Ledger

For Tropical Cyclone Freddy in February-March 2023, a reviewer argues that the Mozambique phase can be reduced to the weaker first Mozambique landfall. Build a numeric ledger that tests that statement against the full phase record.

Using the event record and quantitative diagnostics, calculate:

- Convert the Madagascar landfall wind from km/h to mph, rounded to one decimal.
- `first_moz_vs_madagascar = first Mozambique landfall mph / converted Madagascar mph`.
- `mozambique_rebound = second Mozambique landfall mph / first Mozambique landfall mph`.
- For each of the two accumulated-rainfall summaries, compute `peak_to_mean = max_mm / mean_mm`; then set `rain_concentration` to the average of those two ratios.
- `duration_fraction = tropical-storm-or-higher duration days / inclusive event-period days`.
- `persistence_index = mozambique_rebound * rain_concentration * duration_fraction / first_moz_vs_madagascar`.

Also count how many of these five tests are true: `first_moz_vs_madagascar < 0.70`, `mozambique_rebound >= 1.75`, both rainfall means are at least 100 mm, both rainfall peaks are at least 300 mm, and `duration_fraction >= 0.90`.

Return JSON only:

```json
{
  "answer": 0.0,
  "pass_count": 0,
  "components": {
    "first_moz_vs_madagascar": 0.0,
    "mozambique_rebound": 0.0,
    "rain_concentration": 0.0,
    "duration_fraction": 0.0
  }
}
```
