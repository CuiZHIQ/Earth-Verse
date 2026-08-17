# September 2024 Nepal Compound Flood-Landslide Diagnostic

A hydrometeorology review team is checking whether the late-September 2024 Nepal event satisfies a compound mountain flood-landslide classification rather than a river-only flood classification.

Compute a six-test compound diagnostic from the technical record. Award one compound-support test for each condition that is satisfied:

1. `rainfall_concentration`: highest reported three-day station rainfall is at least 500 mm and the station-to-gridded-maximum ratio is at least 5.0.
2. `record_rainfall_breadth`: at least 20 stations set new 24-hour rainfall records and at least 100 stations exceeded 200 mm.
3. `historic_river_stage`: at least four river gauges exceeded their historic gauge height and the largest exceedance is greater than 1.0 m.
4. `landslide_signal`: the event record links the rainfall episode to flash floods and landslides damaging homes.
5. `flood_exposure_scale`: flood-affected land is at least 100 km2 and exposed population is at least 50,000 people.
6. `kathmandu_local_exposure`: Kathmandu-area exposed population is at least 40,000 people and potentially affected structures are at least 4,000.

Return only compact JSON with this structure:

```json
{
  "answer": "compound_mountain_flood_landslide;score_N_of_6",
  "label": "compound_mountain_flood_landslide or river_only_flood",
  "compound_score": 0,
  "tests": {
    "rainfall_concentration": true,
    "record_rainfall_breadth": true,
    "historic_river_stage": true,
    "landslide_signal": true,
    "flood_exposure_scale": true,
    "kathmandu_local_exposure": true
  },
  "computed_values": {
    "daman_3day_rainfall_mm": 0,
    "primary_grid_max_mm": 0,
    "station_to_grid_ratio": 0,
    "record_24h_station_count": 0,
    "stations_over_200mm": 0,
    "river_gauges_above_historic_count": 0,
    "largest_gauge_exceedance_m": 0,
    "exposed_people": 0,
    "kathmandu_exposed_people": 0,
    "kathmandu_potentially_affected_structures": 0
  },
  "decision_rule": "compound if score >= 5 and landslide_signal is true",
  "river_only_check": "one sentence explaining why the river-only label fails or passes"
}
```
