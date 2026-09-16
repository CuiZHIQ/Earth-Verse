# Final Answer

The expected compact label is `late_phase_rainfall_runoff_dominant_signal`, with `diagnostic_class` set to `high`.

Expected core JSON:

```json
{
  "answer": "late_phase_rainfall_runoff_dominant_signal",
  "diagnostic_class": "high",
  "numeric_anchors": {
    "event_total_point_rain_mm": 393.6,
    "late_phase_point_rain_mm": 136.6,
    "gridded_rainfall_mean_mm": 118.113,
    "exposed_population_context": 701660.812
  },
  "derived_tests": {
    "late_phase_share_of_event_point_rain": 0.347,
    "gridded_mean_to_late_point_rain_ratio": 0.865
  },
  "structured_findings": {
    "dominant_signal": "Cyclone Freddy's final southern Africa phase is best diagnosed as a late-phase rainfall-runoff signal.",
    "closest_alternative": "Wind intensity is the closest competing reading because Freddy was a tropical cyclone, but the late rainfall ledger and flood timing give it less weight for this target.",
    "timing_test": "The 2023-03-12 through 2023-03-15 rainfall window aligns with the 2023-03-13 through 2023-03-16 Malawi flood catalog entry.",
    "rainfall_test": "Late point rainfall is 34.7% of the event point total, and the paired gridded mean is 86.5% of that late point amount.",
    "imagery_or_exposure_context": "Population, mapped-place, and imagery/change context support analytic importance but should not be treated as direct proof of inundated population, damage, or disruption."
  }
}
```

# Key Computations

`compute_gt.py` reads the local CSX-122 Cyclone Freddy records and regenerates `computed_gt.json` without network access. The task is a hybrid short-answer evaluation: the label, class, numeric anchors, and derived tests are exact targets, while the concise diagnostic reasoning is graded by rubric.

Important anchors:

- Locked event: Cyclone Freddy across Madagascar, Mozambique, and Malawi, 2023-02-06 through 2023-03-15.
- Long-lived cyclone context from the technical report: about 36.0 days at tropical storm status or higher and about 12,785 km traveled.
- Catalog sequence: a red tropical-cyclone feature for Mozambique and Madagascar ending 2023-03-12, followed by an orange Malawi flood feature during 2023-03-13 to 2023-03-16.
- Point rainfall total during the event window: 393.6 mm.
- Late-phase point rainfall from 2023-03-12 through 2023-03-15: 136.6 mm.
- Paired gridded rainfall mean: `(115.284 + 120.942) / 2 = 118.113 mm`.
- Late-phase share of event point rainfall: `136.6 / 393.6 = 0.347`.
- Gridded-mean to late-point-rain ratio: `118.113 / 136.6 = 0.865`.
- Exposure-population context: 701,660.812 people.
- Point wind-gust context: maximum gust of 65.9 km/h, which is cyclone context but not the strongest late-phase diagnostic signal.
- Imagery/change summaries and exposure layers provide context only. They are not event-specific inundation maps, damage inventories, or proof of asset disruption.

# Reasoning Path

1. Separate the candidate readings. Wind intensity, long track persistence, exposed settlements, and image change are all relevant context, but the requested late-phase finding must be anchored in the final days of the southern Africa record.

2. Use the timing ledger first. The tropical-cyclone catalog feature ends on 2023-03-12, and the Malawi flood feature spans 2023-03-13 to 2023-03-16. That sequence lines up with the 2023-03-12 through 2023-03-15 rainfall window, so the final phase is more rainfall-led than wind-led.

3. Use the rainfall arithmetic. The point record totals 393.6 mm, including 136.6 mm in the late phase. That late segment alone is 34.7% of the point total. The paired gridded mean of 118.113 mm is 86.5% of the late point amount, so the gridded summaries independently support a substantial rainfall signal.

4. Keep wind, track persistence, and imagery as secondary readings. Freddy's duration and track length explain why the event had broad context, and 65.9 km/h gusts show that wind was present. However, those values do not outweigh the late rainfall ledger for the final-phase diagnostic target.

5. Treat exposure and imagery carefully. Population and mapped-place context make the signal analytically important, and imagery/change summaries can support broad landscape context. They do not establish inundated population, specific building damage, hospital disruption, or road closure.

# Computed Interpretation

The computed ledger supports a high late-phase rainfall-runoff signal for Cyclone Freddy's final southern Africa phase. The strongest answer gives the rainfall label and class, reports the four numeric anchors and two derived ratios, and explains why wind, track persistence, and image change receive less weight for this specific late-phase diagnostic target.

# Scoring Rubric

Award 20 points total:

- 4 points: Correct final label and class. Full credit for `late_phase_rainfall_runoff_dominant_signal` or a clearly equivalent late-phase rainfall-runoff label plus `high` diagnostic class. Partial credit for identifying heavy rainfall or flooding but missing either the late-phase framing or the class.
- 4 points: Numeric anchors. Award up to 1 point each for event-total point rainfall 393.6 mm within 0.5 mm, late-phase point rainfall 136.6 mm within 0.5 mm, paired gridded mean rainfall 118.113 mm within 1.0 mm, and exposure-population context 701,660.812 people within 1 person.
- 3 points: Derived arithmetic. Full credit for computing late-phase share as 0.347 and gridded-mean to late-point-rain ratio as 0.865, with clear denominators. Partial credit for one correct ratio or for correct formulas with minor rounding error.
- 3 points: Timing ledger. Full credit for connecting the February-March Cyclone Freddy record to the 2023-03-12 through 2023-03-15 rainfall phase and the 2023-03-13 through 2023-03-16 Malawi flood catalog entry. Partial credit for recognizing late timing without linking both date windows.
- 2 points: Competing readings. Full credit for treating wind intensity, track persistence, or image-visible landscape change as plausible but less supported for the late-phase target. Partial credit for naming alternatives without explaining why the rainfall ledger carries more weight.
- 2 points: Imagery and exposure discipline. Full credit for using population and imagery/change context without converting it into realized inundation, casualties, building damage, hospital disruption, or road closure. Partial credit for mild overstatement that does not drive the answer.
- 2 points: Structured output. Full credit for returning the requested JSON with the label, class, numeric anchors, derived tests, and concise findings. Partial credit for mostly correct content with minor formatting or field-name errors.
