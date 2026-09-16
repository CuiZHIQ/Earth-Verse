# Final Answer

```json
{
  "answer": "record_duration_compound_cyclone_high_priority",
  "priority_level": "high",
  "priority_chain": [
    "exceptional_persistence_and_red_alert_cyclone_intensity",
    "wind_rainfall_flooding_from_repeated_land_interactions",
    "life_safety_humanitarian_response_across_southern_africa"
  ],
  "numeric_anchors": [
    {"name": "record_duration_days", "value": 36.0},
    {"name": "maximum_wind_kmh", "value": 250.0},
    {"name": "malawi_dead_or_missing", "value": 1200},
    {"name": "bounded_population_context", "value": 701661}
  ],
  "brief_rationale": "Freddy should be handled as a high-priority compound tropical-cyclone disaster: exceptional duration and red-alert wind intensity combined with repeated land interactions, heavy rainfall, flooding, and major humanitarian consequences. Population, facilities, roads, and imagery provide response context, but they should not be treated as exact national loss or damage totals."
}
```

# Key Computations

Hidden reference files used by `compute_gt.py`:

- `metadata/event.json`
- `metadata/files.csv`
- `data/event_reports/event_reports_003_Locked_event_anchor_Tropical_Cyclone_Freddy_Indian_Ocean_traverse.json`
- `data/event_reports/event_reports_006_CSX-283_05_event_anchor_report_Locked_anchor_WMO.html.html`
- `data/event_catalogs/event_catalogs_001_GDACS_tropical_cyclone_alert_API.json`
- `data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_004_ERA5-Land_hourly_aggregate_stats.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_003_OpenStreetMap_Overpass_bounded_AOI_slice.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`

The event anchor and metadata identify Tropical Cyclone Freddy's Indian Ocean traverse and southern Africa impacts during 2023-02-04 to 2023-03-14. The WMO report text gives 36.0 days at tropical storm status or higher and about 12,785 km travelled at that status. The tropical cyclone catalog entry for FREDDY-23 gives Red alert status and maximum wind severity near 250 km/h.

Rainfall and flood context are supported by event precipitation summaries: one accumulated precipitation layer has event mean near 112.0 mm and maximum near 417.0 mm, with secondary rainfall and reanalysis layers providing comparable event-scale precipitation context. The WMO report text gives more than 1,200 dead or missing and more than 2,100 injured in Malawi, more than 1.3 million people affected and more than 180 deaths in Mozambique, nearly 200,000 people affected in Madagascar, and about 481 million US dollars in reported damage.

Bounded response-context metrics include a population slice of about 701,661 people, 867 critical amenities, 116 road features, and annual embedding-change summary values near 0.01279 mean and 0.56107 maximum. These are planning context, not observed national impact totals.

# Reasoning Path

1. Identify the event as Tropical Cyclone Freddy, a long-lived Indian Ocean cyclone with southern Africa impacts, not a localized one-day flood.
2. Treat duration and intensity as the leading hazard drivers because 36.0 days at tropical storm status or higher, Red alert status, and about 250 km/h wind severity indicate an exceptional tropical-cyclone system.
3. Connect repeated land interactions to wind, rainfall, and flooding rather than separating the disaster into independent flood episodes.
4. Use the reported humanitarian impacts in Malawi, Mozambique, and Madagascar to classify the response posture as high priority and multi-country.
5. Use population, facility, road, and contextual imagery metrics to explain why life-safety, access, shelter, health, and service-continuity concerns matter, while avoiding claims that those bounded or contextual metrics directly measure all national losses.

## Why The Alternatives Fail

A short isolated flood reading misses Freddy's exceptional duration, severe wind signal, repeated land interactions, and multi-country humanitarian impacts.

An image-led monitoring reading gives too much weight to contextual surface-change information. The response posture is driven by cyclone persistence, wind-rainfall-flood processes, and reported impacts, not by imagery alone.

A weak-cyclone watch is contradicted by the Red alert, near-250 km/h wind severity, rainfall/flood context, and major reported life-safety impacts.

# Disaster Interpretation

Freddy is best interpreted as a prolonged compound tropical-cyclone disaster. Its unusual persistence raised the opportunity for repeated land interactions and accumulated hazard effects, while intense winds and event-scale rainfall created a plausible wind-rainfall-flood pathway into severe humanitarian consequences. Operationally, this supports high-priority coordination focused on life safety, flood response, access constraints, shelters, health services, and infrastructure continuity across affected southern Africa settings.

The bounded population, facilities, roads, and annual change metrics help frame response context. They should not be converted into exact affected-population counts, damaged-facility counts, national economic loss estimates, or direct remote-sensing damage footprints.

# Scoring Rubric

Total: 20 points.

- 4 points: Returns `record_duration_compound_cyclone_high_priority` with `priority_level` set to `high`, or a clearly equivalent compact label and high-priority posture.
- 4 points: Provides 2-4 correct numeric anchors within tolerance, including duration near 36.0 days and at least two of near-250 km/h wind, about 1,200 dead or missing in Malawi, about 701,661 bounded population context, or comparable report-supported humanitarian scale.
- 4 points: Explains the hazard driver as exceptional cyclone persistence plus severe tropical-cyclone forcing, not a weak, ordinary, or short-lived cyclone.
- 3 points: Connects repeated land interactions, wind, rainfall, flooding, and southern Africa humanitarian response into one compound impact chain.
- 2 points: Uses settlement, infrastructure, population, and contextual imagery information as response-planning context without turning it into exact national exposure, damage, or loss totals.
- 2 points: Rejects the main distractors: short isolated flood, image-led monitoring case, and weak-cyclone watch.
- 1 point: Returns valid JSON in the requested shape with a concise two- or three-sentence rationale.

Major penalties apply for claiming exact national exposure totals from bounded context layers, treating contextual imagery as direct national damage evidence, reducing the event to only a short Malawi flood, or adding unsupported climate-attribution or exact-loss conclusions.
