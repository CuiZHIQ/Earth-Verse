# Uljin Wildfire Report and Burn-Change Consistency Ledger

A technical review team is checking whether the March 4-13, 2022 Uljin wildfire is numerically consistent with a dry, wind-assisted burn-scar diagnosis rather than a late-rain-control or image-baseline alternative.

Use only package-local evidence. Do not use point-weather products for this task; build the ledger from the event report, package gridded precipitation and wind summaries, Sentinel-2 dNBR, and annual embedding-change context.

Compute these ledger values:

- `report_dry_wind_flag`: 1 if the report text links the event to strong winds and dry weather, otherwise 0.
- `smoke_transport_flag`: 1 if the report text states that smoke moved toward southern Japan, otherwise 0.
- `era5_mean_wind_speed_mps`: vector speed from the ERA5-Land mean 10 m u and v wind components.
- `era5_wind_bearing_to_deg`: direction toward which the ERA5-Land mean wind vector points, degrees clockwise from north.
- `precip_mean_spread_mm`: spread between ERA5-Land, GPM IMERG, and CHIRPS event precipitation means.
- `dnbr_mean`: mean dNBR over the event burn-change window.
- `dnbr_max_to_mean_ratio`: dNBR maximum divided by dNBR mean.
- `dnbr_to_annual_change_mean_ratio`: dNBR mean divided by annual 1-minus-cosine embedding-change mean.
- `reported_charred_area_km2`: reported charred hectares converted to square kilometers.

Apply these tests:

- `report_dry_wind_mechanism_test`: pass if `report_dry_wind_flag = 1`.
- `smoke_transport_context_test`: pass if `smoke_transport_flag = 1`.
- `positive_heterogeneous_burn_test`: pass if `dnbr_mean > 0` and `dnbr_max_to_mean_ratio >= 2.0`.
- `late_rain_control_test`: pass only if the package evidence supports rainfall as the dominant control; otherwise fail.
- `nuclear_damage_overclaim_test`: pass if the answer avoids inferring nuclear-plant damage or radiation release.

Return JSON:

```json
{
  "answer": {
    "report_dry_wind_flag": 0,
    "smoke_transport_flag": 0,
    "era5_mean_wind_speed_mps": 0.0,
    "era5_wind_bearing_to_deg": 0.0,
    "precip_mean_spread_mm": 0.0,
    "dnbr_mean": 0.0,
    "dnbr_max_to_mean_ratio": 0.0,
    "dnbr_to_annual_change_mean_ratio": 0.0,
    "reported_charred_area_km2": 0.0
  },
  "tests": {
    "report_dry_wind_mechanism_test": "pass/fail",
    "smoke_transport_context_test": "pass/fail",
    "positive_heterogeneous_burn_test": "pass/fail",
    "late_rain_control_test": "pass/fail",
    "nuclear_damage_overclaim_test": "pass/fail"
  },
  "interpretation": "<one or two sentences tied to the computed ledger>"
}
```
