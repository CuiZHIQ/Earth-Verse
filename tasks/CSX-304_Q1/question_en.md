# Iraq Dust-Transport Threshold Check

A technical review team is checking whether the April 7-10, 2022 Iraq atmospheric hazard satisfies a deterministic multi-day dust-transport calibration, after accounting for rainfall, heat, wind-only, and durable surface-change countermetrics. Treat point hydrometeorology as package point-weather countermetric input, not as complete spatial evidence for the whole Iraq/Mesopotamia dust corridor.

Compute the following values from the event record:

- `event_days`: inclusive event-window length in days.
- `hydromet`: `regional_precip_mean_mm`, `point_regional_precip_ratio`, `max_temperature_c`, and `temperature_margin_below_35c`.
- `surface_change_max`: maximum annual embedding change.
- `component_scores`: use the formulas below.
- `score_margin`: `dust_transport - max(rain_counter, heat_counter, wind_only_counter, surface_counter)`.
- `final_label`: `iraq_multiday_dust_transport_pass` only if `dust_transport >= 7`, `score_margin >= 4`, regional precipitation stays below both rainfall gates, temperature stays below 35 C, and annual surface-change mean and maximum stay below their gates.

Component-score formulas:

- `dust_transport = 4*[dust/sandstorm family] + 2*[visibility and air-quality wording] + 1*[event_days >= 3] + 1*[Iraq or Mesopotamia location]`
- `rain_counter = 2*[max point precipitation total >= 50 mm] + 1*[regional_precip_mean_mm >= 25 mm] + 1*[regional precipitation maximum >= 50 mm]`
- `heat_counter = 2*[max_temperature_c >= 35 C] + 1*[regional maximum temperature >= 35 C]`
- `wind_only_counter = 1*[max point wind >= 6 m/s] + 1*[regional mean wind vector >= 6 m/s]`
- `surface_counter = 2*[annual surface-change mean >= 0.1] + 1*[surface_change_max >= 0.5]`

Return JSON only:

```json
{
  "event_days": 0,
  "hydromet": {
    "regional_precip_mean_mm": 0.0,
    "point_regional_precip_ratio": 0.0,
    "max_temperature_c": 0.0,
    "temperature_margin_below_35c": 0.0
  },
  "surface_change_max": 0.0,
  "component_scores": {
    "dust_transport": 0,
    "rain_counter": 0,
    "heat_counter": 0,
    "wind_only_counter": 0,
    "surface_counter": 0
  },
  "score_margin": 0,
  "final_label": ""
}
```
