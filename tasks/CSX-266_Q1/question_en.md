# Compound Fire-Atmosphere Priority

For incident-priority reasoning during the 2019-2020 Australian Black Summer heat-drought-fire-smoke event, decide which mechanism is the best primary response priority. The briefing must separate ordinary fuel dryness and burn severity from the more unusual fire-atmosphere escalation pathway, while also accounting for hot dry antecedent weather, wind support, smoke transport, rainfall alternatives, and exposed population context. The operations question is not simply whether fires occurred, but which mechanism should drive the first technical priority label and index.

- `pyroconvective_smoke_injection_priority`
- `fuel_dryness_burn_severity_priority`
- `rainfall_or_flood_priority`
- `population_exposure_only_priority`

Reason across heat and dryness persistence, wind support, burn or land-surface change, smoke or fire-atmosphere escalation, and exposed population context. Return your answer as:

Use these explicit component scores for the priority index:

```text
heat_dryness_score = min(heat_days_ge_40c / 45, 1)
dryness_score = min(longest_dry_run_days / 60, 1)
wind_score = min(wind_days_ge_35kmh / 12, 1)
burn_score = min(max(sentinel2_dnbr_mean, 0) / 0.12, 1)
smoke_score = smoke_escalation_flags / 6
exposure_score = min(population_exposed / 300000, 1)
rainfall_score = min(total_precip_mm / 300, 1)

priority_index =
round(100 * (0.20*heat_dryness_score
           + 0.15*dryness_score
           + 0.10*wind_score
           + 0.15*burn_score
           + 0.30*smoke_score
           + 0.10*exposure_score), 1)

fuel_burn_index =
round(100 * (0.35*heat_dryness_score
           + 0.30*dryness_score
           + 0.20*burn_score
           + 0.15*wind_score), 1)
```

Treat gridded precipitation and heat products, and the dNBR burn-change layer, as bounded coverage context when their available windows end before the full event period.

```json
{
  "answer": "<priority_label>",
  "priority_index": "<value>",
  "evidence_scope": {
    "point_weather": "<coverage role>",
    "gridded_products": "<coverage role>",
    "dnbr": "<coverage role>",
    "population": "<coverage role>"
  },
  "key_metrics": {
    "heat_days_ge_40c": "<value>",
    "longest_dry_run_days": "<value>",
    "wind_days_ge_35kmh": "<value>",
    "sentinel2_dnbr_mean": "<value>",
    "population_exposed": "<value>",
    "smoke_escalation_flags": "<value>"
  },
  "impact_chain": ["<driver>", "<escalation>", "<impact>"]
}
```
