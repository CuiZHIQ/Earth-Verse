# Hassanabad GLOF Pathway-Signal Margin Test

A technical review team is testing whether the 7 May 2022 Hassanabad / Shishper Glacier GLOF record passes a fixed consistency rule for a short-lived localized flood-pathway surface signal under warm conditions.

Compute the following quantities from the task data, rounding numeric outputs to 4 decimals:

- `radar_event_score = 0.65 * clamp(abs(s1_mean_db) / 1.0) + 0.20 * clamp(s1_std_db / 1.0) + 0.15 * clamp(s1_max_db / 5.0)`
- `annual_change_score = clamp(alpha_mean / 0.05)`
- `burn_like_score = 0.70 * clamp(max(dnbr_mean, 0) / 0.3) + 0.30 * clamp(max(dnbr_max, 0) / 0.8)`
- `rainfall_support_score = clamp((gpm_mean_mm + chirps_mean_mm) / 40.0 + era5_precip_mean_mm / 80.0)`
- `context_max_score = max(annual_change_score, burn_like_score, rainfall_support_score)`
- `pathway_margin = radar_event_score - context_max_score`
- `thermal_gate_c = event_day_tmax_mean_c - 30.0`

Use `clamp(x) = min(max(x, 0), 1)`. The rule passes only when `radar_event_score >= 0.55`, `context_max_score <= 0.30`, `pathway_margin >= 0.25`, `rainfall_support_score < 0.20`, and `thermal_gate_c > 0.0`.

Return compact JSON:

```json
{
  "radar_event_score": "<number>",
  "context_max_score": "<number>",
  "pathway_margin": "<number>",
  "rainfall_support_score": "<number>",
  "thermal_gate_c": "<number>",
  "answer": "<pass_or_fail_label>"
}
```
