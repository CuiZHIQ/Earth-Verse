# Early Fire-Weather and Surface-Change Ledger

For the early phase of the 2019-2020 Australian Black Summer bushfires in southeastern New South Wales and the Australian Capital Territory region, compute a compact ledger that tests whether the local data show a compound fire-weather, rainfall counter-evidence, surface-change, and exposure-context signal.

Use the event-overlap daily weather window from 2019-09-01 through 2019-10-16. Count no-rain days, days with both no rain and maximum 10 m wind speed at least 20 km/h, the longest no-rain run, and the hottest overlap day. Then compare nonzero accumulated precipitation against that daily sequencing, summarize the local dNBR and annual embedding-change metrics, and compute this exposure context score:

`context_score = I(population >= 100000) + I(road_features >= 500) + I(sensitive_facilities >= 50)`

where `sensitive_facilities` is the sum of shelter, fire station, school, and police amenities.

Return a compact JSON block with these top-level fields:

- `answer`
- `window`
- `weather`
- `precip`
- `surface`
- `context`
- `gates`

Use these gate rules: `dry_share >= 0.5`, `dry_windy_days >= 5`, `dnbr_mean > 0 and dnbr_max >= 0.66 and alpha_change_max >= 0.25`, and `context_score >= 2`. For this ledger, `rain_negates_weather_signal` is false when both daily weather gates pass despite nonzero precipitation totals, and true if either daily weather gate fails. The final `answer` should be `strong_compound_fire_weather_surface_context_signal` only when at least three of the four gates pass and `rain_negates_weather_signal` is false.
