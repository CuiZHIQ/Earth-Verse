# Final Answer

```json
{
  "answer": "rainfall_late_overflow_facility_exposure",
  "precipitation_concentration": {
    "ratios_by_product": {
      "era5_land": 1.675,
      "gpm_imerg": 3.105,
      "chirps": 1.765
    },
    "largest_product": "gpm_imerg",
    "satellite_daily_max_gap_mm": 87.786
  },
  "timing": {
    "event_window_days": 24,
    "overflow_day_indices": [18, 19],
    "overflow_fractions": [0.75, 0.792],
    "assessment_day_index": 21,
    "assessment_fraction": 0.875,
    "overflow_to_assessment_lags_days": [3, 2]
  },
  "facility_exposure": {
    "likely_affected": 7,
    "apparently_unaffected": 5,
    "total_listed": 12,
    "likely_fraction": 0.583,
    "likely_to_unaffected_ratio": 1.4
  },
  "denominator_check": {
    "affected_state_fraction": 0.722,
    "population_per_listed_facility": 22494.38,
    "population_per_likely_affected_facility": 38561.79,
    "use_as_driver": false
  },
  "decision": "Use the concentrated-rainfall, late-overflow, facility-exposure diagnostic; do not let a single maximum rainfall cell or population denominator replace the local timing and exposure calculation."
}
```

# Key Computations

The event window runs from 2024-08-13 through 2024-09-05, so inclusive duration is 24 days.

Precipitation concentration:

- ERA5-Land: `171.630 / 102.470 = 1.675`.
- GPM IMERG: `258.840 / 83.362 = 3.105`.
- CHIRPS: `171.054 / 96.895 = 1.765`.
- The largest concentration ratio is GPM IMERG at `3.105`.
- The satellite-to-daily maximum precipitation gap is `258.840 - 171.054 = 87.786 mm`.

Overflow and assessment timing:

- Overflow observations on 2024-08-30 and 2024-08-31 correspond to inclusive day indices `18` and `19`.
- Their event-window fractions are `18 / 24 = 0.750` and `19 / 24 = 0.792`.
- The 2024-09-02 facility assessment is day `21`, or `21 / 24 = 0.875` of the event window.
- The assessment lags the two overflow observations by `3` and `2` days.

Facility and denominator calculations:

- Facility count ledger: `7` likely affected, `5` apparently unaffected, `12` total listed.
- Likely affected fraction: `7 / 12 = 0.583`.
- Likely-to-unaffected ratio: `7 / 5 = 1.400`.
- Affected-state fraction: `13 / 18 = 0.722`.
- Population per listed facility: `269932.556 / 12 = 22494.38`.
- Population per likely affected facility: `269932.556 / 7 = 38561.79`.

# Reasoning Path

1. The rainfall products agree that rainfall was substantial, but the diagnostic concentration signal is strongest in GPM IMERG: its `3.105` max-to-mean ratio is much larger than the ERA5-Land and CHIRPS ratios.
2. The maximum-cell result is not sufficient by itself, because the timing ledger places overflow observations at days `18` and `19`, late in a 24-day event window, followed by the day-21 facility assessment.
3. The facility ledger gives a local receptor count: `7 / 12 = 0.583` of listed health facilities are in the likely affected group, with a `1.4` likely-to-unaffected ratio.
4. The broader state and population denominators are useful context checks, but they do not control the local diagnosis because they do not encode the rainfall concentration, overflow timing, or listed-facility split.

# Computed Interpretation

The computed result supports a concentrated-rainfall plus late-overflow sequence linked to local facility exposure. The correct compact answer is therefore `rainfall_late_overflow_facility_exposure`, with population-normalized denominators treated as non-controlling context.

# Scoring Rubric

- 3 points: Correct answer label and JSON shape. Full credit requires the requested JSON fields and the label `rainfall_late_overflow_facility_exposure` or a clearly equivalent compact label. Partial credit: 1-2 points for a mostly complete structure with one or two missing fields, or for a label that captures only rainfall plus overflow without facility exposure.
- 4 points: Precipitation concentration arithmetic. Full credit requires the three ratios `1.675`, `3.105`, and `1.765`, identifies GPM IMERG as largest, and gives the `87.786 mm` maximum gap. Partial credit: 2-3 points for correct ratios with one rounding or naming error; 1 point for using the right formula but missing most values.
- 4 points: Overflow timing reconstruction. Full credit requires a 24-day event window, overflow days `[18, 19]`, fractions `[0.750, 0.792]`, assessment day `21`, assessment fraction `0.875`, and lags `[3, 2]`. Partial credit: 2-3 points for correct dates and lags with an indexing or rounding error; 1 point for recognizing the late-window sequence without the numeric ledger.
- 3 points: Facility exposure ratios. Full credit requires `7` likely affected, `5` apparently unaffected, `12` total, likely fraction `0.583`, and likely-to-unaffected ratio `1.400`. Partial credit: 1-2 points for correct counts with one missing ratio or a small arithmetic error.
- 3 points: Denominator check. Full credit requires `13 / 18 = 0.722`, `22494.38` population per listed facility, `38561.79` population per likely affected facility, and `use_as_driver: false`. Partial credit: 1-2 points for computing the denominators but not clearly rejecting them as the controlling local metric.
- 2 points: Calculation-linked decision. Full credit connects rainfall concentration, late overflow timing, and facility exposure while rejecting single-cell rainfall and population-denominator substitutes. Partial credit: 1 point for a correct final decision that omits one computed support.
- 1 point: Concise computed interpretation. Full credit keeps the interpretation limited to what the diagnostic calculates and avoids extra assertions about precise flood depth, velocity, mortality, or facility service status. Partial credit: 0.5 points for minor extra wording that does not change the answer.
