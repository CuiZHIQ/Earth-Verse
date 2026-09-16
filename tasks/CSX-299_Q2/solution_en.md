# Correct Answer

```json
{
  "evidence_windows": {
    "event_window": {
      "start": "2020-02-06",
      "end": "2020-02-06"
    },
    "precip_wind_window": {
      "start": "2020-02-06",
      "end": "2020-02-06"
    },
    "transport_report_context_date": "2020-03-07"
  },
  "answer": "source_gate_fail",
  "observed_chain_score": 1,
  "counterfactual_chain_score": 0,
  "source_flags_present": 5,
  "dry_precip_product_count": 2,
  "transport_distance_km_lower_bound": 120,
  "annual_change_max_to_mean_ratio": 17.16
}
```

# Key Computations

Use `score = source_gate * lift_gate * wind_align_gate * dry_precip_gate * transport_gate`.

The event record contains five source-chain indicators: primary lakebed source, dry-season evaporation, exposed loose silt, ground lifting, and wind-aligned streamers. That gives `source_flags_present = 5` and an observed source gate of 1.

The event-day precipitation means are 0.031947 mm and 0 mm, so both meet the `<= 0.1 mm` dry threshold and `dry_precip_product_count = 2`. The February 6 event-day numeric window is separate from the NASA report-context transport statement. The report-context eastward reach is more than 120 km, so `transport_distance_km_lower_bound = 120` and the transport-context gate is 1.

The observed calculation is `1 * 1 * 1 * 1 * 1 = 1`. Under the counterfactual, the missing exposed fine sediment forces `source_gate = 0`, so the calculation becomes `0 * 1 * 1 * 1 * 1 = 0`.

The annual surface-change ratio is `0.30763768100903444 / 0.01792625329576648 = 17.16` after rounding. It is a year-scale timing check, not an event-day source gate.

# Reasoning Path

The pass threshold is a chain score of 1. The observed event satisfies the source, lifting, wind-alignment, dry-day, and transport gates. The counterfactual fails because the multiplicative score drops to 0 when the source gate is removed.

# Computed Consequence

Computed consequence: source-limited streamer calibration fails under the counterfactual.

# Scoring Rubric

- 3 points: Returns compact JSON with the required label, both scores, source flag count, dry-precipitation count, transport distance, and annual-change ratio.
- 4 points: Counts all five observed source-chain indicators and forms the observed source, lift, and wind-alignment gates correctly.
- 4 points: Applies the `<= 0.1 mm` event-day mean threshold to both precipitation products and the `>= 120 km` threshold to the report-context transport lower bound.
- 4 points: Uses the multiplicative formula correctly, giving `observed_chain_score = 1` and `counterfactual_chain_score = 0`.
- 2 points: Reports the annual surface-change max-to-mean ratio near 17.16 and treats it as a year-scale timing check.
- 2 points: Uses `source_gate_fail` because the counterfactual score is below the pass score of 1.
- 1 point: Keeps the final sentence to the computed source-gate consequence and does not add impact or process narration.
