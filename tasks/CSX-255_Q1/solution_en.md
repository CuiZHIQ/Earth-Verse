# Final Answer

The correct compact priority answer is:

```json
{
  "answer": "compound_rainfall_flood_landslide_health_monitoring_priority",
  "key_metrics": {
    "event_period": "2023-02-21_to_2023-03-31",
    "rainfall_signature": "ensemble_mean_precip_mm=83.974; ensemble_max_precip_mm=200.145",
    "exposed_population_context": "1090345.7 people"
  },
  "priority_chain": [
    "cyclone_moisture_and_heavy_rainfall",
    "flooding_with_landslide_susceptibility",
    "health_risk_monitoring"
  ],
  "rejected_priorities": [
    "wind_core_only: too narrow for the rainfall-flood cascade",
    "drought_or_heat: contradicted by the wet-event signature",
    "wildfire_or_burn_scar: not the dominant surface-change signal"
  ]
}
```

Cyclone Freddy should be diagnosed as a compound hydrometeorological cascade, not as a wind-only cyclone response.

# Key Computations

Key numerical anchors reproduced by `compute_gt.py` are:

```json
{
  "event_period": "2023-02-21_to_2023-03-31",
  "ensemble_mean_precip_mm": 83.974,
  "ensemble_max_precip_mm": 200.145,
  "exposed_population_context": 1090345.7
}
```

The script reads the event window from the locked event anchor, sums point precipitation over that window, combines three gridded event-rainfall summaries into an ensemble rainfall mean and maximum, reads the population layer as exposure context, counts report language tied to rainfall and flooding, and checks broad land-surface-change and dNBR summaries only to reject a wildfire or burn-scar priority.

Hidden file inputs used by the computation are:

- `metadata/event.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_Cyclone_Freddy_floods_landslides_and_cholera_risk.json`
- `data/event_reports/event_reports_001_Locked_anchor_WMO.html`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_daily_weather_fill.json`
- `data/physical_hazard/physical_hazard_002_NASA_POWER_daily_weather_fill.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json`

Numeric tolerances:

- `ensemble_mean_precip_mm`: 83.974 +/- 2.0 mm.
- `ensemble_max_precip_mm`: 200.145 +/- 3.0 mm.
- `exposed_population_context`: 1,090,345.7 +/- 25,000 people.
- `event_period`: exact start and end dates required.

# Reasoning Path

The decisive signal is a wet tropical-cyclone cascade. The event period from 2023-02-21 to 2023-03-31 captures Freddy's prolonged impact phase across southern Africa. The ensemble rainfall anchors show substantial accumulated precipitation, with a mean near 84 mm and maxima near 200 mm, which is sufficient to support flood-producing runoff and slope-instability concern when paired with the event reports.

The correct answer should connect cyclone moisture and heavy rainfall to flooding, then to landslide susceptibility and health-risk monitoring. The exposed-population value should be treated as a scale-of-exposure context for operational concern, not as a count of people directly affected. The answer should also downgrade wind-core-only response because it misses the rainfall-flood cascade, drought/heat response because the signature is wet-event dominated, and wildfire or burn-scar response because the surface-change checks do not make fire the dominant disaster mode.

# Disaster Interpretation

Freddy's operational significance is its prolonged, repeated tropical-cyclone moisture delivery over vulnerable terrain and communities. The hazard chain is not limited to destructive winds near landfall. Rainfall-driven flooding can affect large areas downstream and can leave soils unstable enough to elevate landslide concern. In southern African emergency operations, that also makes public-health monitoring relevant, especially where flooding and displacement can worsen water, sanitation, and disease risk.

The benchmark therefore rewards a response-priority diagnosis that synthesizes physical forcing, hydrologic impact, slope risk, exposure context, and monitoring needs while avoiding unsupported loss claims.

# Scoring Rubric

Total: 20 points.

- 4 points: Correctly selects `compound_rainfall_flood_landslide_health_monitoring_priority` or a semantically equivalent compact label.
- 4 points: Identifies cyclone moisture and heavy rainfall as the main physical driver and includes the event period and rainfall anchors within tolerance.
- 3 points: Builds the impact chain from flooding to landslide susceptibility and health-risk monitoring.
- 3 points: Uses the exposed-population value as exposure context without converting it into a directly affected population count.
- 3 points: Rejects wind-core-only, drought/heat, and wildfire/burn-scar priorities with event-mechanism reasoning.
- 2 points: Avoids unsupported claims about exact deaths, cholera cases, landslide counts, flood depths, infrastructure losses, or economic damage.
- 1 point: Returns a concise, well-structured JSON answer with the requested fields.

Forbidden overclaims should be penalized: exact death, cholera-case, landslide-count, flood-depth, hospital-disruption, road-closure, outage, or economic-loss totals; claims that all exposed people were directly affected; or claims that negative burn-scar checks prove wildfire damage.
