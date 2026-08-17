# Correct Answer

```json
{
  "answer": "dual_pulse_areal_accumulation",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "reconstruct how rainfall concentration translates into pluvial or urban runoff pressure rather than a generic wet-period label",
  "computed_evidence": {
    "hourly_peak_mm": 201.9,
    "event_window": "2021-07-17/2021-07-23",
    "rainfall_mm": {
      "gpm": {
        "mean_mm": 426.1,
        "max_mm": 484.255
      },
      "chirps": {
        "mean_mm": 256.635,
        "max_mm": 307.595
      },
      "era5_land": {
        "mean_mm": 214.341,
        "max_mm": 261.561
      }
    },
    "peak_to_mean": {
      "gpm": 0.474,
      "chirps": 0.787,
      "era5_land": 0.942
    },
    "mean_to_max": {
      "gpm": 0.88,
      "chirps": 0.834,
      "era5_land": 0.819
    },
    "diagnostic_diagnostic_tests": {
      "peak_to_mean_max": 0.9,
      "mean_min_mm": 200.0,
      "max_min_mm": 250.0,
      "mean_to_max_min": 0.8
    },
    "diagnostic_diagnostic_test_proof": {
      "max_peak_to_mean_ge_0_900": true,
      "all_means_ge_200_mm": true,
      "all_maxima_ge_250_mm": true,
      "all_mean_to_max_ge_0_800": true
    }
  },
  "mechanism_chain": [
    "rainfall burst or accumulation",
    "duration/intensity or areal-load calculation",
    "urban runoff or receptor context",
    "single-number simplification rejection"
  ],
  "decisive_evidence": "Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.",
  "rejected_simplifications": "Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.",
  "bounded_interpretation": "The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals.",
  "formula_derivation": "When converting rainfall to runoff pressure, use V = rainfall_mm / 1000 * area_m2 and explain any runoff coefficient or normalized index."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `hourly_peak_mm`, `event_window`, `rainfall_mm.gpm.mean_mm`, `rainfall_mm.gpm.max_mm`, `rainfall_mm.chirps.mean_mm`, `rainfall_mm.chirps.max_mm`, `rainfall_mm.era5_land.mean_mm`, `rainfall_mm.era5_land.max_mm`.
3. Use the computed values to build the ordered mechanism chain: rainfall burst or accumulation -> duration/intensity or areal-load calculation -> urban runoff or receptor context -> single-number simplification rejection.
4. Weight decisive evidence against alternatives: Rainfall concentration and areal or urban-response evidence should dominate; exposure and image products are supporting context.
5. Reject simpler explanations: Reject a one-gauge, one-hour, exposure-only, or image-primary explanation if the computed rainfall-runoff chain is stronger.
6. Keep the interpretation bounded: The task diagnoses flood pressure and process, not exact inundation depth, building damage, or final loss totals.

Formula/scaling note: When converting rainfall to runoff pressure, use V = rainfall_mm / 1000 * area_m2 and explain any runoff coefficient or normalized index.

Key computed anchors from the package:

- Recompute the numeric fields shown in the answer JSON from the package sources.

# Source Paths

- `data/event_reports/event_reports_002_Wikipedia_2021_Henan_floods.json`
- `data/event_reports/event_reports_003_Locked_event_anchor_July_2021_Henan_Zhengzhou_extreme_rainfall_and_flood.json`
- `data/physical_hazard/physical_hazard_002_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
