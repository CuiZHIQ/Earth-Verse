# February 2023 Southern California Winter Storm: Cross-Source Compression Test

Use only the local CSX-039 event package. Select the package-relative evidence needed to support each numeric value and record the files you used in `data_read`.

Build a compact data diagnosis that identifies the main numeric contrast across the point, report, gridded precipitation, and annual embedding products.

Compute these quantities:

1. From package-local hourly weather evidence: total snowfall in inches, count of hours with temperature at or below 4 C, maximum wind gust in km/h, count of hours with gust at or above 65 km/h, and `max_gust_kmh^2`.
2. From package-local report evidence: high-elevation snow in inches from the nearly 8 ft report value, La Crescenta snow in inches, and the Beverly Hills to downtown Los Angeles rainfall range in millimeters.
3. From independent gridded precipitation evidence: the ratio of the report rainfall upper bound to the larger satellite-event maximum, and the ratio of the report rainfall lower bound to the daily precipitation-event maximum.
4. From annual embedding-change evidence: mean, maximum, and maximum-to-mean ratio of `alphaearth_1_minus_cosine`.

Return a compact JSON object with keys `answer_label`, `metrics`, `decisive_tests`, and `data_read`. The `answer_label` should summarize the cross-source data behavior; avoid inferring social outcomes or field actions.
