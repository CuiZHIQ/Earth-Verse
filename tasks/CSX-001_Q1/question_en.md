# Heat-Source Arbitration Audit

A benchmark reviewer is auditing a proposed CSX-001 heat-intensity answer for the June 2021 Pacific Northwest heat wave. Two package-local physical-hazard files look tempting, but only one can reproduce a daily-window heat calculation and an hourly hot-hour humidity check.

Use only package-local evidence from the CSX-001 event package. Do not use web search, hidden answer files, sibling tasks, or invented values. File paths in the answer must be package-relative.

Task objective:

- Use the locked event anchor as the official inclusive event window.
- Select the strongest physical-hazard source for reconstructing daily Tmax/Tmin and hourly temperature/RH within that window.
- Reject the aggregate-only physical-hazard alternative that cannot reproduce the same calculation.
- Quantify the consequence of using the rejected aggregate temperature maximum as if it were the event-window daily peak.

Calculation rules:

- Filter daily and hourly observations inclusively to the official event window.
- From the selected source, compute the peak daily Tmax and its date.
- From the selected source, compute the hottest 3-day mean daily Tmax and its date window.
- From the selected source, compute the mean relative humidity among hourly rows where air temperature is at least 30 C.
- From the rejected aggregate source, read `stats.temperature_2m_max_c_max`.
- Round temperatures, mean RH, and temperature differences to 1 decimal.

Return only JSON in this schema:

```json
{
  "answer_type": "expert_source_arbitration",
  "event_window_source": "<package-relative path>",
  "selected_source": "<package-relative path>",
  "rejected_source": "<package-relative path>",
  "arbitration_basis": "<compact reason>",
  "event_window": {
    "start_date": "<YYYY-MM-DD>",
    "end_date": "<YYYY-MM-DD>",
    "daily_rows_used": "<integer>",
    "hourly_rows_used": "<integer>"
  },
  "selected_calculation": {
    "peak_daily_tmax_c": "<number>",
    "peak_tmax_date": "<YYYY-MM-DD>",
    "hottest_3day_mean_tmax_c": "<number>",
    "hottest_3day_window": "<YYYY-MM-DD/YYYY-MM-DD>",
    "hot_hours_ge_30c": "<integer>",
    "hot_hour_mean_rh_percent": "<number>"
  },
  "invalid_alternative": {
    "claimed_field": "stats.temperature_2m_max_c_max",
    "rejected_value_c": "<number>",
    "peak_underestimate_if_used_c": "<number>",
    "first_failure": "<compact reason>"
  },
  "source_path_reasoning": {
    "event_window_role": "<compact role>",
    "selected_role": "<compact role>",
    "rejected_role": "<compact role>"
  }
}
```
