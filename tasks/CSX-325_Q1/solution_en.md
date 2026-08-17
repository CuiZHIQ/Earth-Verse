# Correct Answer

```json
{
  "current_pct": 84.4,
  "previous_pct": 68.2,
  "increase_pp": 16.2,
  "relative_increase_pct": 23.8,
  "countries_or_territories": 83,
  "basin_count": 3,
  "passed_tests": 5,
  "conclusion": "heat_stress_escalation_pass"
}
```

# Computation

The NOAA Coral Reef Watch status text reports the source window as 1 January 2023 to 30 September 2025. It gives 84.4% of global coral reef area exposed to bleaching-level heat stress and 68.2% for the previous global event. The absolute increase is `84.4 - 68.2 = 16.2` percentage points. The relative increase is `100 * 16.2 / 68.2 = 23.8%` after rounding to one decimal place.

The same event evidence gives at least 83 countries and territories with mass coral bleaching, and the NOAA article names extensive heat stress across the Atlantic, Pacific, and Indian Ocean basins, so `basin_count = 3`.

All five threshold tests pass: `84.4 >= 80`, `16.2 >= 15`, `23.8 >= 20`, `83 >= 80`, and `3 >= 3`. The compact consequence label is therefore `heat_stress_escalation_pass`.

# Scoring Rubric

- 3 points: Returns valid compact JSON with exactly the requested eight keys and no extra narrative.
- 5 points: Extracts the four package anchors correctly: 84.4%, 68.2%, 83 countries or territories, and three named basins.
- 4 points: Computes `increase_pp = 16.2` and `relative_increase_pct = 23.8` using the stated formulas and one-decimal rounding.
- 4 points: Applies all five threshold tests correctly and reports `passed_tests = 5`.
- 2 points: Gives the final conclusion label `heat_stress_escalation_pass` and treats the marginal repeat-baseline rule as failing the computed thresholds.
- 1 point: Keeps the physical consequence concise: accumulated marine heat-stress extent is the supported diagnostic signal.
- 1 point: Avoids overclaiming measured local mortality, tourism loss, or terrestrial weather causation from these metrics.
