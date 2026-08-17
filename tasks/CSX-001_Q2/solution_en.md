# Final Answer

```json
{
  "answer_type": "forensic_calculation_audit",
  "audit_target": "Audit whether ERA5-Land aggregate temperature_2m_max_c_max can replace the direct daily Open-Meteo series for the sustained heat-load calculation.",
  "source_paths": {
    "event_window_anchor": "data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json",
    "direct_daily_weather": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "population_input": "data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json",
    "wrong_aggregate_source": "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json"
  },
  "event_window": [
    "2021-06-25",
    "2021-07-01"
  ],
  "validated_calculation": {
    "daily_tmax_c": [
      27.3,
      30.1,
      32.2,
      34.0,
      35.5,
      26.7,
      22.3
    ],
    "heat_load_terms_c_days": [
      0.0,
      0.1,
      2.2,
      4.0,
      5.5,
      0.0,
      0.0
    ],
    "heat_load_c_days": 11.8,
    "peak3_tmax_c": 33.9,
    "peak3_window": [
      "2021-06-27",
      "2021-06-29"
    ],
    "peak3_input_tmax_c": [
      32.2,
      34.0,
      35.5
    ],
    "warm_nights": {
      "count": 3,
      "denominator": 7,
      "ratio": 0.43
    },
    "population_sum": 49269.915,
    "population_scaled_heat_load_person_c_days": 581385
  },
  "divergence_audit": {
    "first_divergence_point": "rolling_peak3_tmax_requires_daily_sequence",
    "wrong_operation": "substitute aggregate stats.temperature_2m_max_c_max for the 3-day rolling mean of daily Tmax",
    "wrong_aggregate_value_c": 31.3,
    "correct_peak3_tmax_c": 33.9,
    "difference_correct_minus_wrong_c": 2.6,
    "affected_condition": "peak3_tmax_c >= 33",
    "wrong_condition_result": false,
    "correct_condition_result": true,
    "aggregate_source_defect": "The ERA5 file exposes aggregate stats only; it has no daily.time or daily temperature_2m_max sequence from which to compute rolling means, daily heat-load terms, or warm-night counts."
  },
  "rejected_or_insufficient_alternatives": {
    "data/event_reports/event_reports_004_NOAA_Climate.gov_Event_Tracker_-_Pacific_Northwest_heat.html": {
      "ruling": "insufficient_as_direct_calculation_source",
      "reason": "The NOAA article is the event/report context and locked anchor, but it is not the machine-readable daily weather series used for the requested calculations."
    }
  },
  "final_ruling": {
    "shortcut_accepted": false,
    "corrected_answer_family": "sustained_dry_multiday_heat_load",
    "basis": "The direct event-window daily series gives peak3_tmax_c 33.9 and population-scaled heat load 581385 person-C-days; the aggregate substitution would incorrectly fail the peak3 threshold."
  }
}
```

# Files Inspected

- `metadata/event.json`
- `metadata/files.csv`
- `metadata/sources.csv`
- `README.md`
- `data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json`
- `data/event_reports/event_reports_004_NOAA_Climate.gov_Event_Tracker_-_Pacific_Northwest_heat.html`

# Reference Solving Trace

1. List or inspect the CSX-001 package manifest files. The relevant package-local evidence is the locked anchor, Open-Meteo weather JSON, ERA5-Land aggregate JSON, WorldPop population JSON, and NOAA article.
2. Read `data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json`. Its `temporal_window.start_date` is `2021-06-25` and `temporal_window.end_date` is `2021-07-01`.
3. Read `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`. Confirm `daily.time` spans exactly the locked event window.
4. Use `daily.temperature_2m_max`: `27.3, 30.1, 32.2, 34.0, 35.5, 26.7, 22.3 C`.
5. Compute daily heat-load terms with `max(Tmax_C - 30, 0)`: `0.0, 0.1, 2.2, 4.0, 5.5, 0.0, 0.0 C-days`; the rounded sum is `11.8 C-days`.
6. Compute every 3-day rolling mean of `temperature_2m_max`. The maximum is June 27 to June 29: `(32.2 + 34.0 + 35.5) / 3 = 33.9 C`.
7. Use `daily.temperature_2m_min` for warm nights. Three values meet `>= 16 C` (`16.4, 19.5, 17.8`), so the warm-night ratio is `3 / 7 = 0.43`.
8. Read `data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json`; `population_sum.population = 49269.914585497914`. Multiply by the unrounded heat load `11.800000000000004` and round to `581385 person-C-days`.
9. Read `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`; `stats.temperature_2m_max_c_max = 31.26191101074221`, which rounds to `31.3 C`.
10. Audit the shortcut. The first divergence occurs before thresholding: the ERA5 file provides aggregate statistics only, not a daily sequence. Treating `31.3 C` as `peak3_tmax_c` would make `31.3 >= 33` false, while the correct rolling value makes `33.9 >= 33` true. The numeric impact is `33.9 - 31.3 = 2.6 C`.
11. Reject the NOAA article as a direct calculation source. It supports event context/anchoring, but not the machine-readable daily series needed for heat-load terms and rolling means.
12. Return the compact audit JSON and reject the shortcut.

# Rubric

Total: 20 points.

- Schema and answer type, 3 points: returns JSON with exactly the requested top-level fields and sets `answer_type` to `forensic_calculation_audit`.
- Package-local source paths, 3 points: uses package-relative paths for the locked anchor, Open-Meteo weather series, WorldPop population file, and ERA5 aggregate file; uses no web or hidden answers.
- Event window and direct calculation, 4 points: uses `2021-06-25` through `2021-07-01` and correctly reports daily Tmax, heat-load terms, `heat_load_c_days`, `peak3_tmax_c`, peak window/input values, and warm-night ratio.
- Population-scaled heat load, 2 points: reads the WorldPop population and multiplies it by unrounded heat load to obtain the rounded person-C-days value.
- First divergence audit, 4 points: identifies the first divergence as replacing a rolling daily calculation with aggregate `temperature_2m_max_c_max`, reports `31.3` versus `33.9`, delta `2.6 C`, and the threshold-result flip.
- Insufficient alternative, 2 points: rejects at least one additional package-local source, such as the NOAA narrative article, as insufficient for direct calculation with a content-based reason.
- Final ruling, 2 points: rejects the shortcut and states the corrected answer family without substituting generic disaster explanation or policy prose.

Numeric tolerances:

- `heat_load_c_days`: expected `11.8`, accept `11.6` to `12.0`.
- `peak3_tmax_c`: expected `33.9`, accept `33.7` to `34.1`, with window `2021-06-27` to `2021-06-29`.
- `warm_night_ratio`: expected `0.43`, accept `0.42` to `0.44`.
- `population_scaled_heat_load_person_c_days`: expected `581385`, accept `570000` to `595000`.
- `wrong_aggregate_value_c`: expected `31.3`, accept `31.2` to `31.4`.
- `difference_correct_minus_wrong_c`: expected `2.6`, accept `2.4` to `2.8`.
