# Solution

## Correct Answer

The correct answer is `passes_localized_glof_pathway_signal`.

Expected JSON:

```json
{
  "radar_event_score": 0.6395,
  "context_max_score": 0.2172,
  "pathway_margin": 0.4223,
  "rainfall_support_score": 0.1241,
  "thermal_gate_c": 0.6093,
  "answer": "passes_localized_glof_pathway_signal"
}
```

## Key Computations

Raw anchors are: `s1_mean_db = 0.5553837282`, `s1_std_db = 0.6423338618`, `s1_max_db = 5.4371055441`, `alpha_mean = 0.0108575269`, `dnbr_mean = -0.1587327390`, `dnbr_max = 0.5378942984`, `gpm_mean_mm = 2.9819858104`, `chirps_mean_mm = 0.6202365825`, `era5_precip_mean_mm = 2.7265237899`, and `event_day_tmax_mean_c = 30.6092945486`.

Using `clamp(x) = min(max(x, 0), 1)`:

- `radar_event_score = 0.65 * 0.5553837282 + 0.20 * 0.6423338618 + 0.15 * 1.0 = 0.6395`.
- `annual_change_score = 0.0108575269 / 0.05 = 0.2172`.
- `burn_like_score = 0.70 * 0 + 0.30 * (0.5378942984 / 0.8) = 0.2017`.
- `rainfall_support_score = (2.9819858104 + 0.6202365825) / 40.0 + 2.7265237899 / 80.0 = 0.1241`.
- `context_max_score = max(0.2172, 0.2017, 0.1241) = 0.2172`.
- `pathway_margin = 0.6395 - 0.2172 = 0.4223`.
- `thermal_gate_c = 30.6092945486 - 30.0 = 0.6093 C`.

## Reasoning Path

The computed rule passes every threshold: the radar pathway score is above `0.55`, the strongest context score is below `0.30`, the margin is above `0.25`, rainfall support is below `0.20`, and the event-day thermal gate is positive. The compact process tag is therefore a localized GLOF pathway pulse, not an annual terrain-change, burn-style, or rainfall-dominant signal.

## Scoring Rubric

20 points total:

- JSON schema and rounding (3 pts): returns exactly the six requested fields with numeric values rounded to 4 decimals and the final label as a string. Partial credit: 1 to 2 pts for minor rounding or field-name errors.
- Radar score calculation (4 pts): applies the weighted formula with the maximum VV term clamped to 1.0 and reports `0.6395`. Partial credit: up to 3 pts for correct components with one arithmetic or clamp error.
- Context score calculations (4 pts): computes annual `0.2172`, burn-like `0.2017`, rainfall `0.1241`, and context maximum `0.2172`. Partial credit: 1 pt for each correct score or maximum.
- Margin and threshold tests (4 pts): computes pathway margin `0.4223` and verifies the radar, context, margin, and rainfall thresholds. Partial credit: up to 3 pts for correct margin with incomplete threshold checks.
- Thermal gate (3 pts): computes `thermal_gate_c = 0.6093 C` and uses the positive value in the final rule result. Partial credit: 1 to 2 pts for correct temperature anchor with incomplete subtraction or threshold use.
- Compact consequence label (2 pts): returns `passes_localized_glof_pathway_signal` and keeps the final sentence tied to the calculations without a broad narrative. Partial credit: 1 pt for a close pass label with weaker calculation linkage.
