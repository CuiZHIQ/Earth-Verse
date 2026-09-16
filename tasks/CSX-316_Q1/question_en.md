# Kilimanjaro Cryosphere Priority Diagnosis

A regional climate-risk team is preparing a decision note on the long-running retreat of the ice fields on Mount Kilimanjaro in Tanzania, with the analysis window anchored from February 2000 to February 2020. The team needs to decide whether this case should be handled as a rapid high-mountain emergency, a short-lived weather-driven flood problem, a post-fire recovery problem, or a slow-onset cryosphere change requiring sustained monitoring and adaptation.

Make the diagnosis as a disaster-analysis judgment, not a general climate essay. Use the event duration, short local weather context, broad nearby population context, and the role of direct observation to support the response posture. Be careful not to convert regional exposure context into confirmed direct losses, and do not infer a precise ice-area loss rate unless the reasoning supports it.

Return a compact JSON answer:

```json
{
  "answer": "<compact_priority_label>",
  "key_metrics": {
    "event_window_years": "<value>",
    "local_weather_sample_days": "<value>",
    "mean_daily_temperature_c": "<value>",
    "population_context": "<value>",
    "direct_observation_role": "<phrase>"
  },
  "priority_chain": ["<driver>", "<hazard_mode>", "<response_posture>"]
}
```
