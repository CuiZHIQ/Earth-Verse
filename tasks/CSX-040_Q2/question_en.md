# Central Andes Summer Snowpack Reconciliation

A late January 2021 austral-summer storm affected high terrain in the Central Andes. A technical snow-hazard review needs to reconcile high-elevation point weather, coarse event-accumulated precipitation summaries, and storm-window image statistics.

Build a compact evidence ledger that decides whether the data support a persistent high-elevation snowpack signal or a brief bright-scene/coarse-precipitation artifact.

Return one JSON object with exactly these fields:

- `classification`
- `point_grid_contrast_ratio`
- `snowfall_run_hours`
- `retained_depth_fraction`
- `cold_wind_check`
- `image_check`
- `basis`

Compute:

- `point_grid_contrast_ratio` as total point snowfall depth converted from cm to mm, divided by the largest mean event precipitation among the gridded summaries; round to one decimal place.
- `snowfall_run_hours` as the longest consecutive hourly run with point snowfall greater than 0.
- `retained_depth_fraction` as maximum hourly snow depth divided by total point snowfall depth, both in meters; round to two decimals.
- `cold_wind_check` as a short phrase that includes below-freezing hours, maximum gust, and minimum wind chill. Compute wind chill with `WC = 13.12 + 0.6215*T - 11.37*V^0.16 + 0.3965*T*V^0.16`, where `T` is air temperature in deg C and `V` is 10 m wind speed in km/h, applying the formula only where `T <= 10 C` and `V > 4.8 km/h`.
- `image_check` as a short phrase that uses the bright-white image fraction and annual embedding-change mean.

Keep `basis` to one sentence and distinguish a persistent point snowpack diagnosis from a bright-scene-only explanation.
