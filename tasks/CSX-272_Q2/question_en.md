# Queensland Flood Rainfall-Timing Ledger

During the 2010-2011 La Nina and Queensland floods, convert the CSX-272 package evidence into a numeric consistency ledger for the January 10, 2011 rainfall escalation. Treat gridded precipitation means and maxima as accumulated values over their declared package evidence window, not as January 10 daily totals.

Return only this JSON object, using two decimal places for millimeters and ratios:

```json
{
  "event_span_days": 0,
  "rain_anchor": {
    "date": "YYYY-MM-DD",
    "day_index": 0
  },
  "grid_evidence_window": "YYYY-MM-DD_to_YYYY-MM-DD",
  "grid_mm_ci": {
    "<gridded_source_key>": {
      "mean": 0.00,
      "max": 0.00,
      "ci": 0.00
    }
  },
  "ci_summary": {
    "mean": 0.00,
    "range": 0.00
  },
  "threshold_200mm": {
    "hits": 0,
    "max_margin_mm": 0.00
  },
  "point_peaks": {
    "<point_source_key>": {
      "date": "YYYY-MM-DD",
      "mm": 0.00,
      "lead_days": 0
    }
  },
  "grid_to_point_peak_ratio": 0.00,
  "answer": "<compact_result_code>"
}
```

Definitions: `ci = gridded maximum / gridded mean`; `day_index` is inclusive from the package start date; `lead_days` is the number of days from each point peak to 2011-01-10; `grid_to_point_peak_ratio` is the largest gridded accumulated-window maximum divided by the largest point daily peak. The 200 mm threshold comparison is a contextual accumulated-window magnitude check, not a claim that the gridded maximum occurred on January 10.
