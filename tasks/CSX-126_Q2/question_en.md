# Cyclone Gonu Muscat Landfall-Day Rain-Wind Concentration Test

A tropical-cyclone analysis team is preparing a technical note on Cyclone Gonu near Oman and the Arabian Sea during 1-7 June 2007. The team needs to decide whether the Muscat-area land record supports a concentrated landfall-day rain-and-wind episode, rather than an offshore-only intensity summary, a broad multi-day rain summary, or a daily-weather downgrade.

Compute a five-row threshold ledger. For each row, give the formula or threshold test, the key numeric values with units, and a pass/fail state:

1. `official_landfall_anchor`
2. `subdaily_rain_concentration`
3. `wind_pressure_coupling`
4. `daily_peak_alignment`
5. `area_rain_contrast`

The rainfall row must include rolling-window precipitation fractions for 3 h, 6 h, 12 h, 24 h, 48 h, and 72 h relative to the local event total, plus the longest wet spell. The wind-pressure row must include a gust/wind ratio, pressure fall, and gust-threshold duration counts. The timing row must test whether daily wind and precipitation peaks align on 2007-06-06. The area-contrast row must compare gridded precipitation max/mean ratios across the regional products.

Return a compact JSON object with:

```json
{
  "answer_label": "...",
  "ledger": [
    {"row": "...", "formula_or_test": "...", "key_values": {}, "state": "..."}
  ],
  "rejected_alternatives": ["..."],
  "conclusion": "..."
}
```
