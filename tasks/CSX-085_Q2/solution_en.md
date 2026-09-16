# Correct Answer

```json
{
  "answer": "persistent_cyclone_rainfall_with_regional_service_disruption",
  "task_mode": "deep_mechanism_diagnosis",
  "mechanism_question": "diagnose whether cyclone rainfall persistence and service-context evidence dominate over wind-only severity",
  "computed_evidence": {
    "computed_metrics": {
      "gdacs_peak_wind_kmh": 240.7,
      "gdacs_peak_wind_ms": 66.86,
      "gdacs_alert_level": "Red",
      "openmeteo_event_precip_mm": 373.0,
      "nasa_power_event_precip_mm": 388.82,
      "daily_hourly_total_agreement_ratio": 1.042,
      "openmeteo_wettest_72h_mm": 195.3,
      "openmeteo_wettest_24h_mm": 119.0,
      "openmeteo_wet_hours": 185,
      "openmeteo_longest_wet_run_hours": 39,
      "openmeteo_72h_fraction": 0.524,
      "openmeteo_24h_fraction": 0.319,
      "openmeteo_peak_hour_mm": 17.8,
      "openmeteo_peak_hour_fraction": 0.0477,
      "children_affected_million": 6.0,
      "damaged_schools_lower_bound": 850,
      "damaged_health_centres_lower_bound": 550,
      "damaged_service_sites_lower_bound": 1400,
      "service_sites_per_million_children": 233.3,
      "safe_water_disrupted_people_million": 3.0,
      "education_disruption_ratio_to_affected_children": 0.333,
      "flood_landslide_access_report_flags": true
    },
    "component_evidence_scores": {
      "cyclone_rainfall_load": 3,
      "rainfall_persistence": 3,
      "single_hour_dominance_test": 2,
      "reported_service_disruption_load": 2
    },
    "total_evidence_score": 10,
    "final_label": "persistent_cyclone_rainfall_with_regional_service_disruption",
    "one_sentence_interpretation": "The full 10 of 10 evidence synthesis score supports a persistent multi-day cyclone rainfall diagnosis with large reported child-service disruption, not a single-hour burst diagnosis."
  },
  "mechanism_chain": [
    "cyclone rainfall persistence",
    "regional flood loading",
    "service or receptor context",
    "wind-only rejection"
  ],
  "decisive_evidence": "Rainfall persistence and flood-relevant service context should dominate the process explanation.",
  "rejected_simplifications": "Reject wind-only cyclone interpretation if rainfall persistence is the computed flood mechanism.",
  "bounded_interpretation": "Do not convert service context into exact outage duration or complete infrastructure-loss totals."
}
```

# Solving Path

1. Inspect the local package root and identify the event metadata/report plus the quantitative products needed for the mechanism diagnosis.
2. Recompute the required evidence fields rather than copying a table label. The most important fields to recover are: `computed_metrics.gdacs_peak_wind_kmh`, `computed_metrics.gdacs_peak_wind_ms`, `computed_metrics.gdacs_alert_level`, `computed_metrics.openmeteo_event_precip_mm`, `computed_metrics.nasa_power_event_precip_mm`, `computed_metrics.daily_hourly_total_agreement_ratio`, `computed_metrics.openmeteo_wettest_72h_mm`.
3. Use the computed values to build the ordered mechanism chain: cyclone rainfall persistence -> regional flood loading -> service or receptor context -> wind-only rejection.
4. Weight decisive evidence against alternatives: Rainfall persistence and flood-relevant service context should dominate the process explanation.
5. Reject simpler explanations: Reject wind-only cyclone interpretation if rainfall persistence is the computed flood mechanism.
6. Keep the interpretation bounded: Do not convert service context into exact outage duration or complete infrastructure-loss totals.

Key computed anchors from the package:

- `gdacs_peak_wind_kmh` = `240.7`
- `gdacs_peak_wind_ms` = `66.86`
- `gdacs_alert_level` = `Red`
- `openmeteo_event_precip_mm` = `373.0`
- `nasa_power_event_precip_mm` = `388.82`
- `daily_hourly_total_agreement_ratio` = `1.042`
- `openmeteo_wettest_72h_mm` = `195.3`
- `openmeteo_wettest_24h_mm` = `119.0`

# Source Paths

- `metadata/event.json`
- `data/event_reports/event_reports_001_Locked_package_evidence_report.html`
- `data/other/other_001_UNICEF_-_Children_affected_by_Typhoon_Yagi_floods_and_landslides.html`
- `data/event_catalogs/event_catalogs_001_GDACS_event_list_GeoJSON_API.json`
- `data/physical_hazard/physical_hazard_003_Open-Meteo_historical_weather_point_API.json`
- `data/physical_hazard/physical_hazard_004_NASA_POWER_daily_point_weather_API.json`

# Scoring Rubric

Total: 20 points.

- 4 points: `mechanism_diagnosis` - Identifies the dominant physical process and gives the correct compact answer label or an equivalent diagnosis.
- 5 points: `computed_evidence` - Recomputes the quantitative evidence inherited from the original task and preserves units, signs, ratios, and key values.
- 4 points: `evidence_weighting` - Explains which evidence streams are decisive and which are contextual or weaker proxies.
- 3 points: `counterfactual_rejection` - Rejects at least one tempting simplified explanation using the computed values rather than assertion.
- 2 points: `bounded_interpretation` - States scale, timing, proxy, or uncertainty limits without adding unsupported losses or impacts.
- 2 points: `json_contract` - Returns the requested structured mechanism-diagnosis JSON without reducing the answer to a row-only table or same-scale checklist.
