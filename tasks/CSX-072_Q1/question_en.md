# Rainfall-River Response Score Ledger

During the late September 2024 Nepal floods and landslides, a hydrometeorology team needs to check whether the measured rainfall and river levels support a persistent rainfall plus lagged river-response diagnosis, rather than a single-hour or one-basin explanation.

Compute a five-test score ledger from the incident record. Use the station rainfall totals, record-breaking station counts, river gauge exceedances, point rainfall time series, and gridded rainfall maxima to decide whether the diagnosis passes.

Return compact JSON in this shape:

```json
{
  "test_scores": {
    "station_load": "",
    "record_spread": "",
    "river_response": "",
    "point_persistence": "",
    "grid_contrast": ""
  },
  "computed_values": {},
  "pass_count": 0,
  "final_label": "",
  "rejected_alternative": ""
}
```

Use `"pass"` or `"fail"` for each test. Include the formulas and numeric values needed to justify each test, then give one final label and one rejected alternative in a single phrase each.
