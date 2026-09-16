# Correct Answer

`elapsed_days_to_largest_later_alert_rounded`: `17.0` days.

The Gorkha mainshock timestamp is `2015-04-25T06:11:25.950000Z`. The largest later Nepal EQ alert has severity `7.3` and timestamp `2015-05-12T07:05:19Z`.

# Computation

```text
elapsed_seconds = 2015-05-12T07:05:19Z - 2015-04-25T06:11:25.950000Z
elapsed_seconds = 1,472,033.05
elapsed_days = 1,472,033.05 / 86,400 = 17.037419560185...
round(elapsed_days, 1) = 17.0
```

A compact response should report `target_family` as `earthquake_aftershock_alert_timing` and place `17.0` under `answer.elapsed_days_to_largest_later_alert_rounded`.

# Scoring Rubric

Total: 20 points.

- Mainshock timestamp, 4 points: uses the Gorkha mainshock record with id `us20002926` and timestamp `2015-04-25T06:11:25.950000Z`.
- Later-alert filter, 4 points: filters Nepal EQ alert records to those more than one minute after the mainshock, yielding six later alerts.
- Largest-alert rule, 4 points: uses the later Nepal alert with the largest severity value, `7.3` at `2015-05-12T07:05:19Z`.
- Elapsed-day formula, 4 points: computes timestamp difference divided by `86,400` seconds, giving `17.037420` days before rounding.
- Requested JSON and rounding, 4 points: returns `elapsed_days_to_largest_later_alert_rounded` as `17.0` days with a short timing interpretation.
