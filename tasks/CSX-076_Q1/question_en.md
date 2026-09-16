# 2022 Pakistan Monsoon Flood Load Check

A hydrometeorology team is reviewing the June-October 2022 Pakistan monsoon floods. The team needs a compact numeric diagnosis of whether the package rainfall record supports a persistent accumulated-load event, rather than a severity account driven mainly by one extreme day or by a narrative report statement.

Compute the load ledger from the technical record. Use the full daily point-rainfall series for the June-October event-window persistence metrics. Use the three gridded accumulated-rainfall summaries only for their declared package comparison window; do not treat them as full June-October gridded totals. Return compact JSON with the requested fields, formulas or ratio definitions, units, and a short final label.

Return JSON:

```json
{
  "target_family": "pakistan_monsoon_flood_load_numeric_diagnosis",
  "gridded_means_mm": {
    "gpm": 0,
    "chirps": 0,
    "era5_land": 0
  },
  "gridded_comparison_window": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  },
  "ensemble_mean_mm": 0,
  "point_rainfall": {
    "event_days": 0,
    "total_mm": 0,
    "peak_day_mm": 0,
    "peak_day_share": 0,
    "wet_day_fraction": 0,
    "heavy_day_fraction": 0,
    "longest_heavy_spell_days": 0,
    "max_14day_share": 0
  },
  "threshold_state": "",
  "final_label": ""
}
```
