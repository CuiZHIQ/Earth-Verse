# Heat-Drought Response Priority Ranking

An emergency science cell is preparing a July-August 2022 heat-wave and drought operations brief for the Yangtze River basin and southern China. The local package contains daily and hourly weather, precipitation summaries, a Poyang/Yangtze low-water report, population exposure, and mapped critical amenities.

Build a response-priority ranking from package-local evidence. The model must compute the heat-health and hydrologic stress quantities, compare the candidate priorities, cite package-relative evidence, and explain why the top priority is not selected from a single isolated number.

Rank these four candidate priorities from highest to lowest:

- `cooling_health_and_night_recovery`
- `lake_low_water_and_water_supply`
- `evaporative_demand_drought_monitoring`
- `rainfall_only_or_loss_accounting_first`

The ranking should use at least these evidence families when available in the package: persistent daytime heat, peak apparent heat, hot-night recovery stress, vapor-pressure deficit, Poyang/Yangtze low-water timing, precipitation context, population exposure, and critical amenity or access context.

Use the following normalized strengths when computing the candidate scores:

```text
heat = min(heat_run_days / 14, 1)
apparent = min(peak_apparent_c / 43.0, 1)
warm_nights = min(warm_nights_tmin_ge_28c / 20, 1)
vpd = min(vpd_hours_gt_2p5 / 50, 1)
low_water = min(early_shift_days / 90, 1)
population = min(population_exposed / 10000000, 1)
hospitals = min(hospitals / 20, 1)
shelters = min(shelters / 20, 1)
bridges = min(bridges / 30, 1)
roads = min(highway_features / 200, 1)
precip_context = min(three_product_mean_precip_mm / 250, 1)

cooling_health_and_night_recovery =
  30*heat + 25*apparent + 20*warm_nights + 15*population + 10*hospitals - 3*shelters

lake_low_water_and_water_supply =
  35*low_water + 25*vpd + 10*heat + 10*population + 10*bridges + 5*roads

evaporative_demand_drought_monitoring =
  35*vpd + 20*heat + 15*apparent + 15*low_water + 10*population - 10*precip_context

rainfall_only_or_loss_accounting_first =
  15*precip_context + 10*(1-heat) + 10*(1-apparent) + 10*(1-vpd) + 10*(1-low_water)
```

Return only compact JSON with this shape:

```json
{
  "answer": "short_machine_readable_label",
  "target_family": "heat_drought_response_priority_ranking",
  "source_files_used": ["<package-relative path>", "..."],
  "computed_values": {
    "heat_run_days": 0,
    "peak_apparent_c": 0.0,
    "warm_nights_tmin_ge_28c": 0,
    "vpd_hours_gt_2p5": 0,
    "early_shift_days": 0,
    "population_exposed": 0,
    "hospitals": 0,
    "shelters": 0,
    "bridges": 0,
    "highway_features": 0,
    "three_product_mean_precip_mm": 0.0
  },
  "score_formula": {"normalization": "min(value / threshold, 1.0)", "formulas_used": ["..."]},
  "candidate_priority_scores": {
    "cooling_health_and_night_recovery": 0.0,
    "lake_low_water_and_water_supply": 0.0,
    "evaporative_demand_drought_monitoring": 0.0,
    "rainfall_only_or_loss_accounting_first": 0.0
  },
  "ranked_priorities": [
    {"rank": 1, "priority": "short_machine_readable_label", "reason": "concise evidence-based reason"}
  ],
  "top_priority": "short_machine_readable_label",
  "rejected_top_priority": "short_machine_readable_label",
  "reasoning_path": ["..."]
}
```

Keep the answer at the prioritization level. Do not add casualty, crop-loss, or economic-loss totals unless they are explicitly computed from local package evidence.
