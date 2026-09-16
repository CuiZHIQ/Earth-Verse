# Heat-Source Swap Failure Audit

A benchmark reviewer suspects that a solver used a same-window gridded aggregate heat file in place of the local hourly heat-stress file for CSX-006. Audit that source swap using only CSX-006 package-local evidence. Do not use web search, hidden answers, or invented values.

Use package-relative source paths. Return only compact JSON matching this schema:

```json
{
  "answer_type": "expert_error_attribution",
  "audit_ruling": "<source_swap_fails|source_swap_acceptable>",
  "error_class": "<wrong_source_priority|missing_variable|wrong_scale|other>",
  "correct_source": "<package-relative path>",
  "wrong_source": "<package-relative path>",
  "event_window_source": "<package-relative path>",
  "event_window": {"start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
  "first_missing_variable": "<field path or none>",
  "missing_required_fields": ["<field path>"],
  "corrected_answer": {
    "label": "<heat-stress label>",
    "metrics": {
      "max_apparent_temperature_degC": 0.0,
      "hours_apparent_temperature_ge_40c": 0,
      "warm_nights_tmin_ge_27c": 0,
      "max_air_temperature_degC": 0.0
    }
  },
  "wrong_source_numeric_impact": {
    "wrong_available_temperature_field": "<field path>",
    "wrong_available_temperature_value_degC": 0.0,
    "correct_point_air_temperature_max_degC": 0.0,
    "temperature_peak_difference_degC": 0.0,
    "can_compute_apparent_heat_duration": false,
    "can_compute_warm_nights": false
  },
  "rejected_or_insufficient_alternatives": {
    "<package-relative path>": "<short reason>"
  },
  "reference_solving_trace": ["<step>"]
}
```

Decision rules:

- The source swap fails if the substitute file lacks any required field for the local apparent-heat and warm-night calculation.
- Required evidence roles are hourly apparent temperature, daily minimum temperature, and the official event-window dates; only the heat-stress variables need to be present in the candidate heat source, while the dates may come from the locked event-window anchor.
- The corrected label is `sustained_apparent_heat_with_warm_night_exposure` only if the correct source shows maximum apparent temperature at least 42.0 degC, at least 12 hours of apparent temperature at or above 40.0 degC, and at least 5 nights with minimum temperature at or above 27.0 degC.
- Round degree-C values to one decimal place and report `temperature_peak_difference_degC` as correct point air-temperature maximum minus the wrong-source available temperature maximum.
