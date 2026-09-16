# Nyiragongo Surface-Impact Threshold Ledger

A technical analyst is checking whether the 22-23 May 2021 Mount Nyiragongo eruption near Goma is represented by a concentrated acute surface-change signal with a direct impact anchor, while the event-window rainfall ledger stays below a wet-trigger threshold.

Use the eruption-window event materials and compute the following diagnostics:

- `radar_concentration = radar_pre_post_max_db / radar_pre_post_mean_db`
- `optical_concentration = optical_dnbr_max / optical_dnbr_mean`
- `annual_concentration = annual_change_max / annual_change_mean`
- `acute_vs_annual_ratio = radar_concentration / annual_concentration`
- `rain_mean_mm = mean(two regional accumulated-precipitation means)`
- `people_per_destroyed_home = population_sum / destroyed_homes`
- `fatalities_per_100k = reported_deaths / population_sum * 100000`

Set `surface_gate` to true only if `radar_concentration >= 80`, `optical_concentration >= 20`, and `acute_vs_annual_ratio >= 3`. Set `rain_gate` to true only if `rain_mean_mm >= 10`. Set `impact_gate` to true only if reported deaths are positive and destroyed homes are at least 1000.

Set `answer` to `localized_surface_impact_with_rain_gate_unmet` only when `surface_gate` and `impact_gate` are true while `rain_gate` is false. Otherwise use `threshold_not_met`.

Return compact JSON:

```json
{
  "answer": "<computed_label>",
  "radar_concentration": 0.0,
  "optical_concentration": 0.0,
  "acute_vs_annual_ratio": 0.0,
  "rain_mean_mm": 0.0,
  "people_per_destroyed_home": 0.0,
  "fatalities_per_100k": 0.0,
  "gates": {"surface": false, "rain": false, "impact": false}
}
```
