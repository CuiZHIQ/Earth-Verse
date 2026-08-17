# Final Answer

```json
{
  "answer": {
    "dnbr_max_to_mean_ratio": 2.336,
    "dnbr_mean": 0.303255,
    "dnbr_to_annual_change_mean_ratio": 22.037,
    "era5_mean_wind_speed_mps": 1.392,
    "era5_wind_bearing_to_deg": 331.3,
    "precip_mean_spread_mm": 6.389,
    "report_dry_wind_flag": 1,
    "reported_charred_area_km2": 170.0,
    "smoke_transport_flag": 1
  },
  "interpretation": "The local package supports a dry, wind-assisted wildfire mechanism through the report text, a positive heterogeneous dNBR signal, and a 170.0 km2 reported burned-area anchor. Gridded precipitation remains context rather than a late-rain control, and the ledger should not infer nuclear-plant damage or radiation release.",
  "tests": {
    "late_rain_control_test": "fail",
    "nuclear_damage_overclaim_test": "pass",
    "positive_heterogeneous_burn_test": "pass",
    "report_dry_wind_mechanism_test": "pass",
    "smoke_transport_context_test": "pass"
  }
}
```

# Key Computations

The report text supplies the mechanism flags: it links the fire to strong winds and dry weather, and it describes smoke moving toward southern Japan. It reports nearly 17,000 hectares charred, so `17,000 * 0.01 = 170.0 km2`.

ERA5-Land mean wind components are `u = -0.670 m/s` and `v = 1.220 m/s`. The vector speed is `sqrt(u^2 + v^2) = 1.392 m/s`, and the direction toward which it points is `331.3` degrees clockwise from north.

The event precipitation means are ERA5-Land `9.273 mm`, GPM `2.884 mm`, and CHIRPS `4.456 mm`, so the spread is `9.273 - 2.884 = 6.389 mm`. The dNBR mean is `0.303255`, the dNBR max-to-mean ratio is `0.708527 / 0.303255 = 2.336`, and the dNBR-to-annual-change mean ratio is `22.037`.

# Scoring Rubric

Total: 20 points.

- 4 points: requested JSON ledger with answer, tests, and interpretation.
- 4 points: report mechanism extraction for dry/wind, smoke transport, and no nuclear-damage overclaim.
- 4 points: gridded wind and precipitation calculations.
- 4 points: burn-change and area calculations.
- 2 points: correct pass/fail test states and rejected alternatives.
- 2 points: concise interpretation and limits.
