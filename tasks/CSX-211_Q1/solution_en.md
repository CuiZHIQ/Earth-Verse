# Final Answer

```json
{
  "target_family": "smoke_window_threshold_score_ledger",
  "answer": "surface_smoke_pm25_window",
  "event_window_days": 3,
  "smoke_score": 10,
  "threshold_ledger": {
    "pm25_ug_m3": 400,
    "nyc_pm25_aqi": 175,
    "nyc_record_margin": 8,
    "near_surface_smoke_km": 3,
    "surface_to_elevated_ratio": 0.5,
    "context_countermetric_passes": 0
  },
  "gates": {
    "score_at_least_8": true,
    "pm25_aqi_record": true,
    "near_surface_depth": true,
    "context_countermetrics_low": true
  },
  "computed_consequence": "10/10 smoke-window score with 0 context countermetric passes."
}
```

# Key Computations

The inclusive event window runs from 2023-06-06 through 2023-06-08, so `event_window_days = 3`.

Smoke-window score:

- Window gate: `3 >= 3`, worth 1 point.
- Text gates: Quebec source, coastal-low southward transport, surface-level air degradation, and aerosol optical depth context are all present, worth 4 points.
- PM2.5 gate: highest reported PM2.5 is 400 ug/m3, so `400 >= 400`, worth 2 points.
- NYC AQI gate: NYC PM2.5 AQI is 175 and the previous record is 167, so the margin is `175 - 167 = 8`, worth 2 points.
- Vertical gate: near-surface smoke depth is 3 km, so `3 >= 3`, worth 1 point.

The resulting smoke score is `1 + 4 + 2 + 2 + 1 = 10`.

Vertical layer ratios:

- Near-surface to elevated smoke ratio: `3 / 6 = 0.50`.
- Near-surface to older smoke ratio: `3 / 12 = 0.25`.

Context countermetric gates:

- Surface-change gate is false because Sentinel-2 dNBR is 0.015 and annual embedding change is 0.016, both below 0.100.
- Rainfall gate is false because GPM mean precipitation is 11.0 mm and CHIRPS mean precipitation is 15.4 mm, both below 25.0 mm.
- Heat gate is false because mean max temperature is 30.5 C and maximum temperature is 35.1 C, below the 35.0 C mean and 38.0 C maximum thresholds.

Thus `context_countermetric_passes = 0`.

# Reasoning Path

1. Read the locked event dates and compute the inclusive three-day window.
2. Extract the report text gates for the Quebec source, coastal-low transport, surface-level air degradation, and aerosol optical depth context.
3. Extract the PM2.5 and PM2.5 AQI anchors, then compute the NYC record margin as 8 AQI points.
4. Compare the near-surface smoke depth to the 3 km threshold and keep the 6 km and 12 km layers as ratio checks.
5. Test the context countermetrics against their thresholds: dNBR/annual embedding change, GPM/CHIRPS precipitation, and ERA5-Land heat.
6. Sum the smoke score and apply the rule: a score of at least 8 with zero context countermetric passes yields `surface_smoke_pm25_window`.

# Computed Interpretation

The local package supports a high-confidence smoke-window ledger: the smoke score is 10/10, while surface-change, rainfall, and heat countermetric gates remain below threshold.

# Scoring Rubric

Total: 20 points.

- Final label and format (3 points): Full credit returns compact JSON with `target_family`, `answer`, `event_window_days`, `smoke_score`, `threshold_ledger`, `gates`, and `computed_consequence`. Partial credit: 2 points for the correct answer with one missing field, or 1 point for the right label in prose without the requested compact JSON.
- Window and text gates (3 points): Full credit computes the inclusive 3-day event window and marks the Quebec source, coastal-low transport, surface-air, and aerosol-depth text gates. Partial credit: 2 points for the date window plus two or three text gates, or 1 point for the date window alone.
- PM2.5/AQI record ledger (4 points): Full credit reports PM2.5 at 400 ug/m3, NYC PM2.5 AQI at 175, the prior record at 167, and the 8-point margin. Partial credit: 3 points for three correct values, 2 points for two correct values, or 1 point for one correct PM2.5 or AQI anchor.
- Vertical layer calculation (3 points): Full credit uses the 3 km near-surface smoke depth, 6 km elevated layer, 12 km older layer, and the 0.50 surface-to-elevated ratio. Partial credit: 2 points for two correct layer heights, or 1 point for only the near-surface height.
- Context countermetric gates (3 points): Full credit shows that dNBR 0.015, annual embedding change 0.016, GPM 11.0 mm, CHIRPS 15.4 mm, 30.5 C mean max temperature, and 35.1 C max temperature do not pass their context thresholds. Partial credit: 2 points for four or five correct context anchors, or 1 point for two or three correct anchors.
- Score arithmetic (3 points): Full credit sums the smoke score as 10/10 and applies the rule that a score of at least 8 with zero context countermetric passes yields `surface_smoke_pm25_window`. Partial credit: 2 points for the right label with minor score arithmetic error, or 1 point for the right score without the threshold comparison.
- Concise computed interpretation (1 point): Full credit gives one concise event-specific sentence tied to the ledger without adding casualty, loss, infrastructure, or full-region uniformity statements. Partial credit: 0.5 point for a mostly concise sentence with minor overreach.
