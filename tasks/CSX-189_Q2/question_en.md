# Uljin Wildfire Spread-Pressure Evidence Score

During the March 2022 Uljin wildfire in South Korea, a technical review team is checking whether the local package supports a strong event-window spread-pressure signal without relying on point-weather products.

Use only package-local report text, ERA5-Land gridded wind/precipitation summaries, GPM and CHIRPS precipitation summaries, and Sentinel-2 dNBR. Do not compute a daily peak from point-weather files.

Compute the event-window score:

```text
spread_pressure_score =
  report_dry_wind_component
  + smoke_transport_component
  + gridded_wind_component
  + heterogeneous_burn_component
  - precipitation_context_penalty
```

where:

- `report_dry_wind_component = 40` if the report links the event to strong winds and dry weather, else 0.
- `smoke_transport_component = 15` if the report describes smoke moving toward southern Japan, else 0.
- `gridded_wind_component = 20 * min(era5_mean_wind_speed_mps / 2, 1)`.
- `heterogeneous_burn_component = 25 * min(dnbr_max_to_mean_ratio / 2.5, 1)`.
- `precipitation_context_penalty = 5 * min(precip_mean_spread_mm / 10, 1)`.

Return compact JSON:

```json
{
  "evidence_window": "YYYY-MM-DD_to_YYYY-MM-DD",
  "spread_pressure_score": 0.0,
  "component_scores": {
    "report_dry_wind_component": 0.0,
    "smoke_transport_component": 0.0,
    "gridded_wind_component": 0.0,
    "heterogeneous_burn_component": 0.0,
    "precipitation_context_penalty": 0.0
  },
  "gridded_context": {
    "era5_mean_wind_speed_mps": 0.0,
    "era5_wind_bearing_to_deg": 0.0,
    "precip_mean_spread_mm": 0.0
  },
  "dnbr_mean": 0.0,
  "dnbr_max_to_mean_ratio": 0.0,
  "consistency_note": "one sentence"
}
```
