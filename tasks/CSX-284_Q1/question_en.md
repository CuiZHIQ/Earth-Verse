# Monsoon Flood Response Diagnosis

A regional flood coordination cell is preparing a technical note on the 2022 Pakistan extreme monsoon rainfall and flooding across the Indus basin and affected provinces. They need a compact diagnosis that separates the dominant flood-generating process from compounding factors, then translates that physical diagnosis into an early operational posture.

Decide the dominant hazard mechanism, trace how it becomes an operational impact chain for exposed communities and critical services, and assign the response posture that should guide early coordination. Use quantitative anchors where they are important, distinguish the full event window from the precipitation-product evidence window, and keep the answer focused on disaster analysis rather than a general event summary.

Return a JSON object with this shape:

```json
{
  "mechanism_label": "short_string",
  "impact_chain": "one concise sentence",
  "response_posture": "short_string",
  "evidence_windows": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "precipitation_evidence_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}
  },
  "key_anchors": {
    "duration_days": number,
    "rainfall_signature_mm": number,
    "exposed_population_millions": number,
    "critical_receptor_count": number
  }
}
```
