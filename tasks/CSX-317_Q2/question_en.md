# Lake Palcacocha Rapid-Route Consistency Check

A technical review team is testing whether the Lake Palcacocha / Huaraz case satisfies a rapid glacier-lake outburst route diagnosis.

Compute the following threshold checks from the event record:

- `rapid_index = 30 minutes / reported source-to-city travel time`; the rapid-route test passes when `rapid_index >= 1`.
- `rain_ratio = 1.0` if the event report states rainfall as the controlling trigger, otherwise `0.0`; a rainfall-control diagnosis passes only when `rain_ratio >= 1`.
- `image_lag_years = years between the event date and the contextual satellite snapshot`; extract the snapshot date from the package manifest row for the contextual image, using the URL `TIME=YYYY-MM-DD` query value. An event-window footprint test passes only when `image_lag_years <= 1`.
- `fatality_city_ratio = historical fatalities / threatened city population`.

Return compact JSON:

```json
{
  "answer": "<short consequence label>",
  "metrics": {
    "travel_minutes": 0,
    "rapid_index": 0.0,
    "rain_ratio": 0.0,
    "image_lag_years": 0.0,
    "fatality_city_ratio": 0.0
  },
  "pass_fail": {
    "rapid_route": true,
    "rainfall_control": false,
    "event_window_footprint": false
  },
  "rejected_alternative": "<one short computation-based rejection>",
  "conclusion": "<one sentence>"
}
```
