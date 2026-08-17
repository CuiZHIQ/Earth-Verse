# California Atmospheric-River Diagnostic Ledger

A hydrometeorology review team is checking a compact diagnostic ledger for the atmospheric-river sequence that affected California from December 26, 2022 to January 17, 2023. The test is whether the record supports a rainfall-runoff and sediment-flood pathway as the dominant event diagnosis, rather than a snowpack/storage, wind-disruption, or longer-term landscape-change reading.

Compute these scores from the technical record. Keep the full atmospheric-river event window separate from the point-weather sample window, the area-precipitation product window, and the annual surface-change context used only as a counter-diagnosis check.

- `rainfall = 2*(ppt_mm >= 400) + 1*(heavy50_days >= 4) + 1*(area_min_mm >= 150) + 1*(runoff_sediment_text) + 1*(roadcrit >= 200)`
- `snow_storage = 1*(snow_storage_text) + 1*(wet_period_text)`
- `wind = 1*(wind_kmh >= 25) + 1*(independent_wind_ms >= 10) + 1*(wind_impact_text)`
- `landscape = 1*(sc_mean >= 0.10) + 1*(sc_max >= 0.80)`

Compare the four scores. Classify the lead diagnosis as dominant only if its score is at least 5 and its margin over the second score is at least 3.

Return compact JSON:

```json
{
  "target_family": "candidate_explanation_score_ledger",
  "evidence_windows": {
    "event_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "point_weather_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "area_precipitation_window": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"},
    "surface_change_context": "annual_context"
  },
  "metrics": {
    "ppt_mm": 0,
    "heavy50_days": 0,
    "area_min_mm": 0,
    "roadcrit": 0,
    "wind_kmh": 0,
    "sc_mean": 0,
    "sc_max": 0
  },
  "text_gates": {
    "runoff_sediment": false,
    "snow_storage": false,
    "wet_period": false,
    "wind_impact": false
  },
  "scores": {
    "rainfall": 0,
    "snow_storage": 0,
    "wind": 0,
    "landscape": 0
  },
  "score_comparison": {
    "dominant_signal": "",
    "secondary_signal": "",
    "low_support_signals": []
  },
  "margin": 0,
  "answer": "short_label",
  "computed_consequence": "one sentence tied only to the ledger"
}
```
