# Final Answer

The correct answer is `ashfall_evacuation_and_air_quality_priority`.

Reference response:

```json
{
  "answer": "ashfall_evacuation_and_air_quality_priority",
  "priority_rank": [
    "ashfall_evacuation_and_air_quality_priority",
    "lahar_and_wet_ash_route_monitoring_secondary",
    "lava_or_burn_scar_image_triage_low_priority",
    "ordinary_weather_response_low_priority"
  ],
  "key_numeric_anchors": [
    {"name": "plume_height_km_at_least", "value": 15.0},
    {"name": "evacuated_people_range", "value": [1500, 2000]},
    {"name": "nearby_population_estimate", "value": 2826.8},
    {"name": "critical_service_count", "value": 55}
  ],
  "impact_chain": [
    "explosive_eruption",
    "high_ash_plume_and_nearfield_evacuation",
    "ashfall_air_quality_and_access_management"
  ],
  "rationale": "The event-scale posture should prioritize ashfall, evacuation, and air-quality management because the package ties an explosive eruption and high ash plume to nearby exposed communities and an evacuation order. Wet-ash and lahar-access monitoring is a secondary watch, while image-only lava or burn-scar triage and ordinary weather response are weaker primary framings."
}
```

# Key Computations

## File Selection

Selected files:

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_Calbuco_eruption.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/other/other_001_Volcanic_Ash_Advisory_Centers_advisories.html`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_001_Overpass_small_roads_and_critical_amenities.json`
- `data/exposure_impact/exposure_impact_004_OpenStreetMap_Overpass_bounded_AOI_slice.json`
- `data/remote_sensing/remote_sensing_002_Sentinel-1_GRD_VV_pre_post_change.json`
- `data/physical_hazard/physical_hazard_009_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`

## Text And Package Claims

- The package is the 2015 Calbuco eruption in Chile's Los Lagos Region, with a volcano, ash, and lahar hazard label.
- The main report describes an explosive eruption after a long quiet period.
- The report states that the ash cloud reached at least 15 km above the volcano and threatened nearby communities.
- The report says evacuations were ordered within a 20 km radius, with about 1,500 to 2,000 people evacuated and no casualties reported at that stage.
- The report describes a second high-energy ash pulse, making plume, ashfall, evacuation, and air-quality management central to immediate response.
- The ash-advisory page supports ash-plume relevance, but it does not quantify ground ash depth.

## Python Computation

`compute_gt.py` deterministically reads the CSX-309 package files and writes `computed_gt.json`. It:

- strips local HTML into text and extracts eruption mechanism flags, plume height, and evacuation range;
- counts exposure features and critical-service amenities from local map slices;
- reads nearby population, precipitation summaries, radar change, and burn-index availability;
- scores four response postures using ash mechanism strength, near-field exposure, wet-ash/lahar context, and image context;
- ranks the postures and selects the highest score as the canonical answer.

The scoring rule returns `ashfall_evacuation_and_air_quality_priority` because the ash mechanism score is complete, the near-field exposure score is high, and wet-ash/lahar monitoring is better treated as a secondary watch than as the dominant immediate posture.

## Intermediate Values

```json
{
  "plume_height_km_at_least": 15.0,
  "evacuated_min": 1500,
  "evacuated_max": 2000,
  "nearby_population_estimate": 2826.8,
  "critical_service_count": 55,
  "bounded_highway_features": 171,
  "bounded_building_features": 790,
  "bounded_waterway_features": 19,
  "precip_mean_context_mm": 18.4,
  "radar_mean_change_db": 1.4,
  "radar_max_change_db": 26.8,
  "burn_index_status": "no_sufficient_scenes",
  "ash_mechanism_score": 100.0,
  "nearfield_exposure_score": 98.6,
  "wet_ash_lahar_watch_score": 48.4,
  "image_context_score": 60.0
}
```

Priority scores:

```json
{
  "ashfall_evacuation_and_air_quality_priority": 90.4,
  "lahar_and_wet_ash_route_monitoring_secondary": 73.8,
  "lava_or_burn_scar_image_triage_low_priority": 21.0,
  "ordinary_weather_response_low_priority": 6.1
}
```

# Reasoning Path

1. The event mechanism is an explosive volcanic eruption, not an ordinary weather episode.
2. The reported high ash plume, second ash pulse, and evacuation order make ashfall, plume exposure, air quality, and near-field safety the direct response priority.
3. The package's masked exposure statistics are used as operational exposure context: about 2,827 people, 55 critical-service amenities, and many roads and buildings in the bounded slice.
4. Rainfall and waterways justify watching for lahars or wet-ash route problems, but the primary report emphasizes ash and evacuation rather than rainfall damage.
5. Image-change evidence is contextual, and the burn-index layer lacks sufficient scenes, so lava or burn-scar image triage is not the best primary priority.
6. The best response posture is therefore near-field ashfall, evacuation, and air-quality management, with wet-ash/lahar-access monitoring as a secondary watch.

# Disaster Interpretation

Operationally, the April 2015 Calbuco event should be treated as an explosive volcanic crisis whose immediate public-safety burden is ash exposure and near-field evacuation, not as a rainfall-only or image-mapping task. The reported plume height and repeated ash pulse make respiratory protection, ashfall cleanup, road and service continuity, and clear evacuation messaging the dominant first-cycle concerns. Rainfall, waterways, and road density still matter because wet ash can degrade access and raise lahar concerns, but those are secondary watches that support the main ash-and-evacuation posture. Remote-sensing change indicators can help situational awareness, yet they do not displace the urgent human-exposure and air-quality interpretation.

## Forbidden Overclaims

- Do not claim exact ash depth, ash mass loading, or plume dispersion from this package alone.
- Do not claim precise casualty, mortality, or loss totals beyond the report's limited statement.
- Do not treat precipitation files as proof that lahars did or did not occur everywhere in the region.
- Do not treat radar change as a direct lava or burn-scar map.
- Do not infer official evacuation-zone geometry beyond the reported 20 km radius.

## Scoring Rubric

Total: 20 points.

- 4 points: Selects `ashfall_evacuation_and_air_quality_priority` as the primary answer or uses a clearly equivalent compact label.
- 3 points: Ranks the response postures correctly: ashfall/evacuation/air quality first, wet-ash/lahar access monitoring second, lava or burn-scar image triage third, and ordinary weather response last.
- 4 points: Reports the four key numeric anchors within tolerance: plume at least 15 km, evacuated range 1,500 to 2,000, nearby population about 2,827, and 55 critical-service amenities.
- 3 points: Correctly explains the physical mechanism: explosive eruption, high ash plume, second ash pulse, and near-field exposure leading to evacuation and air-quality management.
- 2 points: Treats wet-ash and lahar-access monitoring as a secondary watch justified by precipitation, waterway, and road context, not as the dominant posture.
- 1.5 points: Rejects lava or burn-scar image triage as the primary decision frame because image-change evidence is contextual and not the immediate life-safety driver.
- 1 point: Rejects ordinary weather response as the main posture.
- 1 point: Avoids unsupported claims about exact ash depth, ash mass loading, exact losses, definitive lahar occurrence, radar-derived lava or burn scars, or official evacuation-zone geometry.
- 0.5 points: Returns concise, well-formed JSON with the requested fields and a practical rationale.
