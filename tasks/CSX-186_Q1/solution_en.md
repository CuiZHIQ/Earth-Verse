# Final Answer

```json
{
  "answer_label": "rapid_growth_burn_signal_pass",
  "growth_increase_acres": 140000,
  "growth_multiplier": 5.67,
  "pulse_to_ten_day_rate_ratio": 7.37,
  "containment_gap_pct_points": 85,
  "dnbr_excess_over_high_threshold": 0.0409,
  "annual_change_peak_to_mean_ratio": 25.57,
  "one_sentence_check": "The 24-hour acreage jump, rate ratio, containment gap, dNBR excess, and annual-change contrast all pass the rapid-growth burn-signal thresholds."
}
```

# Key Computations

The local event report gives an East Troublesome growth pulse from about 30,000 acres to 170,000 acres in about 24 hours, a ten-day burned-area lower bound of more than 190,000 acres, and 15 percent containment on 2020-10-26. The package dNBR summary gives a maximum of 0.7008767967, and the annual embedding-change summary gives a maximum of 0.6702516677 and a mean of 0.0262133237.

- `growth_increase_acres = 170000 - 30000 = 140000`.
- `growth_multiplier = 170000 / 30000 = 5.67`.
- `pulse_to_ten_day_rate_ratio = 140000 / (190000 / 10) = 7.37`.
- `containment_gap_pct_points = 100 - 15 = 85`.
- `dnbr_excess_over_high_threshold = 0.7008767967 - 0.66 = 0.0409`.
- `annual_change_peak_to_mean_ratio = 0.6702516677 / 0.0262133237 = 25.57`.

# Reasoning Path

The ledger first checks whether the 24-hour pulse is large enough in absolute terms: 140,000 acres exceeds the 100,000-acre threshold. It then checks whether that pulse dominates the ten-day lower-bound growth rate: 7.37 exceeds the threshold of 5. The 85 percentage-point containment gap exceeds the 80-point threshold, so the event was still far from full containment on the stated date.

The image-derived checks also pass. The dNBR maximum is 0.0409 above the 0.66 high-signal threshold, and the annual embedding-change peak is 25.57 times the mean. Because every numeric test passes, the deterministic label is `rapid_growth_burn_signal_pass`.

# Computed Interpretation

The computed ledger marks a concentrated rapid-growth episode with a high-end burn-signal check, rather than a slow accumulation pattern. The image metrics are used only as numeric burn-signal checks, not as direct counts of people, structures, or later hydrologic effects.

# Scoring Rubric

Total: 20 points.

- Final JSON and label, 3 points: returns the requested compact JSON and the label `rapid_growth_burn_signal_pass`. Partial credit: 1-2 points for the right label in prose or a JSON object with missing keys.
- Acreage pulse arithmetic, 4 points: extracts 30,000 and 170,000 acres and computes the 140,000-acre increase. Partial credit: 2-3 points for using the right values with minor rounding or transcription errors; 1 point for only citing one acreage anchor.
- Growth-rate and containment checks, 4 points: computes the 5.67 multiplier, 7.37 pulse-to-ten-day ratio, and 85 percentage-point containment gap. Partial credit: 2-3 points for two correct quantities; 1 point for one correct quantity.
- Image-metric calculations, 4 points: computes dNBR excess as 0.0409 and annual-change peak-to-mean ratio as 25.57. Partial credit: 2-3 points for one correct image-derived quantity or a correct threshold sign with rough rounding.
- Threshold ledger decision, 3 points: applies all five pass tests and explains why the label passes. Partial credit: 1-2 points for a correct conclusion with an incomplete threshold ledger.
- Concise computed interpretation, 2 points: keeps the interpretation tied to the computed growth and burn-signal values without adding direct loss, health, or later-flow quantities. Partial credit: 1 point for a mostly numeric interpretation with one extra claim not established by the ledger.
