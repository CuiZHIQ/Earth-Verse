# Smoke-Transport Threshold Ledger

A technical review team is testing a proposed event-window label for the August-September 2000 southern Africa smoke episode:

`regional biomass-burning smoke/aerosol transport with low local ventilation context`

Compute the indices below from the event-window evidence, then test whether the proposed label is numerically consistent. Return only the requested JSON object.

Definitions:

- `source_region_count`: number of distinct named heaviest-burning source regions in the fire/smoke report text.
- `scene_haze_ratio`: event-scene haze fraction divided by pre-scene haze fraction. For each true-color scene, ignore black scan gaps. A haze-candidate pixel has `70 <= luma <= 220` and `saturation <= 0.20`, where `luma = 0.2126R + 0.7152G + 0.0722B` and `saturation = (max(R,G,B) - min(R,G,B)) / max(R,G,B)`.
- `mean_wind_m_s`: mean available daily 10 m wind speed during the event window.
- `low_wind_day_fraction`: fraction of available daily wind values at or below `1.0 m/s`.
- `precip_total_mm`: cumulative available daily precipitation during the event window.
- `dry_day_fraction`: fraction of available daily precipitation values at or below `0.5 mm`.

Pass/fail rules:

- source count passes at `source_region_count >= 3`;
- scene haze change passes at `scene_haze_ratio >= 1.05`;
- low ventilation passes when `mean_wind_m_s <= 1.0` and `low_wind_day_fraction >= 0.80`;
- local dryness passes only when `precip_total_mm <= 50` and `dry_day_fraction >= 0.50`;
- the final consistency label is `regional_biomass_burning_smoke_with_low_ventilation_context` only when source count, scene haze change, and low ventilation all pass; otherwise return `not_proven`.

Return JSON:

```json
{
  "metrics": {
    "source_region_count": 0,
    "scene_haze_ratio": 0.0,
    "mean_wind_m_s": 0.0,
    "low_wind_day_fraction": 0.0,
    "precip_total_mm": 0.0,
    "dry_day_fraction": 0.0
  },
  "pass_fail": {
    "source_count": "pass_or_fail",
    "scene_haze_change": "pass_or_fail",
    "low_ventilation": "pass_or_fail",
    "local_dryness": "pass_or_fail"
  },
  "final_consistency": "label",
  "rejected_alternative": "one short threshold-based rejection"
}
```
