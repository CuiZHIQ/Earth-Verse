# Final Answer

The expected priority label is:

```text
compound_explosive_volcano_tsunami_ashfall_coastal_priority
```

The response diagnosis should identify the event as a compound explosive submarine volcano-tsunami-ashfall emergency. The initial priority should emphasize coastal evacuation and coastal safety, lifeline continuity, ashfall response, and rapid screening for island and coastal surface disturbance.

# Key Computations

The hidden reference computation uses the event identity, the locked event window, the event-specific report, the GDACS event entry, and event-window rainfall summaries from the CSX-310 source files.

Important anchors:

```json
{
  "severity_signal": "Red volcano alert",
  "plume_height_km_max": 50.0,
  "gpm_precip_mm_max": 0.005,
  "chirps_precip_mm_max": 0.0
}
```

The priority chain is:

```json
[
  "submarine_water_magma_explosion",
  "ashfall_and_destructive_tsunami",
  "coastal_evacuation_lifeline_and_ash_response"
]
```

The event report describes a violent submarine eruption in which large water-magma interaction helped drive an explosive event, with a very high plume, ashfall over nearby islands, destructive tsunami waves, and major geomorphic disturbance. The GDACS severity signal is Red. Event rainfall is effectively negligible, so rainfall flooding is not the dominant response pathway. Rapid island/coastal disturbance screening is a response need inferred from the compound event report, not a direct loss measurement.

# Reasoning Path

1. Start from the physical trigger: the eruption was submarine and explosive, with water-magma interaction capable of producing intense blast, plume, ashfall, and tsunami coupling.
2. Link the trigger to the first-order hazards: ashfall threatens health, water supply, aviation, and infrastructure, while destructive tsunami waves make coastal evacuation and coastal safety the immediate life-safety pathway.
3. Use severity and scale anchors: the Red alert and plume height near 50 km are consistent with an extreme volcanic emergency rather than routine ash monitoring.
4. Reject rainfall and ordinary local-weather alternatives: precipitation anchors are near zero, and the report/catalog mechanism explains the disaster priority.
5. Interpret exposure context operationally: coastal communities and lifelines matter for response planning, but the answer does not require a gridded population count.
6. Use disturbance screening carefully: the report-supported island/coastal disturbance motivates rapid reconnaissance, while exact inundation depth, building loss, and casualty estimates remain outside the deterministic answer target.

# Disaster Interpretation

Scientifically, the event is best understood as a high-energy submarine explosive volcanic event that coupled atmospheric, oceanic, and terrestrial hazards. The emergency was compound: the eruption produced ashfall and an extreme plume, generated damaging tsunami waves, and altered island/coastal surfaces.

Operationally, the first response posture should not be organized around a rainfall-flood scenario, a local wind or heat episode, or routine ash observation alone. The priority should be coastal life safety, lifeline continuity, ashfall management, and rapid reconnaissance for island/coastal disturbance. The answer can use the numerical anchors above, but the core judgment is a mechanism-impact chain rather than a table of measurements.

# Scoring Rubric

Total: 20 points.

- 4 points: Gives `compound_explosive_volcano_tsunami_ashfall_coastal_priority` or a semantically equivalent compound volcano-tsunami-ashfall coastal-priority answer.
- 3 points: Provides the correct trigger-to-impact chain: submarine water-magma explosive eruption to ashfall and destructive tsunami to coastal evacuation, lifeline, ashfall, and disturbance-screening priorities.
- 3 points: Uses severity and eruption-scale anchors correctly, including Red alert severity and an extreme plume-scale signal near 50 km, without making the response solely numeric.
- 3 points: Correctly rejects rainfall-flood, local heat/wind, and routine ash-only interpretations using near-zero rainfall and the compound tsunami-plus-ash mechanism.
- 3 points: Explains the disaster mechanism across scales, connecting volcanic forcing, ocean response, ashfall consequences, coastal/island disturbance, and coastal communities or lifelines.
- 2 points: Controls overclaims by not asserting exact casualties, exact building loss, exact tsunami depth, or requiring auxiliary population/surface-change statistics as direct human-loss measurements.
- 2 points: Returns the requested compact JSON object with a clear answer label, priority chain, key anchors, and 2-4 sentences of concise reasoning.
