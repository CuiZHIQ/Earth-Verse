# Super Typhoon Yagi Rainfall-Impact Consistency Check

A hydrometeorology team is preparing a short technical note on Super Typhoon Yagi's September 2024 flood and landslide impacts across Viet Nam, Myanmar, Laos, and Thailand. The team needs to decide whether the record supports a persistent heavy-rainfall, multi-country disruption signal rather than a single-hour rainfall spike or a wind-only explanation.

Use the package point-weather records only to test the local rainfall-window consistency against the daily record. Use the event report to normalize the multi-country disruption indicators and country count; do not treat the single point-weather series as a spatial average for all affected countries.

Using the technical record and quantitative diagnostics, return JSON only with:

```json
{
  "target_family": "yagi_persistent_rainfall_impact_consistency",
  "computed_metrics": {
    "event_days": 0,
    "hour_count": 0,
    "hourly_precipitation_total_mm": 0,
    "daily_precipitation_total_mm": 0,
    "daily_hourly_precipitation_ratio": 0,
    "peak_hour_share_of_hourly_total": 0,
    "peak_daily_share_of_daily_total": 0,
    "mean_hourly_precipitation_rate_mm_h": 0,
    "max_hourly_wind_m_s": 0,
    "hourly_to_daily_wind_ratio": 0,
    "damaged_school_to_health_centre_ratio_lower_bound": 0,
    "viet_nam_water_lack_share_proxy": 0,
    "education_support_share_proxy": 0,
    "myanmar_displacement_per_death_report_scale_ratio": 0,
    "named_country_count": 0
  },
  "tests": {
    "persistent_rainfall": "",
    "single_hour_spike": "",
    "wind_only_explanation": "",
    "regional_disruption": ""
  },
  "final_label": ""
}
```

Use `persistent_heavy_rain_multi_country_disruption_supported` only if the rainfall totals are mutually consistent and above 300 mm, the 288-hour event window is complete, the peak-hour share is below 0.10, wind is weaker than the rainfall-impact explanation, and the report-normalized impact values show disruption in at least four named countries.
