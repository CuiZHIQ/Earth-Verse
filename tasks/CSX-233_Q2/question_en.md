# Noto Peninsula Earthquake Surface-Change Numeric Ledger

A geospatial hazard team is checking whether the 1 January 2024 Noto Peninsula earthquake surface-change signal should be treated as a severe coseismic surface-change case, a rain-confounded case, or a weaker mixed signal.

Compute the following diagnostics from the event metrics:

1. `motion_slip_index = max_pga_g * finite_fault_maximum_slip_m`. The motion/slip gate passes only when `motion_slip_index >= 5.0`.
2. `radar_change_z = radar_mean_db / radar_std_db`. The radar gate passes only when both before/after counts are positive and `radar_change_z < 0`.
3. `embedding_outlier_ratio = annual_embedding_change_max / annual_embedding_change_mean`. The localized-outlier gate passes only when the annual mean is below `0.05` and the ratio is at least `20`.
4. `max_precip_mean_mm = max(event_date_precipitation_mean_estimates)`. The dry-weather gate passes only when this value is below `1.0 mm`.
5. `failure_exposure_ratio = liquefaction_population_alert_value / landslide_population_alert_value`. The failure-exposure gate passes only when the ratio is at least `100` and the liquefaction population alert is red.

Use this final rule: if all five gates pass, set `final_label` to `severe_coseismic_surface_change_localized_outliers_liquefaction_exposure`; otherwise set it to `mixed_or_insufficient_numeric_support`.

Return compact JSON with exactly these fields:

```json
{
  "motion_slip_index": 0.0,
  "radar_change_z": 0.0,
  "embedding_outlier_ratio": 0.0,
  "rain_gate": "pass_dry_not_rain or fail_rain_confounded",
  "failure_exposure_ratio": 0.0,
  "final_label": "..."
}
```
