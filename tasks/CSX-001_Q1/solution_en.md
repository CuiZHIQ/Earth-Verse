# Final Answer

```json
{
  "answer_type": "expert_source_arbitration",
  "event_window_source": "data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json",
  "selected_source": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
  "rejected_source": "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
  "arbitration_basis": "select_direct_daily_hourly_series_over_aggregate_stats",
  "event_window": {
    "start_date": "2021-06-25",
    "end_date": "2021-07-01",
    "daily_rows_used": 7,
    "hourly_rows_used": 168
  },
  "selected_calculation": {
    "peak_daily_tmax_c": 35.5,
    "peak_tmax_date": "2021-06-29",
    "hottest_3day_mean_tmax_c": 33.9,
    "hottest_3day_window": "2021-06-27/2021-06-29",
    "hot_hours_ge_30c": 29,
    "hot_hour_mean_rh_percent": 24.0
  },
  "invalid_alternative": {
    "claimed_field": "stats.temperature_2m_max_c_max",
    "rejected_value_c": 31.3,
    "peak_underestimate_if_used_c": 4.2,
    "first_failure": "aggregate_stats_do_not_contain_daily_sequence_or_hourly_rh_rows"
  },
  "source_path_reasoning": {
    "event_window_role": "locked_inclusive_temporal_filter",
    "selected_role": "direct_daily_tmax_tmin_and_hourly_temperature_rh_series",
    "rejected_role": "aggregate_temperature_stats_only_not_reproducible_for_3day_or_hot_hour_rh"
  }
}
```

# Files Inspected

- `metadata/event.json`
- `metadata/files.csv`
- `metadata/sources.csv`
- `data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`

# Reference Solving Trace

1. Inspect package metadata to confirm the CSX-001 package and identify event reports plus physical-hazard candidates.
2. Read `data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json`; use `temporal_window.start_date = 2021-06-25` and `temporal_window.end_date = 2021-07-01`.
3. Select `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json` because it contains `daily.time`, `daily.temperature_2m_max`, `daily.temperature_2m_min`, `hourly.time`, `hourly.temperature_2m`, and `hourly.relative_humidity_2m`.
4. Filter the Open-Meteo arrays inclusively to 2021-06-25 through 2021-07-01, yielding 7 daily rows and 168 hourly rows.
5. Compute the daily peak from `daily.temperature_2m_max`: the maximum is 35.5 C on 2021-06-29.
6. Compute 3-day means from the filtered daily Tmax sequence. The largest window is 2021-06-27/2021-06-29 with `(32.2 + 34.0 + 35.5) / 3 = 33.9 C` after rounding.
7. Filter hourly rows where `hourly.temperature_2m >= 30 C`; there are 29 rows. Average their `hourly.relative_humidity_2m` values to get 24.0 percent after rounding.
8. Read `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`; its `stats.temperature_2m_max_c_max` is 31.2619..., which rounds to 31.3 C.
9. Reject the ERA5 aggregate because it gives only aggregate stats, not the daily sequence needed for the 3-day calculation or the hourly RH rows needed for the hot-hour mean. If its aggregate max were used as the event peak, the peak would be understated by `35.5 - 31.3 = 4.2 C`.

# Rubric

Total: 20 points.

- JSON schema and answer type (2 points): Returns only the requested JSON with `answer_type = expert_source_arbitration`. Partial credit: 1 point for mostly valid JSON with minor schema omissions.
- Source arbitration (4 points): Selects the Open-Meteo archive, rejects the ERA5-Land aggregate stats file, and cites the locked event anchor, all with package-relative paths. Partial credit: 1-3 points for identifying some but not all roles correctly.
- Event-window filtering (3 points): Uses the inclusive 2021-06-25 to 2021-07-01 window and reports 7 daily rows plus 168 hourly rows. Partial credit: 1-2 points for correct dates with incomplete row accounting.
- Selected-source calculations (5 points): Reports peak Tmax 35.5 C on 2021-06-29, hottest 3-day mean 33.9 C for 2021-06-27/2021-06-29, 29 hot hours, and hot-hour mean RH 24.0 percent. Partial credit: up to 4 points for correct formulas with one missing or slightly misrounded value.
- Invalid alternative and numeric impact (3 points): Reads `stats.temperature_2m_max_c_max` as 31.3 C and computes the 4.2 C peak understatement if it is wrongly substituted. Partial credit: 1-2 points for the right rejected field or the right consequence but not both.
- Source-path reasoning (2 points): Explains that the selected source is direct daily/hourly series evidence and the rejected file is aggregate-only evidence that cannot reproduce the 3-day or hot-hour RH calculations. Partial credit: 1 point for a weaker but still package-grounded reason.
- Evidence boundary discipline (1 point): Does not use web evidence, hidden answers, broad disaster explanation, response advice, or non-package values.
