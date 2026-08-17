# Wet-Cooling Pulse Consistency Test

For the early wet phase of the 2022 Pakistan extreme monsoon floods, compute whether the daily point series and regional precipitation summaries satisfy a wet-cooling monsoon pulse diagnosis. The daily point-series tests use 2022-06-15 through 2022-06-29; the regional precipitation means are the package-supplied accumulated regional summaries and are compared as regional context for the same monsoon-flood package.

Use these formulas:

- `peak_day`: date of maximum daily precipitation in each daily point series.
- `pulse_share_pct`: `100 * precipitation from 2022-06-20 through 2022-06-22 / precipitation from 2022-06-15 through 2022-06-29`.
- `cooling_c`: the same point series' available daily temperature field on 2022-06-15 and 2022-06-16, averaged, minus that series' temperature on the peak-rain day.
- `regional_mean_mm`: mean of the three regional accumulated-precipitation means.
- `regional_spread_pct`: `100 * (largest regional mean - smallest regional mean) / regional_mean_mm`.

The diagnosis passes only if both daily point series share the same peak day, both 3-day pulse shares are at least 50%, both cooling values are at least 5.0 C, the regional mean is at least 200 mm, the regional spread is no more than 15%, the point-series maximum wind reported in m/s is below 10 m/s, and the point-series maximum wind reported in km/h is below 40 km/h.

Return compact JSON with `peak_day`, `peak_precip_mm`, `pulse_share_pct`, `cooling_c`, `regional`, `wind`, and `answer`. Use one decimal place for numeric values.
