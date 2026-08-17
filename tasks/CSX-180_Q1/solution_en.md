# Final Answer

The correct answer is `regional_smoke_aerosol_score_10`.

```json
{
  "answer_label": "regional_smoke_aerosol",
  "total_score": 10,
  "threshold_ledger": {
    "smoke_phrase": 2,
    "source_belt": 2,
    "fire_front": 1,
    "aerosol_window": 2,
    "vegetation_fire_source": 1,
    "wide_event_snapshot": 1,
    "burn_index_zero_count": 1
  },
  "context_counts": {
    "population_2000": 72066,
    "facility_count": 4,
    "highway_elements": 42
  },
  "one_sentence_check": "The 10/10 ledger supports the regional smoke-aerosol label, while the population and facility counts remain separate local context values."
}
```

# Key Computations

- Event window: 2000-08-01 through 2000-09-30, or 61 inclusive days.
- Event report phrase: "river of smoke" is present, worth 2 points.
- Heaviest-burning source belt: western Zambia, southern Angola, northern Namibia, and northern Botswana, so the source-region count is 4 and earns 2 points.
- Reported fire-front length: 20 miles; since 20 >= 10, the fire-front test earns 1 point.
- Aerosol mapping window: 2000-08-14 through 2000-09-29. Inclusive-day formula: `(2000-09-29 - 2000-08-14) + 1 = 47` days, so 47 >= 30 and earns 2 points.
- Aerosol source text: grass and shrubland burning for land management and agriculture is named as a principal source, worth 1 point.
- Event snapshot metadata: 2000-08-31 is inside the event window, and the longitude span is `19 - (-16) = 35` degrees; this earns 1 point.
- Burn-index counts: pre_count = 0 and post_count = 0, so the burn-index test earns 1 point for keeping the ledger on the smoke-aerosol target.
- Local context counts: population_2000 = round(72066.13754191996) = 72066; facility_count = 3 schools + 1 hospital = 4; highway_elements = 2 secondary + 27 tertiary + 13 trunk = 42.
- Total score: `2 + 2 + 1 + 2 + 1 + 1 + 1 = 10`.

# Reasoning Path

First, extract the event-label evidence from the NASA event report. The smoke-river phrase, four-region source belt, and 20-mile fire-front value all pass their assigned tests and contribute 5 points.

Second, compute the aerosol-window test from the air-quality record. The inclusive window from 2000-08-14 to 2000-09-29 has 47 days, and the same record links the aerosol field to grass and shrubland burning; together these add 3 points.

Third, check the image and burn-index tests. The event snapshot date falls within the August-September event window and spans 35 degrees, while the burn-index pre/post counts are both zero. These two tests add the final 2 points.

The population, facility, and highway counts are reported as separate local context counts. They are not added to the 10-point smoke-aerosol score.

# Computed Interpretation

The computed ledger gives the regional smoke-aerosol label a full 10/10 score, with separate local context values of 72,066 people, 4 facilities, and 42 highway elements.

# Scoring Rubric

Award 20 points total:

- 4 points for the final structured answer: returns `regional_smoke_aerosol`, `total_score = 10`, and the compact `regional_smoke_aerosol_score_10` answer string. Partial credit: 2 points for the right label with the wrong total, or 1 point for a smoke-related label without the ledger total.
- 4 points for event-report extraction: identifies the smoke-river phrase, all four source-belt regions, and the 20-mile fire-front value. Partial credit: 1 point for the phrase, 2 points for at least three correct regions, and 1 point for the fire-front value within 1 mile.
- 4 points for aerosol-window arithmetic: computes 47 inclusive days from 2000-08-14 to 2000-09-29 and applies the 30-day threshold correctly. Partial credit: 2 points for the correct dates with an off-by-one day count, and 1 point for recognizing that the window passes the threshold without showing the formula.
- 3 points for source and image tests: credits the grass/shrubland source phrase and verifies that 2000-08-31 lies inside the event window with a 35-degree snapshot span. Partial credit: 1 point for the source phrase and 1-2 points for partially correct image-date or span checks.
- 2 points for burn-index and context counts: reports pre_count = 0, post_count = 0, population_2000 = 72066, facility_count = 4, and highway_elements = 42. Partial credit: 1 point for the burn-index counts or 1 point for at least two correct local context counts.
- 3 points for ledger discipline and format: keeps the seven threshold-test point values separate from local context counts and returns compact JSON with the requested keys. Partial credit: 1-2 points for correct reasoning with missing JSON keys or for mixing a context count into the 10-point score.
