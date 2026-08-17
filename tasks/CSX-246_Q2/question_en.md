# Earthquake-Catalog Sequence Ledger

Reconstruct a compact earthquake-catalog sequence ledger for the 2004-12-26 Sumatra-Andaman event using only local evidence.

Use the GDACS event-list catalog as the ledger source. Treat entries with `eventtype == "EQ"` as earthquake entries, and identify the GDACS mainshock as the Red earthquake entry dated 2004-12-26. Use the locked USGS anchor report only to cross-check the official mainshock magnitude stated there. Use UTC timestamps.

Return only compact JSON:

```json
{
  "window_utc": "YYYY-MM-DDTHH:MM:SS/YYYY-MM-DDTHH:MM:SS",
  "feature_counts": {
    "total": 0,
    "eq": 0,
    "fl": 0,
    "red_eq": 0,
    "orange_eq": 0
  },
  "threshold_counts": {
    "eq_mag_ge_6": 0,
    "post_main_eq_72h": 0,
    "post_main_mag_ge_6_72h": 0
  },
  "mainshock": {
    "gdacs_eventid": 0,
    "time_utc": "YYYY-MM-DDTHH:MM:SS",
    "gdacs_mag": 0.0,
    "usgs_mag": 0.0
  },
  "first_post_main_lag_min": 0.0,
  "max_post_main_mag": 0.0,
  "mag_deltas": {
    "usgs_minus_gdacs_main": 0.0,
    "gdacs_main_minus_max_post": 0.0
  },
  "conclusion": "<label>"
}
```

Definitions:

- `window_utc` spans the first through last GDACS earthquake timestamp in this catalog.
- `feature_counts.total` and `feature_counts.fl` count only GDACS entries whose `fromdate` is on or after the mainshock time, so earlier unrelated flood entries are not part of the sequence ledger.
- `eq_mag_ge_6` counts GDACS earthquake entries with severity at least 6.0.
- `post_main_eq_72h` counts GDACS earthquake entries after the mainshock and at or before 72 hours after it.
- `post_main_mag_ge_6_72h` is the subset of those post-mainshock 72-hour entries with severity at least 6.0.
- `first_post_main_lag_min` is the elapsed minutes from the mainshock to the first later GDACS earthquake entry, rounded to two decimals.
- Magnitude deltas are rounded to one decimal.
- Use `passes_cross_source_catalog_ledger` only when every count, time span, and magnitude delta is internally consistent with these definitions; otherwise use `does_not_pass_cross_source_catalog_ledger`.
