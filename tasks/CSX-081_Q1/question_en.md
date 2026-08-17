# Hurricane Ida Northeast Rainfall Concentration Check

A hydrometeorology team is preparing a short technical note on the September 1-3, 2021 flooding from Hurricane Ida's remnants in the northeastern United States. For this note, use the local package's NYC/Jersey City point-weather window as the rainfall-concentration diagnostic and pair it with the NYC complaint records as the local drainage-feedback diagnostic. The team needs to test whether this package-supported view is better summarized as a concentrated multi-hour rainfall episode with New York City drainage feedback, rather than as a single-hour spike or a city-only problem.

Compute the rainfall concentration and local-feedback values, then return compact JSON in this shape:

```json
{
  "target_family": "ida_northeast_rainfall_concentration_numeric",
  "event_total_mm": 0,
  "peak_hour": {
    "time_utc": "",
    "mm": 0,
    "fraction_of_total": 0
  },
  "max_3h": {
    "start_utc": "",
    "end_utc": "",
    "mm": 0,
    "fraction_of_total": 0
  },
  "max_6h": {
    "start_utc": "",
    "end_utc": "",
    "mm": 0,
    "fraction_of_total": 0
  },
  "nyc_feedback": {
    "record_count": 0,
    "sewer_share": 0,
    "street_flooding_share": 0,
    "sep1_sep2_share": 0,
    "top_hour_share": 0
  },
  "final_label": ""
}
```

Round rainfall totals to 0.1 mm and fractions to 4 decimals. Use a one-line `final_label` that states the numerical consistency result; do not add management guidance.
