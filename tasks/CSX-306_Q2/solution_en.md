# Correct Answer

```json
{
  "answer": "research_supported_volcanic_ash_source_with_temporal_validation_gap",
  "causal_synthesis": [
    "The strongest causal claim is a source-proximal volcanic ash observation because the NASA report directly supports plume, place, instrument, and remote observation context.",
    "The 22-day mismatch prevents a clean same-day package-anchor claim and raises validation need, but it does not create a rainfall mechanism.",
    "Rainfall/weather displacement is rejected because only one of four rain/change gates passes and point rainfall is modest relative to the threshold.",
    "Surface-change reconnaissance is unsupported because both radar and optical pre/post scene counts are zero.",
    "Regional population and OSM statistics define receptor context only; they cannot override the report statement that the volcanic source island is remote and uninhabited."
  ],
  "computed_evidence": {
    "aoi_area_km2": 72059.93,
    "bounded_aoi_amenity_elements": 1000,
    "change_counts": {
      "optical_post_count": 0,
      "optical_pre_count": 0,
      "radar_post_count": 0,
      "radar_pre_count": 0
    },
    "change_scene_total": 0,
    "date_offset_days": 22,
    "locked_anchor_date": "2010-09-03",
    "peak_to_point_ratio": 13.528,
    "point_precip_inputs_mm": {
      "nasa_power_mm": 13.99,
      "open_meteo_mm": 13.3
    },
    "point_precip_mean_mm": 13.645,
    "population": 9346857,
    "population_density_per_km2": 129.709,
    "rain_change_gate_score": 1,
    "regional_mean_precip_mm": 17.825,
    "regional_peak_inputs_mm": {
      "chirps_mm": 39.192,
      "era5_land_mm": 64.043,
      "gpm_imerg_mm": 184.585
    },
    "regional_peak_precip_mm": 184.585,
    "report_acquisition_date": "2010-09-25",
    "report_support_count": 4,
    "small_slice_road_elements": 276
  },
  "confidence_model": {
    "change_observability_score": 0.0,
    "date_alignment_score": 0.267,
    "exposure_context_score": 0.999,
    "rain_context_score": 0.25,
    "report_support_fraction": 1.0,
    "source_mechanism_confidence": 0.84,
    "temporal_conflict_severity": 0.733,
    "validation_need_score": 0.867
  },
  "final_research_conclusion": "The package supports a research-grade volcanic ash source-observation conclusion with a high validation need caused by the 22-day temporal anchor mismatch; rainfall, absent surface-change scenes, and regional exposure context are insufficient to replace the ash-plume mechanism.",
  "rain_gate_tests": {
    "change_scene_available": false,
    "date_offset_le3days": false,
    "point_mean_ge25mm": false,
    "regional_peak_ge100mm": true
  },
  "research_hypotheses": {
    "H1_volcanic_source_observation": "supported",
    "H2_rainfall_weather_displacement": "rejected_as_primary",
    "H3_surface_change_reconnaissance": "unsupported_by_available_scenes",
    "H4_regional_exposure_primary_response": "context_only"
  },
  "scenario_sensitivity": {
    "rainfall_displacement_threshold": {
      "additional_passes_needed": 2,
      "effect": "Rainfall would need at least two additional gate passes to become the primary explanation.",
      "observed_gate_score": 1,
      "passes_needed_for_displacement": 3
    },
    "report_anchor_removed": {
      "effect": "The research claim collapses without the NASA report anchor; the report is the load-bearing evidence stream.",
      "source_confidence_without_report_support": 0.29
    },
    "strict_same_day_consistency": {
      "clean_temporal_claim_passes": false,
      "effect": "The clean event-window claim fails, but the report-supported ash-source mechanism remains stronger than rainfall or surface-change alternatives.",
      "source_confidence_without_date_credit": 0.8
    },
    "surface_change_observability": {
      "effect": "With zero available pre/post scenes, surface-change reconnaissance cannot carry a primary source claim.",
      "observed_scene_total": 0
    }
  },
  "source_roles": {
    "exposure_context": [
      "data/exposure_impact/exposure_impact_001_Overpass_small_roads_and_critical_amenities.json",
      "data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json",
      "data/exposure_impact/exposure_impact_004_OpenStreetMap_Overpass_bounded_AOI_slice.json",
      "data/geospatial_context/geospatial_context_002_compact_per-event_AOI_derived_from_event_bbox.json"
    ],
    "locked_anchor": "data/event_reports/event_reports_003_Locked_event_anchor_2010_Barren_Island_ash_plume.json",
    "point_weather": [
      "data/physical_hazard/physical_hazard_001_NASA_POWER_daily_point_sample.json",
      "data/physical_hazard/physical_hazard_002_Open-Meteo_archive_point_sample.json"
    ],
    "regional_precipitation": [
      "data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json",
      "data/physical_hazard/physical_hazard_005_GPM_IMERG_V07_event_accumulated_precipitation.json",
      "data/physical_hazard/physical_hazard_007_CHIRPS_daily_event_accumulated_precipitation.json"
    ],
    "report_anchor": "data/event_reports/event_reports_001_Locked_package_evidence_report.html",
    "surface_change": [
      "data/remote_sensing/remote_sensing_002_Sentinel-1_GRD_VV_pre_post_change.json",
      "data/physical_hazard/physical_hazard_009_Sentinel-2_SR_Harmonized_dNBR.json"
    ]
  },
  "support_flags": {
    "ash_plume_phrase_present": true,
    "instrument_supported_by_report": true,
    "place_supported_by_report": true,
    "remote_uninhabited_observation_context": true
  },
  "uncertainty_and_validation": {
    "bounded_use_of_masked_exposure": "Use WorldPop, OSM, and AOI values only as derived regional receptor statistics, not as event-location validation or volcanic-source evidence.",
    "main_uncertainty": "temporal_anchor_mismatch_between_locked_event_date_and_report_image_date",
    "validation_need_level": "high",
    "validation_need_score": 0.867,
    "validation_plan": [
      "Verify coeval image acquisition and plume geometry around 2010-09-25 against the package report anchor.",
      "Check ash advisory, aviation, coast-guard, or pilot-observation records for the report-date plume window.",
      "If available, add coeval volcanic ash, thermal, or SO2 observations before using weather or exposure products as explanatory substitutes."
    ]
  }
}
```

