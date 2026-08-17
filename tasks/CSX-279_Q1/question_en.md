# 2015-2016 El Nino Drought Response Briefing

A Pacific emergency coordination team is preparing a technical note on the 2015-2016 El Nino drought emergencies affecting Pacific Island states. The team needs to decide whether the event should be interpreted mainly as a coupled ENSO teleconnection drought with freshwater and crop consequences, or as a different rapid-onset hazard such as direct heat stress, tropical-cyclone damage, flooding, or landslides.

Prepare a concise expert briefing that identifies the dominant disaster mechanism and the first response priority. Support the conclusion with quantitative anchors from the climate-mode behavior, atmospheric coupling, rainfall-distribution signal, and exposed-population scale, then connect those values to the reported island impacts. Treat the gridded rainfall summary as a precipitation-product evidence-window diagnostic of spatial dryness contrast, not as a complete island-by-island reconstruction of the full emergency period.

Return your answer as a JSON object with this structure:

```json
{
  "dominant_mechanism": "<compact mechanism label or phrase>",
  "priority_focus": "<compact priority label or phrase>",
  "evidence_windows": {
    "event_window": "<YYYY-MM-DD_to_YYYY-MM-DD>",
    "precipitation_evidence_window": "<YYYY-MM-DD_to_YYYY-MM-DD>"
  },
  "key_indices": {
    "peak_oni_anomaly_c": "<number>",
    "mean_event_soi": "<number>",
    "dry_pocket_ratio": "<number>",
    "exposed_population_millions": "<number>"
  },
  "impact_chain": ["<driver>", "<hazard_process>", "<priority_impact>"],
  "briefing_note": "<2-4 sentences explaining why this mechanism and priority are strongest>"
}
```
