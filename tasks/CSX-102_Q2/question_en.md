# Pakistan Indus 2010 Rainfall-Routing-Storage Process Chain

You are a hydrologic process analyst reconstructing the late July-August 2010 Pakistan Indus River flood. The task is to verify a full process chain: persistent monsoon rainfall, peak-window persistence, multi-product precipitation consensus, southward river routing, downstream storage or low-drainage amplification, and normalized reported impact.

Use only the local CSX-102 event package. Select package-relative evidence for every calculation and every process-stage claim.

Return JSON with this exact structure:

```json
{
  "target_family": "pakistan_indus_2010_rainfall_routing_storage_process_chain",
  "process_chain": [
    {"stage": "event_window_rainfall_load", "role": "meteorological_input", "computed_values": {}},
    {"stage": "peak_window_persistence_test", "role": "temporal_concentration_check", "computed_values": {}},
    {"stage": "multi_product_precipitation_consensus", "role": "cross_source_precipitation_constraint", "computed_values": {}},
    {"stage": "routing_storage_sequence_flags", "role": "river_routing_and_storage_amplification", "computed_values": {}},
    {"stage": "reported_impact_normalization", "role": "reported_burden_context", "computed_values": {}}
  ],
  "process_tests": [
    {
      "row_id": "event_window_rainfall_load",
      "formula": "<duration, total rainfall, daily mean, wet-day, and wet-spell formulas>",
      "computed_values": {
        "duration_days": 0,
        "event_total_mm": 0,
        "daily_mean_mm_per_day": 0,
        "wet_days_ge_1mm": 0,
        "longest_wet_spell_days_ge_1mm": 0
      },
      "threshold_state": "<pass/fail>",
      "rejected_alternative": "<one short failed interpretation>"
    },
    {
      "row_id": "peak_window_persistence_test",
      "formula": "<7-day maximum fraction and persistence comparison>",
      "computed_values": {
        "max_7day_total_mm": 0,
        "max_7day_start": "<ISO timestamp>",
        "max_7day_fraction_of_total": 0
      },
      "threshold_state": "<pass/fail>",
      "rejected_alternative": "<one short failed interpretation>"
    },
    {
      "row_id": "multi_product_precipitation_consensus",
      "formula": "<consensus mean, spread, concentration, and anomaly formulas>",
      "computed_values": {
        "grid_consensus_mean_mm": 0,
        "grid_spread_fraction": 0,
        "average_max_to_mean_ratio": 0,
        "july_anomaly_pct": 0,
        "august_anomaly_pct": 0,
        "august_to_july_anomaly_ratio": 0,
        "mean_monthly_anomaly_pct": 0
      },
      "threshold_state": "<pass/fail>",
      "rejected_alternative": "<one short failed interpretation>"
    },
    {
      "row_id": "routing_storage_sequence_flags",
      "formula": "<Boolean conjunction of the routed-wave and storage flags>",
      "computed_values": {
        "southward_surge": false,
        "sindh_diversion": false,
        "manchhar_lake": false,
        "slow_retreat": false,
        "storage_or_low_drainage": false,
        "all_sequence_flags_true": false
      },
      "threshold_state": "<pass/fail>",
      "rejected_alternative": "<one short failed interpretation>"
    },
    {
      "row_id": "reported_impact_normalization",
      "formula": "<reported-impact normalization formulas>",
      "computed_values": {
        "flood_extent_sq_km": 0,
        "extent_window_days": 0,
        "affected_people_million_lower_bound": 0,
        "extent_per_million_affected_sq_km": 0,
        "deaths_per_million_affected": 0,
        "houses_per_affected_person": 0,
        "cotton_crop_flooded_pct": 0,
        "rice_crop_flooded_pct": 0
      },
      "threshold_state": "<pass/fail>",
      "rejected_alternative": "<one short failed interpretation>"
    }
  ],
  "proof_conclusion": "<one concise sentence tying the passing rows together>"
}
```

Each process stage must include numeric values and one rejected alternative. The conclusion should synthesize the chain rather than retell the event history.
