# July 2021 Western Europe Floods

A hydrology team is reviewing the 12-16 July 2021 Western Europe floods and needs to test whether a runoff-depth diagnosis should be anchored on the localized Belgian station rainfall peak or on smoother regional precipitation summaries. Compute a compact consistency diagnostic from the technical record.

Return a compact JSON object with this structure:

```json
{
  "task_family": "runoff_translation_consistency_ledger",
  "event_window_days": 0,
  "calculation_rows": [
    {
      "row": "local_rainfall_amplification",
      "formulas": [],
      "values": {},
      "conclusion": ""
    },
    {
      "row": "runoff_depth_translation",
      "formulas": [],
      "values": {},
      "conclusion": ""
    },
    {
      "row": "gridded_precipitation_smoothing_test",
      "formulas": [],
      "values": {},
      "conclusion": ""
    },
    {
      "row": "forecast_timing_context",
      "formulas": [],
      "values": {},
      "conclusion": ""
    },
    {
      "row": "exposure_remote_change_context",
      "formulas": [],
      "values": {},
      "conclusion": ""
    }
  ],
  "final_label": "",
  "consistency_checks": []
}
```

Required calculations:

- In `local_rainfall_amplification`, compute the Jalhay 48-hour rainfall divided by the station-average 48-hour rainfall and by the report-box 48-hour rainfall.
- In `runoff_depth_translation`, use `direct_runoff_mm = rainfall_mm * runoff_fraction` with runoff fractions `0.20` and `0.25`; apply it separately to the report-box rainfall and to the Jalhay rainfall, then compute the local-to-report runoff-range ratio.
- In `gridded_precipitation_smoothing_test`, compare the 48-hour Jalhay and report-box rainfall values with the package event-window gridded accumulated-precipitation maxima as a scale-contrast diagnostic, and state whether those smoother gridded maxima are sufficient as the runoff-depth basis. Do not treat this row as strict same-window gauge-grid verification.
- In `forecast_timing_context`, use the forecast-signal lead hours and ensemble-above-threshold lead hours as timing metrics alongside the rainfall-runoff arithmetic.
- In `exposure_remote_change_context`, compute critical amenities per 100,000 people using OSM elements with `amenity` in `{hospital, clinic, fire_station, police, school, shelter}`. Count road-like highway elements as OSM elements with a `highway` tag except `bus_stop` and `platform`. Use critical amenities plus road-like highways for combined small exposure features per 100,000 people; include remote-change statistics only as change metrics, not as exact flood-depth or loss values.

Use millimetres for rainfall and runoff depths, hours for lead times, and ratios rounded to two decimals unless a source value is already more precise. Keep the final label compact.
