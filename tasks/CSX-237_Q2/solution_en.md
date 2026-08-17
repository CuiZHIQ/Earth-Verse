# Correct Answer

```json
{
  "result": {
    "ledger_score": 4,
    "final_numeric_label": "compound_seismic_high_facility_imbalance",
    "seismic_depth_score": 4.462,
    "school_share": 0.945,
    "safety_care_ratio": 8.167,
    "population_per_non_school_amenity": 105885.0,
    "population_per_care_node": 970612.5
  },
  "ledger": [
    {
      "row": "seismic_depth",
      "values": {
        "magnitude": 8.8,
        "depth_km": 35.0,
        "alert_numeric": 3,
        "seismic_depth_score": 4.462
      },
      "threshold_result": "pass"
    },
    {
      "row": "compound_link",
      "values": {
        "compound_flag": 1,
        "hazard_family": "earthquake_tsunami_geophysical"
      },
      "threshold_result": "pass"
    },
    {
      "row": "facility_imbalance",
      "values": {
        "school_share": 0.945,
        "safety_care_ratio": 8.167,
        "safety_nodes": 49,
        "care_nodes": 6
      },
      "threshold_result": "pass"
    },
    {
      "row": "population_load",
      "values": {
        "population_sum": 5823675.1,
        "non_school_amenities": 55,
        "population_per_non_school_amenity": 105885.0,
        "population_per_care_node": 970612.5
      },
      "threshold_result": "pass"
    }
  ],
  "calculation_note": "All four rows pass: the ledger combines 8.8 magnitude, 35.0 km depth, Red alert, a 0.945 school share, a 49:6 safety-care split, and 5823675.1 people."
}
```

# Calculation Path

The GDACS Chile feature gives magnitude `8.8`, alert level `Red`, and depth `35.0 km`, so `alert_numeric = 3` and `8.8 * 3 / sqrt(35.0) = 4.462`. The event metadata and event name give `compound_flag = 1`.

The bounded OSM amenity slice has 1000 elements: 945 schools, 36 police nodes, 13 fire stations, 3 hospitals, and 3 shelters. Therefore `school_share = 945 / 1000 = 0.945`, `safety_care_ratio = (36 + 13) / (3 + 3) = 8.167`, and `non_school_amenities = 55`.

WorldPop gives `population_sum = 5823675.129996518`, so `population_per_non_school_amenity = 5823675.129996518 / 55 = 105885.0` and `population_per_care_node = 5823675.129996518 / 6 = 970612.5`. Each computed row clears its threshold, giving `ledger_score = 4`; because all four rows pass, the label rule returns `compound_seismic_high_facility_imbalance`.

The OSM and WorldPop files are used for declared derived counts and totals only. Their internal georeferencing metadata is not part of this numeric label.

# Scoring Rubric

- 3 points: Returns compact JSON with the requested result block, four ledger rows, `ledger_score`, and final numeric label.
- 4 points: Extracts the correct structured anchors: magnitude `8.8`, depth `35.0`, Red alert as `3`, compound flag `1`, the six amenity counts from the declared OSM-derived statistics, and WorldPop population from the declared total.
- 5 points: Computes the five derived metrics within tolerance: `4.462`, `0.945`, `8.167`, `105885.0`, and `970612.5`.
- 4 points: Applies all four threshold tests correctly and reports each row as `pass`.
- 2 points: Reports `ledger_score = 4` with label `compound_seismic_high_facility_imbalance`.
- 2 points: Uses unitless ratios and people-per-node loads with clear rounding.
