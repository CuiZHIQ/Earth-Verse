# Barren Island Ash-Plume Research Synthesis

You are preparing a research-grade volcanic-hazard synthesis note for the 2010 Barren Island ash-plume package. The task is not to perform a simple date check or choose one hazard label. The task is to behave like a geoscience researcher working with an incomplete local evidence package: formulate competing hypotheses, compute the available evidence, separate source mechanism from receptor context, identify validation gaps, and state a bounded research conclusion.

Use only the local event package. Inspect the package root, choose the evidence files yourself, compute intermediate values, and keep every cited path package-relative. Do not use web search or outside reports.

Your analysis must test four hypotheses:

- `H1_volcanic_source_observation`: the package supports a source-proximal volcanic ash observation.
- `H2_rainfall_weather_displacement`: rainfall or local weather should displace the ash-source interpretation.
- `H3_surface_change_reconnaissance`: radar/optical pre/post change evidence can carry the primary conclusion.
- `H4_regional_exposure_primary_response`: regional receptor exposure should dominate the scientific interpretation.

Required computations and synthesis:

1. Extract report-supported source evidence: ash-plume phrase, Barren Island/Andaman Sea place support, ALI/EO-1 instrument support, and the report's remote/uninhabited observation context.
2. Compute `date_offset_days = report_acquisition_date - locked_anchor_date`.
3. Compute precipitation counter-evidence:
   - `point_precip_mean_mm = mean(NASA_POWER_precip_mm, Open-Meteo_precip_mm)`
   - `regional_peak_precip_mm = max(ERA5-Land event max, GPM event max, CHIRPS event max)`
   - `regional_mean_precip_mm = mean(ERA5-Land event mean, GPM event mean, CHIRPS event mean)`
   - `peak_to_point_ratio = regional_peak_precip_mm / point_precip_mean_mm`
   - `rain_change_gate_score = count(point_precip_mean_mm >= 25, regional_peak_precip_mm >= 100, date_offset_days <= 3, change_scene_total >= 1)`
4. Compute surface-observability evidence by summing Sentinel-1 and Sentinel-2 pre/post scene counts.
5. Compute exposure-context evidence using package-derived population, AOI area, population density, road elements, and bounded-AOI amenity elements. For the compact AOI polygon, use `aoi_area_km2 = (lon_span * 111.320 * cos(mean_latitude)) * (lat_span * 110.574)` and `population_density_per_km2 = population / aoi_area_km2`.
6. Build a confidence and validation model:
   - `report_support_fraction = report_support_count / 4`
   - `date_alignment_score = max(0, 1 - date_offset_days / 30)`
   - `temporal_conflict_severity = min(date_offset_days / 30, 1)`
   - `rain_context_score = rain_change_gate_score / 4`
   - `change_observability_score = min(change_scene_total / 2, 1)`
   - `exposure_context_score = mean(min(log10(population) / 7, 1), min(amenity_elements / 1000, 1), min(road_elements / 250, 1))`
   - `source_mechanism_confidence = 0.55 * report_support_fraction + 0.20 * (1 - rain_context_score) + 0.10 * (1 - change_observability_score) + 0.15 * date_alignment_score`
   - `validation_need_score = mean(temporal_conflict_severity, 1 - change_observability_score)`
7. Perform scenario sensitivity:
   - strict same-day consistency;
   - rainfall-displacement threshold margin;
   - surface-change observability failure;
   - report-anchor removal.
8. Provide a validation plan that explains what evidence would be needed to turn the bounded conclusion into a cleaner research claim.

Return one JSON object with exactly these top-level fields:

```json
{
  "answer": "",
  "research_hypotheses": {},
  "computed_evidence": {},
  "support_flags": {},
  "rain_gate_tests": {},
  "confidence_model": {},
  "scenario_sensitivity": {},
  "causal_synthesis": [],
  "uncertainty_and_validation": {},
  "source_roles": {},
  "final_research_conclusion": ""
}
```
