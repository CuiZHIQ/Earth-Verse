# Final Answer

The correct structured core is:

```json
{
  "answer": "reef_bleaching_heat_stress_priority",
  "priority": "triage_coral_bleaching_and_reef_ecosystem_heat_stress",
  "dominant_mechanism": "persistent_anomalously_warm_sea_surface_conditions",
  "impact_pathway": ["marine_heatwave", "degree_heating_week_heat_stress", "coral_bleaching_and_reef_ecosystem_risk"],
  "key_metrics": {
    "event_window_days": 121,
    "marine_evidence_score": 13,
    "marine_evidence_score_max": 13,
    "surveyed_reefs_with_bleaching_percent": 93,
    "northern_severely_bleached_percent": 81,
    "degree_heating_week_death_possible_threshold": 8,
    "marine_index_terms": ["SST", "SST anomaly", "HotSpot", "Degree Heating Week", "Bleaching Alert Area", "7-day SST Trend"]
  }
}
```

The operational priority is coral bleaching and reef ecosystem heat-stress triage.

# Key Computations

Selected local evidence:

- `metadata/event.json` identifies the event as the 2016 Great Barrier Reef marine heatwave and bleaching event, with hazard family `marine_heatwave_coastal_ecosystem`.
- The locked event anchor gives the window from 2016-02-01 through 2016-05-31, so `event_window_days = 121`.
- The local climate report links unusually warm water, heat stress, Degree Heating Week reasoning, and widespread coral bleaching.
- The report gives `surveyed_reefs_with_bleaching_percent = 93`, `surveyed_reefs = 900`, `escaped_bleaching_reefs = 68`, `severely_bleached_reefs = 316`, and northern/central/southern severe bleaching of 81%, 33%, and 1%.
- The same report gives Degree Heating Week guideposts: bleaching likely above 4 and significant bleaching/death possible above 8.
- The local marine context supplies SST, SST anomaly, HotSpot, Degree Heating Week, Bleaching Alert Area, and 7-day SST Trend terms.

The transparent evidence score has 13 possible marine/reef components and all 13 are satisfied. No land-weather, population, AOI, or terrestrial remote-sensing product is part of the scored answer.

# Reasoning Path

1. The event identity and time window describe a Great Barrier Reef marine heatwave and coral bleaching event.
2. The mechanism is persistent anomalously warm sea surface conditions, expressed for reefs as accumulated coral heat stress.
3. The impact evidence is direct and severe: 93% of surveyed reefs showed bleaching and the northern section reached 81% severe bleaching.
4. Marine heat-stress products and terms match the mechanism: SST, SST anomaly, HotSpot, Degree Heating Week, Bleaching Alert Area, and 7-day SST Trend.
5. The correct answer keeps the response priority on coral bleaching and reef ecosystem heat stress.

# Scoring Rubric

Total: 20 points.

- 4 points: correct final priority: `reef_bleaching_heat_stress_priority` or an equivalent reef ecosystem heat-stress label.
- 3 points: structured core answer with priority, dominant mechanism, impact pathway, and key metrics.
- 4 points: quantitative reef anchors: 121-day window, marine evidence score 13/13, 93% surveyed-reef bleaching, 81% northern severe bleaching, and DHW threshold 8.
- 3 points: marine heat-stress mechanism linking anomalously warm sea surface conditions to accumulated coral heat stress and DHW reasoning.
- 3 points: reef impact and severity interpretation, including widespread bleaching, severe bleaching counts, and the north-to-south severity gradient.
- 2 points: source-scope discipline: uses reef-specific bleaching, marine heat-stress, OISST, and reef-monitoring evidence rather than land-product proxies.
- 1 point: uncertainty discipline: avoids unsupported loss, mortality, reef-by-reef DHW, or tourism claims.
