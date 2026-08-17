# Caldor Fire Damage-Window Ledger

For the 2021 Caldor Fire near South Lake Tahoe, build a compact numeric ledger that reconciles the incident-impact record with the fire-spread visualization window. Compute the destroyed-plus-damaged structure total, destruction share, confirmed-injury total, firefighter-injury share, elapsed incident-window days, elapsed 12-hour fire-line update intervals from the visualization span, and the days from the final visualization date to containment.

Apply this threshold model: major structure loss is true when affected structures are at least 1,000 and destruction share is at least 0.90; long progression record is true when active days are at least 60 and reconstructed 12-hour intervals are at least 100; responder-heavy injury record is true when confirmed injuries are at least 10 and firefighter share is at least 0.70; late containment tail is true when the post-visualization tail is at least 14 days.

Return compact JSON:

```json
{
  "answer": "<short diagnosis label>",
  "damage_ledger": {
    "structures_destroyed": 0,
    "structures_damaged": 0,
    "affected_structures": 0,
    "destruction_share": 0.0
  },
  "injury_ledger": {
    "civilian_injuries": 0,
    "firefighter_injuries": 0,
    "injury_total": 0,
    "firefighter_injury_share": 0.0
  },
  "window_reconstruction": {
    "event_window_days": 0,
    "active_days": 0,
    "progression_days": 0,
    "progression_intervals_12h": 0,
    "containment_tail_days": 0
  },
  "threshold_flags": {
    "major_structure_loss": false,
    "long_progression_record": false,
    "responder_heavy_injury_record": false,
    "late_containment_tail": false
  },
  "formula_check": ["<short arithmetic check>", "<short date check>"],
  "confidence": "<low|medium|high>"
}
```

Keep the result numeric and concise; keep the output to the ledger only.
