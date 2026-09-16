# Sao Sebastiao Flood-Landslide Mechanism Brief

A hydrometeorology and civil-defense team is preparing an after-action note on the February 18-21, 2023 Sao Sebastiao disaster along the steep coast of Sao Paulo state, Brazil. The key decision is whether the event should be framed primarily as a rainfall-driven compound flood-landslide emergency with localized lifeline priorities, or whether another mechanism better explains the impact pattern.

Diagnose the dominant hazard mechanism and the response priority. Use the local report record to support the diagnosis with quantitative anchors for the reported 24-hour rainfall amount, event-window duration, post-event image timing, rain-saturation process signals, and infrastructure/access impact signals. Explain how the numbers connect to the physical sequence from rainfall to slope failure, flooding, access disruption, and community-level response needs.

Return only a JSON object in this form, using compact labels and numeric values when supported:

```json
{
  "answer": "<compact_mechanism_label>",
  "priority": "<compact_priority_label>",
  "key_metrics": {
    "reported_24h_rain_mm": <number>,
    "event_window_days": <integer>,
    "image_lag_after_event_end_days": <integer>,
    "rain_saturation_signal_count": <integer>,
    "infrastructure_access_signal_count": <integer>
  },
  "impact_chain": ["<trigger>", "<cascade>", "<priority_rationale>"]
}
```
