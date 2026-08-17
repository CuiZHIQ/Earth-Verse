# Ida NYC Station-Hour/Grid Contrast Diagnostic

A hydrometeorology analyst is checking the September 1-2, 2021 Hurricane Ida rainfall-flooding record for New York City. The review question is whether the Central Park record-hour rainfall remains the dominant threshold signal after it is compared with the regional storm-total reference and the gridded event-accumulation summaries.

Return JSON only. Use the technical record to recover the station-hour inches, local time span, the regional "just above 10 inches" storm-total reference as a conservative lower-bound value of 10.0 inches, and the three gridded precipitation summaries. Then compute:

- `station_hour_mm = station_hour_in * 25.4`
- `regional_share_pct = station_hour_in / regional_reference_in * 100`
- `grid_max_over_hour = event_accumulation_max_mm / station_hour_mm`
- `grid_max_over_mean = event_accumulation_max_mm / event_accumulation_mean_mm`
- `below_quarter_count`, the number of gridded summaries with `grid_max_over_hour < 0.25`

Use this exact output shape:

```json
{
  "answer": {
    "station_hour_local": "<YYYY-MM-DD time span>",
    "station_hour_mm": 0.0,
    "regional_share_pct": 0.0,
    "grid_max_over_hour": {
      "<product_label>": 0.0
    },
    "grid_max_over_mean": {
      "<product_label>": 0.0
    },
    "below_quarter_count": 0,
    "label": "<record_hour_dominant_grid_below_quarter | grid_supports_record_hour>"
  },
  "interpretation": "<one calculation-tied sentence>"
}
```

Use `record_hour_dominant_grid_below_quarter` when all three gridded maxima are below one quarter of the station-hour depth; otherwise use `grid_supports_record_hour`.
