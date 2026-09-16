# Pacific Northwest Heat-Wave Calculation Audit

A benchmark reviewer is auditing a proposed shortcut for the June 2021 Pacific Northwest heat-wave package. The shortcut says: because the package contains an ERA5-Land aggregate value named `temperature_2m_max_c_max`, that value can replace the direct daily weather series when deciding whether the event-window heat load is sustained and population-scaled.

Use only evidence inside the CSX-001 event package. Do not use web search, external climate records, or hidden answers from other tasks. Use package-relative paths in every answer field that asks for evidence paths.

Your task is not to produce another threshold ledger. Instead, perform a compact forensic calculation audit:

1. Identify the official event window from the locked event anchor.
2. Use the direct Open-Meteo daily series for exactly that window to reconstruct the minimum calculation path:
   - `heat_load_terms_c_days = max(Tmax_C - 30, 0)` for each event-window day, rounded to 1 decimal.
   - `heat_load_c_days = sum(heat_load_terms_c_days)`, rounded to 1 decimal.
   - `peak3_tmax_c`, the maximum 3-day rolling mean of event-window `Tmax_C`, rounded to 1 decimal, plus its date window.
   - `warm_night_ratio = count(Tmin_C >= 16) / event_window_nights`, rounded to 2 decimals.
   - `population_scaled_heat_load_person_c_days = population_sum * unrounded_heat_load_c_days`, rounded to the nearest integer.
3. Audit the shortcut by comparing the ERA5-Land aggregate `stats.temperature_2m_max_c_max`, rounded to 1 decimal, with the correct `peak3_tmax_c`. Treat the aggregate value as the wrong substitute for the rolling 3-day value and show the numeric consequence for the condition `peak3_tmax_c >= 33`.
4. Include at least one other package-local source that is insufficient or weaker as a calculation source, with a reason tied to file content or source role.

Return JSON only, with exactly these top-level fields:

- `answer_type`: must be `forensic_calculation_audit`
- `audit_target`
- `source_paths`
- `event_window`
- `validated_calculation`
- `divergence_audit`
- `rejected_or_insufficient_alternatives`
- `final_ruling`

Required nested content:

- `source_paths` must include package-relative paths for `event_window_anchor`, `direct_daily_weather`, `population_input`, and `wrong_aggregate_source`.
- `validated_calculation` must include the daily Tmax values, heat-load terms, heat-load sum, peak 3-day Tmax value and window, warm-night count/denominator/ratio, population sum, and population-scaled heat load.
- `divergence_audit` must identify the first divergence point, the wrong aggregate value, the correct rolling value, their difference, the affected condition, the wrong condition result, the correct condition result, and the reason the aggregate file is insufficient for this calculation.
- `rejected_or_insufficient_alternatives` must include at least one non-selected package file and explain why it is not a direct calculation source.
- `final_ruling` must be a compact object, not prose, stating whether the shortcut is accepted and what corrected answer family the package supports.
