# Final Answer

Correct answer:

```json
{
  "target_family": "yagi_rainfall_impact_ratio_ledger",
  "row_results": {
    "rainfall_load": "pass",
    "rainfall_concentration": "pass",
    "wind_context": "context_only",
    "regional_impact_ratios": "pass",
    "local_denominator_test": "reject_scaling",
    "surface_change_metric_role": "context_only"
  },
  "core_values": {
    "hourly_total_mm": 373.0,
    "daily_total_mm": 388.82,
    "daily_to_hourly_ratio": 1.042,
    "hourly_mean_mm_h": 1.295,
    "daily_mean_mm_day": 32.402,
    "max_hour_fraction": 0.0477,
    "max_day_fraction": 0.305,
    "wind_ratio": 1.468,
    "safe_water_ratio": 0.5,
    "education_ratio": 0.333,
    "school_health_ratio": 1.545,
    "children_pop_ratio": 2175.7,
    "school_local_ratio": 60.7,
    "s1_range_db": 24.612,
    "alpha_mean_max_ratio": 0.117
  },
  "rejected_scaling": [
    "Do not scale the 6 million affected-children report by the 2757.761-person local denominator.",
    "Do not scale 850 damaged schools by the 14 local school features.",
    "Do not convert local surface-change metrics into regional loss totals."
  ],
  "final_label": "sustained_rainfall_dominant_regional_flood_landslide_signal",
  "interpretation": "The rainfall totals and concentration ratios support sustained storm-window flood and landslide conditions, while wind and surface-change metrics remain contextual."
}
```

# Key Computations

The storm-window rainfall load is computed from two point weather products:

- Hourly precipitation total: 373.0 mm over 288 hours.
- Daily precipitation total: 388.82 mm over 12 days.
- Hourly mean: `373.0 / 288 = 1.295 mm/h`.
- Daily mean: `388.82 / 12 = 32.402 mm/day`.
- Daily-to-hourly agreement ratio: `388.82 / 373.0 = 1.042`.

The temporal concentration checks are:

- Maximum hourly precipitation fraction: `17.8 / 373.0 = 0.0477`.
- Maximum daily precipitation fraction: `118.6 / 388.82 = 0.305`.

The wind-context calculation converts the daily wind peak and compares the hourly and daily peaks:

- NASA POWER peak wind: `11.81 m/s * 3.6 = 42.516 km/h`.
- Hourly-to-daily wind ratio: `62.4 / 42.516 = 1.468`.

The regional report ratios are:

- Safe-water ratio: `3 / 6 = 0.500`.
- Education ratio: `2 / 6 = 0.333`.
- Damaged school to damaged health-centre ratio: `850 / 550 = 1.545`.

The local denominator and surface-change checks are:

- Local school features: `12 + 2 = 14`.
- Affected-children to local-population ratio: `6000000 / 2757.761 = 2175.7`.
- Damaged-school to local-school ratio: `850 / 14 = 60.7`.
- Sentinel-1 VV change range: `12.074 - (-12.538) = 24.612 dB`.
- AlphaEarth mean/max ratio: `0.007 / 0.060 = 0.117`.

# Reasoning Path

The rainfall-load row passes because the hourly total exceeds 300 mm, the daily total exceeds 350 mm, and the two totals agree within the 0.95-1.10 ratio band. The concentration row also passes: the largest hour accounts for only 4.77 percent of the hourly total, while the largest day accounts for 30.5 percent of the daily total, so the event is not explained by a single-hour pulse.

The wind row is context only. The wind peaks are real storm-context values, but the rainfall-load and concentration tests already satisfy the flood/landslide signal. The reported regional impact ratios pass as internally coherent regional-scale ratios tied to the multi-country event.

The local denominator row rejects scaling because the local population and school counts are far too small to serve as denominators for the regional report totals. The surface-change row is context only because the metrics can describe local surface contrast but do not compute regional loss totals.

# Computed Interpretation

The compact classification is `sustained_rainfall_dominant_regional_flood_landslide_signal`: rainfall magnitude and duration carry the diagnosis, while wind, local denominator, and surface-change checks prevent inflated scaling.

# Scoring Rubric

The answer is scored out of 20 points:

- 3 points: Returns the requested compact JSON with `target_family`, six row results, `core_values`, `rejected_scaling`, `final_label`, and one-sentence interpretation. Partial credit: 1-2 points for a mostly correct structure with missing minor fields.
- 5 points: Computes rainfall load and concentration correctly, including 373.0 mm, 388.82 mm, 1.295 mm/h, 32.402 mm/day, 1.042, 0.0477, and 0.305. Partial credit: 2-4 points for correct totals but missing or rounded-away ratios.
- 3 points: Computes wind and regional report ratios correctly, including 42.516 km/h, 1.468, 0.500, 0.333, and 1.545. Partial credit: 1-2 points for correct formulas with one or two numeric errors.
- 3 points: Computes local denominator and surface-change values correctly, including 14 local schools, 2175.7, 60.7, 24.612 dB, and 0.117. Partial credit: 1-2 points for recognizing the denominator mismatch but omitting one metric group.
- 3 points: Assigns the correct row states: rainfall rows and regional ratios pass, wind and surface change are `context_only`, and local denominator transfer is `reject_scaling`. Partial credit: 1-2 points for the right final direction with one or two row-state mistakes.
- 2 points: Rejects inflated scaling from local population, local school counts, and surface-change metrics. Partial credit: 1 point for rejecting only one or two of the three scaling errors.
- 1 point: Gives the compact rainfall-dominant flood/landslide final label without adding broader statements not computed by the ledger. Partial credit: 0.5 points for a compatible but vague label.
