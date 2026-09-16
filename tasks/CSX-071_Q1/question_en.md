# Ida NYC Rainfall-Scale Diagnostic

A hydrometeorology review team is checking the September 1-2, 2021 Post-Tropical Cyclone Ida flood diagnosis for New York City. The decision is whether the quantitative record supports a short-duration urban rainfall-burst diagnosis, using the Central Park one-hour record and broader event-accumulation summaries.

Return a compact JSON object with:

```json
{
  "central_park_hour_mm_per_h": <number>,
  "regional_peak_lower_bound_mm": <number>,
  "central_hour_to_regional_ratio": <number>,
  "gridded": {
    "era5_land": {
      "max_to_mean_ratio": <number>,
      "central_hour_to_grid_max_ratio": <number>
    },
    "gpm_imerg": {
      "max_to_mean_ratio": <number>,
      "central_hour_to_grid_max_ratio": <number>
    },
    "chirps": {
      "max_to_mean_ratio": <number>,
      "central_hour_to_grid_max_ratio": <number>
    }
  },
  "final_label": "<one short label>",
  "interpretation": "<one sentence tied to the computed values>"
}
```

Use millimeters for precipitation. Treat the report phrase that regional amounts peaked just above 10 inches as a conservative lower-bound input of 10 inches for `regional_peak_lower_bound_mm`. Round ratios to three decimals, and keep the conclusion tied to the conversions and scale ratios rather than to the storm name alone.
