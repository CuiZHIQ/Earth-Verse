# Correct Answer

```json
{
  "answer": "localized_coseismic_patchy_change",
  "bounded_interpretation": "The task does not estimate complete landslide inventory, fatalities, building fragility, or macroseismic intensity maps.",
  "computed_evidence": {
    "evidence_synthesis": [
      {
        "diagnostic_diagnostic_test_result": "pass",
        "evidence_score": 5,
        "row": "ground_motion",
        "values": {
          "alert": "red",
          "depth_km": 19.0,
          "magnitude": 6.8,
          "mmi": 8.459,
          "tsunami_flag": 0
        }
      },
      {
        "diagnostic_diagnostic_test_result": "pass",
        "evidence_score": 3,
        "row": "radar_patchiness",
        "values": {
          "extreme_abs_db": 14.5134,
          "extreme_to_mean": 160.4,
          "extreme_to_sd": 27.2,
          "mean_db": -0.0905
        }
      },
      {
        "diagnostic_diagnostic_test_result": "pass",
        "evidence_score": 3,
        "row": "embedding_patchiness",
        "values": {
          "max": 0.56693,
          "max_to_mean": 62.3,
          "max_to_sd": 55.7,
          "mean": 0.0091
        }
      },
      {
        "diagnostic_diagnostic_test_result": "pass",
        "evidence_score": 4,
        "row": "rainfall_split",
        "values": {
          "chirps_mean_mm": 17.87,
          "field_to_point": 2676.5,
          "gpm_mean_mm": 11.9,
          "point_max_mm": 0.02
        }
      },
      {
        "diagnostic_diagnostic_test_result": "pass",
        "evidence_score": 3,
        "row": "settlement_context",
        "values": {
          "buildings": 510,
          "highways": 380,
          "population": 229886
        }
      }
    ],
    "final_label": "localized_coseismic_patchy_change",
    "one_sentence_numeric_note": "All five component scores meet their gates, giving 18 total points and the localized coseismic patchy-change label.",
    "total_evidence_score": 18
  },
  "decisive_evidence": "Magnitude, depth, and coseismic patchiness carry the decision; precipitation and image context are only checks.",
  "mechanism_chain": [
    "earthquake magnitude/depth anchor",
    "seismic dominance or patchiness metric",
    "secondary product checks",
    "non-seismic rejection"
  ],
  "mechanism_question": "diagnose whether seismic forcing and patchy coseismic response dominate over weather or generic exposure context",
  "rejected_simplifications": "Reject rainfall-trigger, weather, or image-only explanations if seismic evidence is dominant.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `evidence_synthesis`, `final_label`, `one_sentence_numeric_note`, `total_evidence_score`.
3. Use the computed values to build the ordered mechanism chain: earthquake magnitude/depth anchor -> seismic dominance or patchiness metric -> secondary product checks -> non-seismic rejection.
4. Weight decisive evidence against alternatives: Magnitude, depth, and coseismic patchiness carry the decision; precipitation and image context are only checks.
5. Reject simpler explanations: Reject rainfall-trigger, weather, or image-only explanations if seismic evidence is dominant.
6. Keep the interpretation bounded: The task does not estimate complete landslide inventory, fatalities, building fragility, or macroseismic intensity maps.

Key computed anchors from the package:

- `final_label` = `localized_coseismic_patchy_change`
- `ground_motion` = `{"alert": "red", "depth_km": 19.0, "magnitude": 6.8, "maximum_mmi": 8.459, "tsunami_flag": 0}`
- `rainfall` = `{"chirps_max_mm": 35.23162078857422, "chirps_mean_mm": 17.865958361222006, "era5_max_mm": 16.724616289138794, "field_max_mm": 53.52999888546765, "field_to_point": 2676.5, "gpm_max_mm": 53.52999888546765, "gpm_mean_mm": 11.904448432723646, "`
- `remote_sensing` = `{"alpha_max": 0.5669277187181874, "alpha_max_to_mean": 62.3, "alpha_max_to_sd": 55.7, "alpha_mean": 0.009096545927515817, "alpha_stddev": 0.01018414858586108, "s1_extreme_abs_db": 14.513397461953051, "s1_extreme_to_mean": 160.4, "s1_extreme`
- `settlement` = `{"amenities": 21, "buildings": 510, "highways": 380, "population": 229885.5132449541, "waterways": 89}`
- `total_score` = `18`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_002_Locked_event_anchor_2023_Morocco_Al_Haouz_earthquake.json`
- `data/event_catalogs/event_catalogs_004_USGS_event_GeoJSON_us7000kufc.json`
- `data/remote_sensing/remote_sensing_004_Sentinel-1_GRD_VV_pre_post_change.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/physical_hazard/physical_hazard_003_ERA5-Land_hourly_aggregate_stats.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_005_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_daily_point_sample.json`
- `data/physical_hazard/physical_hazard_002_NASA_POWER_daily_point_sample.json`
- `data/exposure_impact/exposure_impact_003_WorldPop_GP_100m_population_sum.json`
- `data/exposure_impact/exposure_impact_004_OpenStreetMap_Overpass_bounded_AOI_slice.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
