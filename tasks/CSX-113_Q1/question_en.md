# Tropical Cyclone Freddy Late-Phase Segmentation

You are an event-timeline analyst reconstructing Tropical Cyclone Freddy's February-March 2023 chronology from the southwest Indian Ocean into southern Africa. The task is to decide whether the final Malawi rainfall episode is a distinct late concentration phase within the long-lived event.

Use only the local CSX-113 event package. Select package-relative evidence for the event chronology, local precipitation timing, and Malawi flood-entry timing.

Segment the event into:

- long-duration cyclone chronology;
- full-period local rainfall accumulation;
- final three-day Malawi rainfall concentration;
- lag from the wettest final-window day to the Malawi flood entry.

Compute:

- `duration_days`: full event duration;
- `event_rain_mm`: total local event-period precipitation from 2023-02-04 through 2023-03-14;
- `late_3day_mm`: rainfall from 2023-03-12 through 2023-03-14;
- `late_share_pct`: `100 * late_3day_mm / event_rain_mm`;
- `lag_hours`: hours between the start of the wettest day in the final window and the Malawi flood entry;
- `status`: `pass` only when `late_3day_mm >= 100`, `late_share_pct >= 25`, and `lag_hours <= 48`.

Return one compact JSON object:

```json
{
  "phases": [
    {"phase": "long_duration_chronology", "time_window": "", "computed_values": {}, "phase_role": ""},
    {"phase": "full_period_rain_accumulation", "time_window": "", "computed_values": {}, "phase_role": ""},
    {"phase": "late_malawi_concentration", "time_window": "", "computed_values": {}, "phase_role": ""},
    {"phase": "flood_entry_lag_alignment", "time_window": "", "computed_values": {}, "phase_role": ""}
  ],
  "duration_days": 0,
  "event_rain_mm": 0.0,
  "late_3day_mm": 0.0,
  "late_share_pct": 0.0,
  "lag_hours": 0.0,
  "status": "pass|fail",
  "interpretation": "<one sentence>"
}
```

The interpretation should explain whether the Malawi episode is a distinct late-phase concentration in the event timeline, using the computed rainfall share and lag rather than broad chronology alone.
