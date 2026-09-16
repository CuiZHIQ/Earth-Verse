# La Conchita Rainfall Window Ledger

For the January 10, 2005 La Conchita landslide package, build a six-point rainfall-trigger ledger from the event-window files. Use the five same-day precipitation estimates from Open-Meteo, NASA POWER, ERA5-Land mean, GPM IMERG mean, and CHIRPS mean. Treat the wettest estimate as a high-side stress-test value: remove it before computing the retained-source statistics.

Use this deterministic ledger:

- 2 points if every retained precipitation estimate is at least 45 mm, otherwise 1 point if three retained estimates meet that threshold, otherwise 0.
- 1 point if the retained-source mean is at least 55 mm.
- 1 point if the retained-source spread is no more than 25 mm.
- 1 point if the USGS report text gives the storm, deep-seated landslide, destroyed-house, and fatality chain.
- 1 point if both Sentinel summaries have no sufficient pre/post scene pairs, so they add no contrary numeric term.

Return compact JSON with these keys:

```json
{
  "answer": "<score_label>",
  "score": "<integer_0_to_6>",
  "removed_source": "<source_label>",
  "precipitation_mm": {
    "removed": "<value>",
    "retained_mean": "<value>",
    "retained_min": "<value>",
    "retained_spread": "<value>"
  },
  "counts": {
    "retained_sources": "<value>",
    "retained_ge_45mm": "<value>"
  },
  "points": {
    "retained_ge_45": "<value>",
    "mean_ge_55": "<value>",
    "spread_le_25": "<value>",
    "report_chain": "<value>",
    "image_neutral": "<value>"
  },
  "classification": "<compact_mechanism_label>",
  "one_sentence_reason": "<brief numeric reason>"
}
```
