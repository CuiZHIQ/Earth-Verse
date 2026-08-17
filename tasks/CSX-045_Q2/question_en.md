# East Asia Cold-Wave Coupled Thermal-Stress Index

A cold-hazard analyst is reconstructing the January 2016 East Asia and subtropical Asia cold wave as a coupled exposure process. The question is whether sustained subzero air temperature, wind-chill amplification, snow falling during cold hours, and observational context form a coherent cold-wave signal, or whether the record is dominated by precipitation totals or image contrast alone.

Use only the local CSX-045 event package. Select package-relative evidence for the hourly temperature and wind series, snowfall timing, precipitation summaries, and image statistics used in the calculation.

Compute a compact cold-wave consistency index. Temperatures are in C, wind speed is in km/h, snowfall is in cm, and image metrics use paired pre-event and event RGB images.

Use these definitions:

- `longest_subzero_run_h`: longest continuous hourly run with `T < 0`.
- `subzero_load_c_h`: `sum(max(0, -T))` over all hourly temperatures.
- Wind chill `WC`: use `T` when `T > 10` or wind speed is at most `4.8`; otherwise use `13.12 + 0.6215*T - 11.37*V^0.16 + 0.3965*T*V^0.16`.
- `apparent_stress_c_h`: `sum(max(0, -10 - WC))` over all hours.
- `snow_subzero_share`: hourly snowfall during `T < 0` divided by total hourly snowfall.
- `precipitation_spread_ratio`: across the three event-mean precipitation summaries, `(maximum mean - minimum mean) / maximum mean`.
- `image_white_delta`: absolute difference between event and pre-event fractions of pixels whose mean RGB value is above `180` and whose channel range is below `30`.
- `consistency_index`:  
  `100 * (0.25*min(longest_subzero_run_h/48,1) + 0.25*min(subzero_load_c_h/150,1) + 0.20*min(apparent_stress_c_h/120,1) + 0.15*snow_subzero_share + 0.10*precipitation_spread_ratio + 0.05*(1 - image_white_delta))`.

Return only compact JSON with these fields:

```json
{
  "longest_subzero_run_h": 0,
  "subzero_load_c_h": 0.0,
  "apparent_stress_c_h": 0.0,
  "snow_subzero_share": 0.000,
  "precipitation_spread_ratio": 0.000,
  "image_white_delta": 0.0000,
  "consistency_index": 0.0,
  "answer": "persistent_cold_wave_consistency_pass"
}
```

Use `persistent_cold_wave_consistency_pass` when the index is at least `75.0`; otherwise use `persistent_cold_wave_consistency_fail`. The final result should be grounded in the coupled thermal-stress components, not in image brightness or precipitation magnitude alone.
