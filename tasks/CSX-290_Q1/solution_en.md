# Final Answer

Correct answer: `rainfall_runoff_sediment_dominant`.

The score ledger is:

```json
{
  "target_family": "candidate_explanation_score_ledger",
  "evidence_windows": {
    "event_window": {
      "start": "2022-12-26",
      "end": "2023-01-17"
    },
    "point_weather_window": {
      "start": "2022-12-26",
      "end": "2023-01-09"
    },
    "area_precipitation_window": {
      "start": "2022-12-26",
      "end": "2023-01-17"
    },
    "surface_change_context": "annual_context"
  },
  "metrics": {
    "ppt_mm": 486.5,
    "heavy50_days": 5,
    "area_min_mm": 193.1,
    "roadcrit": 253,
    "wind_kmh": 27.9,
    "sc_mean": 0.038,
    "sc_max": 0.786
  },
  "text_gates": {
    "runoff_sediment": true,
    "snow_storage": true,
    "wet_period": true,
    "wind_impact": false
  },
  "scores": {
    "rainfall": 6,
    "snow_storage": 2,
    "wind": 1,
    "landscape": 0
  },
  "score_comparison": {
    "dominant_signal": "rainfall",
    "secondary_signal": "snow_storage",
    "low_support_signals": ["wind", "landscape"]
  },
  "margin": 4,
  "answer": "rainfall_runoff_sediment_dominant",
  "computed_consequence": "Only the rainfall-runoff-sediment ledger clears the dominance rule; snowpack is context, while wind and annual surface change stay below lead-diagnosis thresholds."
}
```

# Key Computations

The hidden computation uses the event metadata, locked event-window report, evidence-report text, point precipitation and wind samples, area precipitation summaries, exposure counts, and annual surface-change statistics.

Main numeric values:

- `ppt_mm = 486.5`: total precipitation from the point daily precipitation sample window, 2022-12-26 through 2023-01-09.
- `heavy50_days = 5`: count of point-sample days with daily precipitation at or above 50 mm.
- `area_min_mm = 193.1`: minimum of the three full-event area-mean precipitation estimates for 2022-12-26 through 2023-01-17, rounded to 0.1 mm.
- `roadcrit = 253`: roads plus critical amenities in the exposure footprint.
- `wind_kmh = 27.9`: maximum daily point wind speed in the point-weather sample window.
- `independent_wind_ms = 5.21`: maximum independent daily point wind speed, used in the wind score but not required in the returned metric block.
- `sc_mean = 0.038` and `sc_max = 0.786`: annual surface-change mean and maximum used only as longer-window counter-diagnosis context.

Text gates:

- `runoff_sediment_text = true`: the report text supports saturated-soil runoff and sediment transport.
- `snow_storage_text = true`: the report text includes snowpack or reservoir context.
- `wet_period_text = true`: the report text flags the wet-period context.
- `wind_impact_text = false`: no event-specific damaging-wind impact phrase is used for this ledger.

Score formulas:

- `rainfall = 2*(486.5 >= 400) + 1*(5 >= 4) + 1*(193.1 >= 150) + 1*(true) + 1*(253 >= 200) = 6`.
- `snow_storage = 1*(true) + 1*(true) = 2`.
- `wind = 1*(27.9 >= 25) + 1*(5.21 >= 10) + 1*(false) = 1`.
- `landscape = 1*(0.038 >= 0.10) + 1*(0.786 >= 0.80) = 0`.
- Dominance rule: top score `6 >= 5` and margin `6 - 2 = 4 >= 3`, so the dominant diagnosis is `rainfall_runoff_sediment_dominant`.

# Reasoning Path

1. The precipitation ledger passes every main rainfall-runoff test: large cumulative point precipitation, repeated heavy days, area-wide precipitation, report-supported runoff and sediment language, and exposure to roads or critical amenities.
2. Snowpack and reservoir language is present, but it has only contextual wet-period support and does not match the direct runoff-sediment exposure score.
3. Wind has a modest point-wind threshold hit, but the independent wind sample and report-impact gate do not support a leading wind-disruption diagnosis.
4. Annual surface change remains below both the mean and maximum thresholds, so it cannot outrank the event-window hydrologic ledger.
5. The top score exceeds the dominance threshold and beats the next score by four points, making the final label deterministic.

# Computed Interpretation

The event-window arithmetic supports a rainfall-runoff and sediment-flood diagnosis. Snowpack/storage is a secondary hydrologic context, while wind disruption and annual landscape change do not satisfy the ledger thresholds for the lead diagnosis.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the requested compact JSON with `target_family`, `metrics`, `text_gates`, `scores`, `score_comparison`, `margin`, `answer`, and `computed_consequence`. Partial credit for minor key-name differences that preserve all fields.
- 4 points: Computes the precipitation and exposure metrics correctly: point-weather-window `ppt_mm` about 486.5, `heavy50_days` equal to 5, full-event `area_min_mm` about 193.1, and `roadcrit` equal to 253. Partial credit for two or three correct values or correct threshold states with weaker rounding.
- 3 points: Sets the report-text gates correctly: runoff/sediment true, snow/storage true, wet-period true, and damaging-wind impact false. Partial credit for the right runoff gate with one mistaken contextual gate.
- 3 points: Computes the counter-diagnosis metrics correctly: point-weather-window `wind_kmh` about 27.9, independent wind below 10 m/s, annual-context `sc_mean` about 0.038, and annual-context `sc_max` about 0.786. Partial credit for correct threshold decisions with one missing numeric value.
- 3 points: Applies the four score formulas correctly, yielding rainfall 6, snow_storage 2, wind 1, and landscape 0. Partial credit for one arithmetic error that does not change the top label.
- 3 points: Applies the score-comparison and dominance rule correctly: rainfall is dominant, snow_storage is secondary, wind and landscape remain low support; margin 4; answer `rainfall_runoff_sediment_dominant`. Partial credit for the correct top label but missing margin or secondary comparison.
- 1 point: Keeps the computed consequence bounded to the ledger and avoids extra loss totals, statewide infrastructure totals, direct January damage claims from annual surface-change metrics, or broad narrative expansion.
