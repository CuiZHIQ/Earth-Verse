# Guinsaugon Rainfall Window Ledger

Use the local CSX-223 event package to rebuild a rainfall-window threshold ledger for the 17 February 2006 Guinsaugon landslide.

Use the Open-Meteo daily precipitation series as the first daily series and the NASA POWER `PRECTOTCORR` daily series as the second daily series. Set the event day to `2006-02-17`, the prior 14-day window to `2006-02-03` through `2006-02-16`, and the prior 7-day window to `2006-02-10` through `2006-02-16`.

For each daily series, compute prior-14-day precipitation, prior-7-day precipitation, event-day precipitation, and `prior14 / event_day`. Compute the event-day gridded mean precipitation values from ERA5-Land, GPM IMERG, and CHIRPS, then count how many of those three means are at or below `5 mm`.

Use these gates:

- `openmeteo_gate`: prior14 >= `100 mm`, event_day <= `5 mm`, and ratio >= `20`.
- `power_gate`: prior14 >= `300 mm`, event_day <= `10 mm`, and ratio >= `20`.
- `grid_consensus_gate`: at least two gridded event-day means are <= `5 mm`.

Return compact JSON:

```json
{
  "target_family": "guinsaugon_rainfall_window_threshold_ledger",
  "window": {
    "prior14": "YYYY-MM-DD..YYYY-MM-DD",
    "prior7": "YYYY-MM-DD..YYYY-MM-DD",
    "event_day": "YYYY-MM-DD"
  },
  "daily_metrics": {
    "openmeteo": {
      "prior14_mm": 0,
      "prior7_mm": 0,
      "event_day_mm": 0,
      "ratio_prior14_to_event": 0
    },
    "power": {
      "prior14_mm": 0,
      "prior7_mm": 0,
      "event_day_mm": 0,
      "ratio_prior14_to_event": 0
    }
  },
  "grid_means_mm": {
    "era5_land": 0,
    "gpm": 0,
    "chirps": 0,
    "le5_count": 0
  },
  "gates": {
    "openmeteo_gate": true,
    "power_gate": true,
    "grid_consensus_gate": true
  },
  "answer": "<antecedent_wetness_ledger_pass or antecedent_wetness_ledger_fail>",
  "formula_note": "<one short formula note>"
}
```
