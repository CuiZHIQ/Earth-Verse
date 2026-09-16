## Final Answer

The correct answer is `marine_heatwave_coastal_ecosystem_heat_stress_priority`.

```json
{
  "answer": "marine_heatwave_coastal_ecosystem_heat_stress_priority",
  "priority": "monitor_and_triage_coastal_ecosystem_heat_stress",
  "dominant_mechanism": "persistent_anomalously_warm_sea_surface_conditions",
  "impact_pathway": ["marine_heatwave", "coral_bleaching_heat_stress", "coastal_ecosystem_risk"],
  "key_metrics": {
    "event_window_days": 183,
    "marine_evidence_score": 9,
    "marine_evidence_score_max": 9,
    "marine_index_term_count": 6,
    "marine_index_terms": ["SST", "SST anomaly", "HotSpot", "Degree Heating Week", "Bleaching Alert Area", "7-day SST Trend"],
    "source_flags": {
      "wmo_surface_temperature_context": true,
      "wmo_ecosystem_context": true,
      "oisst_2023_sst_available": true,
      "oisst_2023_sst_anomaly_available": true,
      "coral_bleaching_heat_stress_concept": true
    }
  }
}
```

## Key Computations

- The package metadata identifies a marine heatwave/coastal ecosystem hazard.
- The locked anchor places the event in the Northern Indian Ocean / Arabian Sea from 2023-04-01 through 2023-09-30, giving `event_window_days = 183`.
- The WMO report text provides surface-temperature and ecosystem context.
- The OISST catalog contains 2023 daily SST mean and SST anomaly entries.
- The NOAA Coral Reef Watch product page supplies marine heat-stress concepts: SST, SST anomaly, HotSpot, Degree Heating Week, Bleaching Alert Area, and 7-day SST Trend.

The transparent evidence score has 9 possible components and all 9 are satisfied: marine heatwave hazard family, marine heatwave event name, seasonal window at least 180 days, WMO surface-temperature context, WMO ecosystem context, OISST 2023 SST availability, OISST 2023 SST anomaly availability, coral bleaching heat-stress concept, and at least three marine index terms.

## Reasoning Path

1. The event identity and anchor define a regional marine heatwave context rather than a land heat, rainfall, wind, or land-cover-change task.
2. The mechanism should be framed as persistent anomalously warm sea-surface conditions.
3. The impact pathway is marine heatwave -> coral bleaching heat stress -> coastal ecosystem risk.
4. The answer should not invent exact SST anomaly, DHW, coral mortality, or basin-wide impact values.

## Scoring Rubric

20 points total:

- Priority label (4 pts): selects `marine_heatwave_coastal_ecosystem_heat_stress_priority` or an equivalent compact priority label.
- Dominant mechanism (3 pts): identifies persistent anomalously warm sea-surface conditions.
- Impact pathway (3 pts): connects the pathway to coral bleaching heat stress and coastal ecosystem risk.
- Event duration and evidence score (3 pts): reports the 183-day event window and `marine_evidence_score = 9/9`.
- Marine index concepts (3 pts): names at least three relevant terms such as SST, SST anomaly, HotSpot, Degree Heating Week, Bleaching Alert Area, or 7-day SST Trend.
- Source-scope discipline (2 pts): bases the decision on marine event identity and marine report/catalog context rather than land-weather, population, AOI, or terrestrial remote-sensing proxies.
- Overclaim control (2 pts): avoids unsupported claims about precise SST anomaly magnitude, Degree Heating Week values, coral mortality, flooding dominance, or exact basin-wide impacts.
