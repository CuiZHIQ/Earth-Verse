# Arba'at Flood Timing and Exposure Diagnostic

The late-August 2024 Sudan floods included a severe local sequence around Arba'at Dam and the Al Ganap waterway in Red Sea State. A technical review team needs to test whether the local diagnosis is supported by concentrated rainfall, late-window overflow timing, and health-facility exposure counts, rather than by a single maximum rainfall cell or by population-normalized denominators.

Using the quantitative record for the event, compute a compact diagnostic with these rules:

- Precipitation concentration: for each precipitation summary, compute `max_mm / mean_mm`; identify the largest concentration ratio; compute the millimeter gap between the event-scale satellite maximum and the daily rainfall-product maximum.
- Timing: use inclusive day indexing, where `day_index = observation_date - event_start_date + 1`; compute overflow day indices, their fractions of the event window, the assessment day index and fraction, and lags from each overflow observation to the assessment date.
- Facility exposure: compute `likely affected / total listed` and `likely affected / apparently unaffected`.
- Denominator check: compute `affected states / total states`, `population / total listed facilities`, and `population / likely affected facilities`, then decide whether those denominators should control the local diagnosis.

Return only JSON in this structure:

```json
{
  "answer": "",
  "precipitation_concentration": {
    "ratios_by_product": {},
    "largest_product": "",
    "satellite_daily_max_gap_mm": 0
  },
  "timing": {
    "event_window_days": 0,
    "overflow_day_indices": [],
    "overflow_fractions": [],
    "assessment_day_index": 0,
    "assessment_fraction": 0,
    "overflow_to_assessment_lags_days": []
  },
  "facility_exposure": {
    "likely_affected": 0,
    "apparently_unaffected": 0,
    "total_listed": 0,
    "likely_fraction": 0,
    "likely_to_unaffected_ratio": 0
  },
  "denominator_check": {
    "affected_state_fraction": 0,
    "population_per_listed_facility": 0,
    "population_per_likely_affected_facility": 0,
    "use_as_driver": false
  },
  "decision": ""
}
```

Round ratios and fractions to three decimals, millimeter values to three decimals, and population-per-facility values to two decimals.
