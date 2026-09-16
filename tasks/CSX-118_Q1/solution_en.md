# Final Answer

The canonical answer label is `wind_pressure_timing_core`.

Expected compact JSON:

```json
{
  "classification": "wind_pressure_timing_core",
  "peak_gust_time": "2017-10-16T14:00",
  "peak_gust_kmh": 111.6,
  "peak_wind_time": "2017-10-16T14:00",
  "peak_wind_kmh": 61.4,
  "minimum_pressure_time": "2017-10-16T15:00",
  "minimum_pressure_hpa": 989.6,
  "pressure_lag_hours": 1.0,
  "gust_to_wind_ratio": 1.82,
  "rainfall_total_mm": 5.8,
  "max_hourly_rain_mm": 0.9,
  "official_dublin_gust_kmh": 103.7,
  "point_minus_official_gust_kmh": 7.9,
  "short_conclusion": "Dublin records show a wind and pressure timing peak with modest rain."
}
```

# Key Computations

The reproducible path in `compute_gt.py` reads the local CSX-118 hourly Dublin-area weather JSON and local NHC report PDF.

- The point-weather record has 48 hourly observations from 2017-10-15T00:00 through 2017-10-16T23:00.
- Peak 10 m gust: 111.6 km/h at `2017-10-16T14:00`.
- Peak 10 m wind: 61.4 km/h at `2017-10-16T14:00`.
- Minimum sea-level pressure: 989.6 hPa at `2017-10-16T15:00`.
- Pressure lag from the wind and gust peak to the pressure minimum: 1.0 hour.
- Gust-to-wind ratio: 111.6 / 61.4 = 1.82.
- Point rainfall total: 5.8 mm; maximum hourly rain: 0.9 mm.
- Official Dublin Airport table row: gust 56 kt, 10-minute wind 36 kt, pressure 989.0 hPa.
- Official gust conversion: 56 kt x 1.852 = 103.7 km/h.
- Point-minus-official gust gap: 111.6 - 103.7 = 7.9 km/h.
# Reasoning Path

1. Compute the hourly wind, gust, pressure, and rainfall extrema from the Dublin-area point record.
2. Compare the timing: both wind and gust peak at 14:00 on 16 October, while the lowest pressure occurs one hour later at 15:00.
3. Convert the official Dublin Airport gust from knots to km/h and compare it with the point-weather gust. The 7.9 km/h gap is small enough to support the same high-wind timing signal.
4. Check the rainfall values against the wind-pressure ledger. A 5.8 mm two-day point total and 0.9 mm maximum hourly rain do not define a rain-accumulation core for this Dublin record.
5. The resulting compact classification is therefore `wind_pressure_timing_core`.

# Computed Interpretation

For Dublin, the compact record is a wind and pressure timing ledger: the highest winds and gusts arrive together, followed by the pressure minimum one hour later, while rain remains modest. The official Dublin Airport gust is close to the point-weather gust after unit conversion, so the two records reinforce the same timing and intensity result.

# Scoring Rubric

Total: 20 points.

- 3 points - Core classification: states that the Dublin record is a wind-pressure timing core, not a rain-accumulation core. Partial credit: award up to 2 points for a wind-led label that does not make the timing contrast explicit.
- 4 points - Hourly extrema: reports peak gust 111.6 km/h and peak wind 61.4 km/h at `2017-10-16T14:00`, plus minimum pressure 989.6 hPa at `2017-10-16T15:00`. Partial credit: award partial credit for correct values with one missing time or minor rounding within 0.2 units.
- 3 points - Derived timing and ratio: computes the 1.0 hour lag from wind and gust peak to pressure minimum and the 1.82 gust-to-wind ratio. Partial credit: award up to 2 points for one correct derived value or a correct formula with arithmetic slips.
- 3 points - Rainfall contrast: uses 5.8 mm total point rainfall and 0.9 mm maximum hourly rain to keep rain accumulation secondary. Partial credit: award up to 2 points for the correct total without the hourly check, or for a correct low-rain conclusion with imprecise rounding.
- 3 points - Official table reconciliation: converts the official 56 kt Dublin Airport gust to 103.7 km/h and computes the 7.9 km/h point-minus-official gust gap. Partial credit: award up to 2 points for the correct knot value or conversion without the gap.
- 4 points - Concise ledger and wording: returns the requested compact JSON and a short explanation that stays within the computed weather ledger. Partial credit: award up to 3 points for a mostly complete ledger with minor format omissions and no extra outside numbers.
