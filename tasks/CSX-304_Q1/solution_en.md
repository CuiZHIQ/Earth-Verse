# Correct Answer

```json
{
  "event_days": 4,
  "hydromet": {
    "regional_precip_mean_mm": 5.8182,
    "point_regional_precip_ratio": 9.262,
    "max_temperature_c": 34.59,
    "temperature_margin_below_35c": 0.41
  },
  "surface_change_max": 0.070014,
  "component_scores": {
    "dust_transport": 8,
    "rain_counter": 2,
    "heat_counter": 0,
    "wind_only_counter": 1,
    "surface_counter": 0
  },
  "score_margin": 6,
  "final_label": "iraq_multiday_dust_transport_pass"
}
```

# Computation

The locked window is April 7-10, 2022, so inclusive duration is 4 days. The regional precipitation mean is `(5.321299 + 6.315098) / 2 = 5.8182 mm`; the maximum package point precipitation total is `53.89 mm`, giving `53.89 / 5.8182 = 9.262`. Point hydrometeorology is used as a countermetric input, not as complete spatial evidence for the whole Iraq/Mesopotamia dust corridor. The regional precipitation maximum is `14.1592 mm`, below the 50 mm rainfall gate.

The maximum temperature is `34.5902 C`, so the 35 C margin is `35 - 34.5902 = 0.41 C`. Annual surface-change mean is `0.010858` and maximum is `0.070014`, both below their gates.

The dust-transport score is `4 + 2 + 1 + 1 = 8`. Countermetric scores are rainfall `2`, heat `0`, wind-only `1`, and surface change `0`; therefore `score_margin = 8 - 2 = 6`. All final gates pass, so the computed consequence is `iraq_multiday_dust_transport_pass`.

# Scoring Rubric

- 3 points: Returns the requested six top-level JSON fields with the nested metric groups and final label.
- 5 points: Computes hydrometeorological values correctly, including `regional_precip_mean_mm = 5.8182`, point-to-regional ratio near `9.262`, and the regional rainfall gates.
- 3 points: Computes temperature and surface-change thresholds correctly, including `max_temperature_c = 34.59`, margin `0.41 C`, and `surface_change_max = 0.070014`.
- 4 points: Applies all five component-score formulas correctly and reports scores `8, 2, 0, 1, 0`.
- 3 points: Computes `score_margin = 6` and applies the final threshold rule to get `iraq_multiday_dust_transport_pass`.
- 1 point: Keeps the computed consequence concise and tied to the threshold calculation.
- 1 point: Avoids adding measured health burden, direct damage, or operational advice not produced by the calculation.

Total: 20 points.
