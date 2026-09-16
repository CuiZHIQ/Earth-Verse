# Seismic Facility-Imbalance Ledger

A technical audit is checking a numeric ledger for the 27 February 2010 Maule, Chile earthquake-tsunami event. Use the local package data to extract the event magnitude, depth, alert level, hazard family, event name, bounded OSM amenity counts, and WorldPop population total. Treat every amenity element in the bounded OSM slice as part of the denominator.

Use these definitions:

- `alert_numeric = {"Green": 1, "Orange": 2, "Red": 3}[alert_level]`
- `compound_flag = int(hazard_family == "earthquake_tsunami_geophysical" and "tsunami" in event_name.lower())`
- `seismic_depth_score = magnitude * alert_numeric / sqrt(depth_km)`
- `school_share = school_count / amenity_element_count`
- `safety_care_ratio = (police_count + fire_station_count) / (hospital_count + shelter_count)`
- `population_per_non_school_amenity = population_sum / (amenity_element_count - school_count)`
- `population_per_care_node = population_sum / (hospital_count + shelter_count)`

Apply these thresholds:

- `seismic_depth` passes when `magnitude >= 8.5`, `depth_km <= 70`, `alert_numeric == 3`, and `seismic_depth_score >= 4`.
- `compound_link` passes when `compound_flag == 1`.
- `facility_imbalance` passes when `school_share >= 0.90` and `safety_care_ratio >= 5`.
- `population_load` passes when `population_per_non_school_amenity >= 100000` and `population_per_care_node >= 900000`.

Set `ledger_score` to the number of passing rows. Use `compound_seismic_high_facility_imbalance` only when all four rows pass; otherwise use `partial_numeric_match`.

Return only compact JSON:

```json
{
  "result": {
    "ledger_score": 0,
    "final_numeric_label": "",
    "seismic_depth_score": 0,
    "school_share": 0,
    "safety_care_ratio": 0,
    "population_per_non_school_amenity": 0,
    "population_per_care_node": 0
  },
  "ledger": [
    {"row": "seismic_depth", "values": {}, "threshold_result": ""},
    {"row": "compound_link", "values": {}, "threshold_result": ""},
    {"row": "facility_imbalance", "values": {}, "threshold_result": ""},
    {"row": "population_load", "values": {}, "threshold_result": ""}
  ],
  "calculation_note": ""
}
```
