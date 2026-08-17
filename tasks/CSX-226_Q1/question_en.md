# Enga Landslide Threshold Ledger

For CSX-226, compute a compact threshold ledger for the 24 May 2024 Enga
landslide using the local event package.

Use these formulas:

- `exposure_margin_people = exposed_population - 5000`
- `radar_margin_db = abs(minimum VV post-minus-pre dB) - 20.0`
- `optical_margin = maximum dNBR - 0.45`
- `same_day_precip_max_mm = max(all same-date daily precipitation candidates)`
- `precip_margin_mm = 25.0 - same_day_precip_max_mm`
- `ledger_score = int(exposure_margin_people >= 0) + int(radar_margin_db >= 0) + int(optical_margin >= 0) + int(precip_margin_mm >= 0)`

Assign the classification by the ledger score:

- score 4: `exposed_strong_surface_limited_rain_ledger`
- score 2 or 3: `mixed_surface_exposure_ledger`
- score 0 or 1: `weak_surface_exposure_ledger`

Return JSON:

```json
{
  "answer": {
    "exposure_margin_people": 0.0,
    "radar_margin_db": 0.0,
    "optical_margin": 0.0,
    "same_day_precip_max_mm": 0.0,
    "precip_margin_mm": 0.0,
    "ledger_score": 0,
    "classification": ""
  },
  "interpretation": "<one sentence tied to the computed ledger>"
}
```