# Computation

The local NASA report supports the volcanic-source hypothesis: it contains the ash-plume statement, places the event at Barren Island in the Andaman Sea, names ALI/EO-1 as the observing instrument, and describes the volcanic island as remote and uninhabited with observations from the Indian Coast Guard, passing pilots, and satellites. The locked package anchor date is `2010-09-03`; the report image acquisition date is `2010-09-25`, giving `date_offset_days = 22`.

Point precipitation is `(13.99 + 13.3) / 2 = 13.645 mm`. Regional maximum precipitation is `max(64.043, 184.585, 39.192) = 184.585 mm`. Regional mean precipitation is `mean(12.101, 28.454, 12.919) = 17.825 mm`, and `peak_to_point_ratio = 184.585 / 13.645 = 13.528`. The rain/change gate score is `1` because only the regional-peak precipitation gate passes; point rain is below 25 mm, date alignment fails the 3-day gate, and Sentinel-1 plus Sentinel-2 scene counts sum to `0`.

The exposure products give regional receptor context: population `9346857`, AOI area `72059.93 km2`, population density `129.709 people/km2`, `276` road elements in the small OSM slice, and `1000` bounded-AOI amenity elements. These values support contextual monitoring or receptor awareness, but they do not override the report's volcanic-source statement or make exposure the source mechanism.

The confidence model gives `source_mechanism_confidence = 0.84` and `validation_need_score = 0.867`. The high source confidence comes from complete report support and weak counter-evidence; the high validation need comes from the 22-day temporal mismatch and absent pre/post surface-change scenes.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the requested JSON with answer, research_hypotheses, computed_evidence, confidence_model, scenario_sensitivity, causal_synthesis, uncertainty_and_validation, source_roles, and final_research_conclusion.
- 4 points: Extracts the NASA report support flags, locked anchor date, report acquisition date, 22-day offset, and source roles from package-local files.
- 4 points: Correctly computes point precipitation, regional precipitation, peak/point ratio, rain-change gate score, surface-scene total, exposure statistics, source confidence, validation-need score, and sensitivity margins.
- 4 points: Tests the volcanic-source, rainfall-displacement, surface-change, and exposure-only hypotheses; identifies report-supported volcanic ash observation as the research conclusion while bounding the temporal mismatch.
- 3 points: Explains why strict date consistency fails, why rainfall would need two additional gate passes to displace the source mechanism, why no surface-change evidence can carry the conclusion, and why removing the report anchor collapses the research claim.
- 2 points: Proposes a validation route using coeval imagery/plume geometry, ash advisory or aviation observations, and targeted volcanic-source confirmation, while keeping exposure data as receptor context rather than source evidence.
