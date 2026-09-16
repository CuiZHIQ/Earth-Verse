# Final Answer

```json
{
  "target_family": "yagi_persistent_rainfall_impact_consistency",
  "computed_metrics": {
    "event_days": 12,
    "hour_count": 288,
    "hourly_precipitation_total_mm": 373.0,
    "daily_precipitation_total_mm": 388.82,
    "daily_hourly_precipitation_ratio": 1.0424,
    "peak_hour_share_of_hourly_total": 0.0477,
    "peak_daily_share_of_daily_total": 0.305,
    "mean_hourly_precipitation_rate_mm_h": 1.295,
    "max_hourly_wind_m_s": 17.333,
    "hourly_to_daily_wind_ratio": 1.4677,
    "damaged_school_to_health_centre_ratio_lower_bound": 1.5455,
    "viet_nam_water_lack_share_proxy": 0.5,
    "education_support_share_proxy": 0.3333,
    "myanmar_displacement_per_death_report_scale_ratio": 1882.35,
    "named_country_count": 4
  },
  "tests": {
    "persistent_rainfall": "pass",
    "single_hour_spike": "fail",
    "wind_only_explanation": "fail",
    "regional_disruption": "pass"
  },
  "final_label": "persistent_heavy_rain_multi_country_disruption_supported"
}
```

# Key Computations

The event window from 2024-09-07 through 2024-09-18 is 12 inclusive days, matching 288 hourly records. Point rainfall totals are consistent across hourly and daily summaries: `388.82 / 373.0 = 1.0424`, and both exceed 300 mm.

The rainfall was not dominated by one hour: `17.8 / 373.0 = 0.0477`, below the 0.10 single-hour-spike threshold. The peak day contributed `118.6 / 388.82 = 0.305`, and the mean hourly rate over the full window was `373.0 / 288 = 1.295 mm/h`. Wind converts to `62.4 / 3.6 = 17.333 m/s`, and the hourly-to-daily wind ratio is `17.333 / 11.81 = 1.4677`.

Regional report normalization gives `850 / 550 = 1.5455` damaged schools per damaged health centre as a lower-bound ratio, `3 / 6 = 0.5` for Viet Nam safe-water need relative to the regional children-affected figure, `2 / 6 = 0.3333` for education-support need, and `320000 / 170 = 1882.35` displacements per reported death in Myanmar. Viet Nam, Myanmar, Laos, and Thailand are all named, so the named-country count is 4.

# Reasoning Path

The rainfall-consistency test passes because the hourly and daily precipitation totals are close, both are above the 300 mm heavy-rainfall threshold, and the hourly record count matches the full 12-day window. The single-hour-spike explanation fails because the peak hour accounts for only 4.77 percent of the hourly total.

The wind-only explanation fails for this task because the converted wind speed supplies cyclone context but does not explain the report-normalized flood and landslide disruption as well as persistent rainfall does. The regional disruption test passes because the normalized report values cover multiple sectors and all four named countries.

Combining those tests yields the final label `persistent_heavy_rain_multi_country_disruption_supported`.

# Computed Interpretation

The quantitative record supports a sustained rainfall-driven regional disruption signal: heavy precipitation persisted across a complete multi-day window, while the report-normalized impacts show broad education, water, displacement, and country-coverage anchors.

# Scoring Rubric

- 4 points: Final JSON answer and label. Full credit requires valid JSON with the requested target family, all requested metric groups, test states, and the exact final label. Partial credit: 2-3 points for the correct label with minor JSON omissions; 1 point for a recognizable but incomplete conclusion.
- 4 points: Rainfall-window and precipitation calculations. Full credit requires 12 days, 288 hours, 373.0 mm, 388.82 mm, ratio 1.0424, mean hourly rate 1.295, and correct units. Partial credit: up to 3 points for mostly correct rainfall values with one or two arithmetic or rounding errors.
- 3 points: Peak-concentration tests. Full credit requires peak-hour share 0.0477, peak-day share 0.305, and the conclusion that the single-hour-spike test fails. Partial credit: 1-2 points for computing only one peak share or drawing the right conclusion from approximate values.
- 3 points: Wind conversion and interpretation. Full credit requires 17.333 m/s, wind ratio 1.4677, and rejecting a wind-only explanation. Partial credit: 1-2 points for correct conversion without the ratio or with weak interpretation.
- 4 points: Regional impact normalization. Full credit requires the school-health ratio 1.5455, water proxy 0.5, education proxy 0.3333, Myanmar displacement-per-death ratio 1882.35, named-country count 4, and lower-bound/proxy wording. Partial credit: up to 3 points for correct values with missing proxy wording or one omitted ratio.
- 2 points: Concise computed interpretation. Full credit requires tying persistent rainfall and multi-country disruption together without adding response actions or unverified realized-loss assertions. Partial credit: 1 point for a concise but less specific interpretation.
