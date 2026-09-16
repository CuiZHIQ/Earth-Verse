# Final Answer

```json
{
  "answer_type": "denominator_scale_audit",
  "decision": "population_denominator_required_for_service_exposure_rate",
  "source_paths": {
    "event_anchor": "data/event_reports/event_reports_005_Locked_event_anchor_2015_India-Pakistan_heat_wave.json",
    "regional_heat": "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
    "population_denominator": "data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json",
    "asset_numerator": "data/exposure_impact/exposure_impact_006_OpenStreetMap_Overpass_bounded_AOI_slice.json",
    "smaller_overpass_candidate": "data/exposure_impact/exposure_impact_003_Overpass_small_roads_and_critical_amenities.json",
    "india_report_context": "data/event_reports/event_reports_003_Wikipedia_2015_Indian_heat_wave.json",
    "pakistan_report_context": "data/event_reports/event_reports_004_Wikipedia_2015_Pakistan_heat_wave.json",
    "manifest": "metadata/files.csv"
  },
  "event_window": {
    "start_date": "2015-05-01",
    "end_date": "2015-06-30",
    "days_inclusive": 61
  },
  "regional_heat_context": {
    "dataset": "ECMWF/ERA5_LAND/HOURLY",
    "temperature_2m_max_c_max": 46.25,
    "temperature_2m_max_c_mean": 45.12,
    "temperature_2m_max_c_min": 43.27
  },
  "selected_exposure_inputs": {
    "population": 3193357.78,
    "population_m": 3.19,
    "asset_category_counts": {
      "hospital": 192,
      "school": 57,
      "police": 12,
      "shelter": 1,
      "fire_station": 1
    },
    "heat_health_assets": 263,
    "selected_osm_elements": 1000
  },
  "calculations": {
    "assets_per_million_people": 82.36,
    "residents_per_heat_health_asset": 12142.04
  },
  "counterfactual_audit": {
    "osm_elements_as_denominator": {
      "wrong_denominator": 1000,
      "wrong_fraction": 0.263,
      "error_class": "wrong_denominator_mixed_osm_feature_inventory"
    },
    "smaller_overpass_as_numerator": {
      "wrong_assets": 24,
      "wrong_assets_per_million_people": 7.52,
      "undercount_assets": 239,
      "selected_to_wrong_asset_ratio": 10.96,
      "error_class": "wrong_numerator_incomplete_overpass_slice"
    },
    "reported_deaths_as_denominator": {
      "india_deaths": 2500,
      "pakistan_deaths": 2000,
      "combined_reported_deaths": 4500,
      "why_rejected": "reported deaths are impact context, not exposed population or service inventory"
    }
  },
  "minimal_evidence_set": [
    "data/event_reports/event_reports_005_Locked_event_anchor_2015_India-Pakistan_heat_wave.json",
    "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
    "data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json",
    "data/exposure_impact/exposure_impact_006_OpenStreetMap_Overpass_bounded_AOI_slice.json",
    "data/exposure_impact/exposure_impact_003_Overpass_small_roads_and_critical_amenities.json",
    "data/event_reports/event_reports_003_Wikipedia_2015_Indian_heat_wave.json",
    "data/event_reports/event_reports_004_Wikipedia_2015_Pakistan_heat_wave.json",
    "metadata/files.csv"
  ],
  "ruling": "population_scaled_exposure_density_supported",
  "reference_trace": [
    "Use metadata/files.csv to identify locked event anchor, ERA5-Land stats, WorldPop sum, bounded OSM slice, smaller Overpass candidate, and report contexts.",
    "Read the locked anchor temporal_window and compute inclusive days from 2015-05-01 through 2015-06-30.",
    "Read ERA5-Land temperature_2m_max_c_* fields as regional heat context only.",
    "Read WorldPop population_sum.population and convert to millions.",
    "Count only hospital, school, police, shelter, and fire_station amenities in the bounded OSM AOI slice.",
    "Compute assets per million people and residents per heat-health asset.",
    "Reject OSM element count, the smaller Overpass slice, and reported deaths as denominator or numerator shortcuts."
  ]
}
```

# Files Inspected

- `metadata/files.csv` for package-relative source selection.
- `data/event_reports/event_reports_005_Locked_event_anchor_2015_India-Pakistan_heat_wave.json` for `temporal_window.start_date` and `temporal_window.end_date`.
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json` for `dataset` and `stats.temperature_2m_max_c_*`.
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json` for `population_sum.population`.
- `data/exposure_impact/exposure_impact_006_OpenStreetMap_Overpass_bounded_AOI_slice.json` for the selected amenity numerator.
- `data/exposure_impact/exposure_impact_003_Overpass_small_roads_and_critical_amenities.json` for the incomplete-numerator counterfactual.
- `data/event_reports/event_reports_003_Wikipedia_2015_Indian_heat_wave.json` and `data/event_reports/event_reports_004_Wikipedia_2015_Pakistan_heat_wave.json` for reported-death context.

# Computation Notes

The locked event window runs from 2015-05-01 through 2015-06-30, so the inclusive duration is `(2015-06-30 - 2015-05-01) + 1 = 61` days.

ERA5-Land is used only as heat context: max cell peak `46.2466979980469 -> 46.25`, mean cell peak `45.11882448571625 -> 45.12`, and minimum cell peak `43.2659851074219 -> 43.27`.

WorldPop gives `population_sum.population = 3193357.7794705867`, rounded to `3193357.78`, or `3.19` million people. The bounded OSM AOI slice contains `192 + 57 + 12 + 1 + 1 = 263` heat-health service assets.

Rates:

- `assets_per_million_people = 263 / (3193357.7794705867 / 1000000) = 82.36`
- `residents_per_heat_health_asset = 3193357.7794705867 / 263 = 12142.04`

# Rejected Alternatives

Using all `1000` OSM elements as a denominator gives `263 / 1000 = 0.263`, but that is a mixed feature-inventory fraction, not a population-scaled exposure rate.

Using the smaller Overpass candidate gives only `24` qualifying assets, or `7.52` assets per million people. It undercounts the selected bounded slice by `239` assets, and the selected numerator is `10.96` times larger.

The report anchors give `2500 + 2000 = 4500` reported deaths. Those are impact context values, not exposed population and not a service-inventory denominator.

# Scoring Rubric

Total: 20 points.

- 3 points: Requested JSON schema with package-relative paths and no external evidence.
- 3 points: Correct event window and ERA5 heat-context fields.
- 3 points: Correct WorldPop denominator and million-person conversion.
- 4 points: Correct bounded OSM numerator and category counts.
- 3 points: Correct rate calculations and rounding.
- 3 points: Correct rejection of OSM element count, smaller Overpass numerator, and reported-death denominator.
- 1 point: Correct final ruling and reproducible trace without generic disaster explanation.
