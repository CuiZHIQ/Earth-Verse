# El Nino Fire-Haze Preparedness Brief

A regional disaster-risk team is preparing an early-action note on the 2015-2016 El Nino and Indonesian drought/fire-haze crisis across Indonesia and Maritime Southeast Asia. The decision is whether the incident record supports a forecast-triggered peat-fire and haze preparedness priority, or whether planning should be framed around another dominant hazard mechanism.

Prepare a compact expert JSON briefing that links the climate teleconnection to fuel and land conditions, smoke exposure, air-quality health risk, and transport disruption. Anchor the diagnosis with the peak Oceanic Nino Index, the number of 2015-2016 ONI seasons at or above 1.5 C, the surface carbon monoxide ratio relative to usual conditions, and the ratio between the reported Pollutant Standards Index value and its hazardous threshold. Also make clear why heavy-rain flooding, cyclone or coastal surge, heat-only response, and image-only burn-scar interpretation are not the primary operational frame.

Return only compact JSON in this structure:

```json
{
  "priority": "<compact_priority_label>",
  "mechanism": ["<driver>", "<fuel_or_land_condition>", "<impact_pathway>"],
  "key_indices": {
    "peak_oni": "<value>",
    "oni_ge_1_5_seasons": "<value>",
    "co_surface_ratio_to_usual": "<value>",
    "psi_hazard_ratio": "<value>"
  },
  "context_scope": {
    "precipitation_products": "<coverage and role>",
    "remote_sensing": "<coverage and role>",
    "population": "<coverage and role>"
  },
  "rejected_alternatives": {
    "heavy_rain_flooding": "<brief reason>",
    "cyclone_or_coastal_surge": "<brief reason>",
    "heat_only_response": "<brief reason>",
    "image_only_burn_scar": "<brief reason>"
  },
  "action_logic": "<one sentence explaining the preparedness priority>"
}
```
