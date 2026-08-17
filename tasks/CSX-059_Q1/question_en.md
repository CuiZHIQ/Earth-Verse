# Short-Duration Rainfall Threshold Ledger

During the evening of September 1, 2021, the remnants of Ida produced flash flooding in New York City while also contributing to a broad northern Mid-Atlantic rain shield. A hydrometeorology reviewer wants to test whether the New York City phase satisfies a short-duration pluvial-burst rule rather than a slow routed-river explanation.

Using the technical record, compute the rainfall ledger with these definitions:

- `record_hour_mm = record_hour_inches * 25.4`
- `regional_total_floor_mm = regional_total_floor_inches_floor * 25.4`
- `hour_to_regional_floor_ratio = record_hour_inches / regional_total_floor_inches_floor`
- the burst rule passes when `record_hour_mm >= 75.0` and `hour_to_regional_floor_ratio >= 0.30`

Return compact JSON with `target_family`, `metrics`, `gates`, `answer`, `rejected_alternative`, and `computed_consequence`.

Round millimeters to one decimal place and the ratio to three decimals. Keep `computed_consequence` to one sentence tied only to the ledger.
