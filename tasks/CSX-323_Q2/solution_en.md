# Correct Answer

```json
{
  "event_window_days": 1127,
  "event_window_years": 3.09,
  "source_result_count": 6,
  "marine_heatwave_term_count": 14,
  "ecosystem_impact_term_count": 6,
  "northeast_pacific_reference_count": 6,
  "score": 6,
  "final_label": "scale_window_pass"
}
```

# Derivation

The locked event window is 2013-12-01 through 2016-12-31, inclusive:

`event_window_days = 1127`

`event_window_years = 1127 / 365 = 3.09`

The local event-search metadata reports `source_result_count = 6`. After cleaning the local event-search snippets and combining them with the event metadata, the reference computation counts:

- `marine_heatwave_term_count = 14`
- `ecosystem_impact_term_count = 6`
- `northeast_pacific_reference_count = 6`

The six evidence tests all pass: the package hazard family is marine heatwave/coastal ecosystem, the locked event scope is basin scale, the event lasts at least 365 days, the marine-heatwave term count is at least 3, ecosystem-impact language is present, and Northeast Pacific context is present. Thus `score = 6` and `final_label = scale_window_pass`.

# Scoring Rubric

Total: 20 points.

- 4 points: returns the requested JSON keys with numeric values rounded as specified.
- 4 points: computes the locked inclusive event window and 3.09-year duration correctly.
- 4 points: reports the source-result, marine-heatwave, ecosystem-impact, and Northeast Pacific text-evidence counts.
- 4 points: applies the six evidence tests without using short point-weather, Sentinel-2, or other land-product samples.
- 2 points: gives `scale_window_pass` only because all six tests pass.
- 2 points: keeps the interpretation within scale-window evidence and avoids unmeasured mortality, economic totals, service-disruption totals, or non-event land-product proxies.
