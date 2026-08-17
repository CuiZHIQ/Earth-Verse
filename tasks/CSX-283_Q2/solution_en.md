# Correct Answer

The persistence index is **8.81** with **5** of 5 ledger tests true.

# Key Computations

- Madagascar wind conversion: `130 km/h * 0.621371 = 80.8 mph`.
- First Mozambique ratio: `50.0 / 80.8 = 0.62`.
- Mozambique rebound ratio: `90.0 / 50.0 = 1.80`.
- GPM peak-to-mean: `416.971989 / 111.974912 = 3.724`.
- CHIRPS peak-to-mean: `327.362244 / 115.358573 = 2.838`.
- Rain concentration: `(3.724 + 2.838) / 2 = 3.281`.
- Event-period duration fraction: `36.0 / 39 = 0.923`.
- Final index: `1.80 * 3.281 * 0.923 / 0.619 = 8.81`.

# Reasoning Path

The first Mozambique landfall was weaker than the Madagascar landfall after unit conversion, but the later Mozambique landfall was 1.80 times the first Mozambique wind speed. Both rainfall summaries have means above 100 mm and peaks above 300 mm, and the tropical-storm duration covers 36 of the 39 inclusive event days. The numeric result is therefore a high persistence score rather than a first-strike wind score.

# Scoring Rubric

- 4 points: Reports the final persistence index as 8.81 within +/-0.01.
- 3 points: Correctly converts 130 km/h to 80.8 mph and computes the 0.62 first Mozambique-to-Madagascar ratio.
- 3 points: Computes the 1.80 Mozambique rebound ratio from 90.0 mph and 50.0 mph.
- 4 points: Computes both rainfall peak-to-mean ratios and their average rain concentration of about 3.28.
- 3 points: Uses the 39-day inclusive event period and 36.0-day duration to obtain 0.923.
- 2 points: Counts all five threshold tests correctly.
- 1 point: Returns the requested compact JSON with numeric values rounded sensibly.

Total: 20 points.
