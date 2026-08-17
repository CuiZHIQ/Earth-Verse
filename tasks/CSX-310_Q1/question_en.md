# Emergency Priority Diagnosis for the Hunga Tonga-Hunga Ha'apai Event

A Pacific emergency coordination team is preparing its first technical priority note for the January 15, 2022 Hunga Tonga-Hunga Ha'apai eruption and tsunami in Tonga. The decision problem is not simply whether an eruption occurred, but which hazard pathway should dominate the first response posture when explosive volcanic forcing, tsunami waves, ashfall, rainfall flooding alternatives, and lifeline continuity are all plausible concerns.

Decide the initial response-priority diagnosis. Your answer should identify the dominant trigger-to-impact chain, explain why it outranks rainfall flooding or ordinary local-weather response, and connect the hazard interpretation to coastal communities, lifeline continuity, ashfall response, and rapid screening for island/coastal disturbance. Base the physical diagnosis on the event report and catalog evidence; treat any auxiliary package products as context rather than direct loss or location proof.

Return a compact JSON object:

```json
{
  "answer": "<priority_label>",
  "priority_chain": ["<trigger>", "<hazard_pathway>", "<response_priority>"],
  "key_anchors": {
    "severity_signal": "<short phrase>",
    "eruption_scale": "<short phrase>",
    "rainfall_alternative": "<short phrase>",
    "exposure_context": "<short phrase>"
  },
  "brief_reasoning": "<2-4 sentences>"
}
```
