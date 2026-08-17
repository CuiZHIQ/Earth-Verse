# La Conchita Threshold-Window Score Ledger

A geohazard analyst is auditing the 10 January 2005 La Conchita, California slope failure with two competing diagnostic ledgers: a rainfall-threshold process ledger and an image-change window ledger.

Use the provided event records to compute a compact ledger. Count how many of the five precipitation estimates meet the 45 mm event-day threshold, compute their one-decimal mean, compute the inclusive event-window length in days, and use the Sentinel-1 and Sentinel-2 pre/post scene counts to test whether image-change timing can carry the diagnosis.

Use these formulas:

```text
rainfall_index = min(100, mean_precip_mm / 75 * 100)
impact_index = min(100, fatalities * 5 + destroyed_houses * 2)
process_text_index = 100 when the metadata, anchor note, and report text jointly support storm rainfall plus deep-seated landslide movement; otherwise scale by matching source checks
sensor_window_index = 100 only when both Sentinel ledgers have at least one pre-event and one post-event scene; otherwise 0
rainfall_process_score = round(0.45 * rainfall_index + 0.35 * impact_index + 0.20 * process_text_index)
image_change_score = round(0.45 * sensor_window_index + 0.35 * impact_index)
score_margin = rainfall_process_score - image_change_score
```

Return your answer as JSON:

```json
{
  "answer": "<compact_diagnosis_label>",
  "threshold_window_ledger": {
    "rain_sources_ge_45mm": "<integer>",
    "mean_consensus_mm": "<one_decimal>",
    "event_window_days": "<integer>",
    "sentinel_scene_counts": "<S1 pre/post and S2 pre/post counts>"
  },
  "numeric_diagnosis": {
    "rainfall_index_0_100": "<one_decimal>",
    "impact_index_0_100": "<integer>",
    "sensor_window_index_0_100": "<integer>",
    "rainfall_process_score": "<integer>",
    "image_change_score": "<integer>",
    "score_margin": "<integer>"
  },
  "formula_proof": "<one or two sentences explaining which ledger wins and why>"
}
```
