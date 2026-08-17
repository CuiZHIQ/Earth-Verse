# ENSO-Driven Island Drought Response Pressure Model

Use only the local CSX-171 event package. Select package-relative evidence for every value used.

Develop a compact disaster-science model for the 2015-2016 El Nino drought impacts, focusing on how an ocean-atmosphere circulation shift translated into western Pacific freshwater stress and health-response pressure. Your answer must synthesize multiple independent package evidence streams and make their roles clear in `source_paths`.

Compute the following quantities from discovered package evidence:

1. Reconstruct the event window length in inclusive days.
2. From the western Pacific island drought narrative, extract Koror's observed rainfall since January, rainfall deficit, and record-depth context. Compute:
   - `koror_normal_inches = observed_inches + deficit_inches`
   - `observed_fraction_normal = observed_inches / koror_normal_inches`
   - `deficit_fraction_normal = deficit_inches / koror_normal_inches`
   - `record_depth_norm = min(record_years / 75, 1)`
3. Use the physical hazard precipitation summaries for the common short precipitation slice. This package slice is an early-window moisture offset, not proof of later recovery. Compute inclusive slice days, each product's mean daily precipitation rate, the multi-product daily mean, and:
   - `wet_slice_pct_window = 100 * wet_slice_days / event_window_days`
   - `wet_pulse_relief_credit = 15 * min((wet_slice_pct_window / 15), 1) * min((multisensor_daily_mean_mm / 6), 1)`
4. Use the drought-process report text to support a mechanism chain. Count four binary mechanism markers: shifted Walker circulation, rainfall displaced farther east, western Pacific drying, and positive outgoing-longwave/clearer-sky evidence. Compute `mechanism_support_score = 100 * true_marker_count / 4`.
5. Use catalog and gridded exposure data to compute:
   - `exposure_ratio = catalog_people_at_risk / gridded_population`
   - `exposure_norm = min(exposure_ratio, 1)`
6. Use local critical-facility context to count schools and hospitals in the populated AOI sample. Compute `critical_facility_norm = min((school_count + hospital_count) / 10, 1)`.
7. Use the health-response report to compute:
   - `health_gap_musd = health_sector_need_musd - who_requirement_musd`
   - `health_gap_fraction = health_gap_musd / health_sector_need_musd`
   - `who_requirement_share_pct = 100 * who_requirement_musd / health_sector_need_musd`
8. Derive:
   - `local_freshwater_stress_score = 100 * (0.50 * deficit_fraction_normal + 0.20 * record_depth_norm + 0.15 * dam_storage_failure_flag + 0.15 * rationing_flag)`
   - `duration_persistence_norm = min(event_window_days / 426, 1)`
   - `operational_response_pressure_index = 100 * (0.25 * local_freshwater_stress_score / 100 + 0.15 * mechanism_support_score / 100 + 0.15 * duration_persistence_norm + 0.20 * exposure_norm + 0.15 * health_gap_fraction + 0.10 * critical_facility_norm) - wet_pulse_relief_credit`
9. Run a delayed-recovery scenario in which drought-related health impacts persist 60 days beyond the package event window and the short precipitation-slice moisture offset is not operationally effective:
   - `scenario_duration_norm = min((event_window_days + 60) / 426, 1)`
   - `delayed_recovery_pressure_index` uses the same pressure-index formula, with `scenario_duration_norm` replacing `duration_persistence_norm` and `wet_pulse_relief_credit = 0`
   - `scenario_delta = delayed_recovery_pressure_index - operational_response_pressure_index`
10. Use the remote-sensing evidence to state whether paired optical change analysis is supported. Do not infer surface-change magnitude if paired scenes are unavailable.

Return a single JSON object with exactly these top-level keys:

```json
{
  "source_paths": {},
  "process_model": {},
  "computed_metrics": {},
  "scenario_analysis": {},
  "remote_sensing_constraint": {},
  "final_interpretation": ""
}
```

Round percentages and index values to one decimal, rainfall rates to two decimals, ratios and fractions to three decimals, and population counts to whole people.
