# Gorkha Later-Alert Timing Anchor

During the 25 April to mid-May 2015 Gorkha earthquake sequence in Nepal, compute a timing anchor for the later-alert phase.

Use the Gorkha mainshock timestamp and the later Nepal earthquake alert records after it. Treat alerts within the first minute after the mainshock as part of the initial alert, then use the later Nepal EQ alert with the largest severity value.

Compute:

```text
round((largest_later_alert_time_utc - mainshock_time_utc).total_seconds() / 86400, 1)
```

Return JSON:

```json
{
  "target_family": "earthquake_aftershock_alert_timing",
  "answer": {
    "elapsed_days_to_largest_later_alert_rounded": 0.0
  },
  "formula": "<timestamp arithmetic used>",
  "interpretation": "<one short sentence>"
}
```
