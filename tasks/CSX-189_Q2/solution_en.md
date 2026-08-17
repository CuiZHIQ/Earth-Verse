# Final Answer

```json
{
  "component_scores": {
    "gridded_wind_component": 13.9,
    "heterogeneous_burn_component": 23.4,
    "precipitation_context_penalty": 3.2,
    "report_dry_wind_component": 40.0,
    "smoke_transport_component": 15.0
  },
  "consistency_note": "The evidence-window score is driven by report dry-wind and smoke-transport flags plus a positive heterogeneous dNBR signal; precipitation spread is a context penalty, not a daily peak control.",
  "dnbr_max_to_mean_ratio": 2.336,
  "dnbr_mean": 0.303255,
  "evidence_window": "2022-03-04_to_2022-03-13",
  "gridded_context": {
    "era5_mean_wind_speed_mps": 1.392,
    "era5_wind_bearing_to_deg": 331.3,
    "precip_mean_spread_mm": 6.389
  },
  "spread_pressure_score": 89.1
}
```

# Key Computations

The report text supplies the two binary components: strong winds plus dry weather gives `40.0`, and smoke transport toward southern Japan gives `15.0`.

ERA5-Land mean wind components are `u = -0.670 m/s` and `v = 1.220 m/s`, so the mean wind speed is `1.392 m/s` and the vector points toward `331.3` degrees. The gridded wind component is `20 * min(1.392 / 2, 1) = 13.9`.

The dNBR mean is `0.303255`; the dNBR max-to-mean ratio is `0.708527 / 0.303255 = 2.336`, giving a heterogeneous-burn component of `23.4`. The precipitation means from ERA5-Land, GPM, and CHIRPS span `6.389 mm`, so the precipitation context penalty is `3.2`.

Final score:

```text
40.0 + 15.0 + 13.9 + 23.4 - 3.2 = 89.1
```

# Scoring Rubric

Total: 20 points.

- 4 points: structured score ledger.
- 4 points: report dry-wind and smoke-transport components.
- 4 points: gridded wind and precipitation calculations.
- 3 points: dNBR mean, max-to-mean ratio, and burn component.
- 3 points: score arithmetic.
- 2 points: bounded interpretation that avoids daily point-weather peak and facility-damage claims.
