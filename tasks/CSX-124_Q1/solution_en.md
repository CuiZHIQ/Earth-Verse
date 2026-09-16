# Final Answer

```json
{
  "event_window": "2023-02-06 to 2023-02-16",
  "rainfall": {
    "total_mm": 153.0,
    "wettest_day": "2023-02-13",
    "wettest_mm": 114.1,
    "wet_share": 0.746,
    "peak_remainder": 2.933
  },
  "gridded": {
    "max_mm": 117.205,
    "mean_peak_mean": 1.306
  },
  "wind_coast": {
    "gust_kmh": 106.6,
    "wind_energy_k": 11.364,
    "coastal_index": 15.9
  },
  "image_exposure": {
    "sar_span_db": 31.096,
    "sar_mean_db": 1.878,
    "emb_max_mean": 59.699,
    "population_k": 304.521,
    "road_share": 0.935
  },
  "score": {
    "hits": 7,
    "total": 7,
    "value": 1.0,
    "class": "high_compound_signal"
  }
}
```

Compact answer key: `score_1.00_7_of_7`.

# Key Computations

The inclusive event window is 2023-02-06 to 2023-02-16.

Rainfall from the hourly point series sums to 153.0 mm. The wettest day is 2023-02-13 with 114.1 mm, so `wet_share = 114.1 / 153.0 = 0.746` and `peak_remainder = 114.1 / (153.0 - 114.1) = 2.933`.

The three gridded precipitation ratios are `95.442 / 70.806 = 1.348`, `117.205 / 94.564 = 1.239`, and `103.507 / 77.811 = 1.330`. Their average is 1.306, and the largest gridded event maximum is 117.205 mm.

The local peak gust is 106.6 km/h, giving `wind_energy_k = 106.6^2 / 1000 = 11.364`. The coastal proxy is `10.9 + 10 * 0.5 = 15.9`.

The SAR contrast is `15.962 - (-15.133) = 31.096 dB`, with mean change 1.878 dB. The annual embedding contrast is `0.426521 / 0.007144 = 59.699`. The exposure context is 304.521 thousand people and `935 / 1000 = 0.935` road-tagged share.

# Reasoning Path

Apply one hit for each true gate: total rainfall at least 150 mm, wettest-day share at least 0.70, mean gridded peak-to-mean ratio at least 1.25, wind-energy proxy at least 10, coastal index at least 15, SAR span at least 30 dB, and the combined exposure context of population at least 300 thousand plus road share at least 0.90.

All seven gates pass:

- `153.0 >= 150`
- `0.746 >= 0.70`
- `1.306 >= 1.25`
- `11.364 >= 10`
- `15.9 >= 15`
- `31.096 >= 30`
- `304.521 >= 300` and `0.935 >= 0.90`

The final score is therefore `7 / 7 = 1.0`. Because `1.0 >= 0.85`, the deterministic class is `high_compound_signal`.

# Computed Interpretation

The ledger is internally consistent across rainfall concentration, gridded precipitation structure, wind and coastal proxies, image-change contrast, and local exposure context. The computed result is not a partial signal; it reaches the maximum seven-gate score.

# Scoring Rubric

Total: 20 points.

- 5 points: Rainfall concentration ledger. Full credit computes total rainfall, wettest day, wettest-day share, and peak-to-remainder ratio with units implied by field names. Partial credit: award 2-4 points for correct rainfall extraction with one derived ratio missing or rounded poorly.
- 3 points: Gridded precipitation ratios. Full credit computes each max-to-mean ratio and reports both the 1.306 mean ratio and 117.205 mm largest gridded maximum. Partial credit: award 1-2 points for using fewer summaries or making one arithmetic error.
- 3 points: Wind and coastal proxies. Full credit computes `wind_energy_k = 11.364` and `coastal_index = 15.9`. Partial credit: award 1-2 points for extracting raw wind, wave, and surge values but missing one formula.
- 3 points: Image and exposure contrasts. Full credit computes SAR span, SAR mean, embedding max-to-mean contrast, population in thousands, and road-tagged share. Partial credit: award 1-2 points for correct raw values but incomplete derived contrasts.
- 4 points: Seven-gate score. Full credit applies all seven thresholds, obtains 7 hits out of 7, and reports `score_1.00_7_of_7` with `high_compound_signal`. Partial credit: award 1-3 points for a correct score with missing gate details or one wrong threshold result.
- 2 points: Compact numeric JSON. Full credit returns the requested compact JSON fields with numeric rounding close to the answer key. Partial credit: award 1 point for correct values in a less compact structure.
