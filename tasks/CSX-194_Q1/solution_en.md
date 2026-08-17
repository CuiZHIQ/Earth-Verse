# Final Answer

```json
{
  "target_family": "black_summer_coupled_process_model",
  "source_paths": {
    "event_context": [
      "metadata/event.json",
      "data/event_reports/event_reports_003_Locked_event_anchor_2019-2020_Australian_Black_Summer_bushfires.json"
    ],
    "weather_and_precipitation": [
      "data/physical_hazard/physical_hazard_001_Open-Meteo_daily_weather_fill.json",
      "data/physical_hazard/physical_hazard_002_NASA_POWER_daily_weather_fill.json",
      "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json",
      "data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json",
      "data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json"
    ],
    "burn_and_surface_change": [
      "data/physical_hazard/physical_hazard_009_Sentinel-2_SR_Harmonized_dNBR.json",
      "data/remote_sensing/remote_sensing_004_Google_Satellite_Embedding_annual_cosine-change_stats.json"
    ],
    "exposure": [
      "data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json",
      "data/exposure_impact/exposure_impact_004_OpenStreetMap_Overpass_bounded_AOI_slice.json"
    ],
    "smoke_and_response_context": [
      "data/event_reports/event_reports_001_Locked_anchor_report_NASA_Earth_Observatory.html",
      "data/other/other_001_WMO_Australia_fires_after_hottest_driest_year_on_record.html"
    ]
  },
  "process_model": {
    "event_period": {"start": "2019-09-01", "end": "2020-02-29"},
    "analysis_window": {"start": "2019-09-01", "end": "2019-10-16", "days": 46},
    "baseline_classification": "extreme_coupled_fire_smoke_response_case"
  },
  "computed_metrics": {
    "baseline_weather": {
      "precip_total_mm": 67.3,
      "dry_days": 38,
      "dry_day_fraction": 0.826,
      "longest_dry_spell_days": 12,
      "hot_windy_days": 1,
      "max_temp_c": 27.5,
      "max_wind_kmh": 30.3,
      "gridded_precip_consensus_mm": 63.311,
      "point_to_grid_precip_ratio": 0.956,
      "fire_weather_stress_norm": 0.647
    },
    "burn_surface_smoke_exposure": {
      "dnbr_mean": 0.123,
      "dnbr_max": 0.974,
      "dnbr_spread": 0.851,
      "annual_embedding_change_mean": 0.03,
      "annual_embedding_change_max": 0.377,
      "max_smoke_height_km": 19,
      "firestorms_minimum": 21,
      "population": 344722,
      "road_features": 914,
      "amenity_features": 78,
      "burn_severity_norm": 0.787,
      "surface_change_norm": 0.72,
      "smoke_pyroconvective_norm": 0.982,
      "exposure_load_norm": 0.916
    },
    "baseline_coupled_process_index": 78.721
  },
  "scenario_analysis": {
    "perturbation": {"temperature_c": 2.0, "wind_multiplier": 1.15, "precip_multiplier": 0.8},
    "scenario_fire_weather_stress_norm": 0.712,
    "scenario_coupled_process_index": 80.362,
    "scenario_delta": 1.641
  },
  "response_priorities": [
    {"priority": "smoke_air_quality", "score": 88.191, "rank": 1},
    {"priority": "access_evacuation", "score": 78.983, "rank": 2},
    {"priority": "fireline_containment", "score": 74.98, "rank": 3}
  ],
  "mechanism_chain": [
    "Persistent dry days and a 12-day dry spell kept local fuels receptive during the early-season fire window.",
    "High dNBR maxima and measurable annual embedding change show localized severe burning and landscape alteration.",
    "More than 20 pyrocumulonimbus firestorms lofted smoke to 19 km, extending response concern from the fireline to downwind air quality."
  ],
  "final_interpretation": "The observed early-season package evidence supports an extreme coupled fire-smoke response case, with smoke and access/evacuation pressures ranking above direct fireline containment in the baseline prioritization."
}
```

# Key Computations

The broader event period is 2019-09-01 to 2020-02-29. The quantitative overlap used by the daily weather and gridded precipitation products is 2019-09-01 to 2019-10-16, or 46 days.

Weather and precipitation:

- Local precipitation total: `67.3 mm`.
- NASA POWER precipitation total: `53.81 mm`.
- Gridded precipitation consensus: `(69.082 + 62.016 + 58.835) / 3 = 63.311 mm`.
- Point-to-grid precipitation ratio: `((67.3 + 53.81) / 2) / 63.311 = 0.956`.
- Dry days: `38 / 46 = 0.826`.
- Longest dry spell: `12 days`.
- Hot-windy days: `1`.
- Maximum wind: `30.3 km/h`.
- `fire_weather_stress_norm = 0.647`.

