# Final Answer

Correct answer: `transport_scale_pass`

```json
{
  "window_days": 4,
  "plume_speed_kmh": 41.67,
  "local_peak_wind_kmh": 21.6,
  "speed_ratio": 1.93,
  "precip_context_mm": 5.66,
  "diagnosis": "transport_scale_pass"
}
```

# Key Computations

The locked event window runs from 2022-01-18 through 2022-01-21, so the inclusive duration is 4 days. The report states a 4,000 km-long dust plume, giving `4000 / (4 * 24) = 41.67 km/h`.

The daily package point-wind maximum from the m/s series is 3.09 m/s, or `3.09 * 3.6 = 11.12 km/h`. The daily package point-wind maximum already in km/h is 21.6 km/h, so `local_peak_wind_kmh = 21.6`. This is used as a point-wind comparator, not as complete corridor wind evidence. The speed ratio is `41.67 / 21.6 = 1.93`.

The gridded event precipitation maxima are 0.99 mm and 5.6577 mm, so the larger context value is 5.66 mm.

# Reasoning Path

Apply the stated rule: plume length `4000 >= 3000`, duration `4 >= 3`, and speed ratio `1.93 > 1.5`. All three inequalities pass, so the deterministic diagnosis is `transport_scale_pass`. The local point wind is below the plume-scale speed proxy and does not satisfy the ledger as a sufficient local-wind explanation.

# Computed Label

Concise computed label: long-range Saharan dust transport with weak local point-wind support.

# Scoring Rubric

Total: 20 points.

- 4 points: Returns compact JSON with exactly the six requested keys and no extra prose in the final object.
- 5 points: Computes the duration, plume-speed proxy, local wind conversion, wind peak, speed ratio, and precipitation context with correct units and rounding.
- 5 points: Applies all three threshold tests correctly and returns `transport_scale_pass`.
- 3 points: Shows the local wind comparison using the larger converted 10 m wind maximum, not the smaller m/s value alone.
- 2 points: Treats precipitation only as a secondary numeric context value and does not reframe the case as a wet hazard.
- 1 point: Keeps the computed label concise and tied to the calculations while avoiding unsupported local impacts, corridor exposure, health burden, or deposition damage beyond the computed anchors.
