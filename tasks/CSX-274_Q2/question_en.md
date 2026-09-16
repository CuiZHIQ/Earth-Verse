# 1997-1998 El Nino Coupled-Window Threshold Ledger

A seasonal hazards analyst is checking when the 1997-1998 El Nino had both a strong ocean signal and a matching atmospheric signal before using it as context for U.S. winter storm and flood planning.

Using the local event package for `CSX-274`, pair each rolling three-month ONI season from May-July 1997 through March-May 1998 with the mean monthly SOI over the same three calendar months.

Apply this diagnostic rule:

- The ocean condition passes when the ONI anomaly is at least `1.5 C`.
- The atmospheric condition passes when the same-window mean SOI is at most `-2.0`.

Reconstruct the continuous run of windows that pass both conditions. Also identify the qualifying windows that sit exactly on a threshold boundary and the nearest single-condition misses within `0.10` units of the failed threshold.

Return your response as concise JSON:

```json
{
  "qualifying_window_count": 0,
  "first_window": "<season_year>",
  "last_window": "<season_year>",
  "calendar_span": "<YYYY-MM_to_YYYY-MM>",
  "calendar_span_months": 0,
  "tight_boundary_windows": ["<season_year>"],
  "near_miss_windows": ["<season_year>"],
  "diagnosis": "<one sentence>"
}
```
