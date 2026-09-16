# Hurricane Ophelia Wind-Rain Phase Score Ledger

During 9-16 October 2017, Hurricane Ophelia moved from the eastern Atlantic toward Ireland and the United Kingdom, weakening before the European impact day but still bringing severe weather. A technical review team needs a calculation-led check of whether the 16 October Ireland/UK impact should be classified as wind-led after the post-tropical transition rather than rainfall-primary.

Compute a compact score ledger with these tests:

- `wind_pressure_path`: one point each for gust at least 100 km/h, sustained wind at least 50 km/h, pressure at most 995 hPa, pressure minimum no more than 2 hours after the gust peak, and the wind maximum falling on 2017-10-16.
- `rain_primary_path`: one point each for impact-day rainfall share at least 0.25, local precipitation peak on the same date as the wind peak, maximum hourly rainfall at least 5 mm, and daily-product precipitation peak on the same date as daily-product wind peak.
- `post_tropical_timing`: one point for the report timing identifying the transition before 2017-10-16 and one point for the report placing the Ireland/UK impact on 2017-10-16.

Return JSON in this shape:

```json
{
  "target_family": "ophelia_wind_rain_phase_score_ledger",
  "score_ledger": {
    "wind_pressure_path": {
      "score": 0,
      "max_score": 5,
      "tests": {},
      "key_values": {}
    },
    "rain_primary_path": {
      "score": 0,
      "max_score": 4,
      "tests": {},
      "key_values": {}
    },
    "post_tropical_timing": {
      "score": 0,
      "max_score": 2,
      "tests": {},
      "key_values": {}
    }
  },
  "rejected_path": "",
  "final_label": "",
  "one_sentence_interpretation": ""
}
```

Use numeric values with units inside `key_values`, boolean pass/fail entries inside `tests`, and one concise final label.
