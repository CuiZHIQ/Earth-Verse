# Correct Answer

Canonical answer key: ledger_score_1.0_gate_hits_7_of_7.

```json
{
  "answer": {
    "local_total_mm": 586.8,
    "peak_day": "20210720",
    "peak_mm": 334.6,
    "nonpeak_mm": 252.2,
    "peak_share": 0.57,
    "peak_to_remainder_ratio": 1.327,
    "regional_hourly_max_mm": 460.1,
    "regional_event_max_mm": 523.3,
    "population_million": 17.68,
    "roads": 130,
    "critical_facilities": 838,
    "facility_density_per_million": 47.41,
    "road_to_facility_ratio": 0.155,
    "surface_change_mean": 0.038,
    "surface_change_max": 0.72,
    "surface_change_max_to_mean": 18.86,
    "gate_hits": 7,
    "gate_total": 7,
    "ledger_score": 1.0
  },
  "calculation_note": "The 334.6 mm peak day supplies 57.0% of the 586.8 mm local event total, while all seven rainfall, urban-inventory, and annual-change gates clear."
}
```

# Key Computations

The local daily corrected precipitation values sum to 586.81 mm, rounded to 586.8 mm. The largest daily value is 334.6 mm on 20210720. The non-peak remainder is 586.81 - 334.6 = 252.21 mm, rounded to 252.2 mm. The peak-day share is 334.6 / 586.81 = 0.570, and the peak-to-remainder ratio is 334.6 / 252.21 = 1.327.

The regional hourly-aggregate precipitation maximum is 460.1 mm, and the regional event-accumulation maximum is 523.3 mm. The mapped population is 17.68 million. The bounded urban slice contains 130 roads and 838 critical facilities, where critical facilities equal schools + hospitals + shelters + police + fire stations. Facility density is 838 / 17.676127 = 47.41 per million people, and the road-to-facility ratio is 130 / 838 = 0.155.

The annual surface-change mean is 0.038 and the maximum is 0.720. Using the unrounded source values, the max-to-mean ratio is 18.86. The seven gates all evaluate true: peak share 0.570 > 0.50, non-peak rainfall 252.2 < 300 mm, regional hourly maximum 460.1 >= 400 mm, regional event maximum 523.3 >= 500 mm, population 17.68 >= 10 million, critical facilities 838 >= 800, and annual surface-change mean 0.038 < 0.05. The ledger score is 7 / 7 = 1.0.

# Reasoning Path

The answer is deterministic because every requested field is derived from structured numeric records. The rainfall ledger first establishes temporal concentration in the Zhengzhou point series, then verifies that the regional precipitation fields are also high enough to satisfy both rainfall gates. The urban inventory calculations add density and service-facility anchors as inventory metrics. The annual surface-change ratio is retained as a separate numeric contrast, with the gate based on the mean value.

# Scoring Rubric

- 4 points: Computes the local rainfall total, peak date, and peak-day rainfall with correct units and rounding.
- 4 points: Computes non-peak rainfall, peak-day share, and peak-to-remainder ratio accurately.
- 3 points: Uses the two regional precipitation maxima and applies their numeric gates correctly.
- 3 points: Computes population, road count, critical-facility count defined as school/hospital/shelter/police/fire-station amenities, facility density, and road-to-facility ratio.
- 2 points: Computes annual surface-change mean, maximum, and max-to-mean contrast.
- 3 points: Reports all seven gate outcomes, gate count, and ledger score.
- 1 point: Returns compact JSON with field names that preserve units and a one-sentence calculation note.

Total: 20 points.
