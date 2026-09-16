# Final Answer

The correct mechanism is `coastal_surge_lifeline_outage_cascade`, and the correct response stance is `critical_lifeline_priority`.

Expected compact JSON:

```json
{
  "answer": "coastal_surge_lifeline_outage_cascade",
  "priority": "critical_lifeline_priority",
  "key_metrics": {
    "risk_index_0_100": 91.8,
    "cyclone_wind_kmh": 167.4,
    "population_exposed": 3848078,
    "cascade_signal_score": 4
  },
  "impact_chain": ["tropical_cyclone_forcing", "coastal_flooding", "power_outage_cascade"]
}
```

# Key Computations

The hidden computation uses the CSX-257 source package for Hurricane Sandy's New York City and New Jersey coastal event.

Primary source anchors:

- `metadata/event.json`: event identity, hazard family, and coastal megacity setting.
- `metadata/files.csv`: source accounting for package-local computation.
- `data/event_reports/event_reports_005_Locked_event_anchor_Hurricane_Sandy_New_York_City_coastal_flood_and_power_outage_cascade.json`: locked event window, location, and coastal flood plus outage-cascade framing.
- `data/event_catalogs/event_catalogs_001_GDACS_disaster_alert_API.json`: Sandy tropical cyclone entry, affected countries, alert context, duration, and wind severity.
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`: exposed population estimate.
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json` and `data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json`: precipitation context used to test the rainfall-only alternative.
- `data/event_reports/event_reports_003_NOAA_NHC_Tropical_Cyclone_Sandy_report_and_tide_gauges.html`: coastal water-level and tide-service context.

`compute_gt.py` performs a deterministic package-local computation:

- Finds the Sandy tropical cyclone feature in the event catalog.
- Extracts maximum wind severity, duration, affected-country context, and alert level.
- Reads the population exposure summary.
- Reads two precipitation summaries and averages their event-window mean precipitation.
- Scores four cascade indicators from the event and locked-anchor wording: coastal, flood, power outage, and cascade.
- Builds a task-specific response-priority index:

```text
35 * wind_norm + 35 * exposure_norm + 20 * cascade_norm + 10 * precip_norm
```

Intermediate values:

```json
{
  "cyclone_wind_kmh": 167.4,
  "population_exposed": 3848078,
  "cascade_signal_score": 4,
  "gpm_mean_mm": 6.6,
  "chirps_mean_mm": 16.0,
  "combined_precip_mean_mm": 11.3,
  "wind_norm": 0.94,
  "exposure_norm": 0.983,
  "cascade_norm": 1.0,
  "precip_norm": 0.452,
  "risk_index_0_100": 91.8
}
```

The index is a benchmark scoring anchor, not a public disaster standard.

# Reasoning Path

1. The event identity and locked anchor define Hurricane Sandy in the New York City and New Jersey coastal setting during 29-30 October 2012.
2. The catalog entry supplies tropical cyclone forcing affecting the United States, with hurricane-strength wind severity around 167.4 km/h and orange alert context.
3. The event text and locked anchor contain all four cascade indicators: coastal, flood, power outage, and cascade. This supports a coastal flood to lifeline-disruption pathway.
4. The exposed population estimate is about 3.85 million, making the response stance critical rather than routine monitoring.
5. Precipitation is present and relevant to the storm environment, but the modest package precipitation anchors and the coastal-cascade framing make a rainfall-only drainage-flood diagnosis too narrow.
6. A wind-only structural interpretation also fails because it omits the flood-to-power-outage cascade that drives the response-priority label.

# Disaster Interpretation

This task is about classifying the dominant cross-scale impact chain in a dense coastal metropolis. Sandy's hazard signature in this benchmark is not just a tropical cyclone wind event and not primarily a pluvial urban-drainage event. The operationally important chain is tropical cyclone forcing, coastal flooding, and disruption of lifeline systems, especially power. The high exposed population and complete cascade signal justify a critical lifeline or critical infrastructure priority stance.

The answer should avoid inventing precise inundation depths, substation outage counts, deaths, economic losses, or borough-level damage totals. Those details are not needed for the benchmark target and are not produced by the deterministic computation. The defensible conclusion is the dominant coastal flood and lifeline outage cascade, supported by the wind, exposure, cascade, precipitation-context, and index anchors.

# Scoring Rubric

Total: 20 points.

- 4 points: Selects `coastal_surge_lifeline_outage_cascade` or an equivalent coastal flood plus power/lifeline outage cascade mechanism.
- 3 points: Selects `critical_lifeline_priority` or an equivalent critical infrastructure/lifeline response stance.
- 4 points: Reports the four quantitative anchors within tolerance: risk index 91.8 +/- 0.5, cyclone wind 167.4 km/h +/- 0.5, exposed population 3,848,078 +/- 5,000, and cascade signal score 4 exactly.
- 3 points: Provides an impact chain equivalent to tropical cyclone forcing -> coastal flooding -> power outage cascade.
- 2 points: Explains or encodes why precipitation is contextual but not the dominant rainfall-only drainage mechanism.
- 2 points: Rejects or avoids the wind-only structural-damage interpretation as incomplete for the Sandy coastal-city cascade.
- 1 point: Avoids unsupported claims about exact inundation depth, peak storm tide, substation counts, deaths, economic loss, or borough-level losses.
- 1 point: Returns concise, valid JSON matching the requested schema.

Common failure modes:

- `rainfall_dominant_urban_drainage_flood`: plausible because precipitation is present, but it underweights the coastal flood and lifeline cascade.
- `wind_only_structural_damage_event`: plausible because cyclone wind is strong, but it misses the coastal flood and outage pathway.
- `mixed_or_uncertain_compound_event`: overly cautious if it refuses to identify the dominant cascade despite the event lock, cyclone context, exposure, and cascade signals.
- `remote_sensing_direct_damage_proof`: overreads visual or contextual layers as direct evidence of detailed outage, damage, or mortality.
