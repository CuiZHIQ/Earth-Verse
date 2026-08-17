# Correct Answer

```json
{
  "answer": "persistent_monsoon_wetting_mountain_flood_landslide_chain_supported",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "diagnose whether persistent rainfall over steep terrain supports a flood, debris, or landslide hazard chain rather than a short shower",
  "computed_evidence": {
    "required_tests": [
      "rainfall_window",
      "peak_burst_test",
      "grid_report_test",
      "terrain_report_test"
    ],
    "key_metrics": {
      "wettest_72h_share": 0.818,
      "wet_hour_fraction": 0.8125,
      "heavy_hour_share": 0.244,
      "wettest_24h_to_72h_ratio": 0.541,
      "outside_24h_share": 0.557,
      "max_daily_to_mean_daily": 1.272,
      "gpm_to_report_marker": 0.226,
      "chirps_to_report_marker": 0.166,
      "terrain_flag_count": 3
    },
    "tolerances": {
      "ratio": 0.005,
      "rate": 0.005,
      "rainfall_mm": 0.1
    }
  },
  "mechanism_chain": [
    "persistent mountain rainfall",
    "terrain-enhanced runoff or slope response",
    "flood-landslide pathway",
    "short-burst simplification rejection"
  ],
  "decisive_evidence": "Duration and mountain-process context should dominate over a single local precipitation value.",
  "rejected_simplifications": "Reject a short convective shower or flat-basin explanation if terrain and persistence are required by the evidence.",
  "bounded_interpretation": "The answer should not infer complete landslide inventories, exact valley hydraulics, or all losses."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `required_tests`, `key_metrics.wettest_72h_share`, `key_metrics.wet_hour_fraction`, `key_metrics.heavy_hour_share`, `key_metrics.wettest_24h_to_72h_ratio`, `key_metrics.outside_24h_share`, `key_metrics.max_daily_to_mean_daily`.
3. Use the computed values to build the ordered mechanism chain: persistent mountain rainfall -> terrain-enhanced runoff or slope response -> flood-landslide pathway -> short-burst simplification rejection.
4. Weight decisive evidence against alternatives: Duration and mountain-process context should dominate over a single local precipitation value.
5. Reject simpler explanations: Reject a short convective shower or flat-basin explanation if terrain and persistence are required by the evidence.
6. Keep the interpretation bounded: The answer should not infer complete landslide inventories, exact valley hydraulics, or all losses.

Key computed anchors from the package:

- `event_precip_mm` = `133.3`
- `event_window_hours` = `96`
- `wettest_72h_mm` = `109.0`
- `wettest_24h_mm` = `59.0`
- `wet_hours` = `78`
- `heavy_hours_ge_3mm` = `19`
- `gpm_grid_max_mm` = `67.895`
- `chirps_grid_max_mm` = `49.763`

# Source Paths

- `data/event_reports/event_reports_004_NASA_Earth_Observatory_-_Severe_flooding_in_Northern_India_and_Nepal.html`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`
- `data/physical_hazard/physical_hazard_009_chirps_event_precip.tif`
- `data/physical_hazard/physical_hazard_011_gpm_imerg_event_precip.tif`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
