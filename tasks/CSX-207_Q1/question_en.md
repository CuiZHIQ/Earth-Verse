# Fire-Weather, Smoke Transport, and Exposure Stress Model

Use only the local CSX-207 event package. Select package-relative evidence for every value family you use.

Build a coupled wildfire-smoke stress model for the August-September 2024 South America episode using the available package records. Treat daily weather as partial event-window coverage when the local package records do not span the full event window; do not infer missing daily values beyond the records present. Use the following definitions, with `clip(x) = min(1, max(0, x))`, haversine distance in kilometers, and all non-integer numeric outputs rounded to 6 decimals.

Return only a JSON object with this structure:

```json
{
  "process_model": {
    "event_window_days": 0,
    "weather_record_days": 0,
    "weather_coverage_fraction": 0.0,
    "aoi_area_km2": 0.0,
    "source_severity_component": 0.0,
    "hot_dry_wind_component": 0.0,
    "transport_exposure_component": 0.0,
    "baseline_stress_index": 0.0,
    "baseline_stress_class": ""
  },
  "computed_metrics": {
    "dnbr_peak_to_mean": 0.0,
    "annual_embedding_peak_to_mean_change": 0.0,
    "hot_diagnostic_mean_max_c": 0.0,
    "dry_day_fraction": 0.0,
    "mean_peak_wind_ms": 0.0,
    "rain_suppression_norm": 0.0,
    "population_person_days_million": 0.0,
    "critical_facility_count": 0,
    "nearest_brazil_wildfire_catalog_km": 0.0
  },
  "scenario_analysis": {
    "scenario": "",
    "scenario_hot_dry_wind_component": 0.0,
    "scenario_transport_exposure_component": 0.0,
    "scenario_stress_index": 0.0,
    "scenario_delta": 0.0,
    "scenario_stress_class": "",
    "worsening_flag": false
  },
  "mechanism_chain": [],
  "source_paths": [],
  "final_interpretation": ""
}
```

Compute the model as follows:

- `event_window_days`: inclusive event-window length from the event time information.
- `weather_record_days`: number of local daily-weather records inside that event window.
- `weather_coverage_fraction = weather_record_days / event_window_days`.
- `aoi_area_km2`: approximate the geospatial polygon as a rectangle using `lon_span * 111.32 * cos(abs(mid_lat))` for width and `lat_span * 111.32` for height.
- `source_severity_component = clip(0.55 * (dNBR_max / 0.9) + 0.30 * (dNBR_mean / 0.15) + 0.15 * (annual_embedding_change_mean / 0.06))`.
- `hot_dry_wind_component = clip(0.35 * heat_exceedance_norm + 0.35 * dry_day_fraction + 0.20 * wind_peak_norm + 0.10 * rain_suppression_norm)`, where:
  - `heat_exceedance_norm = clip((mean of the three maximum-temperature diagnostics - 35) / 7)`;
  - the three diagnostics are the available local daily maximum, the available NASA daily maximum, and the reanalysis maximum;
  - `dry_day_fraction` is the share of local daily-weather records inside the event window with precipitation at or below 0.5 mm;
  - `wind_peak_norm = clip(mean(local peak daily wind converted from km/h to m/s, NASA peak daily wind in m/s) / 10)`;
  - `rain_suppression_norm = clip(1 - max(available GPM mean accumulated precipitation, available CHIRPS mean accumulated precipitation) / 100)`.
- `transport_exposure_component = clip(0.35 * transport_process_text_fraction + 0.25 * person_day_norm + 0.20 * critical_facility_norm + 0.20 * catalog_proximity_norm)`, where:
  - `transport_process_text_fraction` is the share of these six terms found across the event narrative/report text: `wildfire`, `smoke`, `transport`, `air quality`, `PM2.5`, and `human health`; after lowercasing and stripping markup, count each term once if it appears at least once anywhere in the selected reports or locked event-anchor notes, not by repeated occurrences;
  - `person_day_norm = clip(population_sum * event_window_days / 2,000,000)`;
  - `critical_facility_norm = clip((hospitals + schools + police facilities + shelters in the broad exposure slice) / 60)`;
  - `catalog_proximity_norm = clip(1 - nearest Brazil wildfire catalog point distance from the AOI centroid / 1000)`.
- `baseline_stress_index = 100 * (0.40 * source_severity_component + 0.35 * hot_dry_wind_component + 0.25 * transport_exposure_component)`.

For the scenario, recompute the affected terms under: all three temperature diagnostics are 2 C warmer, gridded mean precipitation is 20% lower, both peak wind inputs are 15% higher, and exposed population is 10% higher. Keep source severity, dry-day fraction, narrative term fraction, critical facilities, and catalog proximity unchanged. Set `worsening_flag` to true when `scenario_delta >= 3` and the scenario index is at least 90.

Use stress classes: `extreme` for index >= 85, `severe` for index >= 70, `elevated` for index >= 50, and `moderate` otherwise.
