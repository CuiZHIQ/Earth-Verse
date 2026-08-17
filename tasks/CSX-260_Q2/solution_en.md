# Correct Answer

```json
{
  "ledger_values": {
    "window_days": 6,
    "point_total_mean_mm": 22.6,
    "point_peak_share_mean": 0.582,
    "grid_mean_mm": 33.7,
    "grid_spread_ratio": 2.136,
    "gdacs_flood_alerts": 2,
    "worldpop_millions": 1.025,
    "remote_context_index": 0.134,
    "pass_count": 7
  },
  "gates": {
    "window_6d": true,
    "point_total_ge_20mm": true,
    "point_peak_share_ge_0_55": true,
    "grid_mean_ge_30mm": true,
    "gdacs_alerts_ge_2": true,
    "population_ge_1m": true,
    "remote_context_lt_0_20": true
  },
  "label": "rainfall_flood_window_consistent"
}
```

# Reproducible Computation Notes

The event anchor gives an inclusive window from 2021-07-12 through 2021-07-17, so `window_days = 6`.

For the point precipitation series, the Open-Meteo event-window values sum to 20.20 mm with a 10.10 mm peak, giving a peak share of 0.500. The NASA POWER event-window values sum to 24.96 mm with a 16.55 mm peak, giving a peak share of 0.663. Therefore:

```text
point_total_mean_mm = (20.20 + 24.96) / 2 = 22.6
point_peak_share_mean = (0.500 + 0.663) / 2 = 0.582
```

The gridded event-precipitation means are 45.919 mm from ERA5-Land and 21.499 mm from GPM IMERG:

```text
grid_mean_mm = (45.919 + 21.499) / 2 = 33.7
grid_spread_ratio = 45.919 / 21.499 = 2.136
```

The event catalog contains two overlapping Germany or Belgium flood-alert records, both within the 2021-07-12 to 2021-07-17 window. WorldPop reports a population sum of 1,025,288.541, so `worldpop_millions = 1.025`.

The remote-change countercheck uses Sentinel-2 dNBR mean 0.158 and annual embedding 1-minus-cosine mean 0.111:

```text
remote_context_index = (abs(0.158) + 0.111) / 2 = 0.134
```

All seven gates evaluate true, so `pass_count = 7` and the derived label is `rainfall_flood_window_consistent`. The remote-change value is a context check only; it should not be converted into flood depth, building loss, casualty totals, or climate-attribution fractions.

# Scoring Rubric

Total: 20 points.

- 3 points: Answer shape. Full credit for compact JSON with `ledger_values`, `gates`, and `label`, using the requested field names and units.
- 4 points: Window and point rainfall. Full credit for `window_days = 6`, `point_total_mean_mm = 22.6`, and `point_peak_share_mean = 0.582` within tolerance; partial credit for correct formulas with minor rounding errors.
- 3 points: Gridded rainfall comparison. Full credit for `grid_mean_mm = 33.7` and `grid_spread_ratio = 2.136`; partial credit for using only one gridded mean or reversing the ratio.
- 3 points: Catalog and exposure checks. Full credit for `gdacs_flood_alerts = 2` and `worldpop_millions = 1.025`; partial credit for one correct value.
- 3 points: Remote-change countercheck. Full credit for `remote_context_index = 0.134` from dNBR mean and embedding-change mean, with clear treatment as contextual evidence only.
- 4 points: Threshold result and bounded interpretation. Full credit for all seven gates true, `pass_count = 7`, label `rainfall_flood_window_consistent`, and no extra numerical claims such as exact flood depth, loss totals, or attribution values.
