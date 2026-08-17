# Storm Boris Basin-Flood Score Ledger

Storm Boris produced severe flooding across Central and Eastern Europe in September 2024. A hydrology review team is checking whether the quantitative record supports a basin-river-flood-dominant classification, rather than a flash-flood-only classification.

Compute the following ledger from the technical record:

1. Mark the multiday rainfall test as passed if the maximum three-day rainfall is at least 300 mm.
2. Mark the Oder severity test as passed if the Oder River basin signal reaches at least a 20-year return period.
3. Mark the river-amplification test as passed if at least 5,000 km of rivers exceeded twice the average annual maximum flow.
4. Compute the Romania short-duration flood fatality share as Romania short-duration flood fatalities divided by all reported fatalities; reject the flash-flood-only classification if this share is below one third.

Return a compact JSON object with exactly these keys:

- `answer`: final label.
- `score`: number of ledger tests supporting the final label.
- `three_day_rain_mm`: maximum three-day rainfall in millimetres.
- `oder_rp_years_min`: minimum Oder return-period signal in years.
- `river_length_gt2x_aam_km`: kilometres of rivers beyond twice average annual maximum flow.
- `romania_fatality_share`: the fatality share rounded to three decimals.
- `flash_only_test`: `rejected` or `not_rejected`.
