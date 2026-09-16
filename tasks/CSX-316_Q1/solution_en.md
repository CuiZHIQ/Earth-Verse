# Final Answer

The correct compact answer is `slow_onset_ice_field_monitoring_and_adaptation_priority`.

The event should be diagnosed as long-horizon high-mountain ice-field loss on Kilimanjaro. The appropriate response posture is monitoring and adaptation for water, ecosystem, tourism, and mountain-risk planning, not rapid dispatch for an avalanche, glacial lake outburst flood, short-window storm or snowmelt flood, or burn-scar recovery.

Expected JSON content:

```json
{
  "answer": "slow_onset_ice_field_monitoring_and_adaptation_priority",
  "key_metrics": {
    "event_window_years": 20.0,
    "local_weather_sample_days": 15,
    "mean_daily_temperature_c": 27.81,
    "population_context": 1233444,
    "direct_observation_role": "contextual_not_a_discrete_damage_map"
  },
  "priority_chain": [
    "multi_decadal_high_mountain_ice_retreat",
    "slow_onset_cryosphere_loss",
    "monitoring_and_adaptation"
  ]
}
```

# Key Computations

The reference computation uses the hidden event package for CSX-316, including package metadata, the locked Kilimanjaro ice-field retreat event anchor, short local weather samples, regional precipitation and temperature summaries, formal direct-observation scene-status summaries, broad population context, a small critical-amenity sample, glacier-inventory context, and the package file manifest.

Key files used by `compute_gt.py`:

- `metadata/event.json`
- `data/event_reports/event_reports_004_Locked_event_anchor_Kilimanjaro_ice-field_retreat.json`
- `data/physical_hazard/physical_hazard_001_NASA_POWER_daily_point_sample.json`
- `data/physical_hazard/physical_hazard_002_Open-Meteo_archive_point_sample.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_005_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/remote_sensing/remote_sensing_001_Sentinel-1_GRD_VV_pre_post_change.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_001_Overpass_small_critical-amenity_sample.json`
- `data/event_catalogs/event_catalogs_002_GLIMS_glacier_database_and_RGI_outlines.html`
- `metadata/files.csv`

Computed ground-truth values:

```json
{
  "event_window_days": 7306,
  "event_window_years": 20.0,
  "local_weather_sample_days": 15,
  "mean_daily_temperature_c": 27.81,
  "max_daily_temperature_c": 28.55,
  "nasa_power_precip_total_mm": 36.88,
  "open_meteo_precip_total_mm": 26.4,
  "population_context": 1233444,
  "small_critical_amenity_count": 0,
  "insufficient_direct_observation_products": 2
}
```

Numeric tolerances for scoring are 20.0 event-window years within +/-0.2 years, 15 local weather sample days exactly, 27.81 degrees C mean daily temperature within +/-0.05 degrees C, and 1,233,444 people as broad population context within +/-1 person.

# Reasoning Path

1. The locked event anchor spans February 21, 2000 through February 21, 2020, an inclusive 7,306-day window, or about 20.0 years. That duration is inconsistent with a discrete avalanche, outburst flood, short storm flood, or post-fire recovery incident.
2. The event name and metadata identify Kilimanjaro ice-field retreat and classify the rapid cryosphere match as partial because the relevant phenomenon is slow-onset ice loss rather than a sudden snow, ice, or flood emergency.
3. The 15-day local weather samples give environmental context, with mean daily temperature of 27.81 degrees C and modest precipitation totals, but they do not define the multi-decadal event mechanism.
4. Sentinel-1 and Sentinel-2 direct-observation summaries both lack sufficient pre/post scene support for a complete damage or retreat map. Their role is contextual, not a definitive discrete damage product.
5. The broad population value of 1,233,444 people helps frame adaptation relevance around nearby communities and services, but it is not a directly harmed population count.
6. The priority chain is therefore multi-decadal high-mountain ice retreat -> slow-onset cryosphere loss -> monitoring and adaptation.

# Disaster Interpretation

Kilimanjaro ice-field retreat is a chronic high-mountain cryosphere impact problem. Its disaster relevance comes from long-term changes to mountain environments, water and ecosystem planning, tourism-dependent livelihoods, and changing mountain-risk baselines. The operational posture should emphasize monitoring, trend interpretation, risk communication, and adaptation planning.

The event should not be treated as an immediate dispatch trigger unless separate evidence shows a discrete hazard such as an avalanche, glacial lake outburst flood, or acute snowmelt-flood episode. The short weather sample and broad exposure figures are useful context, but neither establishes acute losses or a precise glacier-area change rate.

Forbidden overclaims:

- Do not claim a confirmed immediate avalanche, GLOF, or snowmelt-flood emergency.
- Do not infer a precise glacier area-loss rate from this task.
- Do not turn broad population context into a directly harmed population count.
- Do not claim exact tourism revenue loss, water-supply loss, mortality, facility damage, or service outage.
- Do not treat contextual scene material as a complete direct damage or retreat map.

# Scoring Rubric

Total: 20 points.

- 4 points: Gives the correct final label, `slow_onset_ice_field_monitoring_and_adaptation_priority`, or an unambiguous equivalent.
- 4 points: Reports the required numeric anchors: 20.0 event-window years within +/-0.2 years, 15 local weather sample days exactly, 27.81 degrees C mean daily temperature within +/-0.05 degrees C, and 1,233,444 population context within +/-1 person.
- 4 points: Correctly explains the physical mechanism as multi-decadal Kilimanjaro high-mountain ice-field retreat and slow-onset cryosphere loss.
- 3 points: Provides the correct priority chain from multi-decadal ice retreat to slow-onset cryosphere loss to monitoring and adaptation for water, ecosystem, tourism, and mountain-risk planning.
- 2 points: Correctly interprets direct observation as contextual rather than a complete discrete damage or retreat map.
- 2 points: Separates broad population exposure context from observed damage, direct loss, or directly affected population.
- 1 point: Avoids unsupported acute-emergency, precise area-loss, revenue-loss, mortality, facility-damage, or service-outage claims while keeping the JSON concise and well structured.
