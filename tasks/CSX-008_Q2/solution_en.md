# Final Answer

```json
{
  "answer": "local_dry_heat_fire_weather_chain_supported",
  "target_family": "paper_grade_text_numeric_alignment_audit",
  "event_window": {
    "start_date": "2019-12-01",
    "end_date": "2020-01-31",
    "inclusive_days": 62
  },
  "source_files_used": [
    "data/event_reports/event_reports_003_Locked_event_anchor_2019-2020_Australian_extreme_heat_during_Black_Summer.json",
    "data/event_reports/event_reports_001_Locked_package_evidence_report.pdf",
    "data/physical_hazard/physical_hazard_010_03_World_Weather_Attribution_-_Australian_bushfires_2019-2020.html.html",
    "data/other/other_003_02_NASA_-_Climate_events_of_2020.html.html",
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json",
    "data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json",
    "data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json",
    "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json"
  ],
  "report_claim_alignment": {
    "bom_national_context": "report_supported_national_context",
    "wwa_fire_weather_context": "partial_local_physical_context",
    "nasa_fire_growth_context": "partial_local_burn_heat_context",
    "wmo_locked_anchor": "unsupported_weak_anchor"
  },
  "local_physical_calculations": {
    "temperature_peak_c": 42.2,
    "temperature_peak_time": "2020-01-04T15:00",
    "max_vpd_kpa": 7.62,
    "max_vpd_time": "2020-01-04T15:00",
    "max_wet_bulb_c": 21.8,
    "wet_bulb_shortfall_from_28c": 6.2,
    "hot_dry_hours": 75,
    "warm_nights_tmin_ge_18c": 5,
    "max_apparent_temperature_c": 40.6
  },
  "precipitation_window_check": {
    "coverage_start": "2019-12-01",
    "coverage_end": "2020-01-15",
    "coverage_days": 46,
    "missing_tail_days": 16,
    "coverage_fraction": 0.742,
    "mean_precip_mm": {
      "gpm": 16.79,
      "chirps": 19.21,
      "era5_land": 21.48
    },
    "mean_precip_spread_mm": 4.69
  },
  "burn_change_context": {
    "dnbr_max": 0.953,
    "dnbr_mean": 0.049,
    "dnbr_max_minus_mean": 0.904
  },
  "conflict_resolution": ["scale", "mechanism", "window"],
  "counterfactuals_rejected": ["weak_source", "wrong_window", "wrong_mechanism"],
  "final_label": "local_dry_heat_fire_weather_chain_supported"
}
```

# Evidence And Calculations

The locked event anchor gives the official event window as 2019-12-01 through 2020-01-31, which is 62 inclusive days.

The BOM report is used as national heat, dryness, and fire-weather context. The WWA source supports a broader fire-weather framing around extreme heat and lack of rainfall, while the NASA source supports heat-aided fire growth. The weak WMO locked anchor is not treated as downloaded report text.

For `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`, the peak temperature and peak VPD both occur at `2020-01-04T15:00`: 42.2 deg C and 7.62 kPa. The Stull wet-bulb maximum is 21.8 deg C, 6.2 deg C below the 28 deg C humid-heat threshold. The hot-dry count is 75 hours using `temperature >= 35 C`, `RH <= 20%`, and `VPD >= 4 kPa`. Five nights have daily minimum temperature at least 18 deg C, and the maximum apparent temperature is 40.6 deg C.

The precipitation summaries cover only 2019-12-01 to 2020-01-15, or 46 days. They miss 16 days of the official 62-day window, so the coverage fraction is `46 / 62 = 0.742`. The mean precipitation values are 16.79 mm for GPM IMERG, 19.21 mm for CHIRPS, and 21.48 mm for ERA5-Land; the spread is 4.69 mm.

The dNBR file supplies burn-change context with max 0.953, mean 0.049, and max-minus-mean 0.904. This is not converted into national burned area or affected-population estimates.

# Reference Solving Trace

1. Read the event anchor to establish the official window.
2. Extract short claim-status labels from the BOM, WWA, NASA, and weak WMO anchor sources.
3. Compute wet-bulb temperature, VPD, hot-dry hours, warm nights, and apparent-temperature maximum from Open-Meteo.
4. Compare precipitation product coverage against the official window and compute product means and spread.
5. Read dNBR as burn-change context and resolve scale, mechanism, and window conflicts.

# Scoring Rubric

Total: 20 points.

- 3 points: Uses the requested descriptive JSON schema, official event window, inclusive day count, and package-relative paths for report, weather, precipitation, and burn-change evidence.
- 4 points: Correctly maps BOM, WWA, NASA, and weak WMO-anchor claims to support statuses and short reason codes.
- 4 points: Reconstructs peak temperature/time, VPD, wet-bulb shortfall, hot-dry hours, warm-night count, and apparent-temperature maximum.
- 3 points: Computes the shorter precipitation coverage, missing tail days, coverage fraction, product means, and product spread.
- 2 points: Uses dNBR as local burn-change context and reports max, mean, and max-minus-mean values without converting it into national burned-area claims.
- 3 points: Resolves national/local scale, humid/dry mechanism, and short precipitation-window conflicts with numeric impacts.
- 1 point: Returns the bounded final ruling and package-grounded limitations without external facts or response advice.
