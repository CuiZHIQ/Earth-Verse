# Merapi Volcanic Rainfall and Lahar-Response Stress Model

Using only the local CSX-307 event package, build a disaster-process model for the October-November 2010 Merapi eruption that connects eruptive activity, event-window rainfall, exposed population, mapped response assets, and the absence or presence of direct pre/post remote-sensing support.

In your final answer, cite package-relative evidence for every value you use.

Compute the following from the package:

- `event_days`: inclusive days from the event start date through the event end date.
- `hazard_process_terms`: booleans for whether the event narrative supports `pyroclastic_flows`, `ashfall`, and `lahar_risk`.
- `hazard_process_completeness`: number of supported hazard-process terms divided by `3`.
- `rain_mean_mm`: mean of the three event-window accumulated precipitation mean values from the gridded/model precipitation summaries.
- `rain_peak_mean_mm`: mean of the three event-window accumulated precipitation maximum values from the same summaries.
- `rain_concentration_ratio`: `rain_peak_mean_mm / rain_mean_mm`.
- `rain_spatial_spread_mm`: maximum of the three precipitation maxima minus minimum of the three precipitation maxima.
- `aoi_area_km2`: area of the package AOI polygon in square kilometers. For the rectangular latitude-longitude AOI, use spherical area with Earth radius `6371.0088 km`: `R^2 * delta_lon_radians * (sin(lat_north) - sin(lat_south))`.
- `population_m`: total population divided by `1,000,000`.
- `population_density_per_km2`: total population divided by `aoi_area_km2`.
- `amenity_total`: count of mapped features carrying an `amenity` tag.
- `critical_response_facilities`: count of mapped amenity-tagged hospitals, shelters, police facilities, and fire stations.
- `school_count`: count of mapped amenity-tagged schools.
- `formal_pre_post_scene_count`: total available pre and post counts across the package's formal radar and optical pre/post change summaries.
- `direct_footprint_gap`: `1` when `formal_pre_post_scene_count` is `0`, otherwise `0`.

Normalize components as follows, clipping each normalized input to `[0, 1]`:

```text
duration_norm = min(event_days / 45, 1)
volcanic_trigger_norm =
  0.60 * hazard_process_completeness
+ 0.40 * duration_norm

rain_load_norm = min(rain_mean_mm / 450, 1)
rain_concentration_norm = min(rain_concentration_ratio / 1.6, 1)
rain_spread_norm = min(rain_spatial_spread_mm / 220, 1)
rain_lahar_conditioning_norm =
  0.50 * rain_load_norm
+ 0.30 * rain_concentration_norm
+ 0.20 * rain_spread_norm

population_norm = min(population_m / 12, 1)
critical_facility_norm = min(critical_response_facilities / 100, 1)
school_norm = min(school_count / 250, 1)
amenity_norm = min(amenity_total / 300, 1)
exposure_response_norm =
  0.45 * population_norm
+ 0.25 * critical_facility_norm
+ 0.20 * school_norm
+ 0.10 * amenity_norm

monitoring_gap_norm = direct_footprint_gap

lahar_response_stress_index =
  100 * (
    0.34 * volcanic_trigger_norm
  + 0.31 * rain_lahar_conditioning_norm
  + 0.25 * exposure_response_norm
  + 0.10 * monitoring_gap_norm
  )
```

Then compute a warmer-wetter remobilization scenario in which `rain_mean_mm`, `rain_peak_mean_mm`, and `rain_spatial_spread_mm` each increase by `15%`, while the hazard-process, exposure, and monitoring terms stay unchanged. Recompute the rainfall conditioning component and final index, and report `index_delta`.

Assign `response_priority` from the baseline `lahar_response_stress_index` using this visible mapping: `< 40` = `lower_lahar_response_pressure`, `40` to `< 60` = `moderate_lahar_response_pressure`, `60` to `< 75` = `high_lahar_response_pressure`, and `>= 75` = `very_high_lahar_response_pressure`.

Round index and normalized component values to `3` decimals. Round area, density, precipitation, and population metrics to `3` decimals. Return only JSON with this shape:

```json
{
  "process_model": "merapi_2010_volcanic_rainfall_lahar_response_stress",
  "source_paths": {
    "event_window_and_process": [],
    "precipitation": [],
    "geospatial_context": [],
    "exposure_and_response_assets": [],
    "remote_sensing_support": []
  },
  "computed_metrics": {
    "event_days": 0,
    "hazard_process_terms": {
      "pyroclastic_flows": false,
      "ashfall": false,
      "lahar_risk": false
    },
    "hazard_process_completeness": 0.0,
    "rain_mean_mm": 0.0,
    "rain_peak_mean_mm": 0.0,
    "rain_concentration_ratio": 0.0,
    "rain_spatial_spread_mm": 0.0,
    "aoi_area_km2": 0.0,
    "population_m": 0.0,
    "population_density_per_km2": 0.0,
    "amenity_total": 0,
    "critical_response_facilities": 0,
    "school_count": 0,
    "formal_pre_post_scene_count": 0,
    "direct_footprint_gap": 0
  },
  "normalized_components": {
    "volcanic_trigger_norm": 0.0,
    "rain_lahar_conditioning_norm": 0.0,
    "exposure_response_norm": 0.0,
    "monitoring_gap_norm": 0.0
  },
  "scenario_analysis": {
    "warmer_wetter_remobilization": {
      "rain_mean_mm": 0.0,
      "rain_peak_mean_mm": 0.0,
      "rain_concentration_ratio": 0.0,
      "rain_spatial_spread_mm": 0.0,
      "rain_lahar_conditioning_norm": 0.0,
      "lahar_response_stress_index": 0.0,
      "index_delta": 0.0
    }
  },
  "lahar_response_stress_index": 0.0,
  "response_priority": "",
  "final_interpretation": ""
}
```
