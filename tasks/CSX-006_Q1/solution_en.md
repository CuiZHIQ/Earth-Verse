# Final Answer

```json
{
  "answer_type": "humid_dry_mechanism_audit",
  "mechanism_ruling": "point_evidence_dry_hot_not_humid_dominated",
  "source_paths": {
    "event_window": "data/event_reports/event_reports_003_Locked_event_anchor_March-April_2024_West_Africa_and_Sahel_humid_heat_wave.json",
    "direct_hourly_and_daily_product": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "report_context": "data/event_reports/event_reports_004_World_Weather_Attribution_-_Sahel_humid_heat_wave.html",
    "insufficient_aggregate_product": "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json"
  },
  "event_window": {
    "start_date": "2024-03-31",
    "end_date": "2024-04-04",
    "days": 5
  },
  "calculations": {
    "daily_apparent_heat": {
      "apparent_tmax_c": {
        "2024-03-31": 39.7,
        "2024-04-01": 42.0,
        "2024-04-02": 43.2,
        "2024-04-03": 41.8,
        "2024-04-04": 42.4
      },
      "days_apparent_tmax_ge39c": 5,
      "heat_load_gt39c_c_days": 14.1,
      "hottest_3day_window": {
        "start_date": "2024-04-02",
        "end_date": "2024-04-04",
        "mean_apparent_tmax_c": 42.5
      }
    },
    "warm_nights": {
      "tmin_c": {
        "2024-03-31": 27.6,
        "2024-04-01": 27.5,
        "2024-04-02": 27.5,
        "2024-04-03": 27.5,
        "2024-04-04": 27.9
      },
      "warm_nights_tmin_ge27c": 5,
      "warm_night_ratio": 1.0
    },
    "hot_hour_moisture_gate": {
      "hot_hour_rule": "temperature_2m >= 39 C",
      "hot_hour_count": 39,
      "mean_relative_humidity_pct": 10.36,
      "mean_dew_point_c": 3.58,
      "hot_hours_rh_ge30pct_count": 0
    },
    "apparent_amplification_gate": {
      "mean_hot_hour_apparent_minus_air_c": -2.24,
      "hot_hours_apparent_gt_air_count": 7,
      "daily_mean_apparent_minus_air_c": -1.2,
      "days_apparent_tmax_gt_air_tmax": 1
    }
  },
  "rejected_or_insufficient_alternatives": {
    "anchor_or_report_label_only_humid_dominance": "insufficient_for_point_mechanism_without_hourly_moisture_support",
    "era5_land_aggregate_for_humid_heat": "insufficient_missing_relative_humidity_dew_point_and_apparent_temperature_fields",
    "single_dry_bulb_spike_only": "rejected_because_apparent_heat_load_is_14.1_c_days_and_all_5_nights_have_tmin_ge27c"
  },
  "reference_solving_trace": [
    "Read the locked event anchor to get the 2024-03-31 to 2024-04-04 window.",
    "Use Open-Meteo because it contains both daily apparent Tmax/Tmin and hourly temperature, RH, dew point, and apparent temperature.",
    "Compute the sustained daily apparent-heat and warm-night checks from the daily arrays.",
    "Filter hourly rows to temperature_2m >= 39 C and compute moisture and apparent-minus-air indicators.",
    "Reject anchor/report-label-only humid dominance and ERA5 aggregate substitution because they cannot reproduce the point-scale moisture gate."
  ]
}
```

# Evidence And Calculations

The locked window comes from `data/event_reports/event_reports_003_Locked_event_anchor_March-April_2024_West_Africa_and_Sahel_humid_heat_wave.json`: `2024-03-31` to `2024-04-04`, 5 days.

`data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json` is the direct numeric product because it has the required daily fields (`temperature_2m_max`, `temperature_2m_min`, `apparent_temperature_max`) and hourly fields (`temperature_2m`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`). The apparent-Tmax values are 39.7, 42.0, 43.2, 41.8, and 42.4 C, so the heat load is `(39.7 - 39) + (42.0 - 39) + (43.2 - 39) + (41.8 - 39) + (42.4 - 39) = 14.1 C-days`. The hottest rolling 3-day apparent-Tmax mean is 42.5 C for 2024-04-02 through 2024-04-04. The Tmin values are 27.6, 27.5, 27.5, 27.5, and 27.9 C, so `warm_night_ratio = 5 / 5 = 1.0`.

For the hot-hour moisture gate, 39 hourly rows have `temperature_2m >= 39 C`. Their mean RH is 10.36%, their mean dew point is 3.58 C, and zero hot hours have RH >= 30%. Over the same hot hours, mean `apparent_temperature - temperature_2m` is -2.24 C and only 7 of 39 hot hours have apparent temperature above air temperature. At the daily-max level, mean `apparent_Tmax - air_Tmax` is -1.2 C and only 1 of 5 days has apparent Tmax above air Tmax.

The package anchor provides the humid-heat event label, and the report HTML at `data/event_reports/event_reports_004_World_Weather_Attribution_-_Sahel_humid_heat_wave.html` is useful context for the regional heatwave and reported heat impacts. That label/context alone does not prove point-scale humid dominance. `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json` is insufficient for this audit because it has aggregate temperature, wind, and precipitation statistics but lacks RH, dew point, and apparent temperature fields needed for the moisture and apparent-amplification gates.

# Scoring Rubric

Total: 20 points.

- 2 points: Returns the required JSON schema with the exact seven top-level keys and package-relative paths.
- 2 points: Selects Open-Meteo as the direct numeric source and identifies the locked anchor as the event-window source.
- 3 points: Correctly computes the sustained apparent-heat values: 14.1 C-days, 5 days >= 39 C, and the 2024-04-02 to 2024-04-04 rolling mean of 42.5 C.
- 2 points: Correctly computes warm-night persistence as 5/5 = 1.0.
- 4 points: Correctly filters hot hours (`temperature_2m >= 39 C`) and reports 39 hot hours, 10.36% mean RH, 3.58 C mean dew point, and 0 hot hours with RH >= 30%.
- 3 points: Correctly computes apparent-amplification diagnostics: -2.24 C mean hot-hour apparent-minus-air, 7 hot hours with apparent > air, -1.2 C daily mean apparent-minus-air, and 1 day with apparent Tmax > air Tmax.
- 2 points: Gives the correct mechanism ruling: point evidence is dry-hot/not humid-dominated while still recognizing sustained apparent heat and warm nights.
- 2 points: Rejects the anchor/report-label-only and ERA5-aggregate alternatives for specific evidence reasons, not generic prose.
