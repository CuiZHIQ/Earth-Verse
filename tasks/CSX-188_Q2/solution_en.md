# Final Answer

```json
{
  "event_window": "2023-07-01/2023-08-31",
  "event_window_days": 62,
  "narrative_date_span": "2023-08-22/2023-08-23",
  "active_fire_cues": 4,
  "smoke_transport_cues": 5,
  "settlement_impact_cues": 4,
  "dnbr_max": 0.86,
  "final_label": "passes_smoke_burn_window_ledger"
}
```

# Key Computations

The locked event window runs from 2023-07-01 through 2023-08-31, so inclusive day counting gives 62 days. The report narrative has explicit dated anchors on August 22 and August 23, both in 2023.

The active-fire cue count is 4: many new fires within 24 hours, other fires burning elsewhere, extreme fire weather, and hot/dry/windy conditions continuing on August 23.

The smoke-transport cue count is 5: the Alexandroupolis origin, a plume extending hundreds of miles toward Italy, satellite-observed plume evidence, smoke over the capital city, and smoke detected over Italy plus northern Africa.

The settlement-impact cue count is 4: fires near Athens, homes burned, cars burned, and smoke over the capital city.

The satellite dNBR summary gives `sentinel2_dnbr_max = 0.8597047915007765`, which rounds to `dnbr_max = 0.86` at three decimals. The threshold checks are `4 >= 3`, `5 >= 4`, `4 >= 2`, and `0.8597047915007765 >= 0.660`.

# Reasoning Path

The ledger first fixes the time accounting: the July 1 to August 31 event span is 62 inclusive days, while the narrative smoke episode is bounded by August 22 and August 23. It then counts cue families rather than converting qualitative phrases into exact totals. All three report cue families meet their thresholds, and the peak dNBR metric exceeds the burn-signal threshold. Because all four tests pass, the deterministic label is `passes_smoke_burn_window_ledger`.

# Computed Interpretation

The computed ledger supports a compact smoke-plus-burn signal for the specified window: report cues are dense across active fire, smoke transport, and settlement-impact families, and the peak dNBR value clears the 0.660 threshold.

# Scoring Rubric

Total: 20 points.

- 3 points: Returned JSON shape includes exactly the requested eight fields with compact scalar values and the required `final_label`. Partial credit: minor key-order or rounding-format differences are acceptable, but missing required fields or using a non-JSON answer loses most credit.
- 4 points: Window reconstruction uses the 2023-07-01/2023-08-31 event window, computes 62 inclusive days, and extracts the 2023-08-22/2023-08-23 narrative date span. Partial credit: earns up to 2 points for one correct window and up to 1 point for using exclusive day counting.
- 5 points: Report cue counts are `active_fire_cues=4`, `smoke_transport_cues=5`, and `settlement_impact_cues=4`. Partial credit: about 1.5 points per correct cue family, with small credit for identifying the right family but missing one cue.
- 3 points: dNBR extraction reports the peak value as `dnbr_max=0.86` after rounding from 0.8597047915007765. Partial credit: earns 2 points for the right unrounded value with different presentation, or 1 point for using the dNBR mean instead of the peak.
- 3 points: Threshold arithmetic applies `active_fire_cues >= 3`, `smoke_transport_cues >= 4`, `settlement_impact_cues >= 2`, and `dnbr_max >= 0.660`. Partial credit: earns roughly 0.75 points per correctly evaluated threshold.
- 2 points: Final interpretation is concise and limited to the computed smoke-plus-burn ledger. Partial credit: earns 1 point if the label is right but the explanation converts qualitative report words into exact loss or area totals.
