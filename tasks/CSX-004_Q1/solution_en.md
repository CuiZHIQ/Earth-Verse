# Final Answer

```json
{
  "answer_type": "expert_source_arbitration",
  "decision": "select_regional_aoi_heat_not_point_series",
  "selected_source": {
    "path": "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
    "role": "regional_aoi_temperature_severity",
    "dataset": "ECMWF/ERA5_LAND/HOURLY",
    "coverage_days_inclusive": 46
  },
  "rejected_point_source": {
    "path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "role": "single_high_elevation_point_weather",
    "point_inside_aoi": false,
    "point_elevation_m": 1606.0,
    "point_coverage_days_inclusive": 61,
    "rejection_reason": "full-window coverage does not overcome wrong spatial scale: the point is outside the compact AOI and much cooler than the regional AOI maximum"
  },
  "spatial_check": {
    "aoi_path": "data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json",
    "point_lat": 34.059753,
    "point_lon": 74.8125,
    "aoi_bounds": {
      "min_lon": 78.4,
      "min_lat": 19.9,
      "max_lon": 79.6,
      "max_lat": 21.1
    },
    "distance_point_to_aoi_centroid_km": 1563.074392
  },
  "numeric_consequence": {
    "selected_tmax_max_c": 46.246698,
    "selected_tmax_mean_c": 45.118824,
    "wrong_point_apparent_max_c": 29.8,
    "wrong_point_air_tmax_max_c": 27.9,
    "selected_minus_point_apparent_c": 16.446698,
    "selected_minus_point_air_tmax_c": 18.346698
  },
  "event_window_check": {
    "anchor_path": "data/event_reports/event_reports_005_Locked_event_anchor_2015_India-Pakistan_heat_wave.json",
    "official_window_days_inclusive": 61,
    "selected_hazard_window_days_inclusive": 46,
    "temporal_arbitration_note": "use the regional AOI hazard aggregate for the available heat-severity slice; the point file covers more days but is spatially non-interchangeable"
  },
  "wrong_variable_rejections": {
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json": "precipitation accumulation, not maximum-temperature heat severity",
    "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json": "precipitation accumulation, not maximum-temperature heat severity",
    "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json": "burn-index product with no sufficient scenes, not heat-wave temperature evidence"
  },
  "minimal_evidence_set": [
    "data/event_reports/event_reports_005_Locked_event_anchor_2015_India-Pakistan_heat_wave.json",
    "data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json",
    "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
  ],
  "ruling": "not_interchangeable",
  "reference_trace": [
    "Read the locked event anchor to get the official 2015-05-01 to 2015-06-30 regional event window.",
    "Read the compact AOI polygon and test whether the Open-Meteo point lies inside its bounds.",
    "Read the ERA5-Land aggregate Tmax fields and select them as the regional AOI heat-severity basis.",
    "Read the Open-Meteo daily point maxima and compute the temperature deltas from the selected regional maximum.",
    "Reject precipitation and dNBR files because they do not provide maximum-temperature heat-severity evidence."
  ]
}
```

# Evidence And Calculations

The locked anchor file sets the event as the 2015 India-Pakistan heat wave with a 2015-05-01 to 2015-06-30 official window, or 61 inclusive days.

The compact AOI file gives bounds of lon 78.4 to 79.6 and lat 19.9 to 21.1. The Open-Meteo point is at lat 34.059753, lon 74.8125, elevation 1606.0 m, so it is outside that AOI. The haversine distance from the point to the AOI centroid at lat 20.5, lon 79.0 is 1563.074392 km.

The selected regional heat source is `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`, with dataset `ECMWF/ERA5_LAND/HOURLY`, start 2015-05-01, end 2015-06-15, and 46 inclusive coverage days. Its `stats.temperature_2m_max_c_max` is 46.2466979980469 C and `stats.temperature_2m_max_c_mean` is 45.11882448571625 C.

The rejected point source is `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`. It covers 61 daily records and has `daily.apparent_temperature_max` maximum 29.8 C and `daily.temperature_2m_max` maximum 27.9 C. Source-swap impacts:

- Regional max minus point apparent max: 46.2466979980469 - 29.8 = 16.446697998046897 C.
- Regional max minus point air Tmax max: 46.2466979980469 - 27.9 = 18.3466979980469 C.

The GPM and CHIRPS files are precipitation accumulations, and the Sentinel-2 dNBR file reports no sufficient scenes. They are therefore wrong-variable or insufficient alternatives for a maximum-temperature heat-severity answer.

# Reference Solving Trace

1. Inspect package metadata to find event, AOI, physical hazard, precipitation, and dNBR candidates.
2. Use the locked anchor for the official event window and regional event scope.
3. Use the AOI geometry to test the point source spatially.
4. Select the regional ERA5-Land aggregate as the heat-severity basis and compute its inclusive coverage.
5. Compute point-source maxima and deltas to expose the source-swap failure.
6. Return the fixed JSON schema and mark the sources `not_interchangeable`.

# Rubric

- 4 points: Returns the exact JSON schema with `answer_type` set to `expert_source_arbitration` and the decision/ruling matching the source arbitration.
- 4 points: Selects `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json` as the regional AOI heat source with dataset and 46 inclusive coverage days.
- 4 points: Rejects the Open-Meteo point source using both spatial evidence and numeric consequences, including outside-AOI status, 1606.0 m elevation, 61 point days, and the two temperature deltas.
- 3 points: Computes the AOI bounds and point-to-centroid distance correctly from package-local coordinates.
- 2 points: Uses the locked anchor window correctly and explains why full point-window coverage does not override spatial mismatch.
- 2 points: Rejects precipitation and dNBR files as wrong-variable or insufficient alternatives.
- 1 point: Provides a concise reproducible reference trace and does not add external evidence, hidden answers, or broad disaster explanation.
