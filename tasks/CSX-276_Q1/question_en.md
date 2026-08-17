# Southern Africa Drought Readiness Diagnosis

A regional food-security coordination cell is preparing a 2016 readiness note for
the Southern Africa drylands after the 2015-2016 El Nino. Field teams disagree
about the planning diagnosis: some frame the situation as a teleconnected
dryland drought and food-security readiness problem, while others argue for a
brief local rainy-season precipitation episode, a wildfire or smoke-response
pathway, or a weak climate anomaly with little emergency relevance.

Decide which diagnosis should drive preparedness. Anchor the decision in the
climate-mode strength, persistence, atmosphere-ocean coupling, and local
population context, and express the climate-to-impact logic as a three-step
priority chain.

Return a compact JSON object:

```json
{
  "answer": "<compact_priority_label>",
  "key_metrics": {
    "warm_phase_peak_c": "<value>",
    "strong_season_count": "<value>",
    "coupling_minimum": "<value>",
    "local_population_context": "<value>"
  },
  "priority_chain": ["<climate_driver>", "<remote_mechanism>", "<planning_priority>"]
}
```
