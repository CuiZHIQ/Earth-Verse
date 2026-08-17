# Final Answer

```json
{
  "answer": "persistent_multiday_monsoon_forcing",
  "event_total_mm": 133.3,
  "wettest_72h_mm": 109.0,
  "wettest_72h_window": "2013-06-15T00:00/2013-06-17T23:00",
  "wettest_72h_share": 0.818,
  "wet_hour_fraction": 0.812,
  "peak_hour_share": 0.047,
  "report_heavy_map_gap_mm": 166.7
}
```

# Key Computations

- Event total: sum the 96 hourly precipitation values from 2013-06-15T00:00 through 2013-06-18T23:00, giving 133.3 mm.
- Wettest 72-hour window: the largest rolling 72-hour sum is 109.0 mm, from 2013-06-15T00:00 through 2013-06-17T23:00.
- Wettest-window share: `109.0 / 133.3 = 0.8177`, rounded to 0.818.
- Wet-hour fraction: 78 of 96 hours have at least 0.1 mm, so `78 / 96 = 0.8125`, rounded to 0.812.
- Peak-hour share: the peak hourly precipitation is 6.2 mm at 2013-06-16T06:00, so `6.2 / 133.3 = 0.0465`, rounded to 0.047.
- Report-map threshold gap: the event report states that the heaviest rainfall map class is greater than 300 millimeters; using 300.0 mm as the conservative lower-bound reference, the minimum gap above the local total is `300.0 - 133.3 = 166.7 mm`.

# Reasoning Path

The ledger favors a persistent multi-day monsoon forcing. The wettest 72 hours contain 81.8% of the four-day total, and 81.2% of all hours are wet at the 0.1 mm threshold. By contrast, the largest single hour accounts for only 4.7% of the event total, which is too small for a single-hour-burst summary. The report-map heavy-rain reference is much higher than the local point total, so it should be treated as a threshold contrast rather than substituted into the local ledger.

# Computed Interpretation

For this Uttarakhand-western Nepal package record, the quantitative signal is persistence-dominated: sustained rainfall over most of the event window is the computed basis for the flood-producing rainfall state.

# Scoring Rubric

Total: 20 points.

- Final consistency label, 3 points: uses `persistent_multiday_monsoon_forcing` or an equivalent concise label that rejects a single-hour-burst summary. Partial credit: 1-2 points for identifying multi-day rainfall but giving an ambiguous or overly broad label.
- Event total and window sum, 4 points: reports 133.3 mm total precipitation and 109.0 mm for the wettest 72-hour window with correct units or field names. Partial credit: 1-3 points for one correct value, small rounding mistakes, or correct formulas with a minor extraction error.
- Window timing, 3 points: identifies the wettest 72-hour window as 2013-06-15T00:00 through 2013-06-17T23:00. Partial credit: 1-2 points for finding the correct three calendar days without exact hourly endpoints.
- Ratio calculations, 4 points: gives wettest_72h_share near 0.818, wet_hour_fraction near 0.812, and peak_hour_share near 0.047. Partial credit: 1-3 points for two correct ratios, incorrect rounding, or a correct setup with one arithmetic mistake.
- Report-map threshold contrast, 3 points: computes the minimum 166.7 mm gap between the local event total and the report-extracted greater-than-300 mm heavy-rain reference. Partial credit: 1-2 points for recognizing the map reference is higher but omitting the gap or using imprecise subtraction.
- Formula-linked interpretation, 2 points: explains that high wet-hour and 72-hour shares, combined with a small peak-hour share, support a persistence-dominated rainfall state. Partial credit: 1 point for a correct interpretation that cites only one of these ratios.
- Output discipline, 1 point: returns the requested compact JSON fields without adding unrelated management guidance or broad causal narration. Partial credit: no partial credit; award the point only when the output stays focused on the ledger.
