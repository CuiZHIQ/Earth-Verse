# Western Europe Flood Window Threshold Ledger

During 12-17 July 2021, extreme rainfall over western Europe produced destructive flooding across river valleys and urban corridors in Germany, Belgium, and nearby areas.

A flood-window analyst needs a compact numeric ledger that checks whether the event record is internally consistent with a short rainfall-flood window, exposed population, and regional flood-alert support. Treat remote-change summaries as contextual counterchecks, not as direct measurements of flood depth or damage.

Compute these values from the event record:

- `window_days = end_date - start_date + 1`
- For each of the two daily point-precipitation series, restrict to the event window and compute `total_mm`, `peak_mm`, and `peak_share = peak_mm / total_mm`.
- `point_total_mean_mm = mean of the two point-series totals`
- `point_peak_share_mean = mean of the two point-series peak shares`
- `grid_mean_mm = mean of the two available gridded event-precipitation means`
- `grid_spread_ratio = larger gridded mean / smaller gridded mean`
- `gdacs_flood_alerts = count of Germany or Belgium flood-alert records that overlap the event window`
- `worldpop_millions = population sum / 1,000,000`
- `remote_context_index = mean(abs(Sentinel-2 dNBR mean), annual embedding 1-minus-cosine mean)`

Apply these seven gates:

- `window_6d`: `window_days == 6`
- `point_total_ge_20mm`: `point_total_mean_mm >= 20.0`
- `point_peak_share_ge_0_55`: `point_peak_share_mean >= 0.55`
- `grid_mean_ge_30mm`: `grid_mean_mm >= 30.0`
- `gdacs_alerts_ge_2`: `gdacs_flood_alerts >= 2`
- `population_ge_1m`: `worldpop_millions >= 1.0`
- `remote_context_lt_0_20`: `remote_context_index < 0.20`

Use label `rainfall_flood_window_consistent` when all seven gates are true; otherwise use `partial_flood_window_record`.

Return only compact JSON:

```json
{
  "ledger_values": {
    "window_days": 0,
    "point_total_mean_mm": 0.0,
    "point_peak_share_mean": 0.0,
    "grid_mean_mm": 0.0,
    "grid_spread_ratio": 0.0,
    "gdacs_flood_alerts": 0,
    "worldpop_millions": 0.0,
    "remote_context_index": 0.0,
    "pass_count": 0
  },
  "gates": {
    "window_6d": false,
    "point_total_ge_20mm": false,
    "point_peak_share_ge_0_55": false,
    "grid_mean_ge_30mm": false,
    "gdacs_alerts_ge_2": false,
    "population_ge_1m": false,
    "remote_context_lt_0_20": false
  },
  "label": "<derived label>"
}
```
