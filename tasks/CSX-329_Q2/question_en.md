# Northwest Pacific Reef Heat-Stress Consistency Check

A technical review team is checking whether the 2020 Northwest Pacific coral bleaching episode should be diagnosed from recent marine heat-stress alert logic rather than from single-day, land-weather, population, or surface-change proxies.

Compute the following deterministic ledger for the event and return a compact JSON object.

Definitions:

- `event_days`: inclusive calendar days from the locked event start date to end date.
- `baa_window_days`: the day count in the recent maximum Bleaching Alert Area memory window.
- `alert_support_score`: sum of 12 binary checks: marine heatwave/coastal ecosystem event family; Alert Level 2 wording; Taiwan, Japan, and South China Sea all named; recent August elevation wording; severe bleaching plus mortality wording; later Guam/Micronesia outlook separable from the current event area; HotSpot term; Degree Heating Week term; Bleaching Alert Area term; recent maximum wording; single-day inadequacy or day-to-day fluctuation wording; accumulated heat-stress impact wording.
- `single_day_score`: `HotSpot_term - single_day_inadequacy_flag`.
- `land_precip_exposure_score`: count of these true threshold tests: GPM mean precipitation > 100 mm, CHIRPS mean precipitation > 100 mm, ERA5-Land maximum 2 m temperature > 30 C, WorldPop population > 1,000,000, and road-like OSM features > 100.
- `surface_change_score`: count of these true threshold tests: mean Sentinel-2 dNBR > 0.25 and AlphaEarth mean annual change > 0.10.
- `alert_minus_land`: `alert_support_score - land_precip_exposure_score`.
- `alert_minus_surface`: `alert_support_score - surface_change_score`.
- `event_to_baa_ratio`: `event_days / baa_window_days`, rounded to three decimals.

The diagnosis passes when `alert_support_score >= 10`, `alert_minus_land >= 5`, `alert_minus_surface >= 10`, `event_to_baa_ratio >= 10`, and `single_day_score <= 0`.

Return this JSON shape:

```json
{
  "answer": "<short computed diagnosis label>",
  "alert_support_score": 0,
  "event_days": 0,
  "baa_window_days": 0,
  "context_scores": {
    "single_day": 0,
    "land_precip_exposure": 0,
    "surface_change": 0
  },
  "margins": {
    "alert_minus_land": 0,
    "alert_minus_surface": 0,
    "event_to_baa_ratio": 0.0
  },
  "threshold_result": "<pass/fail label>",
  "rejected_alternative": "<short computed consequence>"
}
```
