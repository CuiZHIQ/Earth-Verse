# Puncak Jaya Glacier Retreat Consistency Diagnosis

A cryosphere monitoring team is reviewing the Puncak Jaya tropical glacier retreat episode in Indonesian Papua during 1 October 2015 through 31 March 2016. The decision is whether the climate and surface-change signals are physically consistent with slow warm-dry ablation stress and sustained glacier retreat, or whether they support a sudden impact trigger such as rain-on-snow flooding, avalanche disruption, or a diagnosed glacial outburst flood.

Using the incident technical record, compute the daily warm-dry signal for the shared local point-weather window and interpret it with the longer retreat-stage context. A consensus warm-dry day is a day when both aligned temperature indicators are at least 28.0 C and both aligned precipitation indicators are at most 0.2 mm. Treat this point-window signal as a package-derived physical-consistency diagnostic, not as a direct glacier-wide mass-balance measurement or exact full-surface dryness map. Support the diagnosis with quantitative anchors and process reasoning: thermal forcing, precipitation and snow-versus-rain context where supported, melt/ablation or glacier mass-balance stress, hydrologic or outburst-flood risk, annual surface-change interpretation, and response or monitoring implications.

Return only JSON in this shape:

```json
{
  "answer": "<compact_mechanism_stage_label>",
  "structured_answer": {
    "warm_dry_index": "<number rounded to 3 decimals>",
    "consensus_warm_dry_days": "<integer>",
    "total_point_days": "<integer>",
    "point_precip_total_mean_mm": "<number rounded to 1 decimal>",
    "point_temperature_mean_c": "<number rounded to 2 decimals>",
    "event_duration_days": "<integer>",
    "thermal_forcing": "<one concise sentence>",
    "precipitation_snow_rain_context": "<one concise sentence>",
    "mass_balance_stress": "<one concise sentence>",
    "hydrologic_outburst_risk": "<one concise sentence>",
    "annual_surface_change_interpretation": "<one concise sentence>",
    "response_monitoring_implication": "<one concise sentence>"
  },
  "key_findings": [
    {"name": "climate_signal", "value": "<brief numeric summary>"},
    {"name": "glacier_process", "value": "<brief mechanism/stage interpretation>"},
    {"name": "monitoring_priority", "value": "<brief operational implication>"}
  ],
  "limitations": ["<unsupported claim avoided>"]
}
```
