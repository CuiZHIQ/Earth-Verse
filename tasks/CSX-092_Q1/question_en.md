# Uttarakhand-Western Nepal Monsoon Rainfall Window Test

A hydrometeorology team is checking the June 2013 Uttarakhand and western Nepal Himalayan basin floods. The question is whether the package's local rainfall record supports a persistent multi-day monsoon forcing, or whether the event could be summarized as a short single-hour burst.

Using the technical record for 15-18 June 2013, compute a compact rainfall-window ledger. Return exactly one JSON object with these fields:

- `answer`
- `event_total_mm`
- `wettest_72h_mm`
- `wettest_72h_window`
- `wettest_72h_share`
- `wet_hour_fraction`
- `peak_hour_share`
- `report_heavy_map_gap_mm`

Round millimeter values to 0.1 mm and ratios to three decimals. The `answer` field should be a short label stating the consistency result. `report_heavy_map_gap_mm` should compare the local event total with the heavy-rain map reference stated in the event report, using the minimum gap implied by the report's lower-bound wording.
