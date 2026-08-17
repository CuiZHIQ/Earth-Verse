# Final Answer

```json
{
  "answer": "urban_lava_flow_impact",
  "response_priority": "life_safety_evacuation_and_emergency_shelter",
  "key_numeric_anchors": {
    "catalog_alert_level": "Red",
    "reported_deaths": 32,
    "reported_destroyed_homes": 1000,
    "aoi_population_rounded": 43914,
    "mean_surface_change_index": 0.0271
  },
  "impact_chain": [
    "volcanic eruption and lava displacement near Goma",
    "fatalities, housing loss, and urban population exposure",
    "life safety evacuation, shelter, and displacement support"
  ],
  "why_alternatives_are_weaker": [
    "ash-centered disruption is not the dominant documented impact pathway",
    "rainfall or lahar flooding is contextual rather than primary",
    "surface change alone misses the reported urban humanitarian impact"
  ]
}
```

# Key Computations

The hidden source selection identifies the event as the 22-23 May 2021 Mount Nyiragongo eruption near Goma in the Democratic Republic of the Congo. The relevant source files are:

- `metadata/event.json`
- `metadata/files.csv`
- `data/event_reports/event_reports_002_Wikipedia_2021_Mount_Nyiragongo_eruption.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_2021_Mount_Nyiragongo_eruption.json`
- `data/event_catalogs/event_catalogs_005_04_event_specific_disaster_catalog_GDACS_event_list_for_package_time_window.json.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_009_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`

`compute_gt.py` extracts the report impact counts with regular expressions, locates the volcano catalog feature for Nyiragongo, rounds the AOI population summary, and records contextual rainfall and remote-sensing change metrics.

Core anchors:

- Catalog alert level: Red.
- Reported deaths: 32.
- Reported destroyed homes: 1,000.
- Rounded AOI population summary: 43,914, used only as exposure context.
- Mean Sentinel-2 surface-change index: 0.0271.
- Contextual mean embedding change: 0.0105.
- Contextual mean event precipitation: 5.02 mm.

# Reasoning Path

The dominant emergency mechanism is an urban lava-flow and displacement impact chain. The event is a volcano eruption near a dense urban area, the catalog alert is Red, and the reported impacts include fatalities and destroyed homes. Those anchors point to immediate life-safety, evacuation, shelter, and displacement-support operations rather than a primarily atmospheric, hydrologic, or image-only interpretation.

The exposure figure supports the urban-risk framing, but it should not be converted into a direct count of affected people. The surface-change metrics are useful corroborating context for physical disturbance, but they do not by themselves establish the humanitarian response priority. The precipitation metric is low-context support for rejecting rainfall or lahar flooding as the dominant mechanism in this task.

The weaker alternatives fail in different ways. Ash-centered aviation or air-quality disruption is plausible for a volcanic event but is not the documented main impact pathway here. Rainfall or lahar flooding is contextual rather than primary. A remote-sensing-only land-surface-change answer notices physical disturbance but stops before the operational humanitarian implication.

# Disaster Interpretation

Scientifically, the event should be interpreted as a volcanic eruption whose most important near-term disaster expression was lava-driven impact in and around Goma. Operationally, that means the first response note should emphasize people exposed to lava-flow damage, fatalities, destroyed housing, evacuation needs, emergency shelter, and displacement support.

The correct analysis should remain disciplined about what the data can support. It should not claim a precise lava-flow footprint, exact displacement total, exact ash plume height, aviation closures as the dominant impact, road closure counts, hospital outages, or infrastructure-loss counts beyond the anchored evidence. It should also avoid treating the population summary as a direct affected-population count.

# Scoring Rubric

Total: 20 points.

- Final mechanism and response priority, 5 points: full credit selects `urban_lava_flow_impact` or an equivalent lava-driven urban displacement mechanism and names life safety, evacuation support, emergency shelter, and displacement assistance as the response priority. Award up to 3 points for the correct lava-driven urban impact mechanism and up to 2 points for the response priority.
- Quantitative anchors, 4 points: full credit uses the Red alert level, 32 deaths, 1,000 destroyed homes, rounded population exposure near 43,914, and mean surface-change index near 0.0271 accurately and in the right role. Award roughly equal credit for each correct anchor within tolerance; give substantial credit for at least three correct anchors when they support the mechanism rather than appear as an isolated metric list.
- Physical mechanism reasoning, 4 points: full credit connects the volcanic trigger and lava displacement near Goma to fatalities, housing destruction, urban exposure, and emergency operations. Award partial credit for recognizing the volcanic or lava trigger without a complete impact chain, or for naming impacts without clearly tying them to the operational priority.
- Cross-scale interpretation, 3 points: full credit uses population and remote-sensing metrics as context without treating them as a complete damage model or as direct affected-population counts. Award partial credit for using either exposure context or surface-change context correctly; withhold credit for converting contextual metrics into unsupported exact damage or affected-person counts.
- Alternative mechanism rejection, 2 points: full credit explains why ash-centered disruption, rainfall or lahar flooding, and image-only interpretations are weaker for immediate operations. Award 1 point for rejecting one or two weaker alternatives with a valid reason; award 2 points only when the answer covers the main ash, rainfall/lahar, and image-only alternatives.
- Overclaim control and output structure, 2 points: full credit avoids unsupported exact footprints, displacement totals, infrastructure-loss claims, and dominant ash/flood claims while returning the requested concise JSON structure. Award 1 point for mostly disciplined claims with minor format issues, or for correct JSON structure with one small unsupported extrapolation; award 0 if unsupported claims drive the conclusion.

Numeric tolerances are defined in `computed_gt.json`; the task is not scored as a broad metric inventory.
