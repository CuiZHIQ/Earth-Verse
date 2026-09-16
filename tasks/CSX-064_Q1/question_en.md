# July 2020 Monsoon Rainfall Threshold Ledger

A hydrometeorology review team is checking the July 2020 South and East Asia monsoon flood diagnosis. The dispute is whether the sampled rainfall diagnostics support calling the sampled area itself a `>100 cm` rainfall maximum, or whether they instead show heavy but sub-threshold local rainfall while the regional record also documents floodplain high-water amplification.

Using the technical record and quantitative diagnostics, compute a compact threshold ledger. Return JSON with exactly these fields: `threshold_mm`, `max_sample_mm`, `threshold_ratio`, `shortfall_mm`, `poyang_excess_m`, `classification`. Round `threshold_ratio` to three decimals and all other computed numeric fields to three decimals where needed. The classification should be a short snake_case phrase deciding the rainfall threshold test and the high-water interpretation.
