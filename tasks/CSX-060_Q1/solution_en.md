# Final Answer

```json
{
  "answer": "compound_mountain_flood_landslide;score_6_of_6",
  "label": "compound_mountain_flood_landslide",
  "compound_score": 6,
  "tests": {
    "rainfall_concentration": true,
    "record_rainfall_breadth": true,
    "historic_river_stage": true,
    "landslide_signal": true,
    "flood_exposure_scale": true,
    "kathmandu_local_exposure": true
  },
  "computed_values": {
    "daman_3day_rainfall_mm": 517.0,
    "primary_grid_max_mm": 73.33,
    "station_to_grid_ratio": 7.05,
    "record_24h_station_count": 25,
    "stations_over_200mm": 105,
    "river_gauges_above_historic_count": 5,
    "largest_gauge_exceedance_m": 3.52,
    "exposed_people": 115000,
    "kathmandu_exposed_people": 46000,
    "kathmandu_potentially_affected_structures": 5000
  },
  "decision_rule": "compound if score >= 5 and landslide_signal is true",
  "river_only_check": "River-only flooding fails because all six compound tests pass, including the station-scale rainfall concentration and the reported landslide signal."
}
```

# Key Computations

The highest reported three-day rainfall was Daman at 517.0 mm. The primary gridded event maximum was 73.33 mm, so the rainfall concentration ratio is:

`517.0 / 73.33 = 7.05`

The rainfall concentration test passes because 517.0 mm is at least 500 mm and 7.05 is at least 5.0.

The record rainfall breadth test passes because 25 stations set new 24-hour rainfall records. The station-bin total over 200 mm is:

`68 + 31 + 5 + 1 = 105 stations`

The river-stage test uses observed maximum gauge height minus historic gauge height. Five stations have positive exceedance. The largest is Narayani River at Devghat:

`13.62 m - 10.10 m = 3.52 m`

That passes the threshold of at least four gauges above historic height and largest exceedance greater than 1.0 m.

The landslide signal test passes because the event record states that localized flash floods and landslides damaged homes.

The flood exposure scale test passes because the largest Nepal flood-impact entry gives about 300 km2 of flood-affected land and about 115,000 exposed people.

The Kathmandu local exposure test passes because the Kathmandu entry gives about 46,000 exposed people and about 5,000 potentially affected structures.

# Reasoning Path

1. The event has a sharp station-scale rainfall maximum: Daman reached 517.0 mm over three days, more than seven times the gridded event maximum.
2. The rainfall was not a lone point anomaly: 25 stations set 24-hour records and 105 stations exceeded 200 mm.
3. River response was historically high at multiple gauges, with five exceedances and a 3.52 m maximum exceedance at Devghat.
4. The rainfall episode was explicitly linked to both flash floods and landslides, so a river-only label leaves out a documented hillslope component.
5. Flood-affected land, exposed population, Kathmandu exposure, and potentially affected structures show that the physical hazard intersected settlements at a measurable scale.
6. The decision rule requires score at least 5 and the landslide test to be true. The score is 6 and the landslide test is true, so the compound mountain flood-landslide label is the deterministic result.

# Computed Interpretation

The computed diagnostic shows that the Nepal event was not just a routed river flood: extreme mountain rainfall, widespread record rainfall, historic river stages, reported landslides, and measured exposed population all pass their thresholds in the same event window.

# Scoring Rubric

Total: 20 points.

- Final label and score, 4 points: full credit for `compound_mountain_flood_landslide;score_6_of_6`, the compound label, and the score of 6 out of 6. Partial credit for the correct label with a wrong score, or the right score without the canonical answer string.
- Rainfall concentration and breadth, 4 points: full credit for Daman 517.0 mm, gridded maximum 73.33 mm, ratio 7.05, 25 record-setting stations, and 105 stations over 200 mm. Partial credit for correct rainfall values with one missing formula, threshold, or station-bin total.
- River-stage calculation, 3 points: full credit for five gauges above historic height and Devghat on the Narayani River as the largest exceedance at 3.52 m. Partial credit for identifying the largest station or count but not both, or for a small arithmetic or rounding error.
- Landslide and exposure tests, 4 points: full credit for passing the landslide signal, 300 km2 flood-affected land, 115,000 exposed people, 46,000 Kathmandu exposed people, and 5,000 potentially affected structures. Partial credit for using only national-scale or only Kathmandu-scale exposure values.
- Decision rule and river-only rejection, 3 points: full credit for applying `score >= 5 and landslide_signal is true` and explaining that river-only flooding fails because it omits the rainfall concentration and landslide components. Partial credit for the right final label with an incomplete rule or weak alternative check.
- Concision and bounded inference, 2 points: full credit for returning compact JSON and avoiding extra casualty, road-loss, facility-damage, or slope-area values not computed here. Partial credit for clear reasoning with minor extra prose or minor nonessential fields.
