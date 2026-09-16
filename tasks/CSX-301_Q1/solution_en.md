# Final Answer

The correct answer is `air_quality_visibility_transport_public_health_priority`.

## Key Computations

Hidden records used:

- `metadata/event.json`: confirms that the event is an extreme dust or sandstorm in East Asia.
- `data/event_reports/event_reports_003_Locked_event_anchor_March_2021_East_Asia_dust_storm.json`: provides the locked event window and regional setting.
- `data/physical_hazard/physical_hazard_002_Open-Meteo_archive_point_sample.json`: provides daily wind and precipitation over the event window.
- `data/physical_hazard/physical_hazard_001_NASA_POWER_daily_point_sample.json`: provides an independent daily point sample for wind and precipitation.
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`: provides gridded precipitation context for the same short event window.
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`: provides population exposure in the area of interest.
- `data/exposure_impact/exposure_impact_001_Overpass_small_roads_and_critical_amenities.json`: provides hospitals, police, fire stations, schools, shelters, and road features.
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`: checks whether annual-scale structural land-cover change is the dominant signal.

Context or ignored files:

- Remote-sensing preview images are useful visual context but are not needed for the deterministic answer.
- Catalog feeds and broad search outputs are not decisive for this mechanism question because the event identity is already locked and the answer depends on local hazard, exposure, and impact-priority metrics.
- Auxiliary HTML duplicates are not needed when the structured local package files provide the necessary evidence.

## Text Claims/Package Claims

- The package metadata identifies the event as the March 2021 East Asia dust storm with hazard family `dust_sandstorm_extreme` and hazard label `Extreme dust or sandstorm`.
- The locked event anchor gives the event window as 2021-03-14 to 2021-03-16 and places the event in Mongolia, northern China, and Korea.
- The package contains short-window meteorological files with wind and low precipitation, which are more relevant to dust transport and visibility than to hydrologic flooding.
- The exposure files show a large population and many critical amenities and roads in the sampled area, supporting an impact priority around public health, visibility, and transport disruption.
- The annual satellite embedding-change mean is small, so the package does not support treating long-term land-cover damage as the main response priority.

`compute_gt.py` calculates:

- Peak daily 10 m wind speed from Open-Meteo and NASA POWER, using kilometers per hour for comparison.
- Event precipitation from Open-Meteo, NASA POWER, and ERA5-Land context.
- Low-precipitation day counts and the longest low-precipitation run.
- Population in millions from WorldPop.
- Counts of critical amenities and road features from the Overpass slice.
- Mean annual AlphaEarth embedding change.
- A deterministic priority classification from hazard family, wind, rainfall, exposure, and annual-change flags.

The classification rule returns `air_quality_visibility_transport_public_health_priority` when the event is a dust/sandstorm, peak wind is at least 20.0 km/h, event rainfall is low, the exposed population and critical-amenity counts are high, and annual embedding change is below 0.05.

## Intermediate Values

```json
{
  "peak_wind_kmh": 22.1,
  "event_precip_mm": 2.4,
  "power_event_precip_mm": 2.1,
  "era5_precip_mean_mm": 1.66,
  "era5_precip_max_mm": 3.75,
  "low_precip_days_le_1mm": 2,
  "population_millions": 11.4,
  "critical_amenities": 89,
  "road_features": 211,
  "annual_embedding_change_mean": 0.026
}
```

## Reasoning Chain

1. The package identifies the hazard as an extreme dust or sandstorm, so the first-order mechanism is airborne dust rather than rainfall, flooding, or burn damage.
2. The short-window weather is consistent with dust-impact reasoning: peak wind reaches about 22.1 km/h, while event precipitation is only about 2.4 mm in the point sample and ERA5-Land mean precipitation is about 1.66 mm.
3. Low rainfall does not support a hydrologic-disruption priority, and it also would not suppress dust as strongly as a wet event would.
4. The WorldPop and Overpass files show substantial exposure: about 11.4 million people, 89 critical amenities, and 211 road features in the sampled area.
5. The annual embedding-change mean is only about 0.026, so the remote-sensing change file is better treated as non-primary context than as evidence for long-term land-cover damage.
6. Combining hazard mechanism, low-rainfall windy context, and high exposure supports an acute air-quality, visibility, transport, and public-health priority.

## Reasoning Path

The structured answer is deterministic, but the explanation should be judged for mechanism quality. The event is a dust/sandstorm rather than a hydrologic or land-cover-change disaster. The event-window meteorology is dry enough that rainfall disruption is not the main response pathway, and the wind signal is sufficient to support dust transport and reduced visibility. High population, road, and critical-amenity exposure make the priority operationally important, but those exposure layers amplify the dust hazard rather than defining it by themselves. The low annual embedding-change mean keeps long-term land-cover damage secondary.

## Final GT

```json
{
  "answer": "air_quality_visibility_transport_public_health_priority",
  "priority_bin": "high_exposure_acute_dust_disruption",
  "key_metrics": {
    "peak_wind_kmh": 22.1,
    "event_precip_mm": 2.4,
    "population_millions": 11.4,
    "critical_amenities": 89,
    "annual_embedding_change_mean": 0.026
  },
  "impact_chain": [
    "dry_windy_surface_conditions",
    "dust_transport_and_low_visibility",
    "public_health_and_transport_priority"
  ]
}
```

## Unsupported Overclaims

- Do not claim exact mortality, hospitalization, airport closure counts, or measured PM concentrations from these local files.
- Do not claim that the point wind sample captures the maximum wind anywhere in Mongolia, northern China, or Korea.
- Do not interpret the annual satellite embedding-change statistic as direct dust concentration or visibility.
- Do not infer a hydrologic disaster priority from the small precipitation values.
- Do not claim that all people in the area of interest were directly affected; WorldPop is an exposure metric, not a confirmed impact count.

## Scoring Rubric

Total: 20 points.

- 3 points: Returns `air_quality_visibility_transport_public_health_priority` or an equivalent compact priority label.
- 3 points: Correctly links the dust/sandstorm hazard to airborne dust, visibility reduction, transport disruption, and respiratory or public-health concerns.
- 4 points: Uses the short-window meteorology correctly, including peak wind near 22.1 km/h, event precipitation near 2.4 mm, NASA POWER precipitation near 2.1 mm, and ERA5-Land mean precipitation near 1.66 mm.
- 3 points: Uses exposure-context metrics correctly, including population near 11.4 million, 89 critical amenities, and 211 road features, without treating them as confirmed direct impacts.
- 3 points: Builds the impact chain from dry windy conditions to dust transport and low visibility to public-health and transport priority.
- 2 points: Correctly treats annual embedding change near 0.026 as non-primary context rather than proof of long-term land-cover damage.
- 2 points: Avoids unsupported claims about exact casualties, hospitalization, measured PM concentrations, airport closure counts, or confirmed direct impacts for all exposed people.

## Disaster Interpretation

This task is an acute dust-impact priority diagnosis, not a generic event-recognition task. A dry, windy short-window setting supports airborne dust transport and visibility degradation, while high population and infrastructure exposure make public-health and transport disruption the practical response concern. The remote-sensing annual embedding statistic is too small and too temporally broad to justify a long-term land-cover-damage priority. The best operational stance is therefore to prepare for air-quality, visibility, transport, and public-health disruption, while avoiding unverified claims about measured PM concentrations or exact realized health outcomes.
