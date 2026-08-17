# Solution

## Final Answer

The correct answer is `basin_scale_marine_heatwave_ecosystem_heat_stress_priority`.

The expected structured answer is:

```json
{
  "answer": "basin_scale_marine_heatwave_ecosystem_heat_stress_priority",
  "priority_index": 1.0,
  "key_metrics": {
    "event_window_days": 1127,
    "event_window_years": 3.09,
    "source_result_count": 6,
    "marine_heatwave_term_count": 10,
    "ecosystem_impact_term_count": 6,
    "northeast_pacific_reference_count": 3
  },
  "impact_chain": [
    "persistent_ocean_heat_anomaly",
    "basin_scale_marine_heatwave",
    "marine_ecosystem_heat_stress_and_foodweb_disruption_priority"
  ]
}
```

## Key Computations

- The package metadata classifies the event as a marine heatwave and coastal ecosystem impact.
- The locked anchor places the event in the Northeast Pacific Ocean from 2013-12-01 through 2016-12-31.
- Local search-result text identifies "The Blob (Pacific Ocean)" as an example of a marine heatwave and notes persistence into 2016.
- Local search-result text also contains harmful or toxic algal bloom context, supporting ecosystem-impact reasoning rather than a generic weather-response framing.

`compute_gt.py` reads local CSX-323 files and deterministically writes `computed_gt.json`. It counts marine-heatwave, ecosystem-impact, and Northeast Pacific terms from the event metadata, locked anchor, and local event-search evidence, computes the event-window length, and then assigns a transparent priority index.

The priority index is:

```text
0.25 * hazard_family_score
+ 0.20 * duration_score
+ 0.20 * marine_term_score
+ 0.20 * ecosystem_context_score
+ 0.15 * basin_context_score
```

The scoring rewards the confirmed marine heatwave family, a multi-year event window, repeated marine heatwave terminology, local ecosystem-impact language, and Northeast Pacific basin context.

Primary computed values:

```json
{
  "answer": "basin_scale_marine_heatwave_ecosystem_heat_stress_priority",
  "priority_index": 1.0,
  "event_window_days": 1127,
  "event_window_years": 3.09,
  "source_result_count": 6,
  "marine_heatwave_term_count": 10,
  "ecosystem_impact_term_count": 6,
  "northeast_pacific_reference_count": 3
}
```

## Reasoning Path

1. The package-level hazard family and event name identify a marine heatwave and coastal ecosystem-impact case, not a flood, windstorm, urban disaster, or terrestrial burn event.
2. The event window spans 1127 days, so the mechanism should be interpreted as persistent basin-scale ocean heat stress rather than a short-duration local weather trigger.
3. Local search-result text repeatedly connects "The Blob" with marine heatwave language and includes toxic or harmful algal bloom context, which points toward marine ecosystem impacts.
4. The local evidence has Northeast Pacific basin context, so the event should not be reduced to a local land-weather, urban-exposure, or terrestrial vegetation-change task.
5. No scored metric in the reference answer depends on point land weather, population, OSM, Sentinel-2, or generic heat-stress product counts.

The impact chain is therefore `persistent_ocean_heat_anomaly -> basin_scale_marine_heatwave -> marine_ecosystem_heat_stress_and_foodweb_disruption_priority`.

## Disaster Interpretation

The disaster priority is marine ecosystem heat stress driven by a persistent ocean heat anomaly. The long duration, repeated marine-heatwave language, and ecosystem-impact context point toward basin-scale ocean impacts such as food-web disruption and harmful algal bloom risk.

Unsupported overclaims:

- Do not claim exact species mortality, fisheries loss, tourism loss, or reef-by-reef bleaching severity from this package alone.
- Do not claim a full climate-attribution result for the event.
- Do not treat point land-weather samples, population products, or terrestrial remote-sensing layers as the primary physical driver of the Northeast Pacific marine heatwave.
- Do not infer a terrestrial wildfire, vegetation-loss, flood, landslide, or urban-service disaster from unrelated generic layers.

## Scoring Rubric

20 points total:

- Priority label (4 pts): selects `basin_scale_marine_heatwave_ecosystem_heat_stress_priority`.
- Duration and scale (3 pts): uses the 1127-day event window and basin-scale marine heatwave framing.
- Heat-stress mechanism (4 pts): uses marine heatwave, Northeast Pacific, and ecological-impact terminology to justify ecosystem heat-stress priority.
- Structured metrics (3 pts): reports the priority index near 1.00 and includes the expected event-window and text-evidence metrics with reasonable rounding.
- Competing-signal rejection (3 pts): correctly treats rainfall, wind, terrestrial disturbance, and urban exposure as non-dominant without relying on land-product proxies.
- Impact-chain quality (2 pts): gives the driver-hazard-impact chain from persistent ocean heat anomaly to marine ecosystem heat stress and food-web disruption.
- Overclaim control (1 pt): avoids unsupported claims about exact mortality, fisheries losses, climate attribution, or direct urban infrastructure impacts.
