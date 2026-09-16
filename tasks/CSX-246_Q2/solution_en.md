# Final Answer

The correct answer is:

```json
{
  "window_utc": "2004-12-26T00:58:50/2004-12-29T21:12:59",
  "feature_counts": {
    "total": 11,
    "eq": 11,
    "fl": 0,
    "red_eq": 1,
    "orange_eq": 10
  },
  "threshold_counts": {
    "eq_mag_ge_6": 4,
    "post_main_eq_72h": 9,
    "post_main_mag_ge_6_72h": 3
  },
  "mainshock": {
    "gdacs_eventid": 9059,
    "time_utc": "2004-12-26T00:58:50",
    "gdacs_mag": 8.5,
    "usgs_mag": 9.1
  },
  "first_post_main_lag_min": 77.12,
  "max_post_main_mag": 6.3,
  "mag_deltas": {
    "usgs_minus_gdacs_main": 0.6,
    "gdacs_main_minus_max_post": 2.2
  },
  "conclusion": "passes_cross_source_catalog_ledger"
}
```

# Computation Notes

The immediate sequence ledger contains 11 GDACS features dated on or after the mainshock time: 11 earthquake entries and no flood entries. Earlier flood entries in the broader catalog are outside the mainshock sequence and are not counted in `feature_counts.total` or `feature_counts.fl`. Among the earthquake entries, one is Red and ten are Orange.

The Red GDACS earthquake on 2004-12-26 is event 9059 at 2004-12-26T00:58:50 with severity 8.5. The locked USGS anchor report states mainshock magnitude 9.1, so the cross-source mainshock magnitude delta is `9.1 - 8.5 = 0.6`.

The GDACS earthquake timestamp window runs from 2004-12-26T00:58:50 through 2004-12-29T21:12:59. Four GDACS earthquake entries have severity at least 6.0. After the mainshock and within 72 hours, there are nine later earthquake entries, three of them with severity at least 6.0. The first later earthquake is at 2004-12-26T02:15:57, which is 77.12 minutes after the mainshock. The maximum later GDACS earthquake severity is 6.3, so the GDACS mainshock-to-later maximum gap is `8.5 - 6.3 = 2.2`.

# Scoring Rubric

Total: 20 points.

- Returned JSON shape (2 points): Includes exactly the requested ledger fields with compact scalar or nested numeric values.
- Source filtering (3 points): Uses the GDACS event-list catalog for counts and timing, filters earthquake entries by `eventtype == "EQ"`, and uses the USGS anchor only for the official 9.1 magnitude cross-check.
- Feature and threshold counts (5 points): Reports sequence total=11, eq=11, fl=0, red_eq=1, orange_eq=10, eq_mag_ge_6=4, post_main_eq_72h=9, and post_main_mag_ge_6_72h=3.
- Time-window reconstruction (4 points): Reports the correct earthquake timestamp window, mainshock timestamp, and 77.12 minute first-later-event lag.
- Magnitude consistency checks (4 points): Reports GDACS mainshock 8.5, USGS mainshock 9.1, max later GDACS severity 6.3, and deltas 0.6 and 2.2.
- Bounded answer discipline (2 points): Keeps the answer limited to catalog arithmetic and cross-source consistency fields.
