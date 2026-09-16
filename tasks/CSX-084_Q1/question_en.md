# 26 July 2005 Mumbai Rainfall Concentration Check

A hydrometeorology review team is checking how to summarize the 26 July 2005 Mumbai flood in a compact technical note. The key issue is whether the event should be diagnosed from the local 24-hour rainfall record and short-duration intensity, or from broader contextual precipitation products that smooth the local maximum.

Compute a numeric diagnosis for the event. Use the local rainfall anchor, the peak rain rate, the previous India single-day rainfall record, the highest contextual precipitation maximum, and the 2005 population exposure context. Return only the JSON object below, with numbers rounded to three decimals where needed:

```json
{
  "answer": "<compact diagnosis label>",
  "reported_24h_mm": <number>,
  "average_24h_rate_mm_per_hour": <number>,
  "peak_rate_mm_per_hour": <number>,
  "peak_to_average_rate_ratio": <number>,
  "excess_over_previous_record_percent": <number>,
  "contextual_max_percent_of_local_anchor": <number>,
  "population_exposure_millions": <number>,
  "interpretation": "<one sentence explaining the numeric diagnosis>"
}
```
