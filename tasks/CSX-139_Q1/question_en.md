# Storm Ciaran Rapid Deepening, Wind-Rain, and Exposure-Load Process Model

Storm Ciaran crossed the North Atlantic into western Europe in late October and early November 2023. Use only the local CSX-139 event package to reconstruct how the storm's rapid deepening, damaging wind field, rainfall footprint, and package AOI exposure combine into an operational response signal.

Select package-relative evidence for every source used in your final JSON.

Compute the following values and model components:

- Event window and broad location from the package narrative/anchor material.
- Maximum 24-hour sea-level pressure fall, its start and end times, minimum sea-level pressure and time, peak 10 m gust and time, hours with gusts at or above 70 km/h, hours with gusts at or above 80 km/h, event precipitation total, and the largest UTC-day precipitation total reconstructed from the hourly record.
- Gridded precipitation context from at least three gridded or aggregate precipitation products: event mean and maximum where available.
- AOI area in km2 from the package polygon using `R = 6371.0088 km` and `area = R^2 * radians(lon_span) * (sin(lat_max) - sin(lat_min))`; then compute population density, critical-facility count, critical-facility density per 1000 km2, and major transport feature count. Count critical facilities as OSM features tagged `school`, `hospital`, `police`, or `fire_station`; count major transport features as OSM highways tagged `trunk`, `secondary`, or `tertiary`.
- A remote-context term from the available annual embedding change statistics.

Use `clip01(x) = min(1, max(0, x))` and compute:

```text
cyclogenesis_norm = clip01(max_24h_pressure_drop_hpa / 30)

gust_energy_ge_70 = sum((gust_kmh / 70)^2 for each hourly gust >= 70 km/h)
wind_impulse_norm =
  average(
    clip01(peak_gust_kmh / 100),
    clip01(gust_hours_ge_70 / 18),
    clip01(gust_energy_ge_70 / 16)
  )

rainfall_spread_norm =
  average(
    clip01(hourly_event_rain_total_mm / 50),
    clip01(hourly_peak_utc_day_rain_mm / 25),
    clip01(gridded_product_1_mean_mm / 20),
    clip01(gridded_product_1_max_mm / 75),
    clip01(gridded_product_2_mean_mm / 20),
    clip01(gridded_product_2_max_mm / 40),
    clip01(gridded_product_3_mean_mm / 10),
    clip01(gridded_product_3_max_mm / 25)
  )

exposure_load_norm =
  average(
    clip01(population_density_per_km2 / 250),
    clip01(critical_facility_density_per_1000km2 / 15),
    clip01(major_transport_feature_count / 120)
  )

remote_context_norm =
  average(
    clip01(embedding_change_mean / 0.03),
    clip01(embedding_change_stdDev / 0.015),
    clip01(embedding_change_max / 0.5)
  )

baseline_compound_index =
  100 * (0.35 * cyclogenesis_norm
       + 0.25 * wind_impulse_norm
       + 0.20 * rainfall_spread_norm
       + 0.15 * exposure_load_norm
       + 0.05 * remote_context_norm)

response_priority_score =
  100 * (0.45 * wind_impulse_norm
       + 0.25 * exposure_load_norm
       + 0.20 * rainfall_spread_norm
       + 0.10 * cyclogenesis_norm)
```

Then run a counterfactual stress scenario: increase every hourly gust by 10%, increase every rainfall input used in `rainfall_spread_norm` by 20%, and increase population by 15%; leave pressure deepening, OSM counts, AOI area, and remote context unchanged. Recompute the wind, rainfall, exposure, compound-index, and response-priority terms. Classify the baseline process as `wind_dominant_compound_storm` when `cyclogenesis_norm >= 0.80`, `wind_impulse_norm >= 0.70`, and `rainfall_spread_norm < 0.70`; otherwise classify it as `mixed_compound_storm`. Classify response tier as `high` when `response_priority_score >= 75`, `elevated` when it is at least 60, and `moderate` otherwise.

Return valid JSON with these top-level keys:

```json
{
  "source_paths": {},
  "computed_metrics": {},
  "process_model": {},
  "scenario_analysis": {},
  "response_priorities": {},
  "mechanism_chain": [],
  "final_interpretation": ""
}
```

Round index and normalized values to three decimals, physical hazard values to one decimal where appropriate, AOI area to one decimal km2, population and density to one decimal, and counts as integers.
