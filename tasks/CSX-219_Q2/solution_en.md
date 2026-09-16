# Final Answer

```json
{
  "rainfall_load": {
    "antecedent_15d_mm": 218.2,
    "event_day_gridded_max_mm": 4.13,
    "antecedent_to_event_day_ratio": 52.83
  },
  "landslide_extent": {
    "avg_speed_mph": 40,
    "overrun_area_sqmi": 0.5,
    "moved_mass_mtons": 18,
    "mass_density_mtons_per_sqmi": 36.0
  },
  "river_extent": {
    "dam_depth_ft": 25,
    "temporary_lake_mi": 2.5,
    "blockage_ft_mi": 62.5
  },
  "context_index_per_100k": 132.51,
  "threshold_score": {
    "passed": 8,
    "possible": 8
  },
  "computed_label": "antecedent_wet_high_mobility_river_blockage"
}
```

# Key Computations

The precipitation ledger uses the 15-day point precipitation sum and the largest event-day gridded precipitation value from the gridded products. The antecedent load is `218.2 mm`, the event-day gridded maximum is `4.13 mm`, and the ratio is:

`218.2 / 4.13 = 52.83`.

The landslide extent ledger uses an average speed of `40 mph`, an overrun area of `0.5 square mile`, and moved mass of `18 million tons`. The derived mass density is:

`18 / 0.5 = 36.0 million tons per square mile`.

The river-blockage ledger uses a maximum dam depth of `25 ft` and temporary lake length of `2.5 miles`, giving:

`25 * 2.5 = 62.5 ft-mi`.

The context index uses `846` OSM ways, `154` OSM amenities, and a context population of `754664.6`:

`(846 + 154) / 754664.6 * 100000 = 132.51`.

The direct-impact index is 3 because fatalities are at least 25, covered homes and other structures are at least 25, and the covered road length is at least 0.5 mile.

# Reasoning Path

1. The rainfall load check passes because `218.2 mm >= 150 mm`.
2. The antecedent/event-day ratio check passes because `52.83 >= 10`, so the final high-score label can use the antecedent-wet branch.
3. The mobility and extent checks pass: `40 mph >= 30 mph`, `0.5 sq mi >= 0.25 sq mi`, and `18 million tons >= 10 million tons`.
4. The river checks pass: `25 ft >= 20 ft` and `2.5 mi >= 2 mi`.
5. The direct-impact check passes because its three component thresholds all pass, producing an index of 3.
6. The threshold score is therefore `8 / 8`. Since the score is at least 7 and the rainfall ratio check passes, the deterministic label is `antecedent_wet_high_mobility_river_blockage`.

# Computed Interpretation

The numeric ledger supports the requested antecedent-wet, high-mobility, river-blockage diagnosis: all eight threshold tests pass, and the rainfall ratio is far above the cutoff needed for the final label.

# Scoring Rubric

Total: 20 points.

- Answer schema and final label (4 points): Returns the six requested top-level JSON fields with unit-bearing field names and gives `antecedent_wet_high_mobility_river_blockage`. Partial credit: 2-3 points for a recoverable JSON object with one missing or renamed field; 1 point for the right label without a usable ledger.
- Rainfall ledger (4 points): Computes `218.2 mm`, `4.13 mm`, and `52.83` within tolerance, and uses the stated ratio formula. Partial credit: 2-3 points for correct rainfall values with one rounding or ratio error; 1 point for using the right variables but not completing the ratio.
- Landslide extent ledger (3 points): Reports `40 mph`, `0.5 sq mi`, `18 million tons`, and `36.0 million tons/sq mi`. Partial credit: 1-2 points for two or three correct extent values or for a correct density formula with one wrong input.
- River and context calculations (3 points): Reports `25 ft`, `2.5 mi`, `62.5 ft-mi`, and `context_index_per_100k = 132.51`. Partial credit: 1-2 points for a correct river product or context formula with one incorrect input or rounding error.
- Threshold score ledger (3 points): Applies all eight threshold checks, including the three-part direct-impact index, and reports `8` of `8`. Partial credit: 1-2 points for mostly correct threshold logic with one or two missed pass states.
- Label rule reasoning (2 points): Connects the `8 / 8` score and passing rainfall-ratio check to the final label. Partial credit: 1 point for the correct label without clearly tying it to both required conditions.
- Concise computed interpretation (1 point): Keeps the interpretation tied to the computed ledger and avoids adding extra outcome estimates. Partial credit: 0.5 points for a correct but wordy interpretation that does not change the computed result.
