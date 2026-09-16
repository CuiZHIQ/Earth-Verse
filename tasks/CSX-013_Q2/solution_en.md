# Final Answer

```json
{
  "answer_type": "text_numeric_alignment_audit",
  "audit_question": "Do package-local report text and local numeric heat files support the same claims without over-extending the local point evidence?",
  "claim_matrix": [
    {
      "alignment": "partial_timing_not_magnitude",
      "claim_id": "C1",
      "claim_label": "regional_four_day_record_heat",
      "numeric_check_ids": [
        "NC2",
        "NC4"
      ],
      "report_values": {
        "threshold_text": "well_over_100f",
        "window": "2021-06-26_to_2021-06-29"
      },
      "ruling": "local_point_confirms_persistent_heat_not_regional_record_magnitude",
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ]
    },
    {
      "alignment": "report_supported_not_local_numeric",
      "claim_id": "C2",
      "claim_label": "portland_three_day_record_sequence",
      "numeric_check_ids": [
        "NC6"
      ],
      "report_values": {
        "portland_avg_f": 112.0,
        "portland_tmax_f": [
          108,
          112,
          116
        ]
      },
      "ruling": "city_claim_not_reproducible_from_local_point_file",
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ]
    },
    {
      "alignment": "report_supported_not_local_numeric",
      "claim_id": "C3",
      "claim_label": "lytton_canada_peak_record_sequence",
      "numeric_check_ids": [
        "NC7"
      ],
      "report_values": {
        "lytton_tmax_c": [
          46.1,
          47.5,
          49.5
        ],
        "lytton_tmax_f": [
          116,
          118,
          121
        ],
        "peak_c": 49.5,
        "peak_f": 121.0
      },
      "ruling": "canada_record_claim_not_reproducible_from_local_point_file",
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ]
    },
    {
      "alignment": "unsupported_by_package_machine_data",
      "claim_id": "C4",
      "claim_label": "high_pressure_downslope_mechanism",
      "numeric_check_ids": [],
      "report_values": {
        "mechanism_terms": [
          "high_pressure",
          "cloudless_sinking_air",
          "downslope_winds"
        ]
      },
      "ruling": "report_text_supports_claim_but_machine_files_lack_pressure_and_descent_variables",
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json"
      ]
    },
    {
      "alignment": "report_supported_not_local_numeric",
      "claim_id": "C5",
      "claim_label": "air_conditioning_vulnerability",
      "numeric_check_ids": [],
      "report_values": {
        "portland_primary_ac_pct": 78,
        "seattle_primary_ac_pct": 44
      },
      "ruling": "worldpop_population_does_not_measure_air_conditioning",
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json"
      ]
    }
  ],
  "counterfactuals": [
    {
      "counterfactual_id": "CF1",
      "rejection_reason": "wrong_location_scale",
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ],
      "wrong_move": "treat_local_open_meteo_point_as_portland_or_lytton",
      "wrong_result": {
        "local_peak_f": 95.9,
        "lytton_peak_shortfall_f": 25.1,
        "portland_avg_gap_f": -22.2
      }
    },
    {
      "counterfactual_id": "CF2",
      "rejection_reason": "missing_mechanism_variables",
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json"
      ],
      "wrong_move": "use_era5_aggregate_as_high_pressure_downslope_proof",
      "wrong_result": {
        "available_wind_stats": [
          "u_component_of_wind_10m",
          "v_component_of_wind_10m"
        ],
        "era5_temperature_2m_max_c_max": 31.3,
        "missing_required_variables": [
          "surface_pressure",
          "geopotential_height",
          "time_resolved_downslope_path"
        ]
      }
    },
    {
      "counterfactual_id": "CF3",
      "rejection_reason": "wrong_modality_for_heat_record_claim",
      "source_paths": [
        "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
        "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json",
        "data/event_catalogs/event_catalogs_001_GDACS_public_event_feeds_and_archive.json",
        "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json",
        "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json"
      ],
      "wrong_move": "use_precip_catalog_or_remote_sensing_as_direct_heat_record_evidence",
      "wrong_result": {
        "chirps_mean_mm": 5.003,
        "dnbr_mean": 0.1178,
        "embedding_change_mean": 0.0311,
        "gdacs_heat_match_count": 0,
        "gpm_mean_mm": 5.279,
        "precip_mean_delta_mm": 0.276
      }
    }
  ],
  "final_ruling": {
    "directly_computable_local_conclusion": "persistent_dry_local_heat_with_limited_wet_bulb_stress",
    "do_not_claim": [
      "local_point_proves_portland_or_lytton_records",
      "era5_aggregate_proves_high_pressure_downslope_mechanism",
      "precip_or_remote_sensing_files_are_direct_heat_record_evidence"
    ],
    "ruling_label": "report_claims_text_supported_local_numeric_only_partial"
  },
  "local_numeric_checks": {
    "NC1": {
      "end": "2021-07-01",
      "label": "official_event_window",
      "source_path": "data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json",
      "start": "2021-06-25"
    },
    "NC2": {
      "all_days_ge_30c": true,
      "dates": [
        "2021-06-26",
        "2021-06-27",
        "2021-06-28",
        "2021-06-29"
      ],
      "days_ge_100f": 0,
      "label": "local_report_window_tmax_sequence",
      "source_path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
      "tmax_c": [
        30.1,
        32.2,
        34.0,
        35.5
      ],
      "tmax_f": [
        86.2,
        90.0,
        93.2,
        95.9
      ],
      "window": "2021-06-26_to_2021-06-29"
    },
    "NC3": {
      "label": "local_peak_and_dryness",
      "peak_time": "2021-06-29T15:00",
      "rh_at_tmax_peak_pct": 18.0,
      "source_path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
      "tmax_peak_c": 35.5,
      "tmax_peak_f": 95.9,
      "wbt_at_tmax_peak_c": 19.0
    },
    "NC4": {
      "hdd30_c_hours": 71.0,
      "hot_day_run_ge_30c": {
        "count": 4,
        "end": "2021-06-29",
        "start": "2021-06-26"
      },
      "hot_hours_ge_30c": 29,
      "label": "local_persistence_heat_load",
      "source_path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
      "warm_nights_ge_16c": 3
    },
    "NC5": {
      "label": "local_wet_bulb_screen",
      "source_path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
      "wbt_hours_ge_28c": 0,
      "wbt_peak_c": 22.0,
      "wbt_peak_time": "2021-06-29T19:00"
    },
    "NC6": {
      "date_matched_delta_f": -22.2,
      "date_matched_local_avg_f": 89.8,
      "hottest_local_3day_avg_f": 93.0,
      "hottest_local_3day_window": "2021-06-27_to_2021-06-29",
      "hottest_local_delta_f": -19.0,
      "label": "portland_claim_local_gap",
      "report_portland_avg_f": 112.0,
      "report_portland_tmax_f": [
        108,
        112,
        116
      ],
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ]
    },
    "NC7": {
      "label": "lytton_claim_local_gap",
      "local_peak_c": 35.5,
      "local_peak_f": 95.9,
      "local_shortfall_c": 14.0,
      "local_shortfall_f": 25.1,
      "report_lytton_peak_c": 49.5,
      "report_lytton_peak_f": 121.0,
      "report_lytton_tmax_c": [
        46.1,
        47.5,
        49.5
      ],
      "report_lytton_tmax_f": [
        116,
        118,
        121
      ],
      "source_paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ]
    }
  },
  "reference_trace": [
    {
      "action": "read_metadata_and_anchor",
      "paths": [
        "metadata/event.json",
        "data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json"
      ],
      "step_id": "T1"
    },
    {
      "action": "extract_report_claim_numbers",
      "paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin"
      ],
      "step_id": "T2"
    },
    {
      "action": "compute_open_meteo_local_heat_checks",
      "paths": [
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ],
      "step_id": "T3"
    },
    {
      "action": "compare_report_city_values_to_local_point_values",
      "paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
      ],
      "step_id": "T4"
    },
    {
      "action": "test_mechanism_and_wrong_modality_decoys",
      "paths": [
        "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
        "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
        "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json",
        "data/event_catalogs/event_catalogs_001_GDACS_public_event_feeds_and_archive.json",
        "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json",
        "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json"
      ],
      "step_id": "T5"
    },
    {
      "action": "emit_fixed_schema_alignment_audit",
      "paths": [
        "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
        "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
        "data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json"
      ],
      "step_id": "T6"
    }
  ],
  "scope": {
    "event_id": "CSX-013",
    "event_name": "June 2021 Pacific Northwest heat wave",
    "evidence_boundary": "package_local_only",
    "official_window": "2021-06-25_to_2021-07-01",
    "report_heat_window": "2021-06-26_to_2021-06-29"
  },
  "source_reliability_ladder": [
    {
      "path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
      "reliability_label": "direct_machine_readable_point_series",
      "role": "direct_local_numeric_heat",
      "source_id": "S1",
      "supports": [
        "NC2",
        "NC3",
        "NC4",
        "NC5"
      ],
      "tier": 1
    },
    {
      "path": "data/event_reports/event_reports_001_Locked_package_evidence_report.bin",
      "reliability_label": "locked_noaa_html_report",
      "role": "locked_report_text_claims",
      "source_id": "S2",
      "supports": [
        "C1",
        "C2",
        "C3",
        "C4",
        "C5"
      ],
      "tier": 2
    },
    {
      "path": "data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json",
      "reliability_label": "locked_event_metadata",
      "role": "event_window_and_scope_anchor",
      "source_id": "S3",
      "supports": [
        "NC1"
      ],
      "tier": 3
    },
    {
      "path": "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
      "reliability_label": "aggregate_stats_missing_pressure_and_trajectory",
      "role": "weak_mechanism_context",
      "source_id": "S4",
      "supports": [],
      "tier": 4
    },
    {
      "paths": [
        "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
        "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json",
        "data/event_catalogs/event_catalogs_001_GDACS_public_event_feeds_and_archive.json",
        "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json",
        "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json"
      ],
      "reliability_label": "not_direct_heat_record_evidence",
      "role": "wrong_modality_decoys",
      "source_id": "S5",
      "supports": [],
      "tier": 5
    }
  ]
}
```

