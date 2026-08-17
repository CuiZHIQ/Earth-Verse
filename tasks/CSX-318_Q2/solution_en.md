# Correct Answer

`seismic_calving_lake_iceberg_consistent`

```json
{
  "chain_score_0_5": 5,
  "mass_million_tons": 30.0,
  "image_lag_days": 8,
  "point_precip": {"total_mm": 42.88, "peak_share": 0.389},
  "wind_peak": {"kmh": 21.1, "lag_days": 8},
  "tsci_0_10": 10,
  "consistency_label": "seismic_calving_lake_iceberg_consistent",
  "computed_consequence": "weather_counterweight_below_threshold"
}
```

# Computation Path

The report-derived chain score is 5: earthquake magnitude is present, Tasman Glacier is the source, Tasman Lake is the receiving medium, icebergs are the lake expression, and the report states the earthquake supplied the final pulse.

The reported ice mass is 30.0 million tons, so `mass_gate = 1`. The image date is 2011-03-02 and the event start is 2011-02-22, so `image_lag_days = 8` and `image_lag_gate = 1`.

For the NASA POWER point precipitation series, the total is `16.70 + 2.21 + 1.01 + 5.51 + 0.54 + 0.00 + 3.18 + 7.00 + 6.73 = 42.88 mm`. The peak daily value is 16.70 mm, so `point_precip_peak_share = 16.70 / 42.88 = 0.389`.

For the Open-Meteo daily wind series, the peak 10 m wind is 21.1 km/h on 2011-03-02. Relative to 2011-02-22, that is an 8-day lag. The weather counterweight gate is therefore 3 because 42.88 mm is below 50 mm, 0.389 is below 0.5, 21.1 km/h is below 30 km/h, and the wind peak occurs after the start date.

`TSCI = 5 + 1 + 1 + 3 = 10`. Since the chain score is 5 and TSCI is at least 9, the compact consequence is `weather_counterweight_below_threshold`.

# Scoring Rubric

- 3 points: Returns the requested compact JSON fields with numeric values in the expected units and a concise label. Partial credit: 1-2 points if the returned JSON is parseable but omits one or two requested fields.
- 4 points: Computes `chain_score_0_5` as 5 from the five report-derived components. Partial credit: 0.8 points for each correctly identified component in the count.
- 3 points: Reports 30.0 million tons, 8 image-lag days, and applies the mass and lag gates correctly. Partial credit: 1 point each for mass, lag, and gate application.
- 4 points: Computes point precipitation total as 42.88 mm and peak share as 0.389 within tolerance. Partial credit: 2 points for the total and 2 points for the ratio.
- 3 points: Computes wind peak as 21.1 km/h at an 8-day lag and sets the weather counterweight gate to 3. Partial credit: 1 point each for wind speed, wind lag, and the gate result.
- 3 points: Computes TSCI as 10 and returns `seismic_calving_lake_iceberg_consistent` with a short weather-counterweight consequence. Partial credit: 1 point each for index, label, and concise consequence.
