# Mocoa Rain-Window Runout Score Ledger

An event analytics team is checking the April 2017 Mocoa, Colombia landslide and debris-flow record. The task is to compute a deterministic ledger, not a narrative. Test whether the record passes a rain-window, reported runout, population, and radar-context score.

Compute these metrics from the technical record:

- `window_days = inclusive days between the locked start date and locked end date`
- `local_two_day_mm = sum(local daily rainfall inside that window)`
- `local_min_day_mm = minimum local daily rainfall inside that window`
- `local_day_max_to_min = maximum local daily rainfall / minimum local daily rainfall`
- `grid_peak_mm = maximum event-window gridded rainfall value`
- `grid_peak_to_mean = grid_peak_mm / gridded rainfall mean from the same product`
- `report_markers = count of these four report markers present: heavy rain trigger, mountain movement, mud across the city, nearby river crossing`
- `population_k = exposed_population / 1000`
- `radar_total_images = radar_pre_count + radar_post_count`

If the package contains more than one point rainfall product, use the local daily rainfall series for the local rain-window gates and report the other point sample as a source-comparison diagnostic instead of silently substituting it into the gates. Include:

- `point_sample_two_day_mm = sum(two-day point rainfall from the independent point sample)`
- `point_sample_min_day_mm = minimum daily value from that independent point sample`
- `point_to_local_two_day_ratio = point_sample_two_day_mm / local_two_day_mm`

Apply these gates:

- `window_gate`: `window_days == 2` and `local_two_day_mm >= 60`
- `daily_distribution_gate`: `local_min_day_mm >= 30` and `local_day_max_to_min <= 1.10`
- `grid_peak_gate`: `grid_peak_mm >= 50` and `grid_peak_to_mean >= 20`
- `report_chain_gate`: `report_markers == 4`
- `population_gate`: `population_k >= 25`
- `radar_context_gate`: `radar_total_images >= 60`

Set `chain_score` to the number of passed gates. Set `final_label` to `mocoa_rain_window_runout_chain_confirmed` when `chain_score >= 5` and `report_chain_gate` is true; otherwise use `mocoa_chain_not_confirmed`.

Return only compact JSON:

```json
{
  "target_family": "mocoa_rain_window_runout_score_ledger",
  "metrics": {
    "window_days": 0,
    "local_two_day_mm": 0.0,
    "local_min_day_mm": 0.0,
    "local_day_max_to_min": 0.0,
    "grid_peak_mm": 0.0,
    "grid_peak_to_mean": 0.0,
    "report_markers": 0,
    "population_k": 0.0,
    "radar_total_images": 0
  },
  "gates": {
    "window_gate": false,
    "daily_distribution_gate": false,
    "grid_peak_gate": false,
    "report_chain_gate": false,
    "population_gate": false,
    "radar_context_gate": false
  },
  "source_comparison": {
    "local_series_two_day_mm": 0.0,
    "point_sample_two_day_mm": 0.0,
    "point_sample_min_day_mm": 0.0,
    "point_to_local_two_day_ratio": 0.0,
    "rainfall_gate_source_policy": "",
    "source_conflict_flag": ""
  },
  "chain_score": 0,
  "final_label": "",
  "computed_consequence": ""
}
```

Round ratios to three decimals and rainfall totals to one or three decimals as shown by the metric precision.
