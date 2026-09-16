# Correct Answer

```json
{
  "event_span_days": 181,
  "rain_anchor": {"date": "2011-01-10", "day_index": 132},
  "grid_evidence_window": "2010-09-01_to_2010-10-16",
  "grid_mm_ci": {
    "era5_land": {"mean": 120.98, "max": 140.06, "ci": 1.16},
    "gpm_imerg": {"mean": 121.75, "max": 171.3, "ci": 1.41},
    "chirps": {"mean": 111.59, "max": 202.71, "ci": 1.82}
  },
  "ci_summary": {"mean": 1.46, "range": 0.66},
  "threshold_200mm": {"hits": 1, "max_margin_mm": 2.71},
  "point_peaks": {
    "open_meteo": {"date": "2010-12-25", "mm": 33.3, "lead_days": 16},
    "nasa_power": {"date": "2010-11-14", "mm": 56.89, "lead_days": 57}
  },
  "grid_to_point_peak_ratio": 3.56,
  "answer": "grid_window_context_point_peaks_before_anchor"
}
```

The answer is `grid_window_context_point_peaks_before_anchor`. The inclusive package span is 181 days, and January 10, 2011 is day 132. The gridded precipitation summaries cover 2010-09-01 to 2010-10-16, so their maxima are accumulated-window context values, not January 10 daily totals. The gridded concentration indices are 140.06/120.98 = 1.16, 171.30/121.75 = 1.41, and 202.71/111.59 = 1.82. The 200 mm threshold ledger has 1 contextual accumulated-window hit with a 2.71 mm margin, while the point peaks occur 16 and 57 days before the rain anchor. The largest gridded maximum to largest point daily peak ratio is 202.71/56.89 = 3.56.

# Scoring Rubric

- 4 points: Computes the 181-day inclusive span and day-index 132 for 2011-01-10.
- 5 points: Extracts the three gridded accumulated-window precipitation means and maxima, reports the 2010-09-01 to 2010-10-16 evidence window, and calculates the three concentration indices without treating them as January 10 daily totals.
- 4 points: Calculates the 200 mm threshold hit count and the 2.71 mm largest margin.
- 4 points: Identifies both point daily peak dates, peak millimeters, and lead-day values.
- 3 points: Computes the 3.56 grid-to-point ratio and returns `grid_window_context_point_peaks_before_anchor`.
