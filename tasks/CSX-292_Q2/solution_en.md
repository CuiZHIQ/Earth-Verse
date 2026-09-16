# Answer

```json
{
  "peak_day": "2022-06-21",
  "peak_precip_mm": {"nasa_power": 26.9, "open_meteo": 21.9},
  "pulse_share_pct": {"nasa_power": 55.0, "open_meteo": 81.7},
  "cooling_c": {"nasa_power": 9.8, "open_meteo": 14.2},
  "regional": {"mean_mm": 238.6, "spread_pct": 10.9},
  "wind": {"nasa_power_max_ms": 5.3, "open_meteo_max_kmh": 27.3},
  "answer": "wet_cooling_monsoon_pulse"
}
```

# Computation

Both daily point precipitation series peak on 2022-06-21, with 26.9 mm and 21.9 mm. The 2022-06-20 through 2022-06-22 totals account for 55.0% and 81.7% of the 2022-06-15 through 2022-06-29 daily precipitation totals.

Cooling is computed within each point series using that series' available daily temperature field: the 2022-06-15 and 2022-06-16 mean minus the peak-day temperature. This gives 9.8 C and 14.2 C. The point-series pulse, cooling, and wind tests use the 2022-06-15 to 2022-06-29 daily records; the regional means are the package-supplied accumulated regional summaries. The three regional precipitation means average to 238.6 mm, with a spread of 10.9%. Maximum winds are 5.3 m/s and 27.3 km/h.

All stated thresholds pass: shared peak day, pulse share at least 50% in both daily series, cooling at least 5.0 C in both daily series, regional mean at least 200 mm, regional spread no more than 15%, and wind below both ceilings. The compact consequence is a wet-cooling monsoon pulse; a wind-led or heat-led label fails the computed thresholds.

# Scoring Rubric

- 4 points: JSON contains the requested fields and uses a compact final `answer` label.
- 5 points: peak date, peak precipitation, pulse shares, cooling values, regional precipitation values, and wind maxima are correct within 0.1 units.
- 4 points: formulas are applied to the stated windows and regional means rather than copied from a narrative summary.
- 4 points: all threshold comparisons are evaluated correctly and identify that every component test passes.
- 2 points: the final label follows from the pass state of the numeric tests and rejects wind-led or heat-led labels through the thresholds.
- 1 point: keeps the conclusion within the package-derived calculation.
