# Tornado Concentration and Rating Ledger

A severe-storm climatology analyst is checking the March 31-April 1, 2023 U.S. tornado outbreak for the NWS Chicago forecast area. The task is to decide whether the local episode is best summarized as a dense, mostly lower-rated tornado subset within a very short national tornado window.

Compute a compact ledger with these fields:

- `final_label`
- `local_tornado_count`
- `modal_rating`
- `ef0_ef1_share_pct`
- `national_24h_share_pct`
- `local_national_share_pct`
- `tests_passed`

Use these decision tests: local tornado count at least 20; EF-0 plus EF-1 tornadoes at least 75% of the local total; at least 90% of national confirmed tornadoes occurred within 24 hours; the local share of national confirmed tornadoes is between 10% and 20%, inclusive. Round percentages to one decimal place and add one sentence interpreting the ledger.
