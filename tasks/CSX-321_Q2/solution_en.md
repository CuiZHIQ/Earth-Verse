# Correct Answer

`localized_collapse_consistent`

Expected JSON core:

```json
{
  "answer": "localized_collapse_consistent",
  "optical_extreme_ratio": 67.52,
  "radar_extreme_ratio": 64.09,
  "optical_peak_z": 8.64,
  "radar_peak_z": 11.76,
  "local_signal_gate": true,
  "annual_mean_lt_0.08": true,
  "precipitation_mean_lt_5_mm": true,
  "event_anchor_2022_07_03": true,
  "pass_count": 4,
  "rejected_reading": "massif_wide_or_rain_led"
}
```

# Computation

Optical inputs: mean `0.024941`, maximum `1.684037`, standard deviation `0.192076`.

Radar inputs: mean `0.267552 dB`, maximum `17.147750 dB`, standard deviation `1.435302 dB`.

Context inputs: annual embedding-change mean `0.041398`; same-day hourly gridded precipitation mean `1.808061 mm`.

Calculations:

- `optical_extreme_ratio = 1.684037 / max(abs(0.024941), 0.001) = 67.52`
- `radar_extreme_ratio = 17.147750 / max(abs(0.267552), 0.001) = 64.09`
- `optical_peak_z = (1.684037 - 0.024941) / max(0.192076, 0.001) = 8.64`
- `radar_peak_z = (17.147750 - 0.267552) / max(1.435302, 0.001) = 11.76`

Both extreme ratios exceed `20`, and both peak-z values exceed `5`, so the local-signal gate passes. The annual mean `0.041398` is below `0.08`, and the precipitation mean `1.808061 mm` is below `5 mm`, so the two context gates also pass. The event-date anchor is 2022-07-03, giving four explicit passed gates and the deterministic answer `localized_collapse_consistent`.

Computed consequence: strong local optical and radar extremes are present, while the annual mean-change and same-day precipitation checks are too low for a massif-wide or rain-led reading.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns compact JSON with answer, four computed signal metrics, four explicit gate booleans, pass_count, and rejected_reading.
- 4 points: Computes optical_extreme_ratio as `67.52` and optical_peak_z as `8.64` using the stated formulas, within tolerances `0.05` and `0.02`.
- 4 points: Computes radar_extreme_ratio as `64.09` and radar_peak_z as `11.76` using the stated formulas, within tolerances `0.05` and `0.02`.
- 4 points: Applies all four gates correctly: `local_signal_gate`, `annual_mean_lt_0.08`, `precipitation_mean_lt_5_mm`, and `event_anchor_2022_07_03` are true.
- 2 points: Reports `localized_collapse_consistent` and `pass_count = 4` from the deterministic rule.
- 2 points: Rejects `massif_wide_or_rain_led` as a direct consequence of the low annual mean change and low same-day precipitation mean.
- 1 point: Keeps the consequence concise and does not add loss, volume, runout, or attribution statements beyond the computed gates.
