# Final Answer

The expected priority label is `basin_wide_tsunami_life_safety_priority`.

Canonical compact answer:

```json
{
  "answer": "basin_wide_tsunami_life_safety_priority",
  "mechanism_chain": [
    "megathrust_earthquake_on_plate_interface",
    "seafloor_uplift_displaced_water",
    "basin_wide_tsunami_coastal_life_safety_impact"
  ],
  "priority_rationale": "The first response priority should be tsunami life safety across exposed Indian Ocean coasts, not local shaking alone. The incident record links a magnitude 9.1 plate-interface rupture to seafloor uplift, displaced water, an approximately 30-minute near-source arrival parsed from the report text, more than 30 m reported runup on western Sumatra, and a large exposed coastal population context.",
  "key_findings": [
    "reported magnitude about 9.1",
    "nearest coast arrival about 30 minutes",
    "reported runup greater than 30 m",
    "population context about 8.78 million people"
  ],
  "rejected_interpretations": [
    "local_earthquake_shaking_priority",
    "rainfall_flood_priority",
    "remote_sensing_change_priority"
  ]
}
```

# Key Computations

The reference computation uses these hidden sources:

- `metadata/event.json`: event identity and geophysical tsunami hazard family.
- `data/event_reports/event_reports_001_Locked_anchor_USGS.html`: earthquake-tsunami mechanism, tsunami arrival timing, runup, basin-scale impacts, and loss-of-life context.
- `data/event_reports/event_reports_002_Locked_event_anchor_2004_Sumatra-Andaman_earthquake_and_Indian_Ocean_tsunami.json`: event date and spatial anchor.
- `data/event_catalogs/event_catalogs_003_GDACS_earthquake_alert_API.json`: earthquake alert context.
- `data/physical_hazard/physical_hazard_001_ERA5-Land_hourly_aggregate_stats.json`, `data/physical_hazard/physical_hazard_002_GPM_IMERG_V07_event_accumulated_precipitation.json`, and `data/physical_hazard/physical_hazard_003_CHIRPS_daily_event_accumulated_precipitation.json`: precipitation context for rejecting ordinary rainfall flooding as the primary mechanism.
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`: exposed-population context.
- `data/remote_sensing/remote_sensing_001_Sentinel-1_GRD_VV_pre_post_change.json`: image-change availability context.

Key extracted and computed values:

```json
{
  "reported_magnitude": 9.1,
  "near_source_arrival_minutes": 30.0,
  "maximum_reported_runup_m": 30.0,
  "population_context_millions": 8.78,
  "gdacs_alert_level": "Red",
  "rainfall_primary_supported": false,
  "event_precipitation_means_mm": {
    "gpm": 0,
    "chirps": 0,
    "era5_land": 0.002581
  },
  "remote_sensing_change_primary_supported": false
}
```

The magnitude, near-source arrival, and runup anchors are parsed from the USGS report text rather than supplied as fixed constants. The population value is calculated as `8779523.348484986 / 1,000,000 = 8.78 million`. The precipitation means are all near zero; the GT script treats ordinary rainfall flooding as unsupported as a primary mechanism when the maximum event-window mean is not greater than 10 mm. The Sentinel-1 change layer has `no_sufficient_scenes`, so it cannot be used as the primary basis for response priority, but that absence is not evidence that inundation or damage did not occur.

# Reasoning Path

1. The event trigger is a very large plate-interface Sumatra-Andaman megathrust earthquake, not a meteorological flood process.
2. The dominant disaster pathway is not shaking alone. The earthquake uplifted the seafloor, displaced the overlying water column, and generated tsunami waves that propagated across the Indian Ocean.
3. Arrival-time pressure makes this a life-safety emergency: northern Sumatra had roughly 30 minutes before tsunami arrival, while more distant coasts had longer but still urgent warning windows.
4. Reported runup greater than 30 m along western Sumatra and a population context of about 8.78 million support prioritizing coastal warning, evacuation, rescue, medical triage, and access restoration.
5. Ordinary rainfall flooding is a weak explanation because the precipitation summaries are near zero during the event window.
6. A mainly image-change interpretation is also weak: the relevant change layer lacks sufficient scenes, so it can neither drive the priority nor disprove tsunami impact.

# Disaster Interpretation

Scientifically, this is a subduction-zone earthquake-tsunami chain: rupture on the India-Burma plate interface produced vertical seabed displacement, which displaced seawater and created basin-scale tsunami waves. Operationally, the decisive first-response issue is time-critical coastal life safety across multiple Indian Ocean shorelines. Local shaking matters near the rupture, but it is not the mechanism that explains the multi-country mortality and coastal destruction pattern. The correct briefing should therefore emphasize tsunami warning and evacuation logic, rapid search and rescue, exposed coastal populations, and caution against converting absent image-change products into a no-impact claim.

Unsupported overclaims:

- Do not claim that the record provides a full hydrodynamic tsunami simulation.
- Do not infer precise country-by-country mortality or response performance.
- Do not make rainfall or ordinary flood indicators the primary disaster trigger.
- Do not treat missing image-change evidence as proof that inundation or coastal damage did not occur.
- Do not treat local shaking alone as the dominant basin-scale life-safety pathway.

# Scoring Rubric

Total: 20 points.

- 3 points: Final priority label and stance. Full credit selects `basin_wide_tsunami_life_safety_priority` or a clearly equivalent label and frames the first response around tsunami coastal life safety. Partial credit for naming tsunami as important without making it the first response priority.
- 4 points: Mechanism chain. Full credit links megathrust or plate-interface earthquake, seafloor uplift or vertical displacement, water displacement, tsunami propagation, and coastal impact. Partial credit for a correct but incomplete chain, such as earthquake to tsunami without the seafloor-displacement step.
- 4 points: Quantitative anchors. Full credit uses magnitude about 9.1, near-source arrival about 30 minutes, runup greater than about 30 m, and population context about 8.78 million with correct units and interpretation. Partial credit is up to 1 point per anchor within tolerance.
- 3 points: Timing and response-priority reasoning. Full credit explains why short warning time and basin-scale coastal exposure make warning, evacuation, rescue, and life-safety actions the first priority. Partial credit for generic emergency language without time-pressure logic.
- 2 points: Rejection of competing mechanisms. Full credit rejects shaking-only, rainfall-first, and image-change-first interpretations for mechanism-specific reasons. Partial credit for rejecting alternatives without explaining why they are physically weaker.
- 2 points: Cross-scale disaster interpretation. Full credit connects geophysical trigger, ocean-basin propagation, local runup severity, and exposed-population implications. Partial credit for discussing only physical hazard or only exposure.
- 2 points: Output discipline and uncertainty control. Full credit returns the requested compact JSON, stays concise, and avoids unsupported claims about simulations, precise country losses, rainfall causation, or no impact from missing imagery. Partial credit for a mostly correct answer with formatting problems or minor overreach.
