# Correct Answer

```json
{
  "answer": "rapid_ice_entry_glof_route",
  "metrics": {
    "travel_minutes": 15,
    "rapid_index": 2.0,
    "rain_ratio": 0.0,
    "image_lag_years": 58.2,
    "fatality_city_ratio": 0.1167
  },
  "pass_fail": {
    "rapid_route": true,
    "rainfall_control": false,
    "event_window_footprint": false
  },
  "rejected_alternative": "Rainfall control fails because the report does not state rainfall as the controlling trigger.",
  "conclusion": "The numbers support a rapid ice-entry GLOF route toward Huaraz, with rainfall and delayed imagery failing the stated control tests."
}
```

# Computation Path

The reported source-to-city travel time is 15 minutes, so `rapid_index = 30 / 15 = 2.0`; this passes the rapid-route threshold because it is at least 1. The report does not state rainfall as the controlling trigger, so `rain_ratio = 0.0`; this fails the rainfall-control threshold. The event date is 1941-12-13 and the contextual satellite snapshot date is extracted from the package manifest URL as 2000-02-24, giving `image_lag_years = 58.2`; this fails the event-window footprint threshold. The historical severity ratio is `7000 / 60000 = 0.1167`.

The short consequence label is `rapid_ice_entry_glof_route`: a minutes-scale lake-to-city route is numerically consistent, while rainfall control and event-window image footprint alternatives fail their thresholds.

# Scoring Rubric

- 4 points: Returns the requested compact JSON structure with `answer`, `metrics`, `pass_fail`, `rejected_alternative`, and `conclusion`.
- 4 points: Computes the route quantities correctly: `travel_minutes = 15` and `rapid_index = 2.0`.
- 3 points: Computes `rain_ratio = 0.0` from the absence of a report-supported rainfall trigger and marks rainfall control as false.
- 3 points: Computes `image_lag_years = 58.2` and marks event-window footprint as false.
- 2 points: Computes `fatality_city_ratio = 0.1167` and treats it as a historical severity ratio, not a present loss count.
- 2 points: Gives the final label `rapid_ice_entry_glof_route` or an equivalent short GLOF-route label tied to the numeric tests.
- 1 point: Gives one rejected alternative that follows directly from a failed threshold.
- 1 point: Avoids overclaiming new losses, mapped inundation, or facility failure beyond the computed checks.
