# Pakistan 2022 Monsoon Persistence Test

A hydrometeorology team is reviewing the June-September 2022 Pakistan monsoon floods to decide whether the rainfall and flood-duration diagnostics support a sustained Indus-basin storage signal rather than a short-pulse rainfall signal.

Compute these quantities from the technical record:

- `event_days = inclusive_days(anchor_start, anchor_end)`
- `point_total_mm = sum(daily_point_precip_mm)`
- `event_mean_daily_mm = point_total_mm / event_days`
- `peak_to_mean_intensity = max(daily_point_precip_mm) / event_mean_daily_mm`
- `heavy_rain_persistence = count(daily_point_precip_mm >= 10 mm/day) / event_days`
- `red_window_fraction = red_flood_days / event_days`
- `grid_mean_spread_fraction = (max(gridded_window_mean_precip_mm) - min(gridded_window_mean_precip_mm)) / mean(gridded_window_mean_precip_mm)`
- `peak_window_share = max_7day_sum(daily_point_precip_mm) / point_total_mm`

Apply these gates:

- `intensity_gate`: `peak_to_mean_intensity >= 8.0`
- `persistence_gate`: `heavy_rain_persistence >= 0.25` and `red_window_fraction >= 0.70`
- `regional_consensus_gate`: `grid_mean_spread_fraction <= 0.10`
- `pulse_guardrail`: `peak_window_share < 0.40`

Use the point daily rainfall and GDACS flood duration over the full locked flood window. Use gridded precipitation means only as a cross-product agreement check over their declared shared gridded comparison window, not as a full June-September event-window rainfall total.

Set `final_label` to `sustained_indus_storage_signal` when all four gates pass; otherwise use `short_pulse_or_inconclusive_signal`.

Return compact JSON:

```json
{
  "target_family": "pakistan_2022_monsoon_indus_persistence_gate",
  "metrics": {
    "peak_to_mean_intensity": 0.0,
    "heavy_rain_persistence": 0.0,
    "red_window_fraction": 0.0,
    "grid_mean_spread_fraction": 0.0,
    "peak_window_share": 0.0
  },
  "gates": {
    "intensity_gate": false,
    "persistence_gate": false,
    "regional_consensus_gate": false,
    "pulse_guardrail": false
  },
  "final_label": "<label>",
  "computed_consequence": "<short consequence derived from the gates>"
}
```
