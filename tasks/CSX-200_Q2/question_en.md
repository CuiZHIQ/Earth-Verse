# Post-Fire Surface-Change Consistency Check

A technical review team is testing whether the July-August 2023 Greece wildfire surface-change metrics support a patchy fire-linked burn diagnosis or a broad uniform burn diagnosis.

Compute the local post-fire consistency test using these rules:

- `dnbr_peak_z = (dnbr_max - dnbr_mean) / dnbr_std_dev`.
- `annual_peak_mean_ratio = annual_change_max / annual_change_mean`.
- `local_high_dnbr` is true when `dnbr_max >= 0.66`.
- `uniform_scene_burn` is true when `dnbr_mean >= 0.27`.
- `mixed_scene` is true when `dnbr_mean < 0` and `dnbr_std_dev >= 0.10`.
- `localized_annual_change` is true when `annual_change_max >= 0.75`, `annual_change_mean < 0.10`, and `annual_peak_mean_ratio >= 10`.

Return a compact JSON object with:

```json
{
  "dnbr_metrics": {
    "dnbr_max": 0,
    "dnbr_mean": 0,
    "dnbr_std_dev": 0,
    "dnbr_peak_z": 0
  },
  "annual_change_metrics": {
    "annual_change_max": 0,
    "annual_change_mean": 0,
    "annual_peak_mean_ratio": 0
  },
  "threshold_flags": {
    "local_high_dnbr": false,
    "uniform_scene_burn": false,
    "mixed_scene": false,
    "localized_annual_change": false
  },
  "consistency_class": "<final class>",
  "interpretation": "<one sentence explaining what the calculations prove>"
}
```

Use `consistent_patchy_high_severity_fire_change` as the final class only if `local_high_dnbr`, `mixed_scene`, and `localized_annual_change` are true while `uniform_scene_burn` is false.
