# Correct Answer

```json
{
  "answer": "sustained_marine_heat_stress",
  "bounded_interpretation": "The task does not estimate full coral mortality, fisheries loss, or ecological recovery.",
  "computed_evidence": {
    "evidence_synthesis_values": {
      "crw_core_product_count": 4,
      "crw_core_product_ratio": 1.0,
      "dhw_proxy_c_weeks": 26.143,
      "duration_days": 183,
      "evidence_score": 6,
      "land_counter_passes": 6,
      "sst_anom_hits_2023": 1
    },
    "land_counter_values": {
      "dnbr_abs_mean": 0.066,
      "embedding_mean": 0.023,
      "gpm_peak_mean_ratio": 1.437,
      "land_sample_ratio": 0.251,
      "population_file_share": 0.4,
      "visual_luma_delta_norm": 0.149
    },
    "tolerances": {
      "crw_core_product_ratio": 0.001,
      "dhw_proxy_c_weeks": 0.002,
      "duration_days": 0,
      "evidence_score": 0,
      "land_counter_passes": 0,
      "land_ratios": 0.002,
      "sst_anom_hits_2023": 0
    }
  },
  "decisive_evidence": "SST anomaly and persistence should decide the marine mechanism; land precipitation or exposure is contextual.",
  "formula_derivation": "Use thermal excess times duration, analogous to degree-heating accumulation where supported by package fields.",
  "mechanism_chain": [
    "sea-surface thermal anomaly",
    "duration or persistence",
    "land-context countercheck",
    "marine-stress conclusion"
  ],
  "mechanism_question": "diagnose whether sustained sea-surface thermal stress dominates over land-weather or generic coastal context",
  "rejected_simplifications": "Reject land-weather or generic coastal-impact explanations if marine thermal stress is dominant.",
  "task_mode": "deep_mechanism_diagnosis"
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `evidence_synthesis_values.crw_core_product_count`, `evidence_synthesis_values.crw_core_product_ratio`, `evidence_synthesis_values.dhw_proxy_c_weeks`, `evidence_synthesis_values.duration_days`, `evidence_synthesis_values.evidence_score`, `evidence_synthesis_values.land_counter_passes`, `evidence_synthesis_values.sst_anom_hits_2023`, `land_counter_values.dnbr_abs_mean`.
3. Use the computed values to build the ordered mechanism chain: sea-surface thermal anomaly -> duration or persistence -> land-context countercheck -> marine-stress conclusion.
4. Weight decisive evidence against alternatives: SST anomaly and persistence should decide the marine mechanism; land precipitation or exposure is contextual.
5. Reject simpler explanations: Reject land-weather or generic coastal-impact explanations if marine thermal stress is dominant.
6. Keep the interpretation bounded: The task does not estimate full coral mortality, fisheries loss, or ecological recovery.

Formula/scaling note: Use thermal excess times duration, analogous to degree-heating accumulation where supported by package fields.

Key computed anchors from the package:

- `event` = `{"event_name": "2023 Indian Ocean/Arabian Sea marine heatwave context", "hazard_family": "marine_heatwave_coastal_ecosystem", "hazard_label": "Marine heatwave and coastal ecosystem impact", "location": "Northern Indian Ocean / Arabian Sea",`
- `land_counter_flags` = `{"dnbr_abs_mean_lt_0_10": true, "embedding_mean_lt_0_05": true, "gpm_peak_mean_ratio_lt_1_50": true, "land_sample_ratio_lt_0_30": true, "population_file_share_lt_0_50": true, "visual_luma_delta_norm_lt_0_20": true}`
- `marine_product_hits` = `{"baa7": true, "dhw": true, "hotspot": true, "ssta": true}`
- `raw_context` = `{"event_luma": 144.471, "gpm_max_mm": 152.471, "gpm_mean_mm": 106.104, "land_sample_days": 46, "population_sum": 11398880.519, "pre_luma": 106.506}`
- `threshold_flags` = `{"crw_core_product_count_eq_4": true, "crw_core_product_ratio_eq_1": true, "dhw_proxy_c_weeks_ge_4": true, "duration_days_ge_90": true, "land_counter_passes_ge_5": true, "sst_anom_hits_2023_ge_1": true}`

# Source Paths

- `metadata/event.json`
- `metadata/files.csv`
- `data/event_reports/event_reports_003_Locked_event_anchor_2023_Indian_Ocean_Arabian_Sea_marine_heatwave_context.json`
- `data/other/other_001_NOAA_Coral_Reef_Watch_5km_products.html`
- `data/event_catalogs/event_catalogs_002_NOAA_OISST_PSL_ERDDAP_sea-surface_temperature_THREDDS_catalog_XML.xml`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/exposure_impact/exposure_impact_002_WorldPop_GP_100m_population_sum.json`
- `data/remote_sensing/remote_sensing_002_Google_Satellite_Embedding_annual_cosine-change_stats.json`
- `data/remote_sensing/remote_sensing_003_pre.jpg`
- `data/remote_sensing/remote_sensing_004_event.jpg`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
