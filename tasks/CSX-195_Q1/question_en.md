# Australian Smoke Upper-Air Ledger

During the late December 2019 to early January 2020 smoke episode from southeastern Australia over the South Pacific, a technical review team wants a compact ledger that tests whether the record is dominated by upper-air smoke transport rather than by local surface-change mapping.

Compute the following values from the incident record and quantitative diagnostics:

- `event_days`: inclusive days in the dated event window.
- `image_to_height_lag_days`: days from the January 4, 2020 natural-color image anchor to the January 6, 2020 smoke-height anchor.
- `altitude_margin_km`: minimum reported smoke height minus a 12 km upper-air threshold.
- `transport_signal_count`: count of six report signals: January 4 image context, tan smoke wording, pyrocumulonimbus wording, paired December 29 and January 4 fire-cloud dates, Pacific/New Zealand transport wording, and snow-darkening plus more-than-halfway global travel wording.
- `transport_score`: one point each for event duration between 10 and 16 days inclusive, image-to-height lag no more than 2 days, altitude margin at least 0 km, and at least 5 transport signals.
- `surface_score`: one point each for mean burn-index proxy at least 0.27, mean annual feature-change proxy at least 0.05, and the event-dated image falling inside the event window. Treat this as a local surface-proxy comparison score, not as proof of an event burn perimeter.
- `score_gap`: `transport_score - surface_score`.
- `final_label`: `upper_air_smoke_transport_pass` if `transport_score` is 4 and `score_gap` is at least 2; otherwise `mixed_signal_recheck`.

Return only compact JSON with exactly those eight keys, using integer counts and kilometre values rounded to one decimal when needed.
