# Final Answer

The correct priority is `compound_heat_drought_water_supply_priority`.

Expected compact response:

```json
{
  "answer": "compound_heat_drought_water_supply_priority",
  "priority_index": 99.3,
  "component_scores": {
    "heat_extremity": 0.973,
    "drought_water_stress": 1.0,
    "reported_human_impact": 1.0,
    "official_response": 1.0,
    "local_exposure": 1.0
  },
  "impact_chain": [
    "persistent_extreme_heat",
    "yangtze_meteorological_drought",
    "water_supply_and_drought_relief_priority"
  ],
  "brief_reasoning": "Record-scale heat, Yangtze-region precipitation deficit, drought warning, and reservoir operations jointly point to a compound heat-drought water-supply emergency. The reported affected population and economic loss make the water-supply pathway operationally dominant, while heat-only, flood-response, and land-change framings omit key evidence."
}
```

The answer may use equivalent wording, but it must make compound heat plus Yangtze drought and water-supply stress the primary operational priority. A heat-only health-alert answer is incomplete, and flood response or generic land-change monitoring are not the dominant priority for this event record.

# Key Computations

Selected hidden evidence:

- `metadata/event.json`: identifies the event as the 2022 China heat wave and Yangtze drought, with hazard family `compound_cascading_events`.
- `data/physical_hazard/physical_hazard_007_WMO_China_extreme_weather_heat_and_drought.html`: provides the institutional claims about record heat, low precipitation along the Yangtze, affected population, economic loss, reservoir operations for water supply, and drought warnings.
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`: provides event-window gridded heat intensity.
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`: provides local exposed population context.
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json` and `data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json`: provide precipitation context but do not override the documented drought mechanism.
- `data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json` and `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`: provide land-change context but do not define the main response priority.

Documented claims used by `compute_gt.py`:

- The heat wave was described as the strongest since complete meteorological observations began in 1961.
- By 15 August, the heat wave had broken the 2013 duration record of 62 days.
- Temperatures above 40 C had the largest incidence on record.
- Provinces and cities along the Yangtze River had low precipitation and long-lasting high temperatures, with some places more than 80 percent below normal precipitation.
- Drought in July affected 5.527 million people and caused 2.73 billion Chinese yuan in direct economic loss.
- Reservoir groups in the Yangtze River Basin were operated to fight drought and ensure water supply.
- An orange warning of meteorological drought was issued.

Computed values:

```json
{
  "priority_index": 99.3,
  "severity_bin": "very_high",
  "component_scores": {
    "heat_extremity": 0.973,
    "drought_water_stress": 1.0,
    "reported_human_impact": 1.0,
    "official_response": 1.0,
    "local_exposure": 1.0
  },
  "era5_max_tmax_c": 39.5,
  "era5_mean_tmax_c": 36.4,
  "affected_people_millions": 5.527,
  "economic_loss_billion_yuan": 2.73,
  "population_in_aoi": 8453613,
  "alternative_priority_scores": {
    "compound_heat_drought_water_supply_priority": 99.3,
    "heat_only_health_alert_priority": 83.1,
    "flood_response_priority": 27.0,
    "remote_sensing_land_change_priority": 23.9
  }
}
```

The priority index is a weighted 0-100 score:

- heat extremity: 25 percent;
- drought and water-stress evidence: 30 percent;
- reported human and economic impact: 20 percent;
- official response evidence: 15 percent;
- local exposure: 10 percent.

# Reasoning Path

1. Establish the event type: the metadata and institutional report identify a compound heat wave and Yangtze drought, not a single-hazard heat alert or flood event.
2. Confirm heat extremity: official text claims record strength, record duration, and unprecedented incidence of temperatures above 40 C; ERA5-Land gives additional event-window heat intensity with maximum Tmax near 39.5 C and mean Tmax near 36.4 C.
3. Confirm drought-water stress: the Yangtze-region text claims low precipitation, prolonged high temperature, deficits exceeding 80 percent below normal in some places, an orange meteorological drought warning, and reservoir operations to secure water supply.
4. Tie hazard to impact: the reported 5.527 million affected people and 2.73 billion Chinese yuan in direct economic loss make the event an operational emergency, not only a climatological anomaly.
5. Compare alternatives: heat-only alerting is relevant but omits the water-supply pathway; event-window precipitation grids are not a basis for making flood response primary; dNBR and embedding-change signals are contextual and too weak to displace the documented drought-relief priority.

# Disaster Interpretation

This event is best interpreted as a compound heat-drought disaster in which persistent extreme temperatures amplified meteorological drought and water-supply stress along the Yangtze River system. The response-relevant mechanism is not merely heat exposure; it is the coupling of heat, precipitation deficit, reservoir management, drought warning, affected population, and economic disruption.

Operationally, the main priority should be drought relief and water-supply management under extreme heat conditions. Heat-health measures remain important, but they are a component of the compound response rather than the dominant framing. Flood response and remote-sensing land-change investigation are scientifically weaker as primary priorities because the documented response pathway centers on drought and water supply.

Unsupported overclaims to avoid:

- Do not claim a formal hydrological drought attribution study or return-period analysis.
- Do not infer exact mortality or morbidity counts from this event record.
- Do not treat event-window accumulated precipitation summaries alone as disproving the WMO drought claim, which concerns prolonged heat and regional precipitation deficits along the Yangtze.
- Do not make remote-sensing land change the main priority without connecting it to documented water-supply and drought-relief actions.
- Do not use outside sources to extend the event timeline, impact totals, or policy response.

# Scoring Rubric

Total: 20 points.

- 4 points: Correct final priority and index. Full credit requires `compound_heat_drought_water_supply_priority` or a clearly equivalent label, priority index near 99.3, and very-high severity interpretation. Partial credit for identifying compound heat-drought but omitting the index or severity.
- 4 points: Correct quantitative anchors and component scores. Full credit requires the five component scores, ERA5 heat anchors, affected population, economic loss, and local exposed population. Partial credit for using only some metrics or missing units.
- 3 points: Physical mechanism attribution. Full credit connects persistent extreme heat, Yangtze-region precipitation deficit, meteorological drought, and water-supply stress. Partial credit for describing heat and drought separately without explaining their coupling.
- 3 points: Impact and official response interpretation. Full credit links affected people, direct economic loss, reservoir operations, and drought warning to operational priority. Partial credit for mentioning impacts without explaining why they shift response priorities.
- 2 points: Cross-scale synthesis. Full credit integrates report claims, gridded heat context, exposure, precipitation context, and remote-sensing context without over-weighting any single product. Partial credit for relying on only text or only numeric evidence.
- 2 points: Rejection of weaker alternatives. Full credit explains why heat-only, flood-response, and land-change framings are weaker as primary priorities. Partial credit for rejecting only one or two alternatives.
- 2 points: Concise structure and uncertainty control. Full credit returns the requested JSON-style answer, uses compact expert reasoning, and avoids unsupported mortality, attribution, or outside-source claims. Partial credit for a correct conclusion with loose formatting or minor overstatement.
