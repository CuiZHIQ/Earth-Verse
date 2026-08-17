# Correct Answer

```json
{
  "answer": "phreatic_report_dry_window",
  "max_precip_mm": 0.536591,
  "dry_margin_mm": 0.463409,
  "sources_below_1mm": 5,
  "anchor_score": 8,
  "reported_hikers": 36,
  "rain_gate": "fail_lt_1mm",
  "consistency_note": "All five event-day precipitation summaries are below 1 mm while the phreatic narrative anchor score is 8, so the computed label is phreatic_report_dry_window."
}
```

# Computation

The five precipitation summaries are 0.01, 0.0, 0.5365908145904541, 0.11499999463558197, and 0.0 mm. Therefore:

`max_precip_mm = 0.536591`, `dry_margin_mm = 1.0 - 0.5365908145904541 = 0.463409`, and `sources_below_1mm = 5`.

Exact event-narrative counts are: phreatic=2, ash=2, ballistic=1, hikers=1, little_warning=1, unexpectedly=1. Their sum is `anchor_score = 8`. The reported hiker count is `36`. Because `max_precip_mm < 1.0`, the rain gate state is `fail_lt_1mm`; with `anchor_score >= 6` and `reported_hikers > 0`, the label is `phreatic_report_dry_window`.

# Scoring Rubric

- 3 points: Returns compact JSON with answer, max_precip_mm, dry_margin_mm, sources_below_1mm, anchor_score, reported_hikers, rain_gate, and one calculation-tied note.
- 5 points: Computes max_precip_mm as 0.536591 mm, dry_margin_mm as 0.463409 mm, and sources_below_1mm as 5.
- 5 points: Computes exact counts phreatic=2, ash=2, ballistic=1, hikers=1, little_warning=1, unexpectedly=1, anchor_score=8, and reported_hikers=36.
- 4 points: Applies the 1.0 mm threshold, marks rain_gate as fail_lt_1mm, and returns phreatic_report_dry_window.
- 2 points: Keeps the consequence concise, tied to the computed threshold and count results, and free of extra inferences.
- 1 point: Uses millimeter units and reasonable rounding within 1e-6 for the two decimal-valued fields.
