# Final Answer

Canonical answer label: `major_structure_loss_with_long_progression_record`.

Expected compact JSON:

```json
{
  "answer": "major_structure_loss_with_long_progression_record",
  "damage_ledger": {
    "structures_destroyed": 1005,
    "structures_damaged": 81,
    "affected_structures": 1086,
    "destruction_share": 0.925
  },
  "injury_ledger": {
    "civilian_injuries": 5,
    "firefighter_injuries": 16,
    "injury_total": 21,
    "firefighter_injury_share": 0.762
  },
  "window_reconstruction": {
    "event_window_days": 68,
    "active_days": 68,
    "progression_days": 52,
    "progression_intervals_12h": 104,
    "containment_tail_days": 15
  },
  "threshold_flags": {
    "major_structure_loss": true,
    "long_progression_record": true,
    "responder_heavy_injury_record": true,
    "late_containment_tail": true
  },
  "formula_check": [
    "1005+81=1086; 1005/1086=0.925; 5+16=21; 16/21=0.762",
    "2021-08-14 to 2021-10-21 is 68 elapsed days; 2021-08-15 to 2021-10-06 is 52 days, or 104 12-hour intervals; tail to containment is 15 days"
  ],
  "confidence": "high"
}
```

# Key Computations

The hidden computation uses these package records:

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_anchor_report_NASA_Scientific_Visualization_Studio.html`
- `data/event_reports/event_reports_003_event_package.json_source_plan.locked_event_anchor.evidence_url.html`
- `data/event_reports/event_reports_005_Locked_event_anchor_2021_Caldor_Fire_near_South_Lake_Tahoe.json`

The incident-impact ledger is arithmetic:

- Affected structures: 1,005 destroyed + 81 damaged = 1,086.
- Destruction share: 1,005 / 1,086 = 0.925.
- Confirmed injuries: 5 civilian + 16 firefighter = 21.
- Firefighter injury share: 16 / 21 = 0.762.

The time ledger is date math:

- Locked event window: 2021-08-14 to 2021-10-21 = 68 elapsed days.
- CAL FIRE active-duration field: 68 active days, matching the elapsed window.
- NASA spread visualization span: 2021-08-15 to 2021-10-06 = 52 elapsed days.
- At one update every 12 hours, 52 days x 24 / 12 = 104 update intervals.
- Date from the final visualization day to containment: 2021-10-21 minus 2021-10-06 = 15 days.

# Reasoning Path

The threshold ledger has four true flags. Major structure loss is true because 1,086 affected structures is above 1,000 and the destruction share is above 0.90. Long progression record is true because the active-duration value is 68 days and the reconstructed 12-hour interval count is 104. The injury record is responder-heavy because total confirmed injuries are above 10 and 16 of 21 injuries are firefighter injuries. The late-tail flag is true because the containment tail after the final visualization date is 15 days.

The final label follows directly from the two primary numeric gates in the prompt: major structure loss and long progression record are both true. The other two true flags are supporting ledger results, not extra loss estimates.

# Computed Interpretation

This is a numeric consistency task for a wildfire incident record. The answer should stay inside the computed ledger: structures, injuries, elapsed days, update intervals, and threshold flags. It should not infer deaths, exact economic loss, damaged roads, shelter totals, or a new spread period after the final visualization date.

# Scoring Rubric

Total: 20 points.

- 3 points: final numeric diagnosis. Gives `major_structure_loss_with_long_progression_record` or an equivalent label that states major structure loss with a long progression record. Partial credit: 1-2 points for the correct direction with a missing or imprecise label.
- 4 points: structure ledger. Reports 1,005 destroyed, 81 damaged, 1,086 affected structures, and destruction share about 0.925. Partial credit: 1 point for each correct destroyed/damaged/affected/share component.
- 3 points: injury ledger. Reports 5 civilian injuries, 16 firefighter injuries, 21 total confirmed injuries, and firefighter share about 0.762. Partial credit: 1-2 points for correct injury totals with one missing share or category.
- 4 points: window reconstruction. Reconstructs 68 elapsed event-window days, 52 visualization-span days, 104 12-hour intervals, and a 15-day tail to containment. Partial credit: 1 point for each correct date or interval component.
- 3 points: threshold ledger. Sets all four threshold flags to true using the stated cutoffs and the computed values. Partial credit: 1-2 points for mostly correct flags with one cutoff or arithmetic error.
- 2 points: formula consistency. Shows enough arithmetic or date math to make the totals, shares, intervals, and tail reproducible. Partial credit: 1 point for showing either the arithmetic checks or the date checks.
- 1 point: compact structured output. Returns concise JSON with the requested ledger fields and stays within the computed values. Partial credit: 0.5 points for minor formatting issues that leave the ledger gradable.
