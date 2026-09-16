# Final Answer

```json
{
  "answer_type": "expert_error_attribution",
  "corrected_classification": "compound_persistent_heat_with_water_stress",
  "error_attribution": {
    "error_class": "wrong_operation_and_overdominant_index",
    "rejected_counterfactual": "humid_heat_only",
    "wrong_operation": "Treating any wet-bulb >=30 C hour as sufficient to dominate the event diagnosis.",
    "correct_operation": "Count wet-bulb >=30 C hours inside the locked window and compare that duration with persistent daily heat and water-stress evidence."
  },
  "evidence_basis": {
    "event_window": {
      "path": "data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json",
      "start": "2022-06-01",
      "end": "2022-08-31",
      "daily_records": 92,
      "hourly_records": 2208
    },
    "heat_source": {
      "path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
      "compound_run_days": 11,
      "compound_run_start": "2022-08-12",
      "compound_run_end": "2022-08-22",
      "peak_apparent_temp_c": 44.0,
      "peak_apparent_temp_date": "2022-08-20"
    },
    "humidity_check": {
      "path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
      "wet_bulb_ge_30_hours": 1,
      "max_wet_bulb_c": 30.6,
      "max_wet_bulb_time": "2022-08-16T18:00",
      "humid_heat_duration_threshold_hours": 24
    },
    "water_stress_report": {
      "path": "data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html",
      "role": "direct_event_context",
      "matched_terms": [
        "poyang lake",
        "drought",
        "drained",
        "freshwater lake",
        "water levels",
        "irrigation",
        "shipping",
        "drinking water"
      ]
    }
  },
  "calculation_check": {
    "compound_heat_rule": "Tmax >=35 C AND Tmin >=28 C AND apparent_temperature_max >=40 C",
    "wet_bulb_formula": "Stull approximation from hourly temperature_2m and relative_humidity_2m",
    "humid_heat_shortfall_hours": 23,
    "apparent_minus_wet_bulb_peak_c": 13.4
  },
  "insufficient_alternatives": [
    {
      "basis": "humid_heat_only",
      "paths": [
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ],
      "reason_code": "insufficient_duration",
      "numeric_or_path_reason": "Only 1 hour has estimated wet-bulb >=30 C, 23 hours below the 24-hour duration threshold."
    },
    {
      "basis": "event_anchor_only",
      "paths": [
        "data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json"
      ],
      "reason_code": "weak_context",
      "numeric_or_path_reason": "The anchor supplies the 2022-06-01 to 2022-08-31 window but not the daily heat, hourly wet-bulb, or Poyang Lake stress measurements."
    }
  ],
  "minimal_required_paths": [
    "data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json",
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html"
  ],
  "final_assessment": "The humid-heat-only diagnosis is an operation error: one high wet-bulb hour is insufficient, while the package supports persistent compound heat with Poyang Lake water stress."
}
```

# Evidence And Calculations

Files inspected:

- `metadata/files.csv`
- `metadata/sources.csv`
- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html`

The locked anchor gives the event window as `2022-06-01` through `2022-08-31`. The Open-Meteo archive has 92 daily records and 2208 hourly records inside that inclusive window.

Daily heat calculation used these Open-Meteo fields: `daily.time`, `daily.temperature_2m_max`, `daily.temperature_2m_min`, and `daily.apparent_temperature_max`. A compound heat day required `temperature_2m_max >= 35 C`, `temperature_2m_min >= 28 C`, and `apparent_temperature_max >= 40 C`. The longest consecutive run is 11 days, from `2022-08-12` through `2022-08-22`. The peak daily apparent temperature is `44.0 C` on `2022-08-20`, rounded to 0.1 C.

Hourly humid-heat calculation used `hourly.temperature_2m` and `hourly.relative_humidity_2m`. Applying the Stull wet-bulb approximation gives only 1 hourly record at or above `30 C`; the maximum estimated wet bulb is `30.6 C` at `2022-08-16T18:00`. Because the humid-heat-only rule requires at least 24 hours, the shortfall is `24 - 1 = 23` hours. The difference between the peak apparent temperature and peak wet bulb is `44.0 - 30.6 = 13.4 C`.

The strongest water-stress context is the NASA Earth Observatory Poyang Lake report. Its text supports the event context through terms including `poyang lake`, `drought`, `drained`, `freshwater lake`, `water levels`, `irrigation`, `shipping`, and `drinking water`.

# Rejected Alternatives

`humid_heat_only` is rejected because the same heat archive contains only 1 wet-bulb hour at or above 30 C, which is 23 hours below the stated 24-hour duration threshold.

`event_anchor_only` is insufficient because the anchor supplies the event name and locked dates, but it does not contain the daily heat series, hourly wet-bulb inputs, or Poyang Lake water-stress context needed to reproduce the answer.

# Reference Solving Trace

1. Read `metadata/files.csv` to locate the locked anchor, Open-Meteo archive, and Poyang Lake report.
2. Read `data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json` and take the inclusive event window `2022-06-01` to `2022-08-31`.
3. Read `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`; filter daily and hourly rows to the locked window.
4. Compute the compound heat run from daily max, daily min, and daily apparent max fields; record 11 days from `2022-08-12` to `2022-08-22`.
5. Compute the peak daily apparent temperature; record `44.0 C` on `2022-08-20`.
6. Compute hourly wet bulb with the Stull approximation; count 1 hour at or above `30 C`, with maximum `30.6 C` at `2022-08-16T18:00`.
7. Compare the wet-bulb duration to the 24-hour humid-heat-only rule; reject `humid_heat_only` with a 23-hour shortfall.
8. Read the NASA Poyang Lake report and use the matched water-stress terms as direct event context.
9. Return the compact expert-error-attribution JSON above.

# Scoring Rubric

Total: 20 points.

- 3 points: Required `expert_error_attribution` schema and corrected classification `compound_persistent_heat_with_water_stress`.
- 3 points: Correct package-relative source paths for the locked anchor, Open-Meteo archive, NASA Poyang Lake report, and rejected alternatives.
- 3 points: Correct locked event window and record counts: 92 daily records and 2208 hourly records.
- 4 points: Correct heat calculation: 11-day compound heat run from `2022-08-12` to `2022-08-22`, and 44.0 C apparent-temperature peak on `2022-08-20`.
- 3 points: Correct humid-heat error attribution: 1 wet-bulb hour at or above 30 C, max wet bulb 30.6 C at `2022-08-16T18:00`, and 23-hour shortfall from the 24-hour threshold.
- 2 points: Correctly identifies the NASA Poyang Lake report as direct water-stress context without inventing SPI, reservoir volume, loss, health, or response values.
- 2 points: Rejects at least one insufficient alternative with a numeric or source-path reason, and does not substitute a generic disaster explanation for the requested JSON.
