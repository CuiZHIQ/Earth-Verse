# Zhengzhou Rainfall-Concentration Ledger

During the July 2021 Henan extreme-rainfall episode, a hydrometeorology analyst needs a calculation ledger for Zhengzhou rather than a narrative summary. Use the incident technical record and quantitative layers to test whether the local point rainfall series is dominated by a single day while the regional precipitation field and mapped urban fabric also clear fixed numeric gates.

Compute the local event total, peak date, peak-day depth, non-peak remainder, peak-day share, regional maximum precipitation values, mapped population in millions, bounded road count, critical-facility count, annual surface-change mean and maximum, peak-to-remainder ratio, facility density per million people, road-to-facility ratio, surface-change max-to-mean ratio, and a seven-gate ledger score. For this ledger, `critical_facilities` is the count of school, hospital, shelter, police, and fire-station amenity features in the package urban-context slice.

Gates:

- Peak-day share > 0.50
- Non-peak remainder < 300 mm
- Regional hourly-aggregate precipitation maximum >= 400 mm
- Regional event-accumulation precipitation maximum >= 500 mm
- Mapped population >= 10 million
- Critical-facility count >= 800
- Annual surface-change mean < 0.05

Return JSON:

```json
{
  "answer": {
    "local_total_mm": 0.0,
    "peak_day": "YYYYMMDD",
    "peak_mm": 0.0,
    "nonpeak_mm": 0.0,
    "peak_share": 0.0,
    "peak_to_remainder_ratio": 0.0,
    "regional_hourly_max_mm": 0.0,
    "regional_event_max_mm": 0.0,
    "population_million": 0.0,
    "roads": 0,
    "critical_facilities": 0,
    "facility_density_per_million": 0.0,
    "road_to_facility_ratio": 0.0,
    "surface_change_mean": 0.0,
    "surface_change_max": 0.0,
    "surface_change_max_to_mean": 0.0,
    "gate_hits": 0,
    "gate_total": 7,
    "ledger_score": 0.0
  },
  "calculation_note": "<one sentence identifying the strongest numeric contrast>"
}
```
