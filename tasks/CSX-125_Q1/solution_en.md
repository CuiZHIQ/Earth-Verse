# Final Answer

The supported label is `persistent_multi_pulse_rainfall_exposure`, with all four tests passing. The compact answer is:

```json
{
  "label": "persistent_multi_pulse_rainfall_exposure",
  "passed_tests": 4,
  "storm_days": 36.0,
  "window_days": 39,
  "storm_window_fraction": 0.923,
  "event_total_mm": 375.2,
  "max_72h_mm": 111.7,
  "max_72h_share": 0.298,
  "grid_peak_mm": 192.2,
  "grid_peak_ratio": 1.046,
  "population_million": 5.29,
  "isolated_72h_burst_rejection": "The isolated 72-hour burst summary fails because the wettest 72 hours are only 29.8% of local event rainfall while the storm and window durations are long."
}
```

# Key Computations

The local calculation reads the event metadata, locked date anchor, WMO report text, hourly weather series, gridded precipitation summaries, and compact population total.

The locked window is 2023-02-04 through 2023-03-14. Inclusive counting gives `39` days. The WMO report text gives `36.0` days at tropical-storm status or higher. The duration fraction is `36.0 / 39 = 0.923`.

The package point-weather hourly precipitation series is filtered to the locked event window and has 936 hourly values from 2023-02-04T00:00 through 2023-03-14T23:00. Its event total is `375.2 mm`. The wettest 72-hour rolling sum is `111.7 mm`, spanning 2023-03-12T00:00 through 2023-03-14T23:00. The 72-hour share is `111.7 / 375.2 = 0.298`, below the 0.35 test limit.

The gridded precipitation peaks are `192.2 mm` from GPM and `183.8 mm` from CHIRPS. The larger peak is therefore `192.2 mm`, and the larger-to-smaller ratio is `192.2 / 183.8 = 1.046`, within the 1.10 agreement limit. The compact population total is `5,286,729.5`, or `5.29 million`.

# Reasoning Path

First, the duration test passes because the storm-status duration is at least 30 days and the inclusive event window is at least 35 days. These two checks rule out a short-window summary.

Second, the rainfall-distribution test passes because the wettest 72 hours do not dominate the local rainfall total. A 29.8% share means most rainfall lies outside the wettest three-day interval, while the event total still exceeds 300 mm.

Third, the gridded precipitation test passes because the two gridded peaks are close enough to give the same high-rainfall signal: the peak is at least 180 mm and the peak ratio is only 1.046. Fourth, the population-loading test passes because the compact population total exceeds 5.0 million. With four of four tests passing, the final label is the persistent multi-pulse rainfall-exposure case.

# Computed Interpretation

Freddy's record is best summarized as a prolonged cyclone-linked rainfall and exposure episode. The numbers combine long duration, rainfall spread beyond one 72-hour interval, agreement between two gridded precipitation peaks, and a multi-million-person population total.

# Scoring Rubric

Total: 20 points.

- 4 points: Gives the final label `persistent_multi_pulse_rainfall_exposure` and states that all four tests pass. Partial credit: 2-3 points for a correct persistent rainfall-exposure label with an incomplete pass count; 1 point for a generic long-lived cyclone label.
- 3 points: Computes the duration ledger correctly: 36.0 storm-status days, 39 inclusive window days, and a 0.923 duration fraction. Partial credit: 1-2 points for one or two correct duration values with missing arithmetic.
- 4 points: Computes the rainfall-distribution ledger correctly: 375.2 mm event total, 111.7 mm wettest 72-hour total, and 0.298 share below 0.35. Partial credit: 2-3 points for two correct rainfall values; 1 point for using rainfall values without the share test.
- 3 points: Computes the gridded precipitation comparison correctly: 192.2 mm larger peak, 183.8 mm smaller peak, and 1.046 peak ratio below 1.10. Partial credit: 1-2 points for the correct peaks but missing or misreading the ratio.
- 2 points: Uses the 5.29 million compact population value and applies the 5.0 million threshold correctly. Partial credit: 1 point for citing population without the threshold comparison.
- 2 points: Explains why the isolated 72-hour burst summary fails using the 29.8% share and the long event duration. Partial credit: 1 point for rejecting the burst summary using only one of those two ideas.
- 2 points: Provides one concise JSON object with the requested fields, including `isolated_72h_burst_rejection`, and avoids extra realized-loss claims not calculated in the ledger. Partial credit: 1 point for a mostly complete answer with minor formatting or rounding issues.
