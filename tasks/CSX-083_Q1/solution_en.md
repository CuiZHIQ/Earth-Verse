# Final Answer

The compact answer key is `ratio_3.38_extreme_local_maximum`.

```json
{
  "reported_storm_total_mm": 744.8,
  "point_event_total_mm": 220.61,
  "reported_to_point_ratio": 3.38,
  "concentration_class": "spatially concentrated extreme local maximum",
  "computed_interpretation": "The reported local maximum is more than three times the nearby point-window total, so it should be treated as a focused storm maximum rather than an ordinary wet-period accumulation."
}
```

# Key Computations

The event report gives a local storm rainfall total of 744.8 mm at a Beijing reservoir during the Doksuri-remnant flood period. The daily point rainfall series for the event window contains five values:

```text
7.94 + 97.29 + 69.33 + 37.70 + 8.35 = 220.61 mm
```

The concentration ratio is:

```text
744.8 / 220.61 = 3.376..., rounded to 3.38
```

The classification threshold is 3.0. Since 3.38 >= 3.0, the result is a spatially concentrated extreme local maximum.

Numeric tolerance targets:

- `reported_storm_total_mm`: 744.8 mm within 0.1 mm.
- `point_event_total_mm`: 220.61 mm within 0.01 mm.
- `reported_to_point_ratio`: 3.38 within 0.02.

# Reasoning Path

First, treat the 744.8 mm value as the reported local storm-maximum anchor, not as the point-series sum. Second, sum all five daily point rainfall values across 2023-07-29 to 2023-08-02 to obtain 220.61 mm. Third, divide the reported local storm total by the summed point-window total. The ratio is about 3.38, which passes the 3.0 concentration threshold.

The result rules out a same-scale reading in which the reported maximum is merely comparable to the point-window accumulation. The data instead show a strong local maximum relative to the point series.

# Computed Interpretation

For this North China flood episode, the calculation supports a focused extreme-rainfall diagnosis: the local reported storm maximum is about 3.4 times the point-window rainfall total. That interpretation follows from the ratio alone and does not require adding exact loss estimates beyond the computed rainfall comparison.

# Scoring Rubric

Award 20 points total:

- Reported storm rainfall total (4 points): Reports `reported_storm_total_mm` as 744.8 mm within 0.1 mm and identifies it as the reported local storm total. Partial credit for a nearby value or the right number without clear units or role.
- Point event-window rainfall total (4 points): Sums the five daily point rainfall values to 220.61 mm within 0.01 mm. Partial credit for using most daily values correctly with a minor arithmetic or rounding error.
- Rainfall concentration ratio (4 points): Computes `reported_to_point_ratio` as 3.38 within 0.02, or an equivalent about-3.4x comparison. Partial credit for using the correct numerator and denominator with modest rounding error.
- Threshold classification (3 points): Applies the 3.0 decision rule and labels the result as a spatially concentrated extreme local maximum. Partial credit for stating that the reported total is much larger but omitting the threshold test.
- Distinction between local maximum and point-window sum (2 points): Keeps the reported storm maximum separate from the point rainfall sum and does not treat either as a basinwide mean. Partial credit for a minor wording issue that does not change the arithmetic.
- Computed interpretation (2 points): Gives a concise interpretation tied directly to the ratio and the Doksuri-remnant flood episode. Partial credit for a generic extreme-rainfall sentence that does not clearly use the ratio.
- Structured output clarity (1 point): Returns the requested compact JSON-like object with clear units. Partial credit for mostly following the fields with minor formatting or unit omissions.
