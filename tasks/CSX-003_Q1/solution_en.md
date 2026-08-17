# Final Answer

```json
{
  "answer_type": "evidence_sufficiency_ruling",
  "ruling": "partially_supported",
  "claim_ruling": {
    "supported_part": "The package supports late-August heat timing and report-based Poyang Lake drought or low-water context.",
    "insufficient_part": "The package precipitation accumulations are not sufficient as a direct late-August drought measurement for the heat peak."
  },
  "selected_evidence": {
    "event_window": {
      "path": "data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json",
      "start": "2022-06-01",
      "end": "2022-08-31",
      "expected_days": 92
    },
    "heat_timing": {
      "path": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
      "daily_records_in_window": 92,
      "peak_apparent_temperature_c": 44.0,
      "peak_apparent_temperature_date": "2022-08-20",
      "compound_heat_run": {
        "start": "2022-08-12",
        "end": "2022-08-22",
        "days": 11,
        "rule": "Tmax >=35 C, apparent >=40 C, Tmin >=28 C"
      }
    },
    "drought_low_water_context": {
      "path": "data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html",
      "evidence_role": "direct_report_context",
      "matched_terms": [
        "Prolonged heat and drought",
        "Poyang Lake",
        "largest freshwater lake",
        "water levels"
      ]
    }
  },
  "calculation_check": {
    "precipitation_summary_window": {
      "era5": ["2022-06-01", "2022-07-16"],
      "gpm": ["2022-06-01", "2022-07-16"],
      "chirps": ["2022-06-01", "2022-07-16"]
    },
    "precipitation_to_heat_peak_gap_days": 35,
    "precipitation_product_conflict": {
      "gpm_mean_mm": 457.495,
      "chirps_mean_mm": 371.964,
      "difference_mm": 85.53,
      "ratio": 1.23
    }
  },
  "insufficient_alternatives": [
    {
      "basis": "Use ERA5, GPM, or CHIRPS precipitation accumulations as a direct late-August drought metric.",
      "paths": [
        "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
        "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
        "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json"
      ],
      "reason_code": "wrong_window",
      "numeric_or_path_reason": "The latest precipitation summary ends 2022-07-16, 35 days before the 2022-08-20 apparent-temperature peak."
    },
    {
      "basis": "Select one gridded precipitation product as the precise event drought amount.",
      "paths": [
        "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
        "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json"
      ],
      "reason_code": "product_conflict",
      "numeric_or_path_reason": "GPM mean 457.495 mm versus CHIRPS mean 371.964 mm; difference 85.53 mm and ratio 1.23."
    },
    {
      "basis": "Use Sentinel-2 dNBR as the direct heat-drought evidence.",
      "paths": [
        "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json"
      ],
      "reason_code": "wrong_measurement_type",
      "numeric_or_path_reason": "The file reports Sentinel-2 dNBR burn-index statistics over 2022-06-01 to 2022-08-30, not daily heat timing or precipitation."
    }
  ],
  "minimal_required_paths": [
    "data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json",
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html",
    "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json"
  ],
  "final_assessment": "Rule partially supported: use Open-Meteo for late-August heat timing and the NASA report for drought or low-water context, but do not use the early-window precipitation summaries as the direct late-August drought metric."
}
```

# Reference Solving Trace

1. Inspect `metadata/event.json`, `metadata/files.csv`, and `metadata/sources.csv` to identify the CSX-003 package inventory and source roles. The useful evidence for this ruling is the locked event anchor, Open-Meteo daily heat archive, NASA Poyang Lake report, ERA5/GPM/CHIRPS precipitation summaries, and one weak-source decoy.
2. Read `data/event_reports/event_reports_003_Locked_event_anchor_2022_China_heat_wave_and_drought.json`. Use `temporal_window.start_date = 2022-06-01` and `temporal_window.end_date = 2022-08-31`; the inclusive expected day count is 92.
3. Read `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`. Filter `daily.time`, `daily.temperature_2m_max`, `daily.temperature_2m_min`, and `daily.apparent_temperature_max` to the locked window. The archive has 92 daily rows in-window. The maximum apparent temperature is 44.0 C on `2022-08-20`.
4. Compute the longest same-day compound heat run using `temperature_2m_max >= 35`, `apparent_temperature_max >= 40`, and `temperature_2m_min >= 28`. The longest run is 11 days from `2022-08-12` through `2022-08-22`.
5. Read `data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Parched_Poyang_Lake.html`. It directly supports drought or low-water context through terms including `Prolonged heat and drought`, `Poyang Lake`, `largest freshwater lake`, and `water levels`.
6. Read the precipitation summaries:
   - `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
   - `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
   - `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`
7. All three precipitation summaries cover `2022-06-01` to `2022-07-16`. The latest precipitation-summary end is therefore 35 days before the `2022-08-20` apparent-temperature peak, so these files are not sufficient as direct late-August drought measurements.
8. Compare GPM and CHIRPS means over their shared window. GPM mean is 457.495 mm and CHIRPS mean is 371.964 mm. The difference is `457.4946622079963 - 371.9643930976495 = 85.53 mm`, and the ratio is `457.4946622079963 / 371.9643930976495 = 1.23`. This product conflict is an additional reason not to choose one precipitation product as the precise drought amount.
9. Reject `data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json` as a direct heat-drought source because it reports Sentinel-2 dNBR burn-index statistics, not daily heat timing or precipitation.
10. The correct ruling is `partially_supported`: Open-Meteo plus the NASA report supports late-August heat timing and drought/low-water context, while the gridded precipitation summaries are insufficient for the proposed direct late-August drought metric.

# Rubric

Award up to 20 points:

- 3 points for the required JSON schema with `answer_type = evidence_sufficiency_ruling` and `ruling = partially_supported`.
- 4 points for using the locked `2022-06-01` to `2022-08-31` event window, 92 daily records, the `44.0 C` apparent-temperature peak on `2022-08-20`, and the 11-day compound heat run from `2022-08-12` to `2022-08-22`.
- 3 points for using the NASA Poyang Lake report as direct drought/low-water context and identifying matched terms rather than treating metadata alone as evidence.
- 3 points for showing that ERA5, GPM, and CHIRPS all end on `2022-07-16`, 35 days before the heat peak.
- 2 points for the GPM/CHIRPS conflict arithmetic: GPM `457.495 mm`, CHIRPS `371.964 mm`, difference `85.53 mm`, ratio `1.23`.
- 3 points for rejecting or marking insufficient the precipitation basis and at least one weak alternative source with package-relative paths and reason codes.
- 2 points for using only package-local evidence, with no web search, hidden answers, invented values, or broad disaster essay.
