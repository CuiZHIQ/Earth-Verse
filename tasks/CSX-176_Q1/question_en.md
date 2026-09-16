# Greece Wildfires Late-August Phase Ledger

A wildfire-smoke analyst is reviewing the July-August 2023 Greece wildfire sequence and needs a compact phase code for the renewed late-August activity. The record includes event-description text and satellite-observation notes, but the final answer should stay focused on extracted anchors rather than broad impact commentary.

Decide which late-August code is best supported:

- `late_august_active_fire_smoke_phase`
- `annual_burned_area_context`
- `athens_only_local_fire_phase`

Build a small score ledger from the incident record:

- `late_august_active_fire_smoke`: count 1 point each for late-August fires igniting within 24 hours, a plume from the Alexandroupolis area toward Italy, the satellite observation date, next-day hot/dry/windy fire-weather continuation, and smoke observed over Italy plus northern Africa.
- `annual_burned_area_context`: count 1 point only if the record gives an annual burned-area comparison.
- `athens_only_local_fire`: count 1 point only if the record gives Athens-specific homes/cars/smoke impacts.

Return compact JSON with:

```json
{
  "canonical_label": "...",
  "date_ledger": {
    "image_date": "YYYY-MM-DD",
    "weather_smoke_context_date": "YYYY-MM-DD"
  },
  "score_ledger": {
    "late_august_active_fire_smoke": 0,
    "annual_burned_area_context": 0,
    "athens_only_local_fire": 0
  },
  "anchor_ledger": ["..."],
  "rationale": "one sentence"
}
```
