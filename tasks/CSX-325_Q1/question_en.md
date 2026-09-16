# Coral Bleaching Heat-Stress Extent Test

A technical review team is checking whether NOAA's status text for the fourth global coral bleaching event satisfies a quantitative accumulated heat-stress escalation rule rather than a marginal repeat-baseline rule. Use the status-window evidence reported in the local package as the temporal basis; the calculation is a global heat-stress extent test and does not require a separate spatial product.

Compute these fields:

- `current_pct`: percent of global coral reef area exposed to bleaching-level heat stress during the current event.
- `previous_pct`: comparable percent for the previous global coral bleaching event.
- `increase_pp`: `current_pct - previous_pct`.
- `relative_increase_pct`: `100 * increase_pp / previous_pct`.
- `countries_or_territories`: documented count with mass coral bleaching or bleaching-level heat stress.
- `basin_count`: number of named ocean basins with extensive bleaching-level heat stress.
- `passed_tests`: count of these tests that pass: `current_pct >= 80`, `increase_pp >= 15`, `relative_increase_pct >= 20`, `countries_or_territories >= 80`, and `basin_count >= 3`.
- `conclusion`: `heat_stress_escalation_pass` if all five tests pass; otherwise `heat_stress_escalation_fail`.

Round percentage outputs to one decimal place. Use the displayed one-decimal `increase_pp` when computing `relative_increase_pct`. Return compact JSON with exactly those eight keys and no prose outside the JSON.
