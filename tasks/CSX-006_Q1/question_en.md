# Sahel Heat Mechanism Audit

A prior answer treated CSX-006 as a humid-heat-dominated point event because the package anchor labels the episode a humid heat wave and the 5-day apparent-temperature ledger is sustained. Audit that mechanism claim using only the CSX-006 package-local evidence. Do not use web search, hidden answers, or invented values.

Use the locked event window from the package. For the numeric product you select, filter to that window and compute:

- `heat_load_gt39c_c_days = sum(max(daily_apparent_Tmax - 39 C, 0))`.
- Count the days with `daily_apparent_Tmax >= 39 C` and identify the hottest rolling 3-day window by mean `daily_apparent_Tmax`.
- `warm_night_ratio = count(daily_Tmin >= 27 C) / event_window_days`.
- Hot-hour moisture gate using hourly records where `temperature_2m >= 39 C`: hot-hour count, mean relative humidity, mean dew point, and count with relative humidity >= 30%.
- Apparent-amplification gate: mean `(hourly_apparent_temperature - hourly_temperature_2m)` over hot hours, count of hot hours where apparent temperature exceeds air temperature, daily mean `(apparent_Tmax - air_Tmax)`, and count of days where apparent Tmax exceeds air Tmax.

Return compact JSON with exactly these top-level keys: `answer_type`, `mechanism_ruling`, `source_paths`, `event_window`, `calculations`, `rejected_or_insufficient_alternatives`, and `reference_solving_trace`.

Rules:

- Use package-relative source paths only.
- Distinguish direct point-level numeric evidence from report context and aggregate products.
- A regional/report label alone is not enough to prove point-scale humid dominance.
- Classify the mechanism as `point_evidence_dry_hot_not_humid_dominated` if the hot-hour mean RH is below 30%, no hot hours have RH >= 30%, and apparent temperature is not amplified above air temperature on average.
