# Southeast Asia Haze Threshold Ledger

A technical review team is checking a numeric smoke-severity ledger for the 2015 Southeast Asia haze linked to Indonesian fires during August-November 2015. Using the incident record and quantitative diagnostics, compute the four threshold tests below and return the final ledger.

Use these definitions. Treat report phrases such as "above", "nearly", "about", and "more than" as benchmark anchors for this ledger, not as exact physical measurements:

- `psi_excess_ratio` = peak PSI anchor / hazardous PSI threshold anchor; this test passes if the ratio is at least 5.0.
- `co_anomaly_ratio` = peak reported surface carbon monoxide anchor over Borneo / usual average carbon monoxide anchor; this test passes if the ratio is at least 10.0.
- `resp_cases_per_exposed_million` = reported respiratory-problem case anchor / reported high-smoke-exposed people lower-bound anchor in millions; this test passes if the benchmark rate is at least 10000.
- `service_markers_per_100k` = (schools + hospitals + police amenities + fire stations + shelters) / local population * 100000; this is a package-derived receptor-context density test, not an event-time facility impact count, and it passes if the rate is at least 8.0.

Return only compact JSON with `psi_excess_ratio`, `co_anomaly_ratio`, `resp_cases_per_exposed_million`, `service_markers_per_100k`, `threshold_pass_count`, and `final_label`. Round ratios and rates to three decimals. Use `smoke_threshold_confirmed` when at least three of the four tests pass; otherwise use `smoke_threshold_not_confirmed`.
