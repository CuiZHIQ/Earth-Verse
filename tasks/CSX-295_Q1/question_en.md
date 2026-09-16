# Transport-Scale Consistency Check

For the January 2022 Saharan dust outbreak over the Atlantic, test whether the quantitative record is consistent with a long-range plume-scale transport signal rather than a package point-wind-only signal.

Compute this compact ledger:

1. `window_days`: inclusive event duration in days.
2. `plume_speed_kmh`: reported plume length divided by `window_days * 24`.
3. `local_peak_wind_kmh`: the larger package point-wind 10 m daily maximum after converting any m/s value to km/h; use it as a point-wind comparator, not as complete corridor wind evidence.
4. `speed_ratio`: `plume_speed_kmh / local_peak_wind_kmh`.
5. `precip_context_mm`: the larger event-accumulated precipitation maximum from the gridded precipitation summaries.
6. `diagnosis`: `transport_scale_pass` if plume length is at least 3000 km, `window_days` is at least 3, and `speed_ratio` is greater than 1.5; otherwise `local_wind_sufficient`.

Return compact JSON with exactly those six keys. Round numeric values except `window_days` to two decimals.
