# Final Answer

Correct answer: `all_five_tests_pass`.

```json
{
  "target_family": "pakistan_indus_2010_rainfall_routing_storage_process_chain",
  "process_chain": [
    {"stage": "event_window_rainfall_load", "role": "meteorological_input", "computed_values": {"duration_days": 36, "event_total_mm": 347.8, "daily_mean_mm_per_day": 9.661, "wet_days_ge_1mm": 15, "longest_wet_spell_days_ge_1mm": 9}},
    {"stage": "peak_window_persistence_test", "role": "temporal_concentration_check", "computed_values": {"max_7day_total_mm": 219.9, "max_7day_start": "2010-08-02T06:00", "max_7day_fraction_of_total": 0.632}},
    {"stage": "multi_product_precipitation_consensus", "role": "cross_source_precipitation_constraint", "computed_values": {"grid_consensus_mean_mm": 215.4, "grid_spread_fraction": 0.149, "average_max_to_mean_ratio": 1.84, "july_anomaly_pct": 70, "august_anomaly_pct": 102, "august_to_july_anomaly_ratio": 1.457, "mean_monthly_anomaly_pct": 86.0}},
    {"stage": "routing_storage_sequence_flags", "role": "river_routing_and_storage_amplification", "computed_values": {"southward_surge": true, "sindh_diversion": true, "manchhar_lake": true, "slow_retreat": true, "storage_or_low_drainage": true, "all_sequence_flags_true": true}},
    {"stage": "reported_impact_normalization", "role": "reported_burden_context", "computed_values": {"flood_extent_sq_km": 37280, "extent_window_days": 51, "affected_people_million_lower_bound": 18.0, "extent_per_million_affected_sq_km": 2071.1, "deaths_per_million_affected": 110.278, "houses_per_affected_person": 0.0944, "cotton_crop_flooded_pct": 10, "rice_crop_flooded_pct": 20}}
  ],
  "process_tests": [
    {"row_id": "event_window_rainfall_load", "formula": "duration = end - start + 1; daily_mean = event_total / duration; pass if duration = 36 days, event_total > 300 mm, wet_days >= 10, and longest_wet_spell >= 7 days", "computed_values": {"duration_days": 36, "event_total_mm": 347.8, "daily_mean_mm_per_day": 9.661, "wet_days_ge_1mm": 15, "longest_wet_spell_days_ge_1mm": 9}, "threshold_state": "pass", "rejected_alternative": "single_day_burst"},
    {"row_id": "peak_window_persistence_test", "formula": "max_7day_fraction = max_168h_total / event_total", "computed_values": {"max_7day_total_mm": 219.9, "max_7day_start": "2010-08-02T06:00", "max_7day_fraction_of_total": 0.632}, "threshold_state": "pass", "rejected_alternative": "wettest_week_only"},
    {"row_id": "multi_product_precipitation_consensus", "formula": "mean product total, normalized spread, max/mean concentration, and monthly anomaly ratios", "computed_values": {"grid_consensus_mean_mm": 215.4, "grid_spread_fraction": 0.149, "average_max_to_mean_ratio": 1.84, "july_anomaly_pct": 70, "august_anomaly_pct": 102, "august_to_july_anomaly_ratio": 1.457, "mean_monthly_anomaly_pct": 86.0}, "threshold_state": "pass", "rejected_alternative": "single_product_proof"},
    {"row_id": "routing_storage_sequence_flags", "formula": "all_sequence_flags_true = southward_surge AND sindh_diversion AND manchhar_lake AND slow_retreat AND storage_or_low_drainage", "computed_values": {"southward_surge": true, "sindh_diversion": true, "manchhar_lake": true, "slow_retreat": true, "storage_or_low_drainage": true, "all_sequence_flags_true": true}, "threshold_state": "pass", "rejected_alternative": "downstream_storage_only_trigger"},
    {"row_id": "reported_impact_normalization", "formula": "extent and reported impacts normalized by affected population and event window", "computed_values": {"flood_extent_sq_km": 37280, "extent_window_days": 51, "affected_people_million_lower_bound": 18.0, "extent_per_million_affected_sq_km": 2071.1, "deaths_per_million_affected": 110.278, "houses_per_affected_person": 0.0944, "cotton_crop_flooded_pct": 10, "rice_crop_flooded_pct": 20}, "threshold_state": "pass", "rejected_alternative": "raw_impact_counts_only"}
  ],
  "proof_conclusion": "All five tests pass: persistent monsoon rainfall was routed southward through the Indus system and remained amplified by downstream storage."
}
```

# Key Computations

Duration is `36` days and daily mean rainfall is `347.8 / 36 = 9.661 mm/day`. The wettest seven-day window is `219.9 mm` from `2010-08-02T06:00`, or `219.9 / 347.8 = 0.632` of the event total. Multi-product consensus is `(197.9 + 218.2 + 230.1) / 3 = 215.4 mm`, and spread is `(230.1 - 197.9) / 215.4 = 0.149`.

The monthly anomaly ratio is `102 / 70 = 1.457`; the mean monthly anomaly is `86.0%`. Impact normalization gives `37280 / 18.0 = 2071.1 sq km per million affected`, `1985 / 18.0 = 110.278 deaths per million affected`, and `1.7e6 / 18.0e6 = 0.0944 houses per affected person`.

# Reasoning Path

The answer is not a one-row rainfall calculation. It requires a chain: persistent event-window rainfall, a strong but not exclusive peak week, multi-product precipitation agreement, a southward routing and storage sequence, and normalized reported burden. All five process tests pass, so the chain supports a rainfall-routing-storage proof rather than a single-day or downstream-storage-only explanation.

# Scoring Rubric

Total: 20 points.

- 3 points: Returns the target family, five process-chain stages, five process tests, computed values, rejected alternatives, and proof conclusion. Partial credit for a complete structure missing one row.
- 4 points: Reconstructs rainfall-window values correctly: 36 days, 347.8 mm, 9.661 mm/day, 15 wet days, and 9-day wet spell. Partial credit for mostly correct rainfall values with one missing metric.
- 3 points: Computes the peak-window persistence values correctly: 219.9 mm, `2010-08-02T06:00`, 0.632, and rejection of wettest-week-only reasoning. Partial credit for the peak total without the fraction or timestamp.
- 4 points: Computes multi-product precipitation consensus correctly: 215.4 mm, 0.149 spread, 1.84 concentration, 70%, 102%, 1.457, and 86.0%. Partial credit for correct consensus with one missing anomaly value.
- 3 points: Identifies all routing-storage flags and the all-true conjunction. Partial credit for at least three correct flags.
- 2 points: Normalizes reported impact correctly using extent, affected population, deaths, houses, and crop percentages. Partial credit for raw counts without normalization.
- 1 point: Keeps the conclusion concise and tied to the computed process chain.
