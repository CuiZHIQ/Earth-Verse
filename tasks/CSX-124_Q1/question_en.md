# Cyclone Gabrielle Compound-Signal Ledger

A hydrometeorology verification team is preparing a technical note on Cyclone Gabrielle in February 2023 over New Zealand. They need a compact numeric ledger showing whether the local rainfall concentration, gridded precipitation structure, wind and coastal proxies, image-change contrast, and exposure context jointly cross a high compound-signal threshold.

Return only JSON with these top-level keys:

- `event_window`: the inclusive date span as `YYYY-MM-DD to YYYY-MM-DD`.
- `rainfall`: `total_mm`, `wettest_day`, `wettest_mm`, `wet_share`, and `peak_remainder`.
- `gridded`: `max_mm` and `mean_peak_mean`.
- `wind_coast`: `gust_kmh`, `wind_energy_k`, and `coastal_index`.
- `image_exposure`: `sar_span_db`, `sar_mean_db`, `emb_max_mean`, `population_k`, and `road_share`.
- `score`: `hits`, `total`, `value`, and `class`.

Use these formulas:

- `wet_share = wettest_day_mm / total_mm`.
- `peak_remainder = wettest_day_mm / (total_mm - wettest_day_mm)`.
- For each gridded precipitation summary, compute `max_mm / mean_mm`; `mean_peak_mean` is the average of those three ratios, and `max_mm` is the largest gridded event maximum.
- `wind_energy_k = gust_kmh^2 / 1000`.
- `coastal_index = largest_wave_m + 10 * storm_surge_m`.
- `sar_span_db = sar_max_db - sar_min_db`.
- `emb_max_mean = embedding_max / embedding_mean`.
- `population_k = population / 1000`.
- `road_share = road_tagged_elements / all_local_elements`.

Score one hit for each true gate: `total_mm >= 150`, `wet_share >= 0.70`, `mean_peak_mean >= 1.25`, `wind_energy_k >= 10`, `coastal_index >= 15`, `sar_span_db >= 30`, and both `population_k >= 300` plus `road_share >= 0.90`. Set `value = hits / total`; use `high_compound_signal` when `value >= 0.85`, otherwise use `partial_compound_signal`.

Round millimetres and km/h to one decimal where shown by the source values, round ratios and indices to three decimals, and keep the score to three decimals or an equivalent shorter JSON number.
