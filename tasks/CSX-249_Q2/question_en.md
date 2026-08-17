# Heat-Drought Evidence Score Ledger

Use the local package for the 2022 China heat wave and Yangtze drought. Build a calculation-first numeric ledger from structured values and the event report text where the report supplies duration and water-stress anchors. Treat gridded precipitation, surface-change, embedding-change, and population summaries as bounded context checks rather than standalone proof of the regional drought mechanism.

Compute these derived values:

- `event_window_days = inclusive_days(locked_start_date, locked_end_date)`
- `heat_streak_days = inclusive_days(2022-06-13, 2022-08-15)`, using the report date when the prior 62-day record had been exceeded
- `record_excess_days = heat_streak_days - 62`
- `heat_peak_mean_delta_c = ERA5_Tmax_max_c - ERA5_Tmax_mean_c`
- `gpm_chirps_mean_diff_mm = abs(GPM_mean_mm - CHIRPS_mean_mm)`
- `dnbr_max_mean_ratio = Sentinel2_dNBR_max / abs(Sentinel2_dNBR_mean)`
- `embedding_max_mean_ratio = embedding_change_max / embedding_change_mean`
- `population_million = WorldPop_population_sum / 1,000,000`

Score the ledger:

- `heat_core = 2*(ERA5_Tmax_mean_c >= 35) + 2*(ERA5_Tmax_max_c >= 39) + 1*(heat_peak_mean_delta_c <= 4) + 1*(red_heat_warning_count >= 30)`
- `persistence = 1*(event_window_days >= 90) + 2*(heat_streak_days > 62) + 1*(record_excess_days >= 2)`
- `dry_stress = 2*(Yangtze_precip_deficit_pct >= 80) + 1*(affected_population_million >= 5) + 1*(direct_loss_billion_cny >= 2) + 1*(water_supply_flag == 1)`
- `context_checks = 1*(gpm_chirps_mean_diff_mm <= 0.5) + 1*(dnbr_max_mean_ratio >= 20 and abs(dnbr_mean) < 0.05) + 1*(embedding_max_mean_ratio >= 20 and embedding_mean < 0.05) + 1*(population_million >= 8)`
- `total_score = heat_core + persistence + dry_stress + context_checks`

Use `class_label = "sustained_heat_yangtze_dry_stress_confirmed"` when `total_score >= 17`, `heat_core == 6`, `persistence >= 3`, and `dry_stress >= 4`; otherwise use `"evidence_support_incomplete"`.

Return only compact JSON with `component_scores`, `total_score`, `class_label`, the derived values, and the core report anchors used in the ledger.
