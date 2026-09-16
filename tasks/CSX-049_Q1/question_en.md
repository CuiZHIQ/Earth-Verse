# Hurricane Ida NYC Rainfall-Concentration and Urban Disruption Diagnosis

A hydrometeorology team is reconstructing the September 1-2, 2021 rainfall flooding associated with Hurricane Ida in New York City and the broader Northeast. The task is to diagnose whether the package evidence supports a short-window, spatially concentrated pluvial-flood mechanism with urban disruption, rather than a diffuse multi-day rainfall episode.

Use only the local CSX-049 event package. Select package-relative evidence for the event window, precipitation fields, and contemporaneous impact report signals.

Compute:

- `event_window_days`: inclusive event duration.
- `precip_max_mm`: maximum event precipitation from the three precipitation evidence streams, returned under the fixed keys `era5`, `gpm`, and `chirps`.
- `max_to_mean_ratios`: max-to-mean precipitation ratios for the same three streams.
- `satellite_max_disagreement_percent`: `abs(GPM_max - CHIRPS_max) / mean(GPM_max, CHIRPS_max) * 100`.
- `report_flag_count`: count of six urban-disruption flags from report evidence: road shutdowns, public transit disruption, flight cancellations, stranded cars, high-water rescues, and flash-flood emergency statements.
- `score_0_to_6`: one point each for a two-day window, ERA5 maximum at least 10 mm, both satellite maxima at least 18 mm, all three max-to-mean ratios at least 5, report flag count at least 5, and GPM-CHIRPS maximum disagreement at most 5%.
- `answer_label` and `computed_interpretation`.

Return only compact JSON:

```json
{
  "answer_label": "<label>",
  "event_window_days": 0,
  "precip_max_mm": {
    "era5": 0.0,
    "gpm": 0.0,
    "chirps": 0.0
  },
  "max_to_mean_ratios": {
    "era5": 0.0,
    "gpm": 0.0,
    "chirps": 0.0
  },
  "satellite_max_disagreement_percent": 0.0,
  "report_flag_count": 0,
  "score_0_to_6": 0,
  "computed_interpretation": "<one sentence>"
}
```

The interpretation should connect the short window, spatial concentration, cross-source agreement, and urban-disruption evidence into a pluvial-flood mechanism diagnosis.