Burn, surface, smoke, and exposure:

- dNBR mean = `0.123`; dNBR max = `0.974`; dNBR spread = `0.851`.
- Annual embedding-change mean = `0.030`; annual embedding-change max = `0.377`.
- Burn severity norm = `0.787`; surface-change norm = `0.720`.
- The NASA narrative supports `firestorms_minimum = 21`, `max_smoke_height_km = 19`, and transport to both New Zealand and South America, giving `smoke_pyroconvective_norm = 0.982`.
- WorldPop and OpenStreetMap-derived exposure give population `344,722`, road features `914`, amenity features `78`, and `exposure_load_norm = 0.916`.

Coupled process:

```text
baseline_coupled_process_index
= 100 * (0.25*0.647 + 0.25*0.787 + 0.20*0.720 + 0.15*0.982 + 0.15*0.916)
= 78.721
```

Sensitivity case:

- Daily maximum temperature: `+2.0 C`.
- Daily maximum wind: `* 1.15`.
- Local and gridded precipitation: `* 0.80`.
- Scenario hot-windy days increase from `1` to `3`.
- Scenario fire-weather stress becomes `0.712`.

```text
scenario_coupled_process_index = 80.362
scenario_delta = 80.362 - 78.721 = 1.641
```

The classification rule is satisfied because `78.721 >= 75`, `1.641 >= 1.0`, `0.982 >= 0.90`, and `0.916 >= 0.85`. Therefore the classification is `extreme_coupled_fire_smoke_response_case`.

# Reasoning Path

The daily-weather record shows persistent fuel-drying conditions during the early-season window, while three independent gridded precipitation summaries keep the rainfall estimate in the same low range. The dNBR and embedding-change products then connect that meteorological stress to observed burn severity and landscape alteration. The official smoke narrative moves the problem from a local fireline hazard to a coupled fire-atmosphere event: more than 20 firestorms, 15-19 km smoke injection, and documented long-range transport. The exposure data show that the local receptor load is high enough for smoke and access/evacuation pressure to outrank direct containment in the baseline response scores.

# Scoring Rubric

Total: 20 points.

- Self-directed package discovery and citations (3 points): Identifies relevant package files across reports, hazard products, remote sensing, and exposure, and cites package-relative paths in the requested `source_paths` structure. Partial credit: 1-2 points if citations are present but omit one major evidence family.
- Weather-window and rainfall reconstruction (4 points): Uses the 2019-09-01 to 2019-10-16 quantitative window, computes 46 days, 67.3 mm local precipitation, 38 dry days, 12-day longest dry spell, 1 hot-windy day, 27.5 C max temperature, 30.3 km/h max wind, 63.311 mm gridded precipitation consensus, and point-to-grid ratio 0.956. Partial credit: 1-3 points for correct windowing with minor rounding errors or one missing precipitation source.
- Burn, surface-change, smoke, and exposure terms (5 points): Extracts dNBR mean 0.123, dNBR max 0.974, annual change mean 0.030, annual change max 0.377, 15-19 km smoke height, more than 20 firestorms, smoke transport to New Zealand and South America, population 344722, 914 road features, and 78 amenity features. Partial credit: 1-4 points according to how many evidence families and numeric anchors are correctly recovered.
- Formula implementation and baseline classification (4 points): Computes fire_weather_stress_norm 0.647, burn_severity_norm 0.787, surface_change_norm 0.720, smoke_pyroconvective_norm 0.982, exposure_load_norm 0.916, baseline coupled_process_index 78.721, and classifies the event as `extreme_coupled_fire_smoke_response_case`. Partial credit: 1-3 points for correct component logic but an incorrect final rounded index or label.
- Sensitivity and response-priority reasoning (3 points): Applies the +2 C, 1.15 wind, 0.80 precipitation perturbation, obtains scenario fire-weather stress 0.712, scenario coupled index 80.362, delta 1.641, and ranks `smoke_air_quality` before `access_evacuation` before `fireline_containment`. Partial credit: 1-2 points if the scenario is applied but response ranking or delta is wrong.
- Disaster-process interpretation (1 point): Explains the physical chain from persistent dry weather and burn severity to pyrocumulonimbus smoke injection and receptor-response pressure without generic wildfire commentary. No partial credit.
