# June 2021 Pacific Northwest Heat-Wave Numeric Diagnosis

A public-health climatology team is preparing a technical note on the late-June 2021 Pacific Northwest and western Canada heat wave. They need a compact numeric diagnosis that distinguishes sustained heat load from a single peak-day, humid-heat, drought, fire/smoke, or visible-damage interpretation.

Compute the following event indices for the 2021-06-25 to 2021-07-01 window:

- cumulative daytime heat load in degree C-days, using `sum(max(Tmax - 30 C, 0))`;
- hottest 3-day mean of daily maximum air temperature;
- night recovery ratio, using `count(Tmin >= 16 C) / event_window_days`;
- peak apparent-minus-air temperature delta, using `max(apparent_temperature_max) - max(temperature_2m_max)`;
- local population heat-load proxy, using `population_sum * cumulative_heat_load`.

Return JSON:
```json
{
  "heat_load_c_day": <number>,
  "hottest_3day_tmax_mean_c": <number>,
  "night_recovery_ratio": <number>,
  "apparent_air_peak_delta_c": <number>,
  "population_heat_load_proxy_person_c_day": <number>,
  "diagnosis": "<short mechanism label>"
}
```

After the JSON, add one sentence explaining why the indices support the diagnosis.
