# Arid-Wadi Flood Coupling and Humanitarian Access Stress Model

The August-September 2024 flooding around Port Sudan and the Arba'at Dam was not just a rainfall total problem. It involved heavy rain falling onto terrain and channels with limited usual runoff tolerance, visible wet-channel or floodwater response, service disruption, and humanitarian access pressure.

Using only the local CSX-054 event package, select package-relative evidence for every source value and qualitative process claim used in the final JSON.

Compute the following process model. Use `clip(x)` to mean clipping to the range 0 to 1.

1. Determine the inclusive event duration `D` from the package event window.
2. From the available accumulated-precipitation products, take the maximum event accumulation from each product. Let `Pmax` be the largest of those maxima and `N170` be the count of products with maxima at least 170 mm.
3. Compute:

```text
peak_norm = clip(Pmax / 300)
product_consensus_norm = N170 / 3
daily_load_norm = clip((Pmax / D) / 15)
rainfall_load_score =
100 * (0.45 * peak_norm
     + 0.30 * product_consensus_norm
     + 0.25 * daily_load_norm)
```

4. From the report narrative and dam or waterway impact record, set:

```text
dam_waterway_norm = 1 if Arba'at Dam evidence reports both reduced reservoir level and overflow or flooded-waterway evidence, otherwise 0
arid_channel_norm = 1 if the event narrative links heavy rain/runoff to arid, ephemeral, or unusually runoff-sensitive channels or areas, otherwise 0
```

5. From the radar pre/post change summary and the annual satellite-embedding change summary, compute:

```text
radar_range_db = radar_change_max_db - radar_change_min_db
surface_change_norm =
0.70 * clip(radar_range_db / 40)
+ 0.30 * clip(embedding_change_max / 1.0)
```

Then compute:

```text
routing_surface_score =
100 * (0.40 * rainfall_load_score / 100
     + 0.25 * dam_waterway_norm
     + 0.20 * surface_change_norm
     + 0.15 * arid_channel_norm)
```

6. Compute humanitarian access stress:

```text
population_norm = clip(AOI_population / 300000)
facility_share = likely_affected_health_facilities / (likely_affected_health_facilities + apparently_unaffected_health_facilities)
state_fraction = flooded_states / total_states
displaced_norm = clip(displaced_people / 150000)
state_displacement_norm = 0.5 * state_fraction + 0.5 * displaced_norm
road_aid_disruption_norm = 1 if the report links flood damage to road/infrastructure disruption and curtailed aid delivery, otherwise 0

humanitarian_access_score =
100 * (0.30 * population_norm
     + 0.25 * facility_share
     + 0.25 * state_displacement_norm
     + 0.20 * road_aid_disruption_norm)
```

7. Compute the baseline compound index:

```text
compound_flood_response_index =
100 * (0.40 * rainfall_load_score / 100
     + 0.30 * routing_surface_score / 100
     + 0.30 * humanitarian_access_score / 100)
```

8. Recompute the index for a wetter/higher-exposure stress test: increase all accumulated-rainfall maxima by 20%, increase AOI population and displaced people by 15%, and keep event duration, facility share, dam/waterway evidence, road/aid evidence, and remote-sensing terms unchanged.

Return one valid JSON object with exactly these top-level fields:

```json
{
  "process_model": {
    "event_window": {"start_date": "", "end_date": "", "inclusive_days": 0},
    "rainfall_load": {
      "product_maxima_mm": {},
      "peak_mm": 0,
      "products_ge_170": 0,
      "daily_load_mm_day": 0,
      "rainfall_load_score": 0
    },
    "routing_and_surface_response": {
      "dam_waterway_norm": 0,
      "arid_channel_norm": 0,
      "radar_range_db": 0,
      "surface_change_norm": 0,
      "routing_surface_score": 0
    },
    "humanitarian_access_stress": {
      "population": 0,
      "facility_share": 0,
      "state_fraction": 0,
      "displaced_people": 0,
      "state_displacement_norm": 0,
      "road_aid_disruption_norm": 0,
      "humanitarian_access_score": 0
    },
    "compound_flood_response_index": 0,
    "classification": ""
  },
  "scenario_analysis": {
    "scenario": "20_percent_more_event_rainfall_and_15_percent_more_people_exposed",
    "compound_flood_response_index": 0,
    "delta_from_baseline": 0,
    "classification": ""
  },
  "mechanism_chain": [],
  "source_paths": []
}
```

Round scores and continuous metrics to two decimals, except proportions and normalized components may be rounded to three decimals. Use the classification `"extreme compound flood-response stress"` for an index of at least 90, `"very high compound flood-response stress"` for 80 to below 90, `"high compound flood-response stress"` for 65 to below 80, and `"moderate compound flood-response stress"` below 65.
