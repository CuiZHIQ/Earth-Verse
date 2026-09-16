# Rainfall Source Reconciliation

A hydrometeorology analyst is comparing the July 2021 Western Europe flood rainfall signal across report text and gridded precipitation summaries. The report gives 48-hour station and regional-box totals, while the gridded event summaries provide ERA5-Land, GPM, and CHIRPS accumulated-precipitation statistics.

Build a compact reconciliation ledger that answers this question: do the gridded event maxima behave like a close proxy for the highest reported 48-hour rainfall, or do they mainly show agreement between two gridded products at a lower intensity scale?

Use the provided data only. Compute the maximum absolute difference between the ERA5-Land and GPM event maxima, the ratio of the ECMWF 48-hour box total to the larger gridded maximum, the ratio of the Jalhay station total to the larger gridded maximum, the Jalhay-minus-Spa station spread, and the 20-25 percent direct-runoff depth implied by the 104 mm box total. Also note whether the CHIRPS event summary contributes finite event totals.

Return a short JSON object:

```json
{
  "answer": "<compact_label>",
  "gridmax_mm": <number>,
  "gpm_era5_max_diff_mm": <number>,
  "report_box_to_gridmax_ratio": <number>,
  "jalhay_to_gridmax_ratio": <number>,
  "station_spread_mm": <number>,
  "runoff_depth_range_mm": [<low>, <high>],
  "chirps_status": "<short_status>",
  "interpretation": "<one sentence>"
}
```
