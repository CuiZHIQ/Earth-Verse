# Correct Answer

```json
{
  "answer": {
    "event_months": 31,
    "cold_oni_months": 25,
    "positive_soi_months": 31,
    "coupled_months": 25,
    "strong_coupled_months": 14,
    "coupled_persistence_score": 0.806,
    "short_slice_fraction": 0.049,
    "people_ratio_min": 4.014
  },
  "classification": "sustained_coupled_event",
  "calculation_note": "The ledger uses 25/31 for coupled persistence, 46/942 for the short precipitation slice, and 20000000/4982987.813 for the people-scale ratio."
}
```

# Computation Path

The event window runs from 2020-09-01 through 2023-03-31, giving 31 monthly index slots and 942 inclusive days. Applying the thresholds to the monthly ONI and SOI tables gives 25 months with ONI <= -0.5, 31 months with SOI > 0, 25 coupled months, and 14 strong coupled months with ONI <= -0.8 and SOI >= 0.7.

The coupled persistence score is `25 / 31 = 0.806`. The short precipitation slice runs from 2020-09-01 through 2020-10-16, so the inclusive fraction is `46 / 942 = 0.049`. The report floor of 20000000 people divided by the compact AOI population of 4982987.813 gives `4.014`.

# Scoring Rubric

- 3 points: Returns compact JSON with the requested numeric fields, classification, and formula note.
- 5 points: Reports the monthly threshold ledger correctly: 31 event months, 25 cold ONI months, 31 positive SOI months, and 25 coupled months.
- 4 points: Reports 14 strong coupled months and computes the persistence score as 25/31 = 0.806.
- 3 points: Uses inclusive dates to compute the short-slice fraction as 46/942 = 0.049.
- 3 points: Computes the people-scale ratio as 20000000/4982987.813 = 4.014.
- 2 points: Keeps count fields integer-valued and rounds derived fractions or ratios to three decimals with clear units.
