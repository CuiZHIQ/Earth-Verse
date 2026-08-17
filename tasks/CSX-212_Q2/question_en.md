# Kathmandu Gridded Smoke-Persistence Threshold Ledger

A regional air-quality analyst is checking the late March to early April 2021 Kathmandu Valley wildfire-smoke episode for a persistent hot, relatively dry, weak-ventilation setup in the technical record. Reconstruct the aggregate threshold ledger for the locked inclusive incident span.

Use the local event package's locked event window, ERA5-Land aggregate temperature, precipitation, and wind statistics, plus GPM and CHIRPS event precipitation summaries. Define:

- `heat_score`: one point each for ERA5 maximum Tmax >= 40 C, ERA5 mean Tmax >= 35 C, and ERA5 minimum Tmax >= 32 C.
- `low_precip_tail_score`: one point each for ERA5 precipitation minimum <= 1 mm, GPM precipitation minimum <= 1 mm, and CHIRPS precipitation minimum <= 1 mm.
- `ventilation_score`: one point when ERA5 mean 10 m wind-vector speed <= 3.5 m/s, and one point when the ERA5 maximum wind-vector screen <= 4.0 m/s.
- `aggregate_persistence_index = 2*low_precip_tail_score + heat_score + 2*ventilation_score`, rounded to 2 decimals.

Return a compact JSON object with exactly these eight top-level keys: `answer`, `event_window`, `heat_block`, `precipitation_block`, `wind_block`, `aggregate_persistence_index`, `threshold_flags`, and `brief_method`.

Required content:

- `answer`: the compact label `gridded_smoke_persistence_threshold_ledger`.
- `event_window`: start date, end date, and inclusive day count.
- `heat_block`: ERA5 maximum, mean, and minimum Tmax values plus `heat_score`.
- `precipitation_block`: ERA5, GPM, and CHIRPS precipitation means, the three-product consensus mean, the three low-tail flags, and `low_precip_tail_score`.
- `wind_block`: ERA5 mean u/v wind, mean wind speed, maximum u/v wind, maximum wind-vector screen, mean ventilation deficit below 3.5 m/s, and `ventilation_score`.
- `aggregate_persistence_index`: numeric index from the formula above.
- `threshold_flags`: booleans for `hot_gridded`, `low_precip_tail`, `weak_ventilation`, and `index_ge_12`.
- `brief_method`: one short sentence naming the gridded heat score, precipitation low-tail score, wind-vector ventilation score, and 2-decimal index rounding.
