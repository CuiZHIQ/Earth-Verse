# Duration-Record Consistency Ledger

A cyclone-risk review panel is checking the proposed technical label for Tropical Cyclone Freddy, which crossed the southern Indian Ocean and affected Madagascar and Mozambique during February-March 2023. The label should rest on the storm-status duration record only if the WMO duration beats the previous John duration benchmark; nearby catalog timing, track distance, wind intensity, local rain/weather, and image/receptor metrics should be computed as tests that either support the label or remain context.

Build a calculation-first consistency ledger with these five rows:

- `duration_record_test`: compute the WMO storm-status duration, GDACS catalog duration, WMO-GDACS duration gap, previous John duration, Freddy's duration advantage, and Freddy/John duration ratio. This row passes the record test only if the WMO duration exceeds the previous John duration.
- `track_distance_check`: compute Freddy and John track distances, the Freddy/John distance ratio, and Freddy's fraction of Earth circumference. This row can support basinwide movement but must fail any distance-record claim unless the ratio is at least 1.
- `wind_energy_check`: compute the GDACS maximum wind, catalog alert level, hurricane-threshold ratio using 119 km/h, and `wind_energy_proxy = (max_wind_kmh / 3.6)^2 * WMO_duration_days`. This row is intensity context, not the record basis.
- `rain_weather_context_check`: compute local point rain total, wet hours, local maximum 72-hour rain, CHIRPS event-accumulated gridded precipitation mean, gridded precipitation maximum, local gust, and local pressure range. This row is regional weather context, not the record basis.
- `image_receptor_context_check`: compute embedding mean change, radar mean change, radar absolute extreme, compact-region population, and pre/event image byte counts. This row is context only.

Return JSON:

```json
{
  "duration_record_status": "",
  "ledger_rows": [
    {
      "row_id": "duration_record_test",
      "calculation": "",
      "computed_value": {},
      "role": "duration_record_basis|basinwide_support_not_distance_record|intensity_context_not_record_basis|rain_weather_context_not_record_basis|image_receptor_context_only"
    },
    {
      "row_id": "track_distance_check",
      "calculation": "",
      "computed_value": {},
      "role": "duration_record_basis|basinwide_support_not_distance_record|intensity_context_not_record_basis|rain_weather_context_not_record_basis|image_receptor_context_only"
    },
    {
      "row_id": "wind_energy_check",
      "calculation": "",
      "computed_value": {},
      "role": "duration_record_basis|basinwide_support_not_distance_record|intensity_context_not_record_basis|rain_weather_context_not_record_basis|image_receptor_context_only"
    },
    {
      "row_id": "rain_weather_context_check",
      "calculation": "",
      "computed_value": {},
      "role": "duration_record_basis|basinwide_support_not_distance_record|intensity_context_not_record_basis|rain_weather_context_not_record_basis|image_receptor_context_only"
    },
    {
      "row_id": "image_receptor_context_check",
      "calculation": "",
      "computed_value": {},
      "role": "duration_record_basis|basinwide_support_not_distance_record|intensity_context_not_record_basis|rain_weather_context_not_record_basis|image_receptor_context_only"
    }
  ],
  "proof_conclusion": ""
}
```
