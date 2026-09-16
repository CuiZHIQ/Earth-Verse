# Southern Africa Smoke-Aerosol Threshold Ledger

During the August-September 2000 southern Africa fire season, NASA described a widespread "river of smoke" associated with fires across the region. A climate-risk analyst needs a compact numerical check of whether the technical record supports a regional smoke-aerosol label rather than a local burn-index or weather-only label.

Compute a 10-point threshold ledger from the local technical record:

- 2 points if the event report contains the smoke-river phrase.
- 2 points if the heaviest-burning source belt contains four named regions.
- 1 point if the reported fire-front length is at least 10 miles.
- 2 points if the aerosol mapping window is at least 30 inclusive days.
- 1 point if the aerosol report names grass and shrubland burning as a principal source.
- 1 point if the event true-color snapshot is inside the August-September event window and spans at least 30 degrees.
- 1 point if the burn-index pre/post scene counts are both zero, so the ledger remains a smoke-aerosol ledger rather than a local burn-index ledger.

Return compact JSON with exactly these keys:

- `answer_label`
- `total_score`
- `threshold_ledger`
- `context_counts`
- `one_sentence_check`

Keep `threshold_ledger` numeric and show the point contribution for each test. In `context_counts`, report the 2000 population, total school-plus-hospital count, and highway-element count from the local settlement context. Do not provide policy advice or a long narrative.
