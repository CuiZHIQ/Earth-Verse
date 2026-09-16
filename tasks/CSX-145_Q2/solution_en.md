# Final Answer

```json
{
  "answer": "extreme_compound_wind_rain_impact_load",
  "answer_type": "score_ledger",
  "canonical_stance": "Yagi reaches the extreme compound wind-rain impact load class because all four tests score 3.",
  "forbidden_claims": [
    "Do not use the elevated or limited class.",
    "Do not claim outage, flood depth, building-level damage, or full landslide inventory."
  ],
  "required_claims": [
    "Wind scores 3: 213 km/h and 133 mph.",
    "Rain scores 3: 254.0 mm report rain.",
    "Impact scores 3: flood or landslide terms, 179 deaths, and 47,500 houses.",
    "Public-service scores 3: 2,485,012.26 people and 89 amenities."
  ],
  "required_metrics": {
    "amenities": 89,
    "deaths": 179.0,
    "houses": 47500.0,
    "population": 2485012.26,
    "rain_mm": 254.0,
    "wind_kmh": 213.0,
    "wind_mph": 133.0
  },
  "score_ledger": {
    "impact": 3,
    "public_service": 3,
    "rainfall": 3,
    "wind": 3
  },
  "total_index_score": 12
}
```

The correct final load class is **extreme compound wind-rain impact load**, with a Compound Impact Load Index of **12 out of 12**.

Primary ground-truth answer: `extreme_compound_wind_rain_impact_load`.

The four component scores are wind severity **3**, rainfall severity **3**, impact cascade **3**, and public-service exposure load **3**. All four threshold tests reach their maximum score, so the event belongs in the top index band rather than either lower class.

# Key Computations

`compute_gt.py` reads the local CSX-145 records used for this index: the UN and NOAA event reports, the event anchor JSON, the WorldPop exposure population summary, and the Overpass public-service amenity extract.

Intermediate values:

- Event window: **2024-09-01 to 2024-09-07**.
- Strongest wind values: **213 km/h**, **133 mph**, and **125 mph**. Wind severity scores **3** because the event reaches at least 200 km/h and at least 125 mph.
- Report rainfall: **10 inches = 254.0 mm**; paired **25 cm = 250.0 mm**. Rainfall severity scores **3** because the supported reported rainfall reaches at least 250 mm.
- Impact cascade values: flooding or landslide terms are present, deaths are **at least 179**, evacuation is **over 50,000** people, and damaged or destroyed houses are **over 47,500**. Impact cascade scores **3** because flooding or landslides are reported with at least 100 deaths and at least 10,000 damaged or destroyed houses.
- Public-service exposure values: WorldPop package exposure population sum **2,485,012.26** and **89** counted public-service amenities, consisting of 25 hospitals, 33 police facilities, 7 fire stations, 12 shelters, and 12 schools. Public-service exposure load scores **3** because the exposure population exceeds 1,000,000 and the amenity count exceeds 75.

Total index score:

`3 + 3 + 3 + 3 = 12`

# Reasoning Path

The index is computed by applying each threshold test to the strongest supported value for that component, then summing the four component scores. The wind component reaches the maximum score through the 213 km/h value and the 125+ mph values. The rainfall component also reaches the maximum score because the supported reported rainfall is at least 250 mm.

The impact component is a reported-loss threshold test, not just a storm-intensity proxy. Flooding or landslides are present, and both the death threshold and damaged-or-destroyed-house threshold are exceeded. The public-service exposure component also reaches the maximum score because the package exposure population estimate is over one million and the counted amenity total is 89. The resulting ledger is 3, 3, 3, and 3. A score of 12 maps to the 10-12 top band, **extreme compound wind-rain impact load**.

# Computed Interpretation

The computed result identifies Yagi as a top-band compound impact case: severe wind and heavy rain coincide with reported flood or landslide impacts, high deaths, extensive house damage, and a dense population and public-service setting. The index does not establish asset-level outages, flood depth, a building-level damage map, or a full landslide inventory; it establishes the top load class from the stated hazard, impact, population, and amenity thresholds.

# Scoring Rubric

Award up to **20 points**:

- **4 points - Final score and load class:** Gives total score **12/12** and the class **extreme compound wind-rain impact load**. Partial credit for the correct top-band class with a missing or slightly misstated score.
- **4 points - Component-score ledger:** Correctly reports wind severity **3**, rainfall severity **3**, impact cascade **3**, and public-service exposure load **3**. Partial credit for three correct component scores or for a correct total with one component mislabeled.
- **3 points - Wind and rainfall anchors:** Uses the relevant wind and rainfall values, including 213 km/h or 125+ mph winds and supported reported rainfall at or above 250 mm. Partial credit for correct threshold logic with incomplete or approximate values.
- **3 points - Impact and exposure anchors:** Connects flooding or landslides with at least 179 deaths, over 47,500 damaged or destroyed houses, package exposure population above 1,000,000, and 89 public-service amenities. Partial credit for including only the impact thresholds or only the exposure thresholds.
- **3 points - Index arithmetic and class mapping:** Shows that `3 + 3 + 3 + 3 = 12` and maps 12 to the 10-12 top band. Partial credit for correct arithmetic without the class mapping, or correct class mapping with one arithmetic slip.
- **2 points - Concise computed interpretation:** Ties the top-band result to the combined wind, rain, reported-loss, population, and public-service indicators without turning the answer into a broad disaster narrative. Partial credit for a generic interpretation that is only partly tied to the computed values.
- **1 point - Output discipline:** Keeps the answer concise, follows the requested 1-2 paragraph format, and avoids extra-data claims such as asset-level outages, flood-depth values, building-level mapping, or a complete landslide inventory. Partial credit if the answer is mostly concise but includes minor off-format material.
