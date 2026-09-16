# Hurricane Ian Landfall Threshold Ledger

Hurricane Ian crossed southwest Florida on September 28, 2022. A forecast verification analyst needs to decide whether the local record should be coded as a synchronized landfall-window case, rather than a later rain-only case.

Using the incident's quantitative record, compute this six-test ledger:

- catalog wind intensity at least 240 km/h;
- local minimum sea-level pressure at most 970 hPa;
- local peak 10 m gust at least 178 km/h;
- peak gust and minimum pressure within 1 hour of each other;
- wettest 24-hour rainfall at least 140 mm and at least 65% of event-total rainfall;
- peak hourly rainfall occurring 0 to 6 hours after the pressure minimum.

Return only compact JSON with this shape:

```json
{
  "label": "...",
  "score": "...",
  "failed_tests": [],
  "anchors": {}
}
```

Use UTC timestamps and round numeric anchors sensibly.
