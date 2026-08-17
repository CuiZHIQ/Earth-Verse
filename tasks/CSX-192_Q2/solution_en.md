# Final Answer

```json
{
  "answer_type": "western_cape_reported_response_pressure_model",
  "event_context": {
    "event_window": ["2017-06-07", "2017-06-14"],
    "event_window_days": 8,
    "localities": "Knysna, Plettenberg Bay, and the Outeniqua Mountains",
    "mountainous_coastal_setting": true
  },
  "reported_impacts": {
    "evacuated_people": 10000,
    "destroyed_house_lower_bound": 500,
    "smoke_component_count": 3,
    "garden_route_closed": true,
    "charter_request_documented": true,
    "fuel_mosaic_fraction": 1.0,
    "drought_strong_wind_signal": true,
    "patchy_pattern_signal": true
  },
  "process_indices": {
    "impact_load_index": 87.5,
    "process_coupling_index": 93.84,
    "compound_response_pressure": 90.35
  },
  "scenario_analysis": {
    "scenario_evacuated_people": 12000,
    "scenario_destroyed_house_lower_bound": 600,
    "scenario_smoke_persistence_days": 10,
    "scenario_impact_load_index": 90.0,
    "scenario_process_coupling_index": 95.71,
    "scenario_compound_response_pressure": 92.57,
    "compound_pressure_delta": 2.22
  },
  "response_priorities": [
    {
      "rank": 1,
      "priority": "evacuation_shelter_and_house_loss_support",
      "basis": "10000 evacuees, more than 500 houses destroyed, and baseline impact_load_index 87.50"
    },
    {
      "rank": 2,
      "priority": "coastal_access_and_smoke_management",
      "basis": "Garden Route closure plus three smoke signals including week-later smoke, Knysna smoke pall, and offshore smoke front"
    },
    {
      "rank": 3,
      "priority": "fuel_mosaic_and_patchy_burn_mapping",
      "basis": "three fuel types, patchy burn wording, and drought/strong-wind spread signal drive process_coupling_index 93.84"
    }
  ],
  "formula_check": "pass"
}
```

# Key Computations

The event window is 2017-06-07 through 2017-06-14, giving `8` inclusive days.

Report anchors:

- `evacuated_people = 10000`
- `destroyed_house_lower_bound = 500`
- three smoke signals: week-later smoke, smoke pall over Knysna, and offshore smoke front
- Garden Route closure is documented
- International Charter / disaster-response support request is documented
- three fuel types are present: natural forest, dense low coastal forest, and commercial timber plantations
- drought and very strong winds are explicitly linked to spread
- patchy burn pattern is explicitly stated

Baseline:

- `impact_load_index = 87.50`
- `process_coupling_index = 93.84`
- `compound_response_pressure = 0.55 * 87.50 + 0.45 * 93.84 = 90.35`

Scenario:

- evacuated people increase to `12000`
- destroyed-house lower bound increases to `600`
- smoke persistence extends to `10` days
- `scenario_compound_response_pressure = 92.57`
- `compound_pressure_delta = 2.22`

# Reasoning Path

The response pressure is high because the report simultaneously supports evacuation burden, house destruction, persistent smoke, coastal access closure, disaster-response imaging support, fuel-mosaic complexity, and drought/strong-wind spread. The scenario raises pressure mainly through a higher house-loss term and longer smoke persistence.

# Scoring Rubric

Total: 20 points.

- 4 points: Extracts the 8-day event window, localities, mountainous/coastal setting, 10000 evacuees, 500-house lower bound, Garden Route closure, and Charter request.
- 4 points: Counts all three smoke signals, all three fuel mosaic terms, drought/strong-wind signal, and patchy-pattern signal.
- 5 points: Applies the formulas and obtains `impact_load_index = 87.50`, `process_coupling_index = 93.84`, and `compound_response_pressure = 90.35`.
- 3 points: Applies the 20% evacuation and house-loss increases plus 10-day smoke persistence, yielding `scenario_compound_response_pressure = 92.57` and delta `2.22`.
- 2 points: Ranks evacuation/house-loss support, coastal access/smoke management, and fuel mosaic/patchy burn mapping with bases tied to computed drivers.
- 2 points: Returns valid JSON with the requested top-level keys and does not use off-event weather, precipitation, dNBR, WorldPop, or OSM products as scored evidence.
