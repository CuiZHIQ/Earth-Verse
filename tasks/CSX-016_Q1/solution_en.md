# Final Answer

```json
{
  "event_window_days": 46,
  "candidate_tests": [
    {
      "test_id": "regional_heat_field_anchor",
      "computed_value": {
        "event_window_days": 46,
        "mean_tmax_margin_over_40c": 4.65,
        "absolute_tmax_margin_over_40c": 6.25,
        "tmax_spatial_range_c": 4.81
      },
      "evidence_result": "pass",
      "role": "primary_heat_anchor"
    },
    {
      "test_id": "cool_point_scale_anchor",
      "computed_value": {
        "inside_regional_study_box": false,
        "nearest_edge_distance_km": 1431.1,
        "point_tmax_max_c": 27.9,
        "gap_from_regional_max_c": 18.35,
        "gap_from_regional_mean_max_c": 16.75,
        "point_heatload_above_25c_c_days": 5.4,
        "longest_run_tmax_ge_25c_days": 3
      },
      "evidence_result": "fail",
      "role": "not_primary_heat_anchor"
    },
    {
      "test_id": "precipitation_relief_anchor",
      "computed_value": {
        "event_totals_mm": [
          112.73,
          97.41,
          110.37
        ],
        "mean_mm_per_day": [
          2.45,
          2.12,
          2.4
        ]
      },
      "evidence_result": "fail",
      "role": "not_primary_heat_anchor"
    },
    {
      "test_id": "image_surface_anchor",
      "computed_value": {
        "surface_change_pre_count": 0,
        "surface_change_post_count": 0,
        "surface_change_status": "no_sufficient_scenes",
        "event_catalog_count": 0
      },
      "evidence_result": "fail",
      "role": "not_primary_heat_anchor"
    },
    {
      "test_id": "exposure_denominator_anchor",
      "computed_value": {
        "population_millions": 10.849,
        "exposure_weighted_mean_margin_c_million": 50.45
      },
      "evidence_result": "pass",
      "role": "supporting_context"
    }
  ],
  "primary_heat_calibration": {
    "label": "regional_heat_field_calibration",
    "primary_anchor": "regional_heat_field_anchor",
    "supporting_context": [
      "exposure_denominator_anchor"
    ],
    "not_primary_heat_anchors": [
      "cool_point_scale_anchor",
      "precipitation_relief_anchor",
      "image_surface_anchor"
    ]
  },
  "one_sentence_interpretation": "The event calibrates as a severe regional heat-field episode; the cool point, precipitation means, and surface-change counts do not replace the regional Tmax field, while exposure is supporting context."
}
```

# Key Computations

The heat window is inclusive from 2015-05-01 to 2015-06-15, so it contains 46
days. The regional Tmax field clears both heat thresholds: mean maximum margin
above 40 C is `44.65 - 40 = 4.65 C`, absolute maximum margin is
`46.25 - 40 = 6.25 C`, and the internal spatial range is
`46.25 - 41.44 = 4.81 C`.

The point record is not compatible with the regional field. It is outside the
regional study box, 1431.1 km from the nearest edge, and has a daily Tmax
maximum of only 27.9 C. That makes it 18.35 C cooler than the regional maximum
and 16.75 C cooler than the regional mean maximum. Its point heatload above
25 C is 5.4 C-days, with a longest Tmax >=25 C run of 3 days.

The precipitation row fails the stated relief rule: the three event totals of
112.73, 97.41, and 110.37 mm become daily means of 2.45, 2.12, and 2.40 mm/day
over the 46-day window, all below 5.0 mm/day. The surface row also fails because
the pre count, post count, and matching event-catalog count are all 0.

The exposure row is contextual. Population is `10.849` million, and
`10.849 * 4.65 = 50.45 C-million`; this scales the passing heat margin by a
population denominator but does not define heat intensity on its own.

# Reasoning Path

First, compute the regional heat-field margins from the gridded Tmax summary.
Because the window is 46 days and both heat margins clear their thresholds, this
row is the only passing physical primary anchor.

Second, test the nearby point record against the regional study box and
temperature-gap rule. It fails both the location check and the 5 C gap rule, so
its small 25 C heatload cannot calibrate the regional heat episode.

Third, divide all precipitation totals by 46 and apply the two-of-three daily
mean rule. None of the products reaches 5.0 mm/day, so precipitation is not a
heat-relief anchor in this diagnostic hierarchy. The surface-change row also fails because it
has no usable before/after count and no matching catalog record.

Finally, keep exposure as context only. The positive population denominator can
weight the already passing heat-field margin, but it is not a standalone
physical heat metric.

# Computed Interpretation

The calibration is `regional_heat_field_calibration`: the severe regional Tmax
field is the primary heat-severity anchor, and exposure only scales the
population context of that physical signal.

# Scoring Rubric

- 3 points: Returns the requested compact JSON structure with `event_window_days`,
  five named tests, `primary_heat_calibration`, and one concise interpretation.
  Partial credit for a mostly correct structure with one missing required field.
- 5 points: Computes the numeric anchors within tolerance: 46 days; 4.65 C mean
  margin; 6.25 C absolute margin; 4.81 C spatial range; 18.35 C and 16.75 C
  point-record gaps; 2.45, 2.12, and 2.40 mm/day precipitation means; 10.849
  million population; and 50.45 C-million exposure context. Partial credit for
  correct formulas with minor rounding or one omitted secondary value.
- 4 points: Applies the threshold rules correctly: regional heat field passes as
  the primary heat anchor; the point record, precipitation, and surface rows
  fail; exposure is supporting context only. Partial credit for one incorrect
  pass/fail state when the underlying arithmetic is otherwise correct.
- 3 points: Shows row-level reasoning that derives each role from computed
  values and thresholds. Partial credit for correct roles with thin explanation.
- 2 points: Rejects at least two tempting substitutes using calculations,
  especially the cool point, broad-window precipitation means, absent
  surface-change pair, or standalone exposure count. Partial credit for one
  correct rejection.
- 2 points: Keeps the interpretation concise and event-specific, identifying a
  regional heat-field calibration without expanding into a general disaster
  essay. Partial credit for a correct label with extra but harmless prose.
- 1 point: Avoids adding realized-impact or action claims beyond the computed
  evidence hierarchy. No credit here if the answer turns the diagnostic task
  into a response note.

Accept small rounding differences: +/-0.05 C for temperature differences,
+/-0.05 mm/day for precipitation daily means, +/-0.01 million for population in
millions, +/-0.1 for C-million exposure context, and +/-0.5 km for the point
distance.
