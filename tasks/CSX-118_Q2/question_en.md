# Cyclone Wind-Pressure Exposure and Response-Priority Model

Ex-Hurricane Ophelia affected Ireland on 15-16 October 2017 with a fast-evolving post-tropical wind field, a rapid pressure change, and widespread tree, power, and road disruption. Build a disaster-process model that explains whether the local package evidence supports wind-pressure disruption as the dominant operational problem, and how response attention should be divided between power/tree clearance, road access, and pluvial flooding.

Use only the local CSX-118 event package. Select package-relative evidence for every source value and qualitative process claim used in the final JSON.

Compute the following quantities:

1. Event-window and hazard timing: local hourly peak gust, minimum pressure, peak-gust to minimum-pressure lag, pressure fall from the maximum pressure during the first event day to the minimum pressure during the second event day, total precipitation, and maximum hourly precipitation.
2. Report-derived wind and impact anchors: convert station gusts from knots to km/h using `1 kt = 1.852 km/h`; extract the Dublin station gust, the maximum Ireland station gust, customers without power, extratropical deaths, and whether the report connects impacts to trees or power lines and to road disruption.
3. Persistence and rainfall contrasts: count event hours with gusts at or above `70 km/h` and `90 km/h`; compute gridded precipitation context from available package summaries.
4. Exposure and context: compute package exposure load from population, transport receptors, and critical-service receptors. Count transport receptors as features with `highway`, `railway`, or `public_transport` tags. Count critical-service receptors as features tagged as shelter, school, hospital, police, or fire station. Treat these as exposure, not measured damage. Use available radar/remote-sensing change summaries as context only, not as direct damage attribution.
5. Baseline process index:

```text
wind_kinetic_norm = min((peak_gust_kmh / 120)^2, 1.5)
pressure_fall_norm = min(pressure_fall_24h_hpa / 30, 1)
gust_persistence_norm =
  0.5 * min((hours_gust_ge_70 / event_hours) / 0.35, 1)
  + 0.5 * min((hours_gust_ge_90 / event_hours) / 0.15, 1)
population_norm = min(population / 1000000, 1)
transport_norm = min(transport_receptors / 75, 1)
critical_service_norm = min(critical_service_receptors / 1000, 1)
exposure_load_norm =
  0.55 * population_norm + 0.25 * transport_norm + 0.20 * critical_service_norm
impact_alignment_norm =
  0.55 * min(customers_without_power / 360000, 1)
  + 0.25 * min(extratropical_deaths / 3, 1)
  + 0.20 * impact_flags
wind_pressure_disruption_index =
  100 * (0.30 * wind_kinetic_norm
       + 0.20 * pressure_fall_norm
       + 0.20 * gust_persistence_norm
       + 0.15 * exposure_load_norm
       + 0.15 * impact_alignment_norm)
```

`impact_flags` is `1` only when both tree/power-line disruption and road disruption are supported by the report; otherwise use `0`.

6. Response priorities:

```text
power_tree_priority =
  100 * (0.35 * wind_kinetic_norm
       + 0.20 * pressure_fall_norm
       + 0.25 * impact_alignment_norm
       + 0.20 * exposure_load_norm)

road_access_priority =
  100 * (0.35 * gust_persistence_norm
       + 0.25 * wind_kinetic_norm
       + 0.20 * transport_norm
       + 0.20 * road_disruption_flag)

rainfall_point_norm =
  0.5 * min(total_precip_mm / 25, 1)
  + 0.5 * min(max_hourly_precip_mm / 5, 1)

gpm_precip_norm =
  0.5 * min(gpm_event_precip_mm_max / 10, 1)
  + 0.5 * min(gpm_event_precip_mm_mean / 5, 1)

era5_precip_norm = min(era5_precipitation_sum_mm_max / 10, 1)

pluvial_priority =
  100 * (0.55 * rainfall_point_norm
       + 0.25 * gpm_precip_norm
       + 0.20 * era5_precip_norm)
```

7. Windier-track scenario: multiply every hourly gust by `1.15`, multiply the pressure fall by `1.10`, then recompute peak gust, threshold-hour counts, the three affected normalized terms, and the wind-pressure disruption index while holding exposure and reported impacts fixed.

Return compact JSON with this structure:

```json
{
  "source_paths": [],
  "process_model": {
    "event_window": {},
    "mechanism_chain": [],
    "baseline_index": {}
  },
  "computed_metrics": {
    "hazard_timing": {},
    "wind_report_anchors": {},
    "rainfall_context": {},
    "exposure_context": {},
    "remote_sensing_context": {}
  },
  "response_priorities": [],
  "scenario_analysis": {},
  "final_interpretation": ""
}
```

Round index values and normalized terms to three decimals, physical measurements to one decimal where appropriate, and shares to three decimals. The final interpretation should be one concise sentence grounded in the computed values.
