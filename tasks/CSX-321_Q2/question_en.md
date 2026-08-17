# Marmolada Collapse Signal Check

Compute a localized-collapse consistency check for the 3 July 2022 Marmolada glacier collapse. Use the event's numeric summaries for post-minus-pre optical change, post-minus-pre radar change, annual embedding change, and same-day hourly gridded precipitation as package-derived local-collapse indicators, not as a precise collapse footprint, runout-volume estimate, or massif-wide damage map.

Use these formulas:

- `optical_extreme_ratio = optical_max / max(abs(optical_mean), 0.001)`
- `radar_extreme_ratio = radar_max / max(abs(radar_mean), 0.001)`
- `optical_peak_z = (optical_max - optical_mean) / max(optical_stdDev, 0.001)`
- `radar_peak_z = (radar_max - radar_mean) / max(radar_stdDev, 0.001)`

The local-signal gate passes when both extreme ratios are at least `20` and both peak-z values are at least `5`. The annual-context gate passes when annual embedding-change mean is below `0.08`. The precipitation-context gate passes when same-day hourly gridded precipitation mean is below `5 mm`. The event-date anchor gate passes when the locked event date is 2022-07-03. `pass_count` is the sum of these four gates.

Return compact JSON:

```json
{
  "answer": "<localized_collapse_consistent or localized_collapse_not_established>",
  "optical_extreme_ratio": 0,
  "radar_extreme_ratio": 0,
  "optical_peak_z": 0,
  "radar_peak_z": 0,
  "local_signal_gate": true,
  "annual_mean_lt_0.08": true,
  "precipitation_mean_lt_5_mm": true,
  "event_anchor_2022_07_03": true,
  "pass_count": 0,
  "rejected_reading": "<short computed consequence>"
}
```
