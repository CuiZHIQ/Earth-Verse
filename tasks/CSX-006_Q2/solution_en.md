# Final Answer

```json
{
  "answer_type": "expert_error_attribution",
  "audit_ruling": "source_swap_fails",
  "error_class": "missing_variable",
  "correct_source": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
  "wrong_source": "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
  "event_window_source": "data/event_reports/event_reports_003_Locked_event_anchor_March-April_2024_West_Africa_and_Sahel_humid_heat_wave.json",
  "event_window": {
    "start_date": "2024-03-31",
    "end_date": "2024-04-04"
  },
  "first_missing_variable": "hourly.apparent_temperature",
  "missing_required_fields": [
    "hourly.apparent_temperature",
    "daily.temperature_2m_min"
  ],
  "corrected_answer": {
    "label": "sustained_apparent_heat_with_warm_night_exposure",
    "metrics": {
      "max_apparent_temperature_degC": 43.2,
      "hours_apparent_temperature_ge_40c": 16,
      "warm_nights_tmin_ge_27c": 5,
      "max_air_temperature_degC": 44.6
    }
  },
  "wrong_source_numeric_impact": {
    "wrong_available_temperature_field": "stats.temperature_2m_max_c_max",
    "wrong_available_temperature_value_degC": 35.3,
    "correct_point_air_temperature_max_degC": 44.6,
    "temperature_peak_difference_degC": 9.3,
    "can_compute_apparent_heat_duration": false,
    "can_compute_warm_nights": false
  },
  "rejected_or_insufficient_alternatives": {
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json": "precipitation-only event accumulation; no heat-stress variables",
    "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json": "precipitation-only event accumulation; no heat-stress variables",
    "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json": "annual remote-sensing change statistic; no event-window hourly or nightly heat fields",
    "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json": "burn-index pre/post statistic; no apparent-temperature or minimum-temperature fields"
  },
  "reference_solving_trace": [
    "Read metadata/files.csv to confirm candidate evidence files are package members.",
    "Read the locked event anchor and take the official window as 2024-03-31 through 2024-04-04.",
    "Inspect the local hourly heat-stress file and find hourly.apparent_temperature plus daily.temperature_2m_min.",
    "Compute max apparent temperature, count hourly apparent temperature values >= 40.0 degC, count daily minimum temperatures >= 27.0 degC, and compute max air temperature.",
    "Inspect the gridded aggregate file and identify stats.temperature_2m_max_c_max as the only available heat maximum while hourly apparent temperature and daily minimum temperature are absent.",
    "Compare 44.6 degC from the local point source with 35.3 degC from the substitute aggregate source, yielding a 9.3 degC peak-temperature difference.",
    "Reject precipitation, annual remote-sensing change, and burn-index files because they cannot reproduce the heat-stress calculation."
  ]
}
```

# Evidence And Calculations

Files inspected:

- `metadata/event.json`
- `metadata/files.csv`
- `metadata/sources.csv`
- `data/event_reports/event_reports_003_Locked_event_anchor_March-April_2024_West_Africa_and_Sahel_humid_heat_wave.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json`

The event anchor gives `temporal_window.start_date = 2024-03-31` and `temporal_window.end_date = 2024-04-04`. The local heat-stress file covers the same five dates and contains the required `hourly.apparent_temperature` and `daily.temperature_2m_min` arrays.

Correct-source metrics from `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`:

- `max(hourly.apparent_temperature) = 43.2` degC.
- `count(hourly.apparent_temperature >= 40.0) = 16` hours.
- `count(daily.temperature_2m_min >= 27.0) = 5` nights.
- `max(hourly.temperature_2m) = 44.6` degC.

The substitute aggregate file has `stats.temperature_2m_max_c_max = 35.342141723632835`, rounded to 35.3 degC. It does not contain `hourly.apparent_temperature` or `daily.temperature_2m_min`, so the first reproducibility failure is `hourly.apparent_temperature`. The numeric consequence for the available dry-temperature maximum is:

```text
44.6 - 35.342141723632835 = 9.257858276367165 degC
rounded to 9.3 degC
```

The corrected label is `sustained_apparent_heat_with_warm_night_exposure` because the local heat-stress source reaches 43.2 degC apparent temperature, has 16 apparent-temperature hours at or above 40.0 degC, and has 5 warm nights at or above 27.0 degC.

# Rubric

Total: 20 points.

- 4 points: Correct source-swap ruling and error class. Full credit requires `source_swap_fails` and `missing_variable`. Partial credit for identifying a wrong source without naming the missing-variable failure.
- 4 points: Correct source paths and event window. Full credit requires the local heat-stress source, the gridded aggregate wrong source, the locked event-window source, and the 2024-03-31 to 2024-04-04 window.
- 4 points: Correct missing-field audit. Full credit requires `hourly.apparent_temperature` as the first missing variable and includes `daily.temperature_2m_min` as another required missing field. Partial credit for one correct missing required field.
- 4 points: Correct calculations. Full credit requires 43.2 degC maximum apparent temperature, 16 apparent-temperature hours at or above 40.0 degC, 5 warm nights, 44.6 degC local point air-temperature maximum, 35.3 degC wrong-source available maximum, and 9.3 degC difference.
- 2 points: Correct rejected alternatives. Full credit rejects precipitation, annual remote-sensing change, and burn-index alternatives with content-based reasons.
- 1 point: Includes a concise reference solving trace with package-relative paths and intermediate values.
- 1 point: Output discipline. Full credit returns compact JSON and does not use web evidence, hidden answers, absolute paths, invented values, or a generic heat-wave essay.