# Evidence Used

Package-local files inspected for the answer:

- `metadata/event.json`
- `metadata/files.csv`
- `metadata/sources.csv`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.bin`
- `data/event_reports/event_reports_003_Locked_event_anchor_June_2021_Pacific_Northwest_heat_wave.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/event_catalogs/event_catalogs_001_GDACS_public_event_feeds_and_archive.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json`

# Key Computations

The event anchor gives the official window as `2021-06-25` through `2021-07-01`. The locked NOAA HTML report supplies the report claims: June 26-29 regional record heat, Portland's `108, 112, 116 F` sequence with `112.0 F` average, Lytton's `116, 118, 121 F` sequence with report-stated Celsius values `46.1, 47.5, 49.5 C`, the high-pressure/downslope mechanism language, and Seattle/Portland primary air-conditioning values of `44%` and `78%`.

From `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`, the local June 26-29 daily Tmax sequence is `30.1, 32.2, 34.0, 35.5 C`, or `86.2, 90.0, 93.2, 95.9 F`. This confirms local persistence above 30 C but not the report's regional/city magnitude above 100 F, since the local point has `0` days at or above 100 F.

Hourly calculations from the same Open-Meteo file give peak local air temperature `35.5 C / 95.9 F` at `2021-06-29T15:00`, RH at that peak of `18.0%`, peak wet-bulb temperature `22.0 C`, `0` hours at or above 28 C wet-bulb, `29` hot hours at or above 30 C, `71.0` C-hours HDD30, a 4-day Tmax run at or above 30 C, and `3` warm nights with Tmin at or above 16 C.

For the Portland claim, the local date-matched June 26-28 mean is `89.8 F`, which is `22.2 F` below the report's Portland `112.0 F` mean. Even the hottest local three-day mean, `93.0 F` for June 27-29, is `19.0 F` below the Portland report value. For the Lytton claim, the report peak is `121.0 F / 49.5 C`, while the local point peak is `95.9 F / 35.5 C`, a local shortfall of `25.1 F / 14.0 C`.

# Rejected Or Insufficient Alternatives

ERA5-Land aggregate stats include temperature and wind-component aggregates, but they do not include surface pressure, geopotential height, or a time-resolved downslope trajectory. They therefore cannot prove the high-pressure/downsloping mechanism, even though the report text supports that claim.

GPM and CHIRPS precipitation files report mean precipitation values of `5.279 mm` and `5.003 mm` with a `0.276 mm` mean difference. GDACS has `0` heat matches in this package slice, and the annual embedding/dNBR files are land-surface or burn-change modalities. These are rejected as direct evidence for heat-record claims.

WorldPop gives a package AOI population of `49269.915`, but it has no air-conditioning field, so it cannot verify the report's Seattle/Portland AC percentages.

# Reference Solving Trace

1. Read `metadata/event.json` and the locked event anchor to set the event ID, hazard family, official date window, and package-local evidence boundary.
2. Parse the locked NOAA HTML report for the five claim records and the numeric report values used in C1-C5.
3. Read the Open-Meteo hourly and daily arrays, filter the official/report windows, convert C to F, and compute HDD30 and wet-bulb values.
4. Compare report city/regional values against the local point values without treating the local point as Portland, Lytton, or the whole region.
5. Inspect ERA5, precipitation, GDACS, embedding, dNBR, and WorldPop files only to classify their source roles and failure modes.
6. Emit the fixed-schema JSON with claim alignments, numeric checks, source ladder, counterfactuals, final ruling, and trace.


# Reasoning-Depth Addendum

The expected final JSON should also include this task-specific reasoning object:

```json
{
  "reasoning_depth": {
    "counterfactual_rejection": "Treating the local point as Portland or Lytton fails because the local peak is far below the report city and Canada records.",
    "evidence_weighting": "Open-Meteo local heat metrics are decisive for local persistence; the NOAA report is decisive for Portland, Lytton, AC vulnerability, and mechanism language.",
    "uncertainty_or_scale_caveat": "ERA5 aggregate wind and temperature statistics cannot by themselves prove high-pressure subsidence or downslope trajectories."
  }
}
```

This addition makes the answer explain the evidence hierarchy, reject the main tempting simplification, and state the bounded scale or uncertainty caveat without changing the numeric ground truth.

# Scoring Rubric

Total: 20 points.

- 2 points: Fixed schema and scope. Full credit returns the exact top-level keys, `text_numeric_alignment_audit` answer type, package-relative paths, official event window, and report heat window.
- 3 points: Report claim extraction. Full credit extracts C1-C5 with the Portland `108/112/116 F` sequence, Lytton `116/118/121 F` and `46.1/47.5/49.5 C` sequence, mechanism terms, and Seattle/Portland AC percentages.
- 5 points: Local numeric recomputation. Full credit reports NC1-NC7, including local Tmax sequence, `35.5 C / 95.9 F` peak, `0` days >=100 F, `29` hot hours, `71.0` C-hours HDD30, `3` warm nights, `22.0 C` peak WBT, and `18.0%` RH at peak temperature.
- 3 points: Text-numeric alignment rulings. Full credit correctly classifies C1 as `partial_timing_not_magnitude`, C2/C3/C5 as `report_supported_not_local_numeric`, and C4 as `unsupported_by_package_machine_data` for machine verification.
- 2 points: Source reliability ladder. Full credit ranks direct local numeric heat, locked report text, anchor metadata, weak ERA5 mechanism context, and wrong-modality decoys with correct roles and paths.
- 3 points: Counterfactual rejections. Full credit includes CF1-CF3 with numeric consequences and reason codes for wrong location scale, missing mechanism variables, and wrong modality.
- 2 points: Reference trace and boundaries. Full credit includes T1-T6 and avoids web evidence, hidden answers, broad mechanism prose, and unscored disaster-response claims.
