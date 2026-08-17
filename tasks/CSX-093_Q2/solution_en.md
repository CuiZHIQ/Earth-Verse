# Final Answer

```json
{
  "event_total_mm": 133.9,
  "wettest_6h_mm": 98.3,
  "six_hour_share": 0.734,
  "wet_run_hours": 23,
  "threshold_counts": {
    "rain": 6,
    "contrast": 3
  },
  "final_state": "rainfall_concentration_signature_supported"
}
```

# Key Computations

The hourly precipitation series contains 72 values. Summing the series gives `event_total_mm = 133.9`. The largest rolling 6-hour total is `wettest_6h_mm = 98.3`, so `six_hour_share = 98.3 / 133.9 = 0.734`. The longest contiguous run with hourly precipitation greater than zero lasts 23 hours.

The six rain tests all pass: the regional peak floor is 254.0 mm, the Central Park record-hour amount is `3.47 in * 25.4 = 88.1 mm`, the wettest 6-hour load is 98.3 mm, the 6-hour share is 0.734, the city record slice has 500 entries, and the top three boroughs account for 0.836 of that slice.

The three contrast tests all pass: point maximum wind speed is 45.2 km/h, the Sentinel-1 mean VV change is -0.429 dB so its absolute magnitude is below 1 dB, and the AlphaEarth mean change is 0.0382.

# Reasoning Path

The ledger first establishes that the event precipitation was concentrated: 98.3 mm fell in the wettest 6-hour window, which is 73.4 percent of the 72-hour total. The independent report and city-record anchors also exceed their rain thresholds, producing `rain_pass_count = 6`.

The contrast side of the ledger checks whether the non-rain metrics would overturn that diagnosis. They do not: wind remains below the 63 km/h test, the mean Sentinel-1 VV change has small absolute magnitude, and the AlphaEarth mean change is below 0.05. This gives `contrast_pass_count = 3`.

The decision rule requires at least five rain passes and at least two contrast passes. Because `6 >= 5` and `3 >= 2`, the deterministic final state is `rainfall_concentration_signature_supported`.

# Computed Interpretation

The computed values support a short-window rainfall concentration signature for the September 1-3, 2021 Northeast phase of Hurricane Ida: most of the 72-hour rainfall total arrived in a 6-hour burst, while the wind and mean image-change checks do not point to a stronger alternate driver in this ledger.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the six requested top-level fields with `threshold_counts` nested as specified. Partial credit: 1-2 points if most required fields are present but minor nesting, naming, or extra-text problems remain; 0 if the required ledger is not recoverable.
- 5 points: Correctly computes hourly rainfall quantities: 133.9 mm event total, 98.3 mm wettest 6-hour load, 0.734 six-hour share, and 23 wet-run hours. Partial credit: about 1 point for each correct rainfall quantity, with small rounding tolerance; lose the relevant credit for wrong aggregation windows, unit mistakes, or treating trace-zero hours as wet.
- 4 points: Correctly evaluates the six rain thresholds using the regional peak floor, Central Park record hour, rolling 6-hour load, 6-hour share, city record count, and top-three borough share. Partial credit: proportional credit for correctly evaluated rain tests; lose credit for missing the inch-to-mm conversion, using the wrong threshold, or miscounting the six-test pass total.
- 3 points: Correctly evaluates the three contrast thresholds using maximum point wind, Sentinel-1 mean VV change, and AlphaEarth mean change. Partial credit: 1 point per correctly evaluated contrast test; lose credit for using the signed Sentinel-1 value instead of its absolute magnitude or reversing a less-than comparison.
- 3 points: Applies the final-state rule exactly and returns `rainfall_concentration_signature_supported`. Partial credit: 1-2 points if the final label is consistent with one threshold count but the other count or the rule wording is partly wrong; 0 for the opposite final state.
- 1 point: Shows enough formula work to make rounding and inch-to-mm conversion auditable. Partial credit: 0.5 point for a mostly clear trace with one missing conversion or rounding note; 0 if no calculation path is shown.
- 1 point: Avoids converting service records into verified flood depth or mean image summaries into a complete inundation map. Partial credit: 0.5 point if the answer has one minor over-broad phrase but keeps the computed ledger intact; 0 for adding major realized-loss or full-map conclusions beyond the computed values.
