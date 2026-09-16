# Coastal Cascade Response Priority

A New York City emergency-management analysis team is preparing a short technical note on Hurricane Sandy's 29-30 October 2012 coastal flood and power-outage cascade. The decision lead needs a compact classification that separates the dominant disaster mechanism from three plausible but incomplete readings: a rainfall-dominant urban drainage flood, a wind-dominant structural-damage event, or an interpretation that stays genuinely mixed and uncertain.

Determine the mechanism label and response-priority stance that best fit the Sandy coastal-city impact chain. Anchor the answer with the event's quantitative indicators for storm severity, exposed population, cascade signal, and response-priority index, then express the driver-to-impact chain in three concise steps.

Use this package-specific response-priority index:

- `wind_norm = min(cyclone_wind_kmh / 178, 1)`
- `exposure_norm = min(log10(population_exposed) / log10(5000000), 1)`
- `cascade_norm = cascade_signal_score / 4`, where the four cascade indicators are coastal/surge context, flood context, power-outage context, and cascade wording.
- `precip_norm = min(combined_precip_mean_mm / 25, 1)`, where combined precipitation mean is the average of the available gridded precipitation means.
- `risk_index_0_100 = 35 * wind_norm + 35 * exposure_norm + 20 * cascade_norm + 10 * precip_norm`.

Return only compact JSON in this form:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority": "<priority_label>",
  "key_metrics": {
    "risk_index_0_100": "<value>",
    "cyclone_wind_kmh": "<value>",
    "population_exposed": "<value>",
    "cascade_signal_score": "<value>"
  },
  "impact_chain": ["<driver>", "<primary_hazard>", "<main_impact>"]
}
```
