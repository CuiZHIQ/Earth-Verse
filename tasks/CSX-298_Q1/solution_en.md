# Final Answer

The correct compact answer is `transatlantic_fine_dust_air_quality_event`.

The correct response priority is `respiratory_air_quality_warning_and_exposure_reduction`.

```json
{
  "answer": "transatlantic_fine_dust_air_quality_event",
  "response_priority": "respiratory_air_quality_warning_and_exposure_reduction",
  "mechanism_summary": "The event is best diagnosed as a trans-Atlantic Saharan fine-dust plume with respiratory air-quality exposure as the lead response priority.",
  "key_numeric_anchors": [
    {
      "name": "event duration",
      "value": 15,
      "unit": "days"
    },
    {
      "name": "point-sampled maximum daily wind speed",
      "value": 31.1,
      "unit": "km/h"
    },
    {
      "name": "point-sampled event precipitation sum",
      "value": 2.37,
      "unit": "mm"
    },
    {
      "name": "rounded exposed-population context",
      "value": 43914,
      "unit": "people"
    }
  ],
  "impact_chain": [
    "saharan_dust_lofting_and_transport",
    "large_dense_transatlantic_plume",
    "fine_particles_near_surface",
    "unhealthy_air_quality_and_respiratory_exposure"
  ]
}
```

The June 2020 Saharan dust "Godzilla" outbreak should be diagnosed as a trans-Atlantic fine-dust air-quality and respiratory-exposure event. Rainfall/flood disruption, heat-stress response, and direct land-surface damage are weaker primary framings for this task.

# Key Computations

The hidden solution uses these package-relative sources:

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/event_reports/event_reports_003_Locked_event_anchor_June_2020_Saharan_dust_Godzilla_outbreak.json`
- `data/physical_hazard/physical_hazard_001_NASA_POWER_daily_point_sample.json`
- `data/physical_hazard/physical_hazard_002_Open-Meteo_archive_point_sample.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_001_Overpass_small_roads_and_critical_amenities.json`
- `data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`

Catalog files are not used as the decisive mechanism evidence. Specialized catalog absence should not outweigh the direct event report and package metadata.

The metadata identifies the hazard family as `dust_sandstorm_extreme`. The locked anchor sets the inclusive event window from 2020-06-14 through 2020-06-28, for an event duration of 15 days.

The main event report describes a very large, dense Saharan dust plume crossing the Atlantic, darkened Caribbean skies, high aerosol loading, poor air quality, unhealthy fine-particle conditions, and low-altitude fine dust that is especially relevant to human health. It also describes dry dusty air inhibiting clouds, which supports the dust-plume pathway over rainfall-driven disruption.

`compute_gt.py` computes the required concise bounded package-derived numeric anchors:

```json
[
  {"name": "event duration", "value": 15, "unit": "days", "tolerance": 0},
  {"name": "point-sampled maximum daily wind speed", "value": 31.1, "unit": "km/h", "tolerance": 0.1},
  {"name": "point-sampled event precipitation sum", "value": 2.37, "unit": "mm", "tolerance": 0.01},
  {"name": "rounded exposed-population context", "value": 43914, "unit": "people", "tolerance": 1}
]
```

Additional hidden context includes low point precipitation from a second daily source, five windy days at or above 25 km/h in the point sample, small annual semantic surface change, about 17,839.5 km2 approximate AOI area, and sparse local exposure features. These are supporting context, not required visible-answer metrics.

# Reasoning Path

1. Event identity and report language point to Saharan dust transport, not flooding, heat, or burn damage.
2. The impact mechanism is atmospheric transport of fine mineral dust across the Atlantic, with near-surface fine particles producing degraded air quality and respiratory exposure.
3. The 15-day window and point wind context support a sustained transport/exposure event.
4. Low point precipitation and the report's dry-dust cloud-inhibition claim weaken a rainfall/flood response framing.
5. Temperature context does not define the event, and the land-surface change metric is small, so heat-stress and burn-scar interpretations are weaker.
6. Population and amenity context make respiratory warning, exposure reduction, and air-quality public-health communication the leading response priority.

Expected structured answer:

```json
{
  "answer": "transatlantic_fine_dust_air_quality_event",
  "response_priority": "respiratory_air_quality_warning_and_exposure_reduction",
  "mechanism_summary": "The event is best diagnosed as a trans-Atlantic Saharan fine-dust plume with respiratory air-quality exposure as the lead response priority.",
  "key_numeric_anchors": [
    {"name": "event duration", "value": 15, "unit": "days"},
    {"name": "point-sampled maximum daily wind speed", "value": 31.1, "unit": "km/h"},
    {"name": "point-sampled event precipitation sum", "value": 2.37, "unit": "mm"},
    {"name": "rounded exposed-population context", "value": 43914, "unit": "people"}
  ],
  "impact_chain": [
    "saharan_dust_lofting_and_transport",
    "large_dense_transatlantic_plume",
    "fine_particles_near_surface",
    "unhealthy_air_quality_and_respiratory_exposure"
  ]
}
```

# Disaster Interpretation

Scientifically, the event is a sustained mineral-dust transport episode: Saharan dust was lofted and carried across the Atlantic in a dense plume, with fine particles affecting near-surface air quality across Caribbean receptors. The relevant disaster pathway is therefore atmospheric transport to human respiratory exposure, not direct inundation, thermal stress, or visible land-cover damage.

Operationally, the leading priority should be public-health-oriented air-quality messaging and exposure reduction. A strong answer may mention protecting people with respiratory vulnerability, reducing outdoor exposure during unhealthy air-quality periods, and communicating that low local rainfall and modest surface-change indicators do not make flooding or land damage the primary concern. The answer should avoid unsupported claims about exact deaths, illnesses, hospitalizations, economic losses, or precise dust concentrations throughout the plume.

# Scoring Rubric

Total: 20 points.

- 4 points: Correct final labels. Award up to 2 points for `transatlantic_fine_dust_air_quality_event` or equivalent mechanism wording, and up to 2 points for `respiratory_air_quality_warning_and_exposure_reduction` or equivalent priority wording.
- 4 points: Quantitative anchors. Award 1 point each for event duration of 15 days, maximum daily wind speed of about 31.1 km/h, point-sampled event precipitation sum of about 2.37 mm, and rounded exposed population of about 43,914 people.
- 4 points: Physical mechanism reasoning. Award for explaining Saharan dust lofting and trans-Atlantic transport, dense plume behavior, fine particles near the surface, and air-quality degradation.
- 3 points: Impact-chain interpretation. Award for connecting source/driver, atmospheric hazard process, near-surface exposure, and respiratory or public-health receptors.
- 2 points: Alternative framing rejection. Award for using event-specific reasoning to reject rainfall/flood disruption, heat stress, and land-surface damage as leading interpretations.
- 2 points: Overclaim control. Award for avoiding exact unsupported health, mortality, economic-loss, or plume-wide concentration claims and for not overinterpreting point meteorology or annual surface-change metrics.
- 1 point: Output quality. Award for concise, structured JSON-compatible output that includes the requested fields and remains readable.
