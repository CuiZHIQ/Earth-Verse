# Heat-Health Exposure Denominator Audit

A benchmark reviewer is auditing whether a heat-health exposure answer for the
2015 India-Pakistan heat wave used the correct denominator. Use only
package-local CSX-004 evidence. Do not use web search, hidden answers from other
tasks, or invented values.

Your task is to couple the regional heat context to the AOI exposure evidence,
compute the heat-health service asset density, and reject denominator or
numerator shortcuts that are not population-scaled exposure evidence.

Rules:

- Use package-relative source paths only.
- Use the package event window from the locked event anchor.
- Use ERA5-Land aggregate stats only as regional heat context, not as an
  exposure denominator.
- Count heat-health service assets from the bounded OSM AOI slice using these
  `amenity` categories only: `hospital`, `school`, `police`, `shelter`,
  `fire_station`.
- Use WorldPop `population_sum.population` as the denominator for an
  assets-per-million-people rate.
- Report the counterfactual effect of two tempting mistakes: using all OSM
  elements as the denominator, and using the smaller Overpass slice as the
  numerator.
- Report why deaths from the India and Pakistan report anchors are impact
  context, not the denominator for service exposure density.
- Round temperatures, population in millions, rates, ratios, and differences to
  2 decimals. Round the OSM feature fraction to 3 decimals.

Return compact JSON only with this exact schema:

```json
{
  "answer_type": "denominator_scale_audit",
  "decision": "<population_denominator_required_for_service_exposure_rate|other>",
  "source_paths": {
    "event_anchor": "<package-relative path>",
    "regional_heat": "<package-relative path>",
    "population_denominator": "<package-relative path>",
    "asset_numerator": "<package-relative path>",
    "smaller_overpass_candidate": "<package-relative path>",
    "india_report_context": "<package-relative path>",
    "pakistan_report_context": "<package-relative path>",
    "manifest": "<package-relative path>"
  },
  "event_window": {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD",
    "days_inclusive": 0
  },
  "regional_heat_context": {
    "dataset": "<dataset>",
    "temperature_2m_max_c_max": 0.0,
    "temperature_2m_max_c_mean": 0.0,
    "temperature_2m_max_c_min": 0.0
  },
  "selected_exposure_inputs": {
    "population": 0.0,
    "population_m": 0.0,
    "asset_category_counts": {
      "hospital": 0,
      "school": 0,
      "police": 0,
      "shelter": 0,
      "fire_station": 0
    },
    "heat_health_assets": 0,
    "selected_osm_elements": 0
  },
  "calculations": {
    "assets_per_million_people": 0.0,
    "residents_per_heat_health_asset": 0.0
  },
  "counterfactual_audit": {
    "osm_elements_as_denominator": {
      "wrong_denominator": 0,
      "wrong_fraction": 0.0,
      "error_class": "<short error class>"
    },
    "smaller_overpass_as_numerator": {
      "wrong_assets": 0,
      "wrong_assets_per_million_people": 0.0,
      "undercount_assets": 0,
      "selected_to_wrong_asset_ratio": 0.0,
      "error_class": "<short error class>"
    },
    "reported_deaths_as_denominator": {
      "india_deaths": 0,
      "pakistan_deaths": 0,
      "combined_reported_deaths": 0,
      "why_rejected": "<short reason>"
    }
  },
  "minimal_evidence_set": [
    "<package-relative path>"
  ],
  "ruling": "<population_scaled_exposure_density_supported|insufficient_evidence|wrong_denominator>",
  "reference_trace": [
    "<short reproducible step>"
  ]
}
```
