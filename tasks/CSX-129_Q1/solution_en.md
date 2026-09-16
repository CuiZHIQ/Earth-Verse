# Final Answer

Correct answer: return the target family `ian_landfall_point_signal_remote_box_consistency_ledger` with five ledger rows. The Florida point passes the severe landfall signal tests, the daily product cross-checks rainfall without replacing the peak gust, and the remote mapped box fails transfer tests for point intensity, bounded precipitation, exposure counts, image summaries, and surge inference.

# Key Computations

The Florida point is `[-81.85431, 26.608084]`. Its local storm-window signal passes the severe landfall tests: maximum gust `185.4 km/h >= 150 km/h`, total precipitation `211.5 mm >= 150 mm`, and minimum pressure `966.9 hPa <= 980 hPa`.

The daily POWER cross-check gives `157.7 mm` total precipitation, so the daily-to-point precipitation ratio is `157.7 / 211.5 = 0.746`. Its maximum wind is `14.05 m/s`, or `50.58 km/h`, and the point gust is `185.4 / 50.58 = 3.665` times larger, so the daily product is a rainfall cross-check rather than a substitute gust estimate.

The compact mapped box is `[-110.225, 43.275, -109.775, 43.725]` with centroid `[-110.0, 43.5]`. The Florida point is outside the box, and the point-to-centroid distance is `sqrt((-81.85431 + 110.0)^2 + (26.608084 - 43.5)^2) = 32.825549 degrees`.

The bounded precipitation context is far below the Florida point total: ERA5-Land max/mean are `30.204164/22.209683 mm`, GPM max/mean are `23.579999/14.884846 mm`, and CHIRPS max/mean are `69.322785/44.000844 mm`. Their maxima are only `0.143`, `0.111`, and `0.328` of the `211.5 mm` point total.

The image and exposure transfer row uses Sentinel-1 counts `16` pre and `18` post, VV mean change `-0.744729 dB`, WorldPop `175.658766`, OSM element count `431`, Wyoming county examples, and `surge_named_layer_present = false`.

# Reasoning Path

1. Establish the local cyclone signal from the Florida point: wind gust, rainfall, and pressure all clear the severe-landfall thresholds.
2. Cross-check precipitation with the daily product while keeping daily 10 m wind separate from the peak gust metric.
3. Test the compact mapped box against the Florida point; the point is outside the box and more than 32 degrees from its centroid.
4. Compare bounded grid precipitation maxima and means with the Florida point total; all bounded maxima are less than 35 percent of the point total.
5. Treat image, population, and mapped-feature summaries as non-transferable remote-box context because the county examples point to Wyoming and no named surge layer is present.

# Computed Interpretation

The defensible compact label is `severe_florida_point_signal_remote_box_rejected`: the Florida point supports severe Hurricane Ian landfall intensity, while the remote mapped box and its attached counts stay out of the Ian landfall calculation.

# Scoring Rubric

- 2 points: Requested JSON ledger. Full credit requires the target family, exactly the five ledger rows, failed transfers, and final consistency label. Partial credit: award 1 point for valid JSON with missing or renamed rows.
- 4 points: Florida point landfall signal. Full credit computes `185.4 km/h`, `211.5 mm`, and `966.9 hPa` with the stated thresholds and passes the row. Partial credit: award 2-3 points for two correct metrics or minor unit errors.
- 3 points: Daily POWER cross-check. Full credit computes `157.7 mm`, precipitation ratio `0.746`, `14.05 m/s = 50.58 km/h`, and gust-to-POWER-wind ratio `3.665`. Partial credit: award 1-2 points for a partial precipitation-only or wind-only cross-check.
- 4 points: Mapped-box distance proof. Full credit gives the point, bbox, centroid, outside-box result, conflict flag, and `32.825549 degrees`. Partial credit: award 2-3 points for the correct mismatch conclusion with an incomplete calculation.
- 3 points: Bounded precipitation ratio check. Full credit compares ERA5, GPM, and CHIRPS mean/max values against `211.5 mm` and rejects substituting the bounded context for the Florida point. Partial credit: award 1-2 points for using only one or two products.
- 3 points: Image and exposure transfer check. Full credit uses Sentinel counts/change, WorldPop, OSM count, Wyoming county examples, and absent surge layer to reject loss-count or surge transfer. Partial credit: award 1-2 points for a correct transfer decision missing several anchors.
- 1 point: Final proof discipline. Full credit provides a concise final label and avoids Ian-wide loss, direct damage, or surge claims not established by the calculations. Partial credit: no credit if the answer adds external planning text or escalates beyond the ledger.
