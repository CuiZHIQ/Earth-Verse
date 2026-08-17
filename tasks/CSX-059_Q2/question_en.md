# Urban Pluvial Overload and Response-Stress Reconstruction

Use only the local CSX-059 event package. Select package-relative evidence for every value you use.

Reconstruct the short-duration flood process for the New York City phase of post-tropical Cyclone Ida by combining the event narrative, gridded precipitation summaries, population exposure, and post-event surface-change summaries. Treat the problem as an urban pluvial-overload diagnosis: a record one-hour rainfall burst occurred inside a broader two-day rain shield, with a dense exposed population and only moderate mean remote-sensing surface change.

Compute the following quantities:

- `duration_days`: inclusive event-window length from the event anchor.
- `central_park_record_hour_mm`: convert the record one-hour Central Park rainfall from inches to millimeters.
- `regional_reference_mm`: convert the northern Mid-Atlantic "just above 10 inches" storm-total reference using a conservative lower-bound value of 10.0 inches.
- `max_gridded_precip_mm`: largest precipitation maximum among the event-window gridded precipitation summaries.
- `mean_gridded_event_mm`: arithmetic mean of the event-window precipitation means from the three gridded precipitation summaries.
- `hour_to_grid_peak_ratio = central_park_record_hour_mm / max_gridded_precip_mm`.
- `regional_to_grid_peak_ratio = regional_reference_mm / max_gridded_precip_mm`.
- `burst_to_areal_daily_ratio = central_park_record_hour_mm / (mean_gridded_event_mm / duration_days)`.
- `population_millions`: exposed population from the package population summary, in millions.
- `population_rain_load_million_person_mm = population_millions * mean_gridded_event_mm`.
- `surface_change_norm = mean(clip(radar_mean_db / 1.0, 0, 1), clip(annual_embedding_mean / 0.05, 0, 1))`.

Then compute an urban pluvial response-stress index:

```text
intensity_norm = clip(central_park_record_hour_mm / 100, 0, 1)
accumulation_norm = clip(max_gridded_precip_mm / 200, 0, 1)
concentration_norm = clip(hour_to_grid_peak_ratio / 0.75, 0, 1)
exposure_norm = clip(population_millions / 10, 0, 1)

urban_pluvial_response_stress =
100 * (0.35 * intensity_norm
     + 0.20 * accumulation_norm
     + 0.20 * concentration_norm
     + 0.15 * exposure_norm
     + 0.10 * surface_change_norm)
```

For a near-future stress test, recompute the index with:

- one-hour rainfall increased by 20%;
- gridded precipitation maxima increased by 10%;
- exposed population increased by 5%;
- the two remote-sensing mean-change values unchanged.

Round millimeter values to three decimals, ratios and normalized components to three decimals, population/load values to three decimals, and index values to one decimal.

Return compact JSON in this form:

```json
{
  "process_model": {
    "event_window": {
      "start_date": "",
      "end_date": "",
      "duration_days": 0
    },
    "rainfall_forcing": {
      "central_park_record_hour_mm": 0.0,
      "regional_reference_mm": 0.0,
      "max_gridded_precip_mm": 0.0,
      "mean_gridded_event_mm": 0.0,
      "hour_to_grid_peak_ratio": 0.0,
      "regional_to_grid_peak_ratio": 0.0,
      "burst_to_areal_daily_ratio": 0.0
    },
    "exposure_load": {
      "population_millions": 0.0,
      "population_rain_load_million_person_mm": 0.0
    },
    "surface_response": {
      "radar_mean_db": 0.0,
      "annual_embedding_mean": 0.0,
      "surface_change_norm": 0.0
    }
  },
  "scenario_analysis": {
    "baseline_index": 0.0,
    "future_short_burst_index": 0.0,
    "index_delta": 0.0,
    "baseline_components": {
      "intensity_norm": 0.0,
      "accumulation_norm": 0.0,
      "concentration_norm": 0.0,
      "exposure_norm": 0.0,
      "surface_change_norm": 0.0
    },
    "scenario_components": {
      "intensity_norm": 0.0,
      "accumulation_norm": 0.0,
      "concentration_norm": 0.0,
      "exposure_norm": 0.0,
      "surface_change_norm": 0.0
    }
  },
  "mechanism_chain": [
    "",
    "",
    ""
  ],
  "source_paths": [],
  "final_interpretation": ""
}
```

The mechanism chain should explain, in three concise clauses, how the record hourly burst, broader rain shield, population exposure, and remote-sensing context combine into the final interpretation.
