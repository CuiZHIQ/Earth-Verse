# Final Answer

```json
{
  "answer": "extreme_persistent_rainfall_deficit_water_supply_drought",
  "window_days": 111,
  "rainfall_ledger_mm": {
    "observed": 203.2,
    "deficit": 558.8,
    "inferred_normal": 762.0
  },
  "rates_mm_day": {
    "observed": 1.83,
    "deficit": 5.03,
    "inferred_normal": 6.86
  },
  "indices": {
    "observed_fraction": 0.267,
    "deficit_index": 0.733,
    "stress_score": 0.733
  },
  "threshold_result": {
    "duration_ge_90": true,
    "observed_fraction_le_0_30": true,
    "deficit_index_ge_0_70": true,
    "record_years_ge_50": true,
    "interpretation": "Observed rain was 27% of normal for 111 days with a 559 mm deficit, meeting every persistence and severity test."
  }
}
```

# Key Computations

The NOAA report was published on 2016-04-20, so the report-effective rainfall window runs from 2016-01-01 through 2016-04-20. Counting both endpoints gives:

```text
window_days = 111
```

The Koror rainfall report gives about 8 inches observed since January, nearly 22 inches below average, and the lowest recorded rainfall in 65 years. The inferred normal rainfall is:

```text
normal_rain_inches = 8 + 22 = 30 inches
```

Depth conversions:

```text
observed_mm = 8 * 25.4 = 203.2 mm
deficit_mm = 22 * 25.4 = 558.8 mm
inferred_normal_mm = 30 * 25.4 = 762.0 mm
```

Daily rates over the 111-day window:

```text
observed_rate = 203.2 / 111 = 1.83 mm/day
deficit_rate = 558.8 / 111 = 5.03 mm/day
normal_rate = 762.0 / 111 = 6.86 mm/day
```

Normalized indices:

```text
observed_fraction = 8 / 30 = 0.267
deficit_index = 22 / 30 = 0.733
stress_score = 0.733 * min(111 / 90, 1) * min(65 / 50, 1) = 0.733
```

# Reasoning Path

The classification rule requires four tests to pass. The duration test passes because 111 days is at least 90 days. The observed-fraction test passes because 0.267 is below 0.30. The deficit-index test passes because 0.733 is above 0.70. The record-span test passes because the reported record-low context is 65 years, above the 50-year threshold.

Since all four tests pass together, the correct label is `extreme_persistent_rainfall_deficit_water_supply_drought`.

# Computed Interpretation

The short-shower alternative fails numerically: over an inclusive 111-day report-effective window, Koror was missing about 559 mm of rainfall while receiving only about 27% of inferred normal rainfall, with a 65-year record-low anchor.

# Scoring Rubric

Total: 20 points.

- Answer schema and units (4 pts): Full credit for the requested six-field JSON, distinct millimeter and millimeter-per-day quantities, and a numeric interpretation sentence. Partial credit: 2-3 points if the JSON is mostly complete but one nested block or unit label is missing; 1 point if the classification is present but the ledger shape is not usable.
- Rainfall ledger (5 pts): Full credit for extracting 8 inches observed and 22 inches below average, computing 30 inches inferred normal, and converting to 203.2 mm, 558.8 mm, and 762.0 mm. Partial credit: 3-4 points for correct inch values with one conversion or inferred-normal error; 1-2 points for using the right quantities but leaving them in inches or mixing observed and deficit depths.
- Duration and rates (3 pts): Full credit for the inclusive 111-day report-effective window and daily rates near 1.83, 5.03, and 6.86 mm/day. Partial credit: 2 points if the day count is correct but one rate is rounded or copied incorrectly; 1 point if the rates are computed with a one-day endpoint error.
- Normalized indices (4 pts): Full credit for observed_fraction near 0.267, deficit_index near 0.733, and stress_score near 0.733 using capped duration and record-span factors. Partial credit: 2-3 points if two of the three indices are correct; 1 point if the ratios use the right numerator values but the wrong denominator or omit one cap.
- Threshold proof and classification (3 pts): Full credit for evaluating all four threshold tests correctly and returning the extreme persistent rainfall-deficit water-supply drought label. Partial credit: 2 points if the final label is correct but one Boolean test is missing; 1 point if the tests are listed but one inequality direction is reversed.
- Bounded interpretation (1 pt): Full credit for rejecting the short-shower interpretation from the calculation while avoiding loss, field-guidance, or broad attribution statements. Partial credit: withhold the point for broad attribution or loss statements that are not computed here.
