# Black Summer Text-Numeric Alignment Analysis

A climate-impact analyst is preparing a package-local technical note for the 2019-2020 Australian Black Summer period. The goal is to connect the report narrative with local weather calculations and burn-change context, while keeping national report claims, short-window precipitation summaries, and local physical measurements in their correct roles.

Use only package-local evidence from CSX-008. Do not use web search, outside thresholds, or hidden answers. Use package-relative source paths only. Extract report evidence as short paraphrased claim labels, not long quotations.

Rules:

- Establish the official event window from the strongest package-local event anchor.
- Select package-local evidence for national-scale heat, dryness, and fire-weather context.
- Select the strongest local hourly or daily weather evidence for Canberra-area heat, humidity, VPD, warm-night, and apparent-temperature calculations.
- Compute wet-bulb temperature with the Stull approximation and vapor pressure deficit as `0.6108 * exp((17.27 * T) / (T + 237.3)) * (1 - RH / 100)`.
- Treat short-window precipitation summaries as local context when their dates do not cover the full official event window.
- Treat burn-index change evidence as local burn-change evidence, but do not repeat a narrow burn-change-only arbitration.
- Do not include AOI-path, WorldPop, OSM, or exposure-denominator fields in the answer. They are not needed for this task.

Return JSON with descriptive field names:

```json
{
  "answer": "<short final label>",
  "target_family": "paper_grade_text_numeric_alignment_audit",
  "event_window": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "inclusive_days": 0
  },
  "source_files_used": ["<package-relative path>", "..."],
  "report_claim_alignment": {
    "bom_national_context": "<status>",
    "wwa_fire_weather_context": "<status>",
    "nasa_fire_growth_context": "<status>",
    "wmo_locked_anchor": "<status>"
  },
  "local_physical_calculations": {
    "temperature_peak_c": 0,
    "temperature_peak_time": "YYYY-MM-DDTHH:MM",
    "max_vpd_kpa": 0,
    "max_vpd_time": "YYYY-MM-DDTHH:MM",
    "max_wet_bulb_c": 0,
    "wet_bulb_shortfall_from_28c": 0,
    "hot_dry_hours": 0,
    "warm_nights_tmin_ge_18c": 0,
    "max_apparent_temperature_c": 0
  },
  "precipitation_window_check": {
    "coverage_start": "YYYY-MM-DD",
    "coverage_end": "YYYY-MM-DD",
    "coverage_days": 0,
    "missing_tail_days": 0,
    "coverage_fraction": 0,
    "mean_precip_mm": {"gpm": 0, "chirps": 0, "era5_land": 0},
    "mean_precip_spread_mm": 0
  },
  "burn_change_context": {
    "dnbr_max": 0,
    "dnbr_mean": 0,
    "dnbr_max_minus_mean": 0
  },
  "conflict_resolution": ["<scale>", "<mechanism>", "<window>"],
  "counterfactuals_rejected": ["<weak_source>", "<wrong_window>", "<wrong_mechanism>"],
  "final_label": "<same final label as answer>"
}
```
