# Storm Boris Rainfall-Exposure Diagnostic

During Storm Boris in September 2024, prolonged rainfall caused severe flooding across parts of Central and Eastern Europe. A hydrometeorology team wants a compact numerical check of whether the local quantitative summaries point to a rainfall-exposure signal, or whether the mean radar surface-change statistic is large enough to dominate the interpretation.

Compute the event ledger using these definitions:

- `mean_peak_precip_mm`: average of the two non-null event-window precipitation maxima.
- `mean_areal_precip_mm`: average of the two non-null event-window areal precipitation means.
- `peak_to_areal_ratio`: `mean_peak_precip_mm / mean_areal_precip_mm`.
- `population_million`: local population divided by 1,000,000.
- `rainfall_population_index`: `mean_peak_precip_mm * population_million`.
- `mean_vv_change_db`: mean post-minus-pre Sentinel-1 VV change.

Use the diagnosis label `rainfall_exposure_dominant_weak_mean_radar_change` when `mean_peak_precip_mm >= 50`, `population_million >= 1`, and `abs(mean_vv_change_db) < 0.25`; otherwise use `mixed_or_radar_dominant_signal`.

Return only compact JSON with those six numeric fields and the `diagnosis` label. Round precipitation, ratios, population, index, and radar change to three decimals.
