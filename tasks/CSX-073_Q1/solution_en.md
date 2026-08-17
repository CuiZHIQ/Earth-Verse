# Final Answer

```json
{
  "label": "drainage_overload_pluvial",
  "total_mm": 133.9,
  "peak_hour_mm": 33.8,
  "peak_hour_time": "2021-09-02T01:00",
  "peak_hour_share": 0.252,
  "hours_ge_10mm": 3,
  "max_run_hours_ge_5mm": 6,
  "sewer_share": 0.914,
  "central_park_peak_in": 3.47
}
```

The correct answer is `drainage_overload_pluvial`: the ledger shows a short, concentrated rainfall burst paired with a sewer-dominated service signal, which is the pattern expected for urban drainage overload.

# Key Computations

The point rainfall series gives a September 1-2 total of 133.9 mm. The largest hourly value is 33.8 mm at 2021-09-02T01:00, so `peak_hour_share = 33.8 / 133.9 = 0.252`. Three hourly values are at least 10 mm, and the longest continuous run at or above 5 mm is 6 hours. The September 2 share of the point total is 109.5 / 133.9 = 0.818, which confirms that most rain fell in the second day of the event window.

The WPC report gives a Central Park wettest-hour value of 3.47 inches, an independent short-duration intensity anchor. The city-service record contains 500 flood-related requests: 457 Sewer and 43 Electric, so `sewer_share = 457 / 500 = 0.914`. The requests span 116 ZIP codes; borough counts are Queens 157, Brooklyn 133, Staten Island 128, Bronx 57, and Manhattan 25.

# Reasoning Path

The threshold rule is satisfied on every required component. The peak hour supplies 25.2% of the two-day point total, above the 20% cutoff. The event has 3 hours at or above 10 mm, meeting the burst-count cutoff. The 6-hour run at or above 5 mm exceeds the 4-hour persistence cutoff. The 91.4% sewer share is above the 85% city-service cutoff.

Those values make a daily-total-only explanation too weak: the total matters, but the diagnostic signal comes from concentration in a few intense hours plus a sewer-heavy complaint distribution. A slow river-rise account is also weaker for this ledger because the service feedback is dominated by sewer and below-grade drainage symptoms rather than a basin-stage metric.

# Computed Interpretation

For this New York City Ida window, the computed result is a concentrated urban pluvial drainage-load event, not merely a high two-day rainfall total.

# Scoring Rubric

Award up to 20 points:

1. Final numeric label and schema, 3 points: returns the requested compact JSON with the label `drainage_overload_pluvial` and the nine required fields. Partial credit: award up to 2 points if the label is equivalent but fields are missing or renamed.
2. Rainfall totals and peak, 4 points: computes 133.9 mm total rainfall, 33.8 mm peak hourly rainfall, and the 2021-09-02T01:00 peak timing or equivalent peak-window reference. Partial credit: award 1 point for a correct total, 1 point for a correct peak value, 1 point for the peak timing, and 1 point for using millimetres consistently.
3. Concentration metrics, 4 points: computes `peak_hour_share = 0.252`, `hours_ge_10mm = 3`, and `max_run_hours_ge_5mm = 6`, then applies the stated thresholds. Partial credit: award up to 3 points if two of the three metrics are correct and the threshold logic is mostly correct.
4. Corroborating report value, 2 points: uses the Central Park wettest-hour value of 3.47 inches as an independent short-duration intensity anchor. Partial credit: award 1 point for mentioning an extreme Central Park hourly value without the correct number or unit.
5. City-service feedback arithmetic, 4 points: uses 500 flood-related complaints, 457 sewer complaints, 43 electric complaints, 116 ZIP codes, and `sewer_share = 0.914` to support drainage-load interpretation. Partial credit: award up to 3 points for correct complaint counts but missing the share or spread.
6. Computed interpretation, 2 points: explains that the event is better represented by concentrated rainfall stressing urban drainage than by a daily-total-only or slow river-rise account. Partial credit: award 1 point for a plausible pluvial interpretation that does not contrast it with weaker daily-total-only reasoning.
7. Concise answer discipline, 1 point: keeps the response focused on the requested ledger and one short interpretation sentence without adding unverified loss estimates. Partial credit: award 0.5 point if the answer is correct but padded with extra narrative.
