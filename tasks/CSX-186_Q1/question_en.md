# Cameron Peak and East Troublesome Growth Ledger

A fire-behavior analytics group is checking a numeric diagnosis for the 2020 Cameron Peak and East Troublesome fires in Colorado. Reconstruct the growth-and-burn ledger from the technical record and decide whether the event satisfies the rapid-growth, high-end burn-signal rule below.

Use these formulas:

- `growth_increase_acres` = acres after the 24-hour growth pulse minus acres before that pulse.
- `growth_multiplier` = acres after the pulse divided by acres before the pulse.
- `pulse_to_ten_day_rate_ratio` = 24-hour growth increase divided by `(minimum East Troublesome acres within ten days / 10)`.
- `containment_gap_pct_points` = `100 - containment percent` on 2020-10-26.
- `dnbr_excess_over_high_threshold` = maximum dNBR minus `0.66`.
- `annual_change_peak_to_mean_ratio` = annual embedding-change maximum divided by annual embedding-change mean.

Apply this pass rule: label the case `rapid_growth_burn_signal_pass` only if `growth_increase_acres >= 100000`, `pulse_to_ten_day_rate_ratio >= 5`, `containment_gap_pct_points >= 80`, `dnbr_excess_over_high_threshold > 0`, and `annual_change_peak_to_mean_ratio >= 20`; otherwise label it `rapid_growth_burn_signal_fail`.

Return a compact JSON object with exactly these keys: `answer_label`, `growth_increase_acres`, `growth_multiplier`, `pulse_to_ten_day_rate_ratio`, `containment_gap_pct_points`, `dnbr_excess_over_high_threshold`, `annual_change_peak_to_mean_ratio`, and `one_sentence_check`.
