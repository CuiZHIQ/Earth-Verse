# Hurricane Ian Peak-Timing Ledger

A meteorology verification desk is reconciling Hurricane Ian across Cuba, Florida, and the southeastern United States during 23-30 September 2022. Determine whether the local wind-pressure-rainfall record is best summarized as a same-hour peak, a wind-pressure-first then rain-later-same-day sequence, or a rain-first sequence.

Return a compact structured answer with:

- `timing_label`: `same_hour_peak`, `wind_pressure_then_rain_same_day`, or `rain_first`.
- Event window, affected countries, alert level, and catalog severity.
- Maximum 10 m wind speed and time, maximum 10 m gust and time, minimum sea-level pressure and time, point rainfall total, peak hourly rainfall and time, and peak daily rainfall and date.
- Lag hours from maximum wind to maximum gust, maximum wind to minimum pressure, maximum wind to peak hourly rainfall, and maximum gust to peak hourly rainfall.
- Daily rainfall share of the point event total and whether the peak daily rainfall occurs on the same date as the wind-pressure peak.
- One sentence explaining why the chosen label follows from the times and ratios.
