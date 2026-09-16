# Final Answer

```json
{
  "answer_type": "remote_sensing_change_attribution",
  "claim": "direct_package_evidence_of_localized_burn_scar_change",
  "ruling": "direct_dnbr_supports_localized_burn_change_but_not_exact_area_or_impact",
  "selected_evidence": {
    "path": "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json",
    "modality": "COPERNICUS/S2_SR_HARMONIZED dNBR",
    "pre_window": [
      "2019-10-02",
      "2019-11-24"
    ],
    "post_window": [
      "2019-12-01",
      "2020-02-29"
    ],
    "post_window_overlap_with_event_days": 62,
    "post_window_extra_days_after_event": 29,
    "stats": {
      "dnbr_max": 0.952729,
      "dnbr_mean": 0.048872,
      "dnbr_min": -1.536823,
      "dnbr_stdDev": 0.081789
    }
  },
  "calculation_check": {
    "event_window_days": 62,
    "dnbr_max_minus_mean": 0.903857,
    "dnbr_max_over_mean": 19.494223,
    "dnbr_max_z_like_above_mean": 11.051036
  },
  "rejected_or_insufficient_alternatives": {
    "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json": {
      "role_error": "generic annual embedding change for 2018-to-2019, not a dNBR burn-index product and not isolated to the official event/post-fire window",
      "numeric_consequence_if_swapped": {
        "wrong_metric_max": 0.493836,
        "wrong_metric_mean": 0.028207,
        "wrong_max_minus_selected_dnbr_max": -0.458894,
        "wrong_mean_minus_selected_dnbr_mean": -0.020666
      }
    },
    "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json": {
      "role_error": "local heat and humidity can support fire-weather context but cannot measure burn scar or surface change",
      "numeric_consequence_if_swapped": {
        "hourly_max_temperature_c": 42.2,
        "relative_humidity_at_hourly_tmax_percent": 8
      }
    }
  },
  "source_paths": {
    "event_window": "data/event_reports/event_reports_003_Locked_event_anchor_2019-2020_Australian_extreme_heat_during_Black_Summer.json",
    "direct_burn_change": "data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json",
    "rejected_embedding_change": "data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json",
    "fire_weather_context_only": "data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json"
  },
  "reference_trace": [
    "Read the locked event anchor and take the official window as 2019-12-01 through 2020-01-31, inclusive.",
    "Inspect the Sentinel-2 dNBR file and verify that its post window 2019-12-01 through 2020-02-29 overlaps all 62 official event days.",
    "Compute dNBR contrast from the Sentinel-2 stats: max minus mean = 0.903857, max over mean = 19.494223, and z-like contrast = 11.051036.",
    "Reject the annual embedding change as a generic 2018-to-2019 cosine-change product and reject Open-Meteo as fire-weather context only."
  ]
}
```

# Key Computations

The official event window from `data/event_reports/event_reports_003_Locked_event_anchor_2019-2020_Australian_extreme_heat_during_Black_Summer.json` is 2019-12-01 through 2020-01-31, which is 62 inclusive days. The Sentinel-2 dNBR post window is 2019-12-01 through 2020-02-29, so it overlaps all 62 event days and adds 29 days after the official event window.

From `data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json`, the dNBR statistics are max 0.952729437828137, mean 0.04887239978486732, min -1.5368227226185045, and stdDev 0.0817893456398192. The required compact calculations are:

- `dnbr_max_minus_mean = 0.952729437828137 - 0.04887239978486732 = 0.903857`
- `dnbr_max_over_mean = 0.952729437828137 / 0.04887239978486732 = 19.494223`
- `dnbr_max_z_like_above_mean = 0.9038570380432697 / 0.0817893456398192 = 11.051036`

The annual embedding file has `alphaearth_1_minus_cosine_max = 0.49383584706500205` and `alphaearth_1_minus_cosine_mean = 0.02820651202978197`. If swapped into the answer as though it were dNBR, the max would be lower than the selected dNBR max by -0.458894 and the mean would be lower by -0.020666, but the stronger reason for rejection is role and temporal mismatch.

# Reference Solving Trace

1. Inspect the event anchor JSON for the official temporal window.
2. Inspect the package remote-sensing and physical-hazard files for candidate products.
3. Select the Sentinel-2 dNBR JSON because it is the direct burn-index product and its post window overlaps the event window.
4. Compute inclusive event-window overlap and dNBR contrast values.
5. Reject the annual embedding product as generic annual change and reject Open-Meteo as context-only heat/humidity evidence.

# Scoring Rubric

- 3 points: Returns the requested JSON schema with the fixed answer type, claim, ruling, selected evidence, calculation check, rejected alternatives, source paths, and reference trace.
- 4 points: Selects `data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json` as the direct burn-change source and reports the product modality and pre/post windows correctly.
- 3 points: Computes temporal alignment correctly: 62 event days, 62 days of dNBR post-window overlap with the event, and 29 extra post-event days.
- 4 points: Reports dNBR stats and contrast calculations correctly, allowing small rounding tolerance for the six-decimal values.
- 3 points: Rejects the annual embedding change source for the correct role and temporal reasons and reports the numeric consequence of the source swap.
- 2 points: Treats the Open-Meteo heat/humidity file as fire-weather context only, not as remote-sensing or burn-scar evidence.
- 1 point: Uses package-relative paths only and does not use external sources, hidden answers, broad disaster prose, or external burn-severity thresholds.
