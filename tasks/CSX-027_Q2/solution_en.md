# Final Answer

```json
{
  "answer": "cooling_health_first_low_water_second",
  "target_family": "heat_drought_response_priority_ranking",
  "source_files_used": [
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json",
    "data/other/other_003_01_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html.html",
    "data/exposure_impact/exposure_impact_002_Overpass_small_roads_and_critical_amenities.json",
    "data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json"
  ],
  "computed_values": {
    "heat_run_days": 17,
    "peak_apparent_c": 44.0,
    "warm_nights_tmin_ge_28c": 25,
    "vpd_hours_gt_2p5": 84,
    "early_shift_days": 100,
    "population_exposed": 11395560,
    "hospitals": 25,
    "shelters": 12,
    "bridges": 32,
    "highway_features": 211,
    "three_product_mean_precip_mm": 383.575
  },
  "score_formula": {
    "normalization": "Each named strength is min(value/threshold, 1.0).",
    "cooling_health_and_night_recovery": "30*heat + 25*apparent + 20*warm_nights + 15*population + 10*hospitals - 3*shelters",
    "lake_low_water_and_water_supply": "35*low_water + 25*vpd + 10*heat + 10*population + 10*bridges + 5*roads",
    "evaporative_demand_drought_monitoring": "35*vpd + 20*heat + 15*apparent + 15*low_water + 10*population - 10*precip_context",
    "rainfall_only_or_loss_accounting_first": "15*precip_context + 10*(1-heat) + 10*(1-apparent) + 10*(1-vpd) + 10*(1-low_water)"
  },
  "candidate_priority_scores": {
    "cooling_health_and_night_recovery": 98.2,
    "lake_low_water_and_water_supply": 95.0,
    "evaporative_demand_drought_monitoring": 85.0,
    "rainfall_only_or_loss_accounting_first": 15.0
  },
  "ranked_priorities": [
    {
      "rank": 1,
      "priority": "cooling_health_and_night_recovery",
      "reason": "Persistent Tmax >= 35 C, 44.0 C apparent heat, 25 warm nights, large exposed population, 25 hospitals, and only 12 shelters make immediate heat-health and night-recovery triage the strongest priority."
    },
    {
      "rank": 2,
      "priority": "lake_low_water_and_water_supply",
      "reason": "The Poyang/Yangtze low-water marker is about 100 days early, and elevated VPD plus 32 bridges and road context support water-level and access management."
    },
    {
      "rank": 3,
      "priority": "evaporative_demand_drought_monitoring",
      "reason": "VPD and persistent heat strongly justify drought monitoring, but this surveillance priority follows the direct heat-health and low-water response priorities."
    },
    {
      "rank": 4,
      "priority": "rainfall_only_or_loss_accounting_first",
      "reason": "Precipitation summaries alone do not explain the heat, VPD, warm-night, and early-low-water chain, and the package does not compute casualty, crop-loss, or economic-loss totals."
    }
  ],
  "top_priority": "cooling_health_and_night_recovery",
  "rejected_top_priority": "rainfall_only_or_loss_accounting_first",
  "reasoning_path": [
    "Use the Open-Meteo daily and hourly file to compute persistent heat, apparent heat, warm nights, and VPD.",
    "Use the NASA Poyang Lake report to recover the about 100-day early dry-season marker.",
    "Use WorldPop and OSM files to add population, hospital, shelter, and bridge/access context.",
    "Score all four candidate priorities with the normalized formula and rank by candidate priority score.",
    "Reject rainfall-only or loss-accounting-first because it misses the heat-VPD-low-water mechanism and would overclaim losses not computed in the package."
  ]
}
```

# Key Computations

The local daily weather series gives a longest run of 17 days with daily Tmax >= 35 C, from 2022-08-07 through 2022-08-23. The peak apparent temperature is 44.0 C, and 25 daily minimum temperatures are at least 28 C.

Hourly vapor-pressure deficit is computed as:

```text
VPD = es(Tair) - es(Tdew)
es(T) = 0.6108 * exp((17.27 * T) / (T + 237.3))
```

Across July-August 2022, 84 hourly values exceed 2.5 kPa. The Poyang/Yangtze timing anchor records dry-season conditions about 100 days earlier than usual. The package exposure context gives about 11,395,560 exposed people, 25 hospitals, 12 shelters, and 32 bridge features in the critical-amenity/access slice.

The precipitation summaries provide context rather than a top-ranked rainfall-only explanation: the three product means are 321.266 mm, 457.495 mm, and 371.964 mm, with a three-product mean of 383.575 mm. These values do not remove the heat, VPD, warm-night, and early-low-water stress chain.

# Priority Score Logic

Each named strength is normalized as `min(value / threshold, 1.0)`. The candidate scores are:

```text
cooling_health_and_night_recovery =
  30*heat + 25*apparent + 20*warm_nights + 15*population + 10*hospitals - 3*shelters = 98.2

lake_low_water_and_water_supply =
  35*low_water + 25*vpd + 10*heat + 10*population + 10*bridges + 5*roads = 95.0

evaporative_demand_drought_monitoring =
  35*vpd + 20*heat + 15*apparent + 15*low_water + 10*population - 10*precip_context = 85.0

rainfall_only_or_loss_accounting_first =
  15*precip_context + 10*(1-heat) + 10*(1-apparent) + 10*(1-vpd) + 10*(1-low_water) = 15.0
```

The resulting ranking is:

1. `cooling_health_and_night_recovery`
2. `lake_low_water_and_water_supply`
3. `evaporative_demand_drought_monitoring`
4. `rainfall_only_or_loss_accounting_first`

# Reasoning Path

This is a prioritization task, so the answer should not stop at the old threshold ledger. The correct path is to combine immediate human heat exposure with night-recovery stress, then compare that with hydrologic low-water timing and evaporative demand. The low-water signal is strong enough to be second, but the combination of persistent daytime heat, high apparent heat, hot nights, large exposed population, and limited shelter context makes the heat-health response the top operational priority.

The rainfall-only or loss-accounting-first candidate is deliberately last. The package does not compute exact casualty, crop-loss, or economic-loss totals, and a rainfall-only interpretation misses the heat-VPD-low-water chain that the local package actually supports.

# Scoring Rubric

Total: 20 points.

- 4 points: Returns the requested JSON with target_family, package-relative source files, computed values, score formula, candidate priority scores, ranked priorities, top_priority `cooling_health_and_night_recovery`, and rejected_top_priority `rainfall_only_or_loss_accounting_first`.
- 4 points: Computes the heat-health anchors correctly: 17 days for the longest Tmax >= 35 C run, 44.0 C peak apparent heat, and 25 nights with Tmin >= 28 C.
- 4 points: Computes or reconstructs the hydrologic/VPD anchors correctly: 84 July-August VPD hours above 2.5 kPa and the about 100-day early Poyang/Yangtze low-water timing.
- 3 points: Uses exposure and access context from local package files: about 11,395,560 people, 25 hospitals, 12 shelters, and 32 bridges, without turning exposure into confirmed casualty or outage counts.
- 3 points: Applies the candidate-score logic well enough to obtain or closely approximate the scores 98.2, 95.0, 85.0, and 15.0, and ranks the candidates in the correct order.
- 2 points: Clearly explains why `rainfall_only_or_loss_accounting_first` is not the top priority and avoids adding unsupported exact loss totals.
