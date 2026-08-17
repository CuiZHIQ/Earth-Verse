# Western Cape Wildfire Reported Process and Response-Pressure Scenario Model

Use only the local CSX-192 event package. Build a structured JSON analysis of the June 2017 Western Cape Knysna and Plettenberg Bay wildfires as a coupled process-and-response problem grounded in the event report.

Infer the inclusive event window from the event anchor. Extract the reported evacuation count, destroyed-house lower bound, smoke-persistence signals, Garden Route access closure, fuel mosaic, drought/strong-wind spread signal, patchy burn wording, mountainous/coastal setting, and whether disaster-response agencies requested satellite/ISS support.

Use these formulas, with `clip(x) = min(1, max(0, x))`:

```text
evacuation_norm = clip(evacuated_people / 10000)
house_loss_norm = clip(destroyed_house_lower_bound / 1000)
smoke_norm = present smoke signals / 3
access_norm = 1 if the Garden Route closure is documented, else 0
charter_request_norm = 1 if the International Charter / response-agency support request is documented, else 0

impact_load_index =
100 * (0.30 * evacuation_norm
     + 0.25 * house_loss_norm
     + 0.20 * smoke_norm
     + 0.15 * access_norm
     + 0.10 * charter_request_norm)
```

Use three smoke signals: smoke visible about a week after ignition, smoke pall over Knysna, and a long offshore smoke front.

```text
fuel_mosaic_fraction = present fuel types among natural forest, dense low coastal forest, and commercial timber plantations / 3
smoke_persistence_ratio = clip(week_later_smoke_days / event_window_days)
event_duration_factor = clip(event_window_days / 14)

process_coupling_index =
100 * (0.30 * drought_strong_wind_norm
     + 0.25 * fuel_mosaic_fraction
     + 0.20 * patchy_pattern_norm
     + 0.15 * smoke_persistence_ratio
     + 0.10 * event_duration_factor)
```

```text
compound_response_pressure =
0.55 * impact_load_index
+ 0.45 * process_coupling_index
```

Run a planning scenario in which destroyed-house lower bound increases by 20%, evacuated people increase by 20%, and smoke persistence is extended to 10 days. Recompute `impact_load_index`, `process_coupling_index`, and `compound_response_pressure`.

Return valid JSON with exactly these top-level keys:

- `answer_type`
- `event_context`
- `reported_impacts`
- `process_indices`
- `scenario_analysis`
- `response_priorities`
- `formula_check`

Round numeric outputs to two decimals except dates, counts, Booleans, and source paths. The `response_priorities` field should rank three operational priorities and tie each to the computed drivers.
