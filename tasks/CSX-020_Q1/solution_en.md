# Correct Answer

```json
{
  "answer": "persistent_heat_exposure",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "separate cumulative heat stress from a single peak-temperature story by combining thermal load, persistence, recovery, and contextual evidence",
  "computed_evidence": {
    "heat_evidence_score": "4/4",
    "heat_evidence_synthesis": {
      "hdd35_c_day": 36.9,
      "longest_ge35c_run_days": 6,
      "days_ge40c": 2,
      "p_hdd35_per_100k": 127.2
    },
    "alternative_flags": {
      "rainfall_centered": false,
      "broad_surface_change": false
    },
    "peak_tmax": {
      "date": "2020-01-04",
      "c": 42.2
    }
  },
  "mechanism_chain": [
    "event-window thermal forcing",
    "accumulated heat-load calculation",
    "persistence or recovery constraint",
    "non-heat alternative rejection"
  ],
  "decisive_evidence": "Accumulated heat load, duration, and exposure scaling carry the mechanism decision; rainfall or image signals only test competing explanations.",
  "rejected_simplifications": "Reject peak-only, rainfall-led, and image-primary explanations when the computed heat-load chain is stronger.",
  "bounded_interpretation": "The result is a package-scale heat mechanism diagnosis, not exact mortality, outage, damage, or full regional attribution.",
  "formula_derivation": "Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `heat_evidence_score`, `heat_evidence_synthesis.hdd35_c_day`, `heat_evidence_synthesis.longest_ge35c_run_days`, `heat_evidence_synthesis.days_ge40c`, `heat_evidence_synthesis.p_hdd35_per_100k`, `alternative_flags.rainfall_centered`, `alternative_flags.broad_surface_change`, `peak_tmax.date`.
3. Use the computed values to build the ordered mechanism chain: event-window thermal forcing -> accumulated heat-load calculation -> persistence or recovery constraint -> non-heat alternative rejection.
4. Weight decisive evidence against alternatives: Accumulated heat load, duration, and exposure scaling carry the mechanism decision; rainfall or image signals only test competing explanations.
5. Reject simpler explanations: Reject peak-only, rainfall-led, and image-primary explanations when the computed heat-load chain is stronger.
6. Keep the interpretation bounded: The result is a package-scale heat mechanism diagnosis, not exact mortality, outage, damage, or full regional attribution.

Formula/scaling note: Derive heat load as sum(max(T - T_ref, 0)); if exposure is used, scale it as heat_load * exposed_population / 100000 and explain the units.

Key computed anchors from the package:

- `event_name` = `2019-2020 Australian extreme heat during Black Summer`
- `hdd35_c_day` = `36.9`
- `days_ge35c` = `16`
- `days_ge40c` = `2`
- `longest_ge35c_run` = `{"days": 6, "start": "2019-12-27", "end": "2020-01-01"}`
- `peak_tmax` = `{"date": "2020-01-04", "c": 42.2}`
- `population` = `344721.75821224134`
- `p_hdd35_per_100k` = `127.2`

# Source Paths

- `metadata/event.json`
- `data/physical_hazard/physical_hazard_001_Open-Meteo_historical_archive.json`
- `data/exposure_impact/exposure_impact_004_WorldPop_GP_100m_population_sum.json`
- `data/physical_hazard/physical_hazard_004_GPM_IMERG_V07_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_006_CHIRPS_daily_event_accumulated_precipitation.json`
- `data/physical_hazard/physical_hazard_008_Sentinel-2_SR_Harmonized_dNBR.json`
- `data/remote_sensing/remote_sensing_003_Google_Satellite_Embedding_annual_cosine-change_stats.json`

# Scoring Rubric

Total: 20 points.

- 3 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact mechanism label or equivalent diagnosis.
- 4 points: `computed_evidence` - Recomputes the package-derived quantitative evidence with correct units, signs, ratios, dates, and rounding.
- 3 points: `formula_derivation` - Shows the requested physical formula, scaling relation, or timing relation and connects it to the computed values.
- 3 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects tempting simplified explanations using computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table.
