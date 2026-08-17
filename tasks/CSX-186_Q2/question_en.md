# Wildfire Snow-Interruption Threshold Ledger

A technical review team is checking the late-October phase of the 2020 East Troublesome fire in Colorado, when the fire expanded explosively and then received mountain snowfall.

Compute a compact threshold ledger showing whether the snowfall should be interpreted as ending the incident or only as a temporary slowdown. Use the documented acreage jump, 24-hour growth interval, containment percentage, and snowfall range.

Return compact JSON:

```json
{
  "growth_increase_acres": <number>,
  "growth_rate_acres_per_hour": <number>,
  "not_contained_percent": <number>,
  "snow_midpoint_inches": <number>,
  "threshold_flags": {
    "explosive_growth": "<pass|fail>",
    "residual_control_gap": "<pass|fail>",
    "snow_moderation": "<pass|fail>"
  },
  "ledger_pass_count": <integer>,
  "final_state": "<temporary_snow_slowdown_residual_risk|snow_ends_incident>",
  "one_sentence_interpretation": "<short computation-based sentence>"
}
```

Use these decision thresholds: explosive growth passes if growth rate is greater than 5,000 acres per hour; residual control gap passes if the not-contained share is at least 80 percent; snow moderation passes if the snowfall midpoint is at least 6 inches. Treat snow as incident-ending only if the residual-control-gap test fails; otherwise classify the result as `temporary_snow_slowdown_residual_risk`.
