# Aru Glacier Collapse Mechanism Brief

In July-September 2016, a catastrophic glacier collapse in the Aru Range of western Tibet raised an urgent cryosphere-hazard question: should the incident be treated as a high-priority glacier-collapse mass-movement monitoring problem, or as a simpler rainfall flood, vegetation-change, or low-priority remote mountain event?

A regional disaster-risk team needs a concise technical diagnosis for monitoring and planning. Use the incident record to classify the dominant mechanism, state the strength of the event-anchor support, and decide the appropriate monitoring priority. Ground the briefing in event-window, source-confidence, and mechanism-consistency anchors rather than auxiliary precipitation, radar, or exposure products.

Return your response as JSON:

```json
{
  "answer": "<compact_interpretation_label>",
  "mechanism": "<compact_mechanism_label>",
  "evidence_strength": "<support_label>",
  "priority": "<priority_label>",
  "key_metrics": {
    "event_window_days": "<value>",
    "correspondence_score": "<value>",
    "mechanism_term_count": "<value>",
    "lock_confidence": "<value>"
  },
  "impact_chain": ["<driver>", "<hazard_process>", "<planning_relevance>"]
}
```
