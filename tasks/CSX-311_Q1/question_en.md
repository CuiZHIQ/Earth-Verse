# Mount Ontake Phreatic Rain-Gate Consistency Check

A technical review team is testing a package-derived diagnosis for the September 27, 2014 Mount Ontake eruption. Compute a threshold proof that compares event-day rainfall support for a rain-mobilized volcanic flow signal against the narrative signal for a sudden phreatic summit event.

Use these definitions:

- `max_precip_mm = max(...)` across the event-day precipitation summaries.
- `dry_margin_mm = 1.0 - max_precip_mm`.
- `sources_below_1mm = count(precip_source_mm < 1.0)`.
- `anchor_score = sum(...)` of exact whole-word or exact phrase counts for `phreatic`, `ash`, `ballistic`, `hikers`, `little warning`, and `unexpectedly` in the event narrative text.
- `reported_hikers` is the integer in the phrase `As many as N hikers`.
- `rain_gate = "fail_lt_1mm"` when `max_precip_mm < 1.0`; otherwise use `"pass_ge_1mm"`.
- `answer = "phreatic_report_dry_window"` when `max_precip_mm < 1.0`, `anchor_score >= 6`, and `reported_hikers > 0`; otherwise use `"rain_gate_or_anchor_check_not_met"`.

Return compact JSON:

```json
{
  "answer": "<short computed label>",
  "max_precip_mm": 0.0,
  "dry_margin_mm": 0.0,
  "sources_below_1mm": 0,
  "anchor_score": 0,
  "reported_hikers": 0,
  "rain_gate": "<gate state>",
  "consistency_note": "<one sentence tied to the calculations>"
}
```
