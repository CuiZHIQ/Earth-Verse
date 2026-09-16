# Wildfire-Smoke Threshold Ledger

A wildfire-smoke analysis team is checking a compact ledger for the July-August 2023 Greece wildfires. Reconstruct the locked event window, the dated narrative span around the smoke episode, three report-cue counts, and the peak satellite dNBR burn signal. Treat qualitative words such as "dozens" or "hundreds" as cue signals only; do not convert them into numeric loss or area totals.

Return only compact JSON with these fields:

```json
{
  "event_window": "YYYY-MM-DD/YYYY-MM-DD",
  "event_window_days": 0,
  "narrative_date_span": "YYYY-MM-DD/YYYY-MM-DD",
  "active_fire_cues": 0,
  "smoke_transport_cues": 0,
  "settlement_impact_cues": 0,
  "dnbr_max": 0.0,
  "final_label": "<label>"
}
```

Use inclusive day counting for `event_window_days`. For `narrative_date_span`, use the earliest and latest explicit calendar dates in the report narrative, inferring 2023 for undated August day mentions.

Count `active_fire_cues` from four tests: many new fires within 24 hours, other fires burning elsewhere, extreme fire weather, and hot/dry/windy conditions continuing on August 23.

Count `smoke_transport_cues` from five tests: Alexandroupolis origin, a smoke plume extending hundreds of miles toward Italy, satellite-observed plume evidence, smoke over the capital city, and smoke detected over Italy plus northern Africa.

Count `settlement_impact_cues` from four tests: fires near Athens, homes burned, cars burned, and smoke over the capital city.

Round `dnbr_max` to three decimals. Use `passes_smoke_burn_window_ledger` only if `active_fire_cues >= 3`, `smoke_transport_cues >= 4`, `settlement_impact_cues >= 2`, and `dnbr_max >= 0.660`. Otherwise use `does_not_pass_smoke_burn_window_ledger`.
