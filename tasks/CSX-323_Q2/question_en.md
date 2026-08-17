# Scale-Window Evidence Summary

Compute a reproducible scale-window evidence summary for the 2013-2016 Northeast Pacific marine heatwave known as "The Blob." Return a compact JSON object with exactly these keys:

`event_window_days`, `event_window_years`, `source_result_count`, `marine_heatwave_term_count`, `ecosystem_impact_term_count`, `northeast_pacific_reference_count`, `score`, `final_label`.

Definitions:

- `event_window_days`: inclusive day count from the locked event start and end dates.
- `event_window_years`: `event_window_days / 365`, rounded to two decimals.
- `source_result_count`: the local event-search total-hit count.
- `marine_heatwave_term_count`: count of marine-heatwave, Blob, and warm-Blob terms in the event metadata plus local event-search snippets.
- `ecosystem_impact_term_count`: count of ecological-impact, harmful/toxic algal bloom, algal bloom, or food-web terms in the local event-search snippets.
- `northeast_pacific_reference_count`: count of Northeast/Northeastern Pacific or Pacific Ocean references in the event metadata plus local event-search snippets.
- `score`: one point for each satisfied test: hazard family is marine heatwave/coastal ecosystem, event scope is basin, `event_window_days >= 365`, `marine_heatwave_term_count >= 3`, `ecosystem_impact_term_count >= 1`, and `northeast_pacific_reference_count >= 1`.
- `final_label`: `scale_window_pass` only when `score` is 6; otherwise `scale_window_fail`.
