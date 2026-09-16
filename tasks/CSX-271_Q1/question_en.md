# 1997-1998 El Nino Flood-Response Diagnosis

A regional emergency operations desk is preparing its initial technical briefing for the 1997-1998 El Nino episode affecting coastal Peru and Ecuador. The briefing must decide whether the response posture should be driven by ENSO-amplified flooding, drought or vegetation stress, wildfire/catalog monitoring, or climate-signal monitoring with no local escalation.

Prepare a compact disaster-analysis diagnosis that links the large-scale climate driver to the local hazard and response priority. Use quantitative anchors where they matter, but keep the answer focused on the operational pathway rather than a broad climate summary.

Return your answer as JSON:

```json
{
  "answer": "<compact_pathway_label>",
  "mechanism_chain": ["<climate_driver>", "<local_hazard>", "<response_focus>"],
  "key_findings": [
    "<finding_1>",
    "<finding_2>",
    "<finding_3>"
  ],
  "priority": "<priority_level>"
}
```
